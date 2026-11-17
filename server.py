#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
App Concursos Públicos - Servidor Web Local e API REST
Zero dependências externas: roda diretamente com a biblioteca padrão do Python 3.
"""

import os
import sys
import json
import random
import mimetypes
import socket
import time
import webbrowser
import threading
import urllib.parse
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')
QUESTOES_FILE = os.path.join(DATA_DIR, 'questoes.json')
EDITAIS_FILE = os.path.join(DATA_DIR, 'editais.json')
USER_DATA_FILE = os.path.join(DATA_DIR, 'user_data.json')

# Tentar carregar GEMINI_API_KEY de arquivos de configuração locais se existirem
GEMINI_KEY = os.environ.get('GEMINI_API_KEY', '')
if not GEMINI_KEY:
    env_paths = [
        os.path.join(os.path.dirname(BASE_DIR), '.youtube-ai-agent', '.env'),
        os.path.join(os.path.dirname(BASE_DIR), '.env'),
        os.path.join(BASE_DIR, '.env')
    ]
    for env_path in env_paths:
        if os.path.exists(env_path):
            try:
                with open(env_path, 'r', encoding='utf-8') as ef:
                    for line in ef:
                        if line.strip().startswith('GEMINI_API_KEY='):
                            GEMINI_KEY = line.strip().split('=', 1)[1].strip().strip('"').strip("'")
                            break
            except Exception:
                pass


def load_json(filepath, default_val=None):
    if not os.path.exists(filepath):
        return default_val if default_val is not None else []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao ler {filepath}: {e}")
        return default_val if default_val is not None else []


def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_user_data():
    default_data = {
        "respostas": {},       # "qid": {"escolhida": "B", "acertou": True, "data": "...", "tentativas": 1}
        "caderno_erros": [],  # lista de IDs das questoes
        "favoritas": [],      # lista de IDs
        "simulados_feitos": [],
        "edital_progresso": {}, # "edital_id": {"topico_key": {"teoria": True, "resumo": False, "questoes": True}}
        "metas": {"diaria": 20, "hoje_respondidas": 0}
    }
    return load_json(USER_DATA_FILE, default_data)


def save_user_data(data):
    save_json(USER_DATA_FILE, data)


def call_gemini_ai(prompt):
    """Consulta rápida à API do Gemini ou gera resposta didática contextual se sem chave"""
    if GEMINI_KEY:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_KEY}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.4, "maxOutputTokens": 800}
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                result = json.loads(response.read().decode('utf-8'))
                text = result['candidates'][0]['content']['parts'][0]['text']
                return text
        except Exception as e:
            print(f"Aviso na chamada Gemini: {e}")
    return None


class AppConcursosHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Log mais limpo no terminal
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.command} {self.path}\n")

    def send_json(self, data, status_code=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Roteamento da API
        if path.startswith('/api/'):
            self.handle_api_get(path, query)
            return

        # Servir Arquivos Estáticos (public/)
        self.handle_static_file(path)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body_bytes = self.rfile.read(content_length)
        body = {}
        if body_bytes:
            try:
                body = json.loads(body_bytes.decode('utf-8'))
            except Exception:
                body = {}

        if path.startswith('/api/'):
            self.handle_api_post(path, body)
            return

        self.send_error(404, "Endpoint não encontrado")

    def handle_static_file(self, path):
        if path == '/' or path == '':
            path = '/index.html'

        # Sanitizar caminho
        rel_path = path.lstrip('/')
        filepath = os.path.abspath(os.path.join(PUBLIC_DIR, rel_path))

        # Bloquear path traversal
        if not filepath.startswith(os.path.abspath(PUBLIC_DIR)):
            self.send_error(403, "Acesso proibido")
            return

        if not os.path.exists(filepath) or os.path.isdir(filepath):
            # Tentar fallback para index.html se for rota SPA
            fallback = os.path.join(PUBLIC_DIR, 'index.html')
            if os.path.exists(fallback):
                filepath = fallback
            else:
                self.send_error(404, "Arquivo não encontrado")
                return

        mime_type, _ = mimetypes.guess_type(filepath)
        if mime_type is None:
            mime_type = 'application/octet-stream'

        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', f"{mime_type}; charset=utf-8" if 'text' in mime_type or 'javascript' in mime_type or 'json' in mime_type else mime_type)
            self.send_header('Content-Length', str(len(content)))
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Erro ao ler arquivo: {e}")

    def handle_api_get(self, path, query):
        questoes = load_json(QUESTOES_FILE, [])
        user_data = get_user_data()

        if path == '/api/filtros':
            bancas = sorted(list(set(q.get('banca') for q in questoes if q.get('banca'))))
            materias = sorted(list(set(q.get('materia') for q in questoes if q.get('materia'))))
            assuntos = sorted(list(set(q.get('assunto') for q in questoes if q.get('assunto'))))
            concursos = sorted(list(set(q.get('concurso') for q in questoes if q.get('concurso'))))
            anos = sorted(list(set(q.get('ano') for q in questoes if q.get('ano'))), reverse=True)
            tipos = sorted(list(set(q.get('tipo') for q in questoes if q.get('tipo'))))

            self.send_json({
                "total_questoes": len(questoes),
                "bancas": bancas,
                "materias": materias,
                "assuntos": assuntos,
                "concursos": concursos,
                "anos": anos,
                "tipos": tipos
            })
            return

        elif path == '/api/questoes':
            # Filtros aplicados
            banca = query.get('banca', [None])[0]
            materia = query.get('materia', [None])[0]
            assunto = query.get('assunto', [None])[0]
            concurso = query.get('concurso', [None])[0]
            tipo = query.get('tipo', [None])[0]
            ano = query.get('ano', [None])[0]
            busca = query.get('busca', [None])[0]
            so_lei = query.get('so_lei', ['false'])[0].lower() == 'true'
            so_sumula = query.get('so_sumula', ['false'])[0].lower() == 'true'
            caderno_erros = query.get('caderno_erros', ['false'])[0].lower() == 'true'
            somente_favoritas = query.get('favoritas', ['false'])[0].lower() == 'true'
            somente_nao_resolvidas = query.get('nao_resolvidas', ['false'])[0].lower() == 'true'
            somente_erradas = query.get('somente_erradas', ['false'])[0].lower() == 'true'
            
            filtradas = []
            for q in questoes:
                qid_str = str(q['id'])
                resp_info = user_data.get('respostas', {}).get(qid_str)

                if banca and q.get('banca') != banca:
                    continue
                if materia and q.get('materia') != materia:
                    continue
                if assunto and q.get('assunto') != assunto:
                    continue
                if concurso and q.get('concurso') != concurso:
                    continue
                if tipo and q.get('tipo') != tipo:
                    continue
                if ano and str(q.get('ano')) != str(ano):
                    continue
                if so_lei and not q.get('eh_lei_seca'):
                    continue
                if so_sumula and not q.get('eh_sumula'):
                    continue
                if caderno_erros and q['id'] not in user_data.get('caderno_erros', []):
                    continue
                if somente_favoritas and q['id'] not in user_data.get('favoritas', []):
                    continue
                if somente_nao_resolvidas and resp_info is not None:
                    continue
                if somente_erradas and (resp_info is None or resp_info.get('acertou') is True):
                    continue
                if busca:
                    termo = busca.lower()
                    texto_completo = (
                        q.get('enunciado', '') + ' ' +
                        q.get('materia', '') + ' ' +
                        q.get('assunto', '') + ' ' +
                        q.get('banca', '') + ' ' +
                        q.get('concurso', '') + ' ' +
                        str(q.get('comentario', ''))
                    ).lower()
                    if termo not in texto_completo:
                        continue

                # Anexar metadados do estudante na questão
                q_copy = dict(q)
                q_copy['usuario_ja_respondeu'] = resp_info is not None
                q_copy['usuario_acertou'] = resp_info.get('acertou') if resp_info else None
                q_copy['usuario_escolha'] = resp_info.get('escolhida') if resp_info else None
                q_copy['no_caderno_erros'] = q['id'] in user_data.get('caderno_erros', [])
                q_copy['favorita'] = q['id'] in user_data.get('favoritas', [])
                filtradas.append(q_copy)

            self.send_json({
                "total": len(filtradas),
                "questoes": filtradas
            })
            return

        elif path == '/api/editais':
            editais = load_json(EDITAIS_FILE, [])
            progresso = user_data.get('edital_progresso', {})
            # Anexar contagem e progresso
            for ed in editais:
                ed_id = ed.get('id')
                ed_prog = progresso.get(ed_id, {})
                total_topicos = 0
                concluidos = 0
                for mod in ed.get('modulos', []):
                    for disc in mod.get('disciplinas', []):
                        for top in disc.get('topicos', []):
                            total_topicos += 1
                            key = f"{disc['nome']}::{top}"
                            if ed_prog.get(key, {}).get('questoes') and ed_prog.get(key, {}).get('teoria'):
                                concluidos += 1
                ed['total_topicos'] = total_topicos
                ed['topicos_concluidos'] = concluidos
                ed['porcentagem'] = round((concluidos / total_topicos * 100), 1) if total_topicos > 0 else 0
            self.send_json(editais)
            return

        elif path == '/api/edital/detalhe':
            edital_id = query.get('id', [None])[0]
            editais = load_json(EDITAIS_FILE, [])
            alvo = next((e for e in editais if e['id'] == edital_id), None)
            if not alvo:
                self.send_json({"error": "Edital não encontrado"}, 404)
                return
            progresso = user_data.get('edital_progresso', {}).get(edital_id, {})
            self.send_json({"edital": alvo, "progresso": progresso})
            return

        elif path == '/api/estatisticas':
            respostas = user_data.get('respostas', {})
            total_respondidas = len(respostas)
            total_acertos = sum(1 for r in respostas.values() if r.get('acertou'))
            total_erros = total_respondidas - total_acertos
            taxa_acerto = round((total_acertos / total_respondidas * 100), 1) if total_respondidas > 0 else 0

            # Desempenho por matéria e por banca
            mapa_questoes = {q['id']: q for q in questoes}
            por_materia = {}
            por_banca = {}

            for qid_str, resp in respostas.items():
                try:
                    qid = int(qid_str)
                except ValueError:
                    continue
                q = mapa_questoes.get(qid)
                if not q:
                    continue
                mat = q.get('materia', 'Outras')
                ban = q.get('banca', 'Outras')

                por_materia.setdefault(mat, {"total": 0, "acertos": 0})
                por_materia[mat]["total"] += 1
                if resp.get('acertou'):
                    por_materia[mat]["acertos"] += 1

                por_banca.setdefault(ban, {"total": 0, "acertos": 0})
                por_banca[ban]["total"] += 1
                if resp.get('acertou'):
                    por_banca[ban]["acertos"] += 1

            # Calcular percentuais
            for k in por_materia:
                t = por_materia[k]["total"]
                a = por_materia[k]["acertos"]
                por_materia[k]["taxa"] = round((a / t * 100), 1) if t > 0 else 0

            for k in por_banca:
                t = por_banca[k]["total"]
                a = por_banca[k]["acertos"]
                por_banca[k]["taxa"] = round((a / t * 100), 1) if t > 0 else 0

            self.send_json({
                "total_banco": len(questoes),
                "total_respondidas": total_respondidas,
                "total_acertos": total_acertos,
                "total_erros": total_erros,
                "taxa_acerto": taxa_acerto,
                "total_caderno_erros": len(user_data.get('caderno_erros', [])),
                "total_favoritas": len(user_data.get('favoritas', [])),
                "simulados_feitos_qtd": len(user_data.get('simulados_feitos', [])),
                "por_materia": por_materia,
                "por_banca": por_banca,
                "historico_simulados": user_data.get('simulados_feitos', [])[-5:]
            })
            return

        self.send_error(404, "Endpoint API GET não encontrado")

    def handle_api_post(self, path, body):
        questoes = load_json(QUESTOES_FILE, [])
        user_data = get_user_data()

        if path == '/api/questoes/responder':
            qid = body.get('questao_id')
            escolhida = body.get('alternativa_escolhida', '').strip().upper()
            tempo_gasto = body.get('tempo_gasto_segundos', 0)

            q = next((item for item in questoes if item['id'] == qid), None)
            if not q:
                self.send_json({"error": "Questão não encontrada"}, 404)
                return

            gabarito = q.get('gabarito', '').strip().upper()
            acertou = (escolhida == gabarito)

            # Gravar resposta
            user_data['respostas'][str(qid)] = {
                "escolhida": escolhida,
                "acertou": acertou,
                "tempo_gasto": tempo_gasto,
                "data": body.get('data')
            }

            # Se errou, adiciona automaticamente ao caderno de erros
            if not acertou:
                if qid not in user_data['caderno_erros']:
                    user_data['caderno_erros'].append(qid)
            else:
                # Se acertou e estava no caderno de erros e pediu para remover ou manter
                pass

            save_user_data(user_data)

            self.send_json({
                "acertou": acertou,
                "gabarito": gabarito,
                "alternativa_escolhida": escolhida,
                "comentario": q.get('comentario'),
                "no_caderno_erros": qid in user_data['caderno_erros']
            })
            return

        elif path == '/api/caderno-erros/toggle':
            qid = body.get('questao_id')
            if qid in user_data['caderno_erros']:
                user_data['caderno_erros'].remove(qid)
                no_caderno = False
            else:
                user_data['caderno_erros'].append(qid)
                no_caderno = True
            save_user_data(user_data)
            self.send_json({"no_caderno": no_caderno, "total": len(user_data['caderno_erros'])})
            return

        elif path == '/api/favoritas/toggle':
            qid = body.get('questao_id')
            if qid in user_data['favoritas']:
                user_data['favoritas'].remove(qid)
                favorita = False
            else:
                user_data['favoritas'].append(qid)
                favorita = True
            save_user_data(user_data)
            self.send_json({"favorita": favorita, "total": len(user_data['favoritas'])})
            return

        elif path == '/api/edital/progresso':
            edital_id = body.get('edital_id')
            key = body.get('chave_topico') # ex: "Língua Portuguesa::Crase"
            tipo_progresso = body.get('tipo') # "teoria", "resumo", "questoes"
            valor = body.get('valor', False)

            if edital_id not in user_data['edital_progresso']:
                user_data['edital_progresso'][edital_id] = {}
            if key not in user_data['edital_progresso'][edital_id]:
                user_data['edital_progresso'][edital_id][key] = {"teoria": False, "resumo": False, "questoes": False}

            user_data['edital_progresso'][edital_id][key][tipo_progresso] = valor
            save_user_data(user_data)
            self.send_json({"status": "ok", "progresso": user_data['edital_progresso'][edital_id][key]})
            return

        elif path == '/api/simulado/gerar':
            tipo_simulado = body.get('tipo', 'misto') # misto, materia, lei_seca, sumula, banca
            materia = body.get('materia')
            banca = body.get('banca')
            quantidade = int(body.get('quantidade', 10))
            tempo_minutos = int(body.get('tempo_minutos', 30))

            pool = list(questoes)
            if tipo_simulado == 'materia' and materia:
                pool = [q for q in pool if q.get('materia') == materia]
            elif tipo_simulado == 'banca' and banca:
                pool = [q for q in pool if q.get('banca') == banca]
            elif tipo_simulado == 'lei_seca':
                pool = [q for q in pool if q.get('eh_lei_seca')]
            elif tipo_simulado == 'sumula':
                pool = [q for q in pool if q.get('eh_sumula')]

            if not pool:
                pool = list(questoes)

            # Embaralhar e selecionar
            random.shuffle(pool)
            selecionadas = pool[:quantidade]

            simulado_id = f"sim_{int(random.random() * 1000000)}"

            # Retornar questões sem vazar gabarito no simulado ativo!
            questoes_limpas = []
            for q in selecionadas:
                questoes_limpas.append({
                    "id": q["id"],
                    "concurso": q.get("concurso"),
                    "ano": q.get("ano"),
                    "banca": q.get("banca"),
                    "materia": q.get("materia"),
                    "assunto": q.get("assunto"),
                    "tipo": q.get("tipo"),
                    "enunciado": q.get("enunciado"),
                    "alternativas": q.get("alternativas")
                })

            self.send_json({
                "simulado_id": simulado_id,
                "tipo": tipo_simulado,
                "titulo": f"Simulado {tipo_simulado.capitalize().replace('_', ' ')} ({len(questoes_limpas)} questões)",
                "tempo_segundos": tempo_minutos * 60,
                "questoes": questoes_limpas
            })
            return

        elif path == '/api/simulado/finalizar':
            respostas_usuario = body.get('respostas', {}) # {"qid": "B"}
            tempo_gasto = body.get('tempo_gasto_segundos', 0)
            tipo_simulado = body.get('tipo', 'misto')

            mapa = {str(q['id']): q for q in questoes}
            detalhes = []
            total = len(respostas_usuario)
            acertos = 0

            for qid_str, esc in respostas_usuario.items():
                q = mapa.get(qid_str)
                if not q:
                    continue
                gabarito = q.get('gabarito', '').strip().upper()
                acertou = (esc.strip().upper() == gabarito)
                if acertou:
                    acertos += 1
                else:
                    if q['id'] not in user_data['caderno_erros']:
                        user_data['caderno_erros'].append(q['id'])

                # Salvar também no histórico individual
                user_data['respostas'][qid_str] = {
                    "escolhida": esc,
                    "acertou": acertou,
                    "tempo_gasto": round(tempo_gasto / max(1, total), 1)
                }

                detalhes.append({
                    "id": q['id'],
                    "materia": q.get('materia'),
                    "assunto": q.get('assunto'),
                    "enunciado": q.get('enunciado'),
                    "alternativas": q.get('alternativas'),
                    "escolhida": esc,
                    "gabarito": gabarito,
                    "acertou": acertou,
                    "comentario": q.get('comentario')
                })

            porcentagem = round((acertos / total * 100), 1) if total > 0 else 0
            registro_simulado = {
                "tipo": tipo_simulado,
                "total": total,
                "acertos": acertos,
                "porcentagem": porcentagem,
                "tempo_segundos": tempo_gasto,
                "data": body.get('data')
            }
            user_data['simulados_feitos'].append(registro_simulado)
            save_user_data(user_data)

            self.send_json({
                "total": total,
                "acertos": acertos,
                "erros": total - acertos,
                "porcentagem": porcentagem,
                "tempo_gasto_segundos": tempo_gasto,
                "detalhes": detalhes
            })
            return

        elif path == '/api/questoes/criar':
            # Adicionar questão autoral ou criada por IA
            novo_id = max([q['id'] for q in questoes] + [0]) + 1
            nova = {
                "id": novo_id,
                "concurso": body.get('concurso', 'Questão Inédita'),
                "orgao": body.get('orgao', 'Inédita'),
                "cargo": body.get('cargo', 'Geral'),
                "ano": int(body.get('ano', 2024)),
                "banca": body.get('banca', 'Inédita / IA'),
                "materia": body.get('materia', 'Direito Constitucional'),
                "assunto": body.get('assunto', 'Geral'),
                "nivel": body.get('nivel', 'Médio'),
                "tipo": body.get('tipo', 'multipla_escolha'),
                "eh_lei_seca": bool(body.get('eh_lei_seca', False)),
                "eh_sumula": bool(body.get('eh_sumula', False)),
                "dificuldade": body.get('dificuldade', 'Médio'),
                "artigo_lei": body.get('artigo_lei', ''),
                "sumula_ref": body.get('sumula_ref', ''),
                "enunciado": body.get('enunciado', ''),
                "alternativas": body.get('alternativas', {}),
                "gabarito": body.get('gabarito', '').upper(),
                "comentario": {
                    "resumo": body.get('comentario_resumo', ''),
                    "analise_alternativas": body.get('comentario_analise', {}),
                    "fundamentacao_legal": body.get('fundamentacao_legal', ''),
                    "pegadinha_da_banca": body.get('pegadinha_da_banca', '')
                }
            }
            questoes.append(nova)
            save_json(QUESTOES_FILE, questoes)
            self.send_json({"status": "criada", "questao": nova})
            return

        elif path == '/api/ia/tutor':
            qid = body.get('questao_id')
            modo = body.get('modo', 'duvida') # 'macete', 'simplificar', 'duvida'
            pergunta_aluno = body.get('pergunta', '').strip()

            q = next((item for item in questoes if item['id'] == qid), None)
            if not q:
                self.send_json({"error": "Questão não encontrada"}, 404)
                return

            # Preparar prompt para o tutor
            com = q.get('comentario', {})
            prompt = f"""Você é um Mentor Especialista em Concursos Públicos de altíssimo nível.
O aluno está resolvendo a seguinte questão e solicitou sua ajuda:

Matéria: {q.get('materia')} | Assunto: {q.get('assunto')} | Banca: {q.get('banca')}
Enunciado: {q.get('enunciado')}
Alternativas: {json.dumps(q.get('alternativas'), ensure_ascii=False)}
Gabarito Oficial: {q.get('gabarito')}
Fundamentação: {com.get('fundamentacao_legal')}
Pegadinha da Banca: {com.get('pegadinha_da_banca')}

Modo de Ajuda Solicitado: {modo}
Pergunta/Dúvida do Aluno: {pergunta_aluno if pergunta_aluno else 'Explique de forma direta e memorável.'}

Diretrizes da resposta:
- Se modo == 'macete': crie um mnemônico fácil, acrônimo ou historinha para nunca mais esquecer este assunto na prova.
- Se modo == 'simplificar': explique como se estivesse explicando para uma pessoa sem conhecimento jurídico ou técnico avançado.
- Se modo == 'duvida': responda com clareza cristalina apontando exatamente onde está a pegadinha.
- Mantenha tom encorajador, focado em aprovação e direto ao ponto."""

            # Tenta chamada Gemini
            resposta_ia = call_gemini_ai(prompt)

            # Fallback inteligente local se offline
            if not resposta_ia:
                if modo == 'macete':
                    resposta_ia = (
                        f"🎯 **Macete para a Banca {q.get('banca')}:**\n\n"
                        f"{com.get('pegadinha_da_banca')}\n\n"
                        f"💡 **Regra de Ouro:** Relacione sempre o conceito-chave com a fundamentação: *{com.get('fundamentacao_legal')}*. "
                        f"Ao ler o enunciado, busque a palavra-chave e elimine imediatamente as alternativas opostas!"
                    )
                elif modo == 'simplificar':
                    resposta_ia = (
                        f"📖 **Explicando em Português Claro:**\n\n"
                        f"{com.get('resumo')}\n\n"
                        f"**Por que o gabarito é a letra {q.get('gabarito')}?**\n"
                        f"Porque a regra geral é: {com.get('fundamentacao_legal')}. Quando a questão tenta complicar com detalhes técnicos, volte para o conceito essencial!"
                    )
                else:
                    resposta_ia = (
                        f"👨‍🏫 **Orientações do Tutor Concurseiro:**\n\n"
                        f"Para acertar essa questão da banca **{q.get('banca')}**, observe que o gabarito é **Letra {q.get('gabarito')}**.\n\n"
                        f"**Fundamentação Legal:** {com.get('fundamentacao_legal')}\n\n"
                        f"**Dica Estratégica:** {com.get('pegadinha_da_banca')}"
                    )

            self.send_json({
                "modo": modo,
                "resposta": resposta_ia
            })
            return

        elif path == '/api/resetar-dados':
            save_user_data({
                "respostas": {},
                "caderno_erros": [],
                "favoritas": [],
                "simulados_feitos": [],
                "edital_progresso": {},
                "metas": {"diaria": 20, "hoje_respondidas": 0}
            })
            self.send_json({"status": "resetado"})
            return

        self.send_error(404, "Endpoint API POST não encontrado")


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def abrir_navegador_auto(port):
    time.sleep(1.0)
    url = f"http://localhost:{port}"
    print(f"[*] Abrindo automaticamente no navegador: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] Não foi possível abrir o navegador automaticamente: {e}")


def run_server(port=8000):
    server_address = ('', port)
    try:
        httpd = HTTPServer(server_address, AppConcursosHandler)
    except OSError as e:
        if "10048" in str(e) or "already in use" in str(e).lower():
            port = 8080
            server_address = ('', port)
            httpd = HTTPServer(server_address, AppConcursosHandler)
        else:
            raise e

    local_ip = get_local_ip()

    print(f"============================================================")
    print(f"🚀 APROVAQUEST INICIADO COM SUCESSO!")
    print(f"👉 No seu Computador/Notebook: http://localhost:{port}")
    print(f"📱 No seu Celular/Tablet (mesmo Wi-Fi): http://{local_ip}:{port}")
    print(f"🚫 Zero anúncios, 100% gratuito e focado no seu estudo")
    print(f"============================================================")

    # Abrir navegador automaticamente em segundo plano
    threading.Thread(target=abrir_navegador_auto, args=(port,), daemon=True).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário.")
        httpd.server_close()


if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port)
