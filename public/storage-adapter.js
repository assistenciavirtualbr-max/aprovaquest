/**
 * AprovaQuest Storage Adapter
 * Habilita funcionamento 100% autônomo e definitivo no GitHub Pages / Web Estática
 * Se a API Python local não estiver disponível (ou no GitHub Pages / Vercel),
 * este adaptador assume instantaneamente, gerenciando dados em memória e localStorage!
 */

(function() {
  const STORAGE_KEY = 'aprovaquest_user_data_v1';
  let cacheQuestoes = null;
  let cacheEditais = null;

  function getLocalUserData() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) {}
    return {
      respostas: {},
      caderno_erros: [],
      favoritas: [],
      simulados_feitos: [],
      edital_progresso: {},
      metas: { diaria: 20, hoje_respondidas: 0 }
    };
  }

  function saveLocalUserData(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {}
  }

  async function carregarBancoLocal() {
    if (cacheQuestoes) return cacheQuestoes;
    const caminhos = ['data/questoes.json', './data/questoes.json', '../data/questoes.json', '/data/questoes.json'];
    for (const c of caminhos) {
      try {
        const res = await window._originalFetch(c);
        if (res.ok) {
          cacheQuestoes = await res.json();
          return cacheQuestoes;
        }
      } catch (e) {}
    }
    return [];
  }

  async function carregarEditaisLocal() {
    if (cacheEditais) return cacheEditais;
    const caminhos = ['data/editais.json', './data/editais.json', '../data/editais.json', '/data/editais.json'];
    for (const c of caminhos) {
      try {
        const res = await window._originalFetch(c);
        if (res.ok) {
          cacheEditais = await res.json();
          return cacheEditais;
        }
      } catch (e) {}
    }
    return [];
  }

  function jsonResponse(obj, status = 200) {
    return new Response(JSON.stringify(obj), {
      status: status,
      headers: { 'Content-Type': 'application/json; charset=utf-8' }
    });
  }

  async function processarApiCliente(urlStr, options = {}) {
    const url = new URL(urlStr, window.location.href);
    const path = url.pathname.replace(/^.*\/api\//, '/api/');
    const method = (options.method || 'GET').toUpperCase();
    const questoes = await carregarBancoLocal();
    const userData = getLocalUserData();

    // ================= GET /api/filtros =================
    if (path === '/api/filtros' && method === 'GET') {
      const bancas = [...new Set(questoes.map(q => q.banca).filter(Boolean))].sort();
      const materias = [...new Set(questoes.map(q => q.materia).filter(Boolean))].sort();
      const assuntos = [...new Set(questoes.map(q => q.assunto).filter(Boolean))].sort();
      const concursos = [...new Set(questoes.map(q => q.concurso).filter(Boolean))].sort();
      const anos = [...new Set(questoes.map(q => q.ano).filter(Boolean))].sort((a,b) => b - a);
      const tipos = [...new Set(questoes.map(q => q.tipo).filter(Boolean))].sort();

      return jsonResponse({
        total_questoes: questoes.length,
        bancas, materias, assuntos, concursos, anos, tipos
      });
    }

    // ================= GET /api/questoes =================
    if (path === '/api/questoes' && method === 'GET') {
      const qParams = url.searchParams;
      const banca = qParams.get('banca');
      const materia = qParams.get('materia');
      const assunto = qParams.get('assunto');
      const tipo = qParams.get('tipo');
      const busca = (qParams.get('busca') || '').toLowerCase().trim();
      const so_lei = qParams.get('so_lei') === 'true';
      const so_sumula = qParams.get('so_sumula') === 'true';
      const nao_resolvidas = qParams.get('nao_resolvidas') === 'true';
      const somente_erradas = qParams.get('somente_erradas') === 'true';
      const favoritas = qParams.get('favoritas') === 'true';
      const caderno_erros = qParams.get('caderno_erros') === 'true';

      const filtradas = questoes.filter(q => {
        const qidStr = String(q.id);
        const respInfo = userData.respostas[qidStr];

        if (banca && q.banca !== banca) return false;
        if (materia && q.materia !== materia) return false;
        if (assunto && q.assunto !== assunto) return false;
        if (tipo && q.tipo !== tipo) return false;
        if (so_lei && !q.eh_lei_seca) return false;
        if (so_sumula && !q.eh_sumula) return false;
        if (caderno_erros && !userData.caderno_erros.includes(q.id)) return false;
        if (favoritas && !userData.favoritas.includes(q.id)) return false;
        if (nao_resolvidas && respInfo) return false;
        if (somente_erradas && (!respInfo || respInfo.acertou)) return false;

        if (busca) {
          const texto = [
            q.enunciado, q.materia, q.assunto, q.banca, q.concurso,
            JSON.stringify(q.comentario || '')
          ].join(' ').toLowerCase();
          if (!texto.includes(busca)) return false;
        }

        return true;
      }).map(q => {
        const qidStr = String(q.id);
        const respInfo = userData.respostas[qidStr];
        return {
          ...q,
          usuario_ja_respondeu: !!respInfo,
          usuario_acertou: respInfo ? respInfo.acertou : null,
          usuario_escolha: respInfo ? respInfo.escolhida : null,
          no_caderno_erros: userData.caderno_erros.includes(q.id),
          favorita: userData.favoritas.includes(q.id)
        };
      });

      return jsonResponse({ total: filtradas.length, questoes: filtradas });
    }

    // ================= POST /api/questoes/responder =================
    if (path === '/api/questoes/responder' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const qid = body.questao_id;
      const escolhida = (body.alternativa_escolhida || '').trim().toUpperCase();
      const q = questoes.find(item => item.id === qid);
      if (!q) return jsonResponse({ error: 'Questão não encontrada' }, 404);

      const gabarito = (q.gabarito || '').trim().toUpperCase();
      const acertou = (escolhida === gabarito);

      userData.respostas[String(qid)] = {
        escolhida,
        acertou,
        tempo_gasto: body.tempo_gasto_segundos || 30,
        data: new Date().toLocaleDateString('pt-BR')
      };

      if (!acertou) {
        if (!userData.caderno_erros.includes(qid)) {
          userData.caderno_erros.push(qid);
        }
      }
      saveLocalUserData(userData);

      return jsonResponse({
        acertou,
        gabarito,
        alternativa_escolhida: escolhida,
        comentario: q.comentario,
        no_caderno_erros: userData.caderno_erros.includes(qid)
      });
    }

    // ================= POST /api/favoritas/toggle =================
    if (path === '/api/favoritas/toggle' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const qid = body.questao_id;
      const idx = userData.favoritas.indexOf(qid);
      let favorita = false;
      if (idx !== -1) {
        userData.favoritas.splice(idx, 1);
      } else {
        userData.favoritas.push(qid);
        favorita = true;
      }
      saveLocalUserData(userData);
      return jsonResponse({ favorita, total: userData.favoritas.length });
    }

    // ================= POST /api/caderno-erros/toggle =================
    if (path === '/api/caderno-erros/toggle' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const qid = body.questao_id;
      const idx = userData.caderno_erros.indexOf(qid);
      let no_caderno = false;
      if (idx !== -1) {
        userData.caderno_erros.splice(idx, 1);
      } else {
        userData.caderno_erros.push(qid);
        no_caderno = true;
      }
      saveLocalUserData(userData);
      return jsonResponse({ no_caderno, total: userData.caderno_erros.length });
    }

    // ================= POST /api/simulado/gerar =================
    if (path === '/api/simulado/gerar' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const tipo = body.tipo || 'misto';
      const quantidade = parseInt(body.quantidade || 10);
      const tempo = parseInt(body.tempo_minutos || 30);

      let pool = [...questoes];
      if (tipo === 'lei_seca') pool = pool.filter(q => q.eh_lei_seca);
      else if (tipo === 'sumula') pool = pool.filter(q => q.eh_sumula);

      if (pool.length === 0) pool = [...questoes];
      pool.sort(() => Math.random() - 0.5);
      const selecionadas = pool.slice(0, quantidade).map(q => ({
        id: q.id,
        concurso: q.concurso,
        ano: q.ano,
        banca: q.banca,
        materia: q.materia,
        assunto: q.assunto,
        tipo: q.tipo,
        enunciado: q.enunciado,
        alternativas: q.alternativas
      }));

      return jsonResponse({
        simulado_id: `sim_${Date.now()}`,
        tipo,
        titulo: `Simulado ${tipo.toUpperCase()} (${selecionadas.length} questões)`,
        tempo_segundos: tempo * 60,
        questoes: selecionadas
      });
    }

    // ================= POST /api/simulado/finalizar =================
    if (path === '/api/simulado/finalizar' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const respostas = body.respostas || {};
      const tempo = body.tempo_gasto_segundos || 0;
      const total = Object.keys(respostas).length;
      let acertos = 0;
      const detalhes = [];

      for (const [qidStr, esc] of Object.entries(respostas)) {
        const q = questoes.find(item => String(item.id) === qidStr);
        if (!q) continue;
        const gab = (q.gabarito || '').trim().toUpperCase();
        const acertou = (esc.trim().toUpperCase() === gab);
        if (acertou) acertos++;
        else {
          if (!userData.caderno_erros.includes(q.id)) {
            userData.caderno_erros.push(q.id);
          }
        }
        userData.respostas[qidStr] = {
          escolhida: esc,
          acertou,
          tempo_gasto: Math.round(tempo / Math.max(1, total))
        };
        detalhes.push({
          id: q.id,
          materia: q.materia,
          assunto: q.assunto,
          enunciado: q.enunciado,
          alternativas: q.alternativas,
          escolhida: esc,
          gabarito: gab,
          acertou,
          comentario: q.comentario
        });
      }

      const pct = total > 0 ? Math.round((acertos / total) * 100) : 0;
      userData.simulados_feitos.push({
        tipo: body.tipo || 'misto',
        total,
        acertos,
        porcentagem: pct,
        tempo_segundos: tempo,
        data: body.data || new Date().toLocaleDateString('pt-BR')
      });
      saveLocalUserData(userData);

      return jsonResponse({
        total,
        acertos,
        erros: total - acertos,
        porcentagem: pct,
        tempo_gasto_segundos: tempo,
        detalhes
      });
    }

    // ================= GET /api/editais =================
    if (path === '/api/editais' && method === 'GET') {
      const editais = await carregarEditaisLocal();
      const prog = userData.edital_progresso || {};
      const formatados = editais.map(ed => {
        let total = 0;
        let concluidos = 0;
        const edProg = prog[ed.id] || {};
        (ed.modulos || []).forEach(m => {
          (m.disciplinas || []).forEach(d => {
            (d.topicos || []).forEach(t => {
              total++;
              const k = `${d.nome}::${t}`;
              if (edProg[k]?.teoria && edProg[k]?.questoes) concluidos++;
            });
          });
        });
        return {
          ...ed,
          total_topicos: total,
          topicos_concluidos: concluidos,
          porcentagem: total > 0 ? Math.round((concluidos / total) * 100) : 0
        };
      });
      return jsonResponse(formatados);
    }

    // ================= GET /api/edital/detalhe =================
    if (path.startsWith('/api/edital/detalhe') && method === 'GET') {
      const id = url.searchParams.get('id');
      const editais = await carregarEditaisLocal();
      const edital = editais.find(e => e.id === id);
      if (!edital) return jsonResponse({ error: 'Edital não encontrado' }, 404);
      return jsonResponse({ edital, progresso: userData.edital_progresso[id] || {} });
    }

    // ================= POST /api/edital/progresso =================
    if (path === '/api/edital/progresso' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const { edital_id, chave_topico, tipo, valor } = body;
      if (!userData.edital_progresso[edital_id]) userData.edital_progresso[edital_id] = {};
      if (!userData.edital_progresso[edital_id][chave_topico]) {
        userData.edital_progresso[edital_id][chave_topico] = { teoria: false, resumo: false, questoes: false };
      }
      userData.edital_progresso[edital_id][chave_topico][tipo] = valor;
      saveLocalUserData(userData);
      return jsonResponse({ status: 'ok', progresso: userData.edital_progresso[edital_id][chave_topico] });
    }

    // ================= GET /api/estatisticas =================
    if (path === '/api/estatisticas' && method === 'GET') {
      const respostas = userData.respostas;
      const totalRespondidas = Object.keys(respostas).length;
      const acertos = Object.values(respostas).filter(r => r.acertou).length;
      const taxa = totalRespondidas > 0 ? Math.round((acertos / totalRespondidas) * 100) : 0;

      const porMateria = {};
      const porBanca = {};
      const mapaQ = new Map(questoes.map(q => [String(q.id), q]));

      for (const [qid, r] of Object.entries(respostas)) {
        const q = mapaQ.get(qid);
        if (!q) continue;
        const mat = q.materia || 'Geral';
        const ban = q.banca || 'Geral';

        if (!porMateria[mat]) porMateria[mat] = { total: 0, acertos: 0, taxa: 0 };
        porMateria[mat].total++;
        if (r.acertou) porMateria[mat].acertos++;

        if (!porBanca[ban]) porBanca[ban] = { total: 0, acertos: 0, taxa: 0 };
        porBanca[ban].total++;
        if (r.acertou) porBanca[ban].acertos++;
      }

      for (const m of Object.keys(porMateria)) {
        porMateria[m].taxa = Math.round((porMateria[m].acertos / porMateria[m].total) * 100);
      }
      for (const b of Object.keys(porBanca)) {
        porBanca[b].taxa = Math.round((porBanca[b].acertos / porBanca[b].total) * 100);
      }

      return jsonResponse({
        total_banco: questoes.length,
        total_respondidas: totalRespondidas,
        total_acertos: acertos,
        total_erros: totalRespondidas - acertos,
        taxa_acerto: taxa,
        total_caderno_erros: userData.caderno_erros.length,
        total_favoritas: userData.favoritas.length,
        simulados_feitos_qtd: userData.simulados_feitos.length,
        por_materia: porMateria,
        por_banca: porBanca,
        historico_simulados: userData.simulados_feitos.slice(-5)
      });
    }

    // ================= POST /api/ia/tutor =================
    if (path === '/api/ia/tutor' && method === 'POST') {
      const body = JSON.parse(options.body || '{}');
      const q = questoes.find(item => item.id === body.questao_id);
      if (!q) return jsonResponse({ error: 'Questão não encontrada' }, 404);
      const com = q.comentario || {};
      const modo = body.modo || 'duvida';

      let resposta = '';
      if (modo === 'macete') {
        resposta = `🎯 **Macete da Banca ${q.banca}:**\n\n${com.pegadinha_da_banca || 'Preste atenção aos termos restritivos.'}\n\n💡 **Dica de Ouro:** Memorize a fundamentação: *${com.fundamentacao_legal || 'Lei Seca'}*. Elimine alternativas absurdas primeiro!`;
      } else if (modo === 'simplificar') {
        resposta = `📖 **Explicando em Português Claro:**\n\n${com.resumo || 'Entenda o conceito central.'}\n\n**Por que o gabarito é Letra ${q.gabarito}?**\nPorque a regra basilar determina: ${com.fundamentacao_legal || 'Texto constitucional ou legal.'}.`;
      } else {
        resposta = `👨‍🏫 **Tutor Concurseiro 24h:**\n\nNesta questão da banca **${q.banca}**, o gabarito oficial é a **Letra ${q.gabarito}**.\n\n⚖️ **Fundamentação:** ${com.fundamentacao_legal || 'Disposição legal.'}\n\n⚠️ **Atenção:** ${com.pegadinha_da_banca || 'Cuidado com trocas de palavras.'}`;
      }

      return jsonResponse({ modo, resposta });
    }

    return jsonResponse({ error: 'Endpoint não encontrado no cliente' }, 404);
  }

  // Interceptar window.fetch
  window._originalFetch = window.fetch;
  window.fetch = async function(resource, options = {}) {
    const urlStr = (typeof resource === 'string') ? resource : (resource.url || '');
    
    // Se não for rota de API, usa o fetch normal
    if (!urlStr.includes('/api/')) {
      return window._originalFetch(resource, options);
    }

    // Se estiver em localhost com porta (ex: localhost:8000), tenta o servidor Python primeiro
    const isLocalServer = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    if (isLocalServer && window.location.port) {
      try {
        const resp = await window._originalFetch(resource, options);
        if (resp.ok) return resp;
      } catch (e) {
        // Servidor offline, faz fallback para o cliente
      }
    }

    // Execução autônoma na Web (GitHub Pages / Vercel / Netlify / Offline)
    return await processarApiCliente(urlStr, options);
  };

  console.log('[AprovaQuest] Adaptador de Armazenamento Ativo. Modo Híbrido (Localhost + Web Estática) Habilitado.');
})();
