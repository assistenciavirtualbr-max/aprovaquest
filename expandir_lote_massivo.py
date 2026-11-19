# -*- coding: utf-8 -*-
import json
import os

QUESTOES_FILE = os.path.join(os.path.dirname(__file__), 'data', 'questoes.json')

with open(QUESTOES_FILE, 'r', encoding='utf-8') as f:
    questoes = json.load(f)

current_id = max([q['id'] for q in questoes]) + 1

LOTE_MASSIVO = [
    # ==================== DIREITO PENAL ====================
    {
        "concurso": "Tribunal de Justiça de São Paulo",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "banca": "Vunesp",
        "materia": "Direito Penal",
        "assunto": "Crimes contra a Administração Pública - Concussão vs Corrupção Passiva",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Código Penal, Art. 316 e Art. 317",
        "sumula_ref": "",
        "enunciado": "Determinado fiscal de posturas municipais, durante vistoria regular em estabelecimento comercial, constata uma infração administrativa menor e, valendo-se expressamente do cargo, EXIGE do comerciante o pagamento imediato de R$ 3.000,00 para não lacrar o imóvel. A conduta praticada pelo agente público amolda-se formalmente ao crime de:",
        "alternativas": {
            "A": "Corrupção passiva.",
            "B": "Prevaricação.",
            "C": "Concussão.",
            "D": "Advocacia administrativa.",
            "E": "Excesso de exação."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "O núcleo do tipo na Concussão (Art. 316 do CP) é o verbo EXIGIR vantagem indevida em razão da função. Na Corrupção Passiva (Art. 317), o verbo é solicitar, receber ou aceitar promessa.",
            "analise_alternativas": {
                "A": "Incorreta. Na corrupção passiva o verbo é 'solicitar' ou 'receber', nunca exigir.",
                "B": "Incorreta. Prevaricação é retardar ou deixar de praticar ato de ofício para satisfazer interesse ou sentimento pessoal.",
                "C": "CORRETA. 'Exigir... vantagem indevida' é a definição literal do crime de Concussão (Art. 316).",
                "D": "Incorreta. Advocacia administrativa é patrocinar interesse privado perante a administração.",
                "E": "Incorreta. Excesso de exação ocorre quando o funcionário exige tributo ou contribuição que sabe indevido."
            },
            "fundamentacao_legal": "Art. 316 do Código Penal.",
            "pegadinha_da_banca": "Dica de ouro: EXIGIR = Concussão. SOLICITAR / RECEBER = Corrupção Passiva. INTERESSE PESSOAL = Prevaricação."
        }
    },
    {
        "concurso": "Polícia Civil de São Paulo",
        "orgao": "PC-SP",
        "cargo": "Investigador de Polícia",
        "ano": 2023,
        "banca": "Vunesp",
        "materia": "Direito Penal",
        "assunto": "Crimes contra a Administração Pública - Peculato",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Código Penal, Art. 312, caput e § 2º",
        "sumula_ref": "",
        "enunciado": "Servidor público que, por negligência ao fechar a repartição no fim do expediente, esquece a porta da tesouraria destrancada, possibilitando que terceiro ingresse no local e subtraia um notebook funcional pertencente ao Estado, pratica:",
        "alternativas": {
            "A": "Peculato-apropriação.",
            "B": "Peculato culposo.",
            "C": "Fato atípico na esfera penal, restando apenas responsabilidade civil-disciplinar.",
            "D": "Condescendência criminosa.",
            "E": "Prevaricação comissiva."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "O funcionário público que, por negligência, imprudência ou imperícia, concorre para que outrem subtraia ou se aproprie de dinheiro ou bem público, comete Peculato Culposo (Art. 312, § 2º).",
            "analise_alternativas": {
                "A": "Incorreta. Peculato-apropriação é doloso e o próprio funcionário se apropria do bem.",
                "B": "CORRETA. Definição estrita do Art. 312, § 2º do Código Penal.",
                "C": "Incorreta. O peculato culposo é expressamente tipificado no Código Penal.",
                "D": "Incorreta. Condescendência criminosa é deixar de responsabilizar subordinado por indulgência.",
                "E": "Incorreta. Não houve satisfação de sentimento pessoal para caracterizar prevaricação."
            },
            "fundamentacao_legal": "Art. 312, § 2º do Código Penal.",
            "pegadinha_da_banca": "Lembre-se: 'A reparação do dano no peculato culposo, se precede à sentença irrecorrível, EXTingue a punibilidade; se lhe é posterior, reduz de metade a pena'."
        }
    },

    # ==================== DIREITO ADMINISTRATIVO ====================
    {
        "concurso": "Tribunal Regional do Trabalho",
        "orgao": "TRT",
        "cargo": "Analista Judiciário",
        "ano": 2024,
        "banca": "FCC",
        "materia": "Direito Administrativo",
        "assunto": "Atos Administrativos - Atributos (PATI) e Extinção",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": True,
        "dificuldade": "Médio",
        "artigo_lei": "Súmula 473 do STF",
        "sumula_ref": "Súmula 473 STF",
        "enunciado": "A respeito da extinção dos atos administrativos e do princípio da autotutela consagrado na jurisprudência do Supremo Tribunal Federal (Súmula 473), assinale a afirmativa correta:",
        "alternativas": {
            "A": "A revogação de um ato administrativo produz efeitos retroativos (ex tunc), desfazendo todas as relações jurídicas pretéritas.",
            "B": "A anulação decorre de vício de ilegalidade, produz efeitos retroativos (ex tunc), e pode ser declarada pela própria Administração ou pelo Poder Judiciário.",
            "C": "O Poder Judiciário pode revogar atos administrativos do Poder Executivo quando constatar inconveniência e inoportunidade pública.",
            "D": "Atos vinculados podem ser livremente revogados a qualquer tempo pelo administrador público.",
            "E": "A anulação de atos administrativos com vício insanável não admite o direito adquirido nem o respeito a terceiros de boa-fé."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Anulação = Ilegalidade (efeito retroativo / ex tunc / feita pela Administração ou Judiciário). Revogação = Mérito/Conveniência (efeito prospectivo / ex nunc / feita EXCLUSIVAMENTE pela Administração).",
            "analise_alternativas": {
                "A": "Incorreta. Revogação tem efeito NÃO retroativo (ex nunc).",
                "B": "CORRETA. Síntese exata da Súmula 473 do STF e do Art. 53 da Lei 9.784/1999.",
                "C": "Incorreta. O Judiciário NUNCA pode revogar ato do Executivo (apenas anular por ilegalidade).",
                "D": "Incorreta. Atos vinculados não comportam juízo de conveniência/oportunidade, logo NÃO são revogáveis.",
                "E": "Incorreta. A anulação deve sempre resguardar os direitos dos terceiros de boa-fé."
            },
            "fundamentacao_legal": "Súmula 473 do STF c/c Art. 53 da Lei Federal nº 9.784/1999.",
            "pegadinha_da_banca": "A pegadinha favorita das bancas: 'O Judiciário revogou o ato por conveniência'. FALSO! Judiciário SÓ ANULA atos de outros poderes, jamais revoga."
        }
    },
    {
        "concurso": "Assembleia Legislativa",
        "orgao": "AL-SP",
        "cargo": "Analista Legislativo",
        "ano": 2023,
        "banca": "Vunesp",
        "materia": "Direito Administrativo",
        "assunto": "Regime Jurídico dos Servidores Públicos - Estabilidade e Demissão",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "CF/88, Art. 41; Lei 8.112/1990",
        "sumula_ref": "",
        "enunciado": "Servidor público civil estável que tem sua demissão anulada por decisão judicial transitada em julgado deve ser reintegrado ao cargo. Se o cargo outrora por ele ocupado estiver provido por outro servidor estável, o ocupante da vaga:",
        "alternativas": {
            "A": "Será sumariamente exonerado sem qualquer indenização pecuniária.",
            "B": "Será reconduzido ao cargo de origem, sem direito a indenização, aproveitado em outro cargo ou posto em disponibilidade.",
            "C": "Será mantido no cargo, enquanto o servidor reintegrado será posto compulsoriamente em disponibilidade remunerada.",
            "D": "Passará a dividir a remuneração integral com o servidor reintegrado até a criação de nova vaga por lei.",
            "E": "Será aposentado compulsoriamente por invalidez administrativa."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Nos termos do Art. 41, § 2º da CF/88, o servidor reintegrado retoma seu cargo. O eventual ocupante que já era estável é reconduzido ao cargo de origem (sem indenização), aproveitado ou posto em disponibilidade.",
            "analise_alternativas": {
                "A": "Incorreta. Servidor estável não pode ser sumariamente exonerado nessa hipótese.",
                "B": "CORRETA. Transcrição literal do Art. 41, § 2º da Constituição Federal de 1988.",
                "C": "Incorreta. O direito de reassumir o cargo é do servidor que teve a demissão anulada (reintegração).",
                "D": "Incorreta. Inexiste essa previsão no ordenamento jurídico.",
                "E": "Incorreta. Aposentadoria não se aplica a essa situação."
            },
            "fundamentacao_legal": "Art. 41, § 2º da Constituição Federal de 1988 c/c Art. 28 da Lei 8.112/1990.",
            "pegadinha_da_banca": "O nome do instituto é REINTEGRAÇÃO (para o demitido que volta) e RECONDUÇÃO (para o que ocupava a vaga e volta ao cargo anterior)."
        }
    },

    # ==================== CONHECIMENTOS BANCÁRIOS ====================
    {
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário Novo",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Garantias do Sistema Financeiro - Alienação Fiduciária vs Penhor",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lei nº 9.514/1997 e Código Civil (Art. 1.361)",
        "sumula_ref": "",
        "enunciado": "No financiamento imobiliário e nas operações de crédito bancário, a alienação fiduciária em garantia se destaca como um dos instrumentos mais utilizados pelas instituições financeiras. Sobre a alienação fiduciária, é correto afirmar que:",
        "alternativas": {
            "A": "O devedor fiduciante transfere ao credor fiduciário a posse direta e a propriedade plena do bem durante todo o contrato.",
            "B": "O credor fiduciário adquire a propriedade resolúvel e a posse indireta do bem, permanecendo o devedor fiduciante com a posse direta.",
            "C": "A garantia fiduciária exige obrigatoriamente a execução judicial prévia para a tomada do imóvel em caso de inadimplência.",
            "D": "O bem gravado com alienação fiduciária pode ser penhorado livremente por dívidas comuns do devedor com outros credores quirografários.",
            "E": "A quitação da dívida pelo fiduciante não extingue a propriedade resolúvel de pleno direito."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Na alienação fiduciária, a propriedade é RESOLÚVEL (pertence ao banco até a última parcela), enquanto a posse DIRETA fica com o cliente (que mora no imóvel ou dirige o carro).",
            "analise_alternativas": {
                "A": "Incorreta. O devedor fica com a posse direta, e o credor com a posse indireta e propriedade resolúvel.",
                "B": "CORRETA. Definição jurídica clássica do Art. 1.361 do Código Civil e da Lei 9.514/1997.",
                "C": "Incorreta. A grande agilidade da Lei 9.514/97 é permitir a execução EXTRAJUDICIAL em cartório.",
                "D": "Incorreta. O bem pertence ao banco; os outros credores só podem penhorar os direitos aquisitivos do contrato.",
                "E": "Incorreta. Com o pagamento integral, a propriedade se consolida de pleno direito no patrimônio do devedor."
            },
            "fundamentacao_legal": "Lei nº 9.514/1997 e Art. 1.361 do Código Civil.",
            "pegadinha_da_banca": "Lembre-se: 'O banco tem a propriedade resolúvel e posse indireta. O cliente tem a posse direta'."
        }
    },
    {
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário",
        "ano": 2023,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Estrutura do SFN - Conselho Monetário Nacional (CMN) vs Banco Central (Bacen)",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Lei nº 4.595/1964; Lei Complementar nº 179/2021",
        "sumula_ref": "",
        "enunciado": "No Sistema Financeiro Nacional (SFN), a distinção entre órgão normativo e entidade supervisora/executora é essencial. Constitui atribuição precípua e exclusiva do Conselho Monetário Nacional (CMN):",
        "alternativas": {
            "A": "Emitir papel-moeda e moeda metálica na forma fixada em lei.",
            "B": "Fixar as diretrizes e metas da política monetária, inclusive a meta para a inflação.",
            "C": "Exercer a fiscalização das instituições financeiras e aplicar penalidades cabíveis.",
            "D": "Realizar operações de redesconto e de empréstimo às instituições financeiras bancárias.",
            "E": "Executar os serviços do meio circulante nacional."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "O CMN é o órgão MÁXIMO e NORMATIVO (ele 'manda/fixa as diretrizes e metas'). O Banco Central é quem EXECUTA e FISCALIZA (ele 'faz').",
            "analise_alternativas": {
                "A": "Incorreta. Emitir moeda é competência executiva do Banco Central do Brasil.",
                "B": "CORRETA. Fixar metas de inflação e diretrizes monetárias é atribuição privativa do CMN.",
                "C": "Incorreta. Fiscalizar e aplicar multas às instituições financeiras é dever do Banco Central.",
                "D": "Incorreta. Redesconto bancário é operação executada pelo Banco Central.",
                "E": "Incorreta. Gerir o meio circulante é competência operacional do Bacen."
            },
            "fundamentacao_legal": "Lei Federal nº 4.595/1964, Art. 3º e 4º.",
            "pegadinha_da_banca": "Macete: 'Verbos normativos (Fixar, Estabelecer, Regular, Determinar diretrizes) = CMN. Verbos operacionais (Emitir, Fiscalizar, Punir, Executar, Custodiar) = Banco Central'."
        }
    },

    # ==================== RACIOCÍNIO LÓGICO-MATEMÁTICO ====================
    {
        "concurso": "Tribunal de Justiça de Minas Gerais",
        "orgao": "TJ-MG",
        "cargo": "Oficial Judiciário",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Raciocínio Lógico-Matemático",
        "assunto": "Lógica Proposicional - Negação de Proposição Composta (Leis de De Morgan)",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Leis de De Morgan",
        "sumula_ref": "",
        "enunciado": "A negação lógica correta da proposição 'O processo é digital E o servidor trabalha em regime presencial' é dada por:",
        "alternativas": {
            "A": "O processo não é digital E o servidor não trabalha em regime presencial.",
            "B": "O processo é digital OU o servidor trabalha em regime presencial.",
            "C": "O processo não é digital OU o servidor não trabalha em regime presencial.",
            "D": "Se o processo não é digital, então o servidor trabalha em regime presencial.",
            "E": "O processo é físico E o servidor está de licença médica."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Primeira Lei de De Morgan: para negar uma conjunção 'P e Q', nega-se a primeira, nega-se a segunda e troca-se o conectivo 'E' pelo conectivo 'OU': ~(P ^ Q) <==> (~P v ~Q).",
            "analise_alternativas": {
                "A": "Incorreta. Negou ambas, mas manteve o conectivo 'E'.",
                "B": "Incorreta. Trocou o conectivo mas não negou as proposições simples.",
                "C": "CORRETA. 'Processo NÃO é digital OU servidor NÃO trabalha em regime presencial'.",
                "D": "Incorreta. A condicional formulada não equivale à negação da conjunção.",
                "E": "Incorreta. Termos estranhos ao raciocínio formal das proposições primitivas."
            },
            "fundamentacao_legal": "Regra de De Morgan para negação de conjunção: ~(P e Q) = (~P ou ~Q).",
            "pegadinha_da_banca": "O erro mais comum do concurseiro é negar as duas partes e continuar com o 'E'. Lembre-se: 'Negou o E, vira OU'."
        }
    },

    # ==================== SEGURIDADE SOCIAL ====================
    {
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Seguridade Social",
        "assunto": "Salário de Benefício - Descarte de Menores Contribuições (EC 103/2019)",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Difícil",
        "artigo_lei": "EC nº 103/2019, Art. 26, § 6º",
        "sumula_ref": "",
        "enunciado": "A respeito do cálculo dos benefícios previdenciários após a Reforma da Previdência (EC 103/2019), julgue o item seguinte:\n\nÉ permitido ao segurado do RGPS excluir contribuições que resultem em redução do valor da sua aposentadoria, desde que mantido o tempo mínimo de contribuição exigido para o benefício, sendo vedada a utilização dos períodos excluídos para qualquer finalidade no regime previdenciário.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "O Art. 26, § 6º da EC 103/2019 criou o descarte de contribuições prejudiciais: se você já cumpriu o tempo mínimo, pode jogar fora as contribuições mais baixas para aumentar a média, mas perde aquele tempo descartado.",
            "analise_alternativas": {
                "C": "CORRETA. Previsão literal e inovadora do Art. 26, § 6º da EC 103/2019.",
                "E": "Incorreta. A regra é amplamente aplicada e vantajosa para elevar a média salarial do segurado."
            },
            "fundamentacao_legal": "Art. 26, § 6º da Emenda Constitucional nº 103/2019.",
            "pegadinha_da_banca": "Atenção: o tempo descartado NÃO pode ser contado para carência nem averbado em outro regime (descartou, sumiu)."
        }
    }
]

for item in LOTE_MASSIVO:
    item["id"] = current_id
    current_id += 1
    questoes.append(item)

with open(QUESTOES_FILE, 'w', encoding='utf-8') as f:
    json.dump(questoes, f, indent=2, ensure_ascii=False)

print(f"Sucesso Total! Banco expandido para {len(questoes)} questões.")
