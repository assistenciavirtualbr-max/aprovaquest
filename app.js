/**
 * AprovaQuest - Motor Client-Side da Aplicação
 * Concursos Públicos Sem Anúncios | R$ 0 Investimento
 */

// Estado Global da Aplicação
const state = {
  visao: 'questoes',
  questoes: [],
  indiceAtual: 0,
  opcaoSelecionada: null,
  questaoRespondida: false,
  
  filtros: {
    busca: '',
    banca: '',
    materia: '',
    assunto: '',
    tipo: '',
    so_lei: false,
    so_sumula: false,
    nao_resolvidas: false,
    somente_erradas: false,
    favoritas: false,
    caderno_erros: false
  },

  // Simulado ativo
  simulado: {
    ativo: false,
    id: null,
    questoes: [],
    indice: 0,
    respostas: {}, // { id: 'B' }
    segundosRestantes: 0,
    intervaloTimer: null,
    tempoTotal: 0
  },

  // Edital
  editalAtivoId: null,
  editaisDisponiveis: [],

  // Estatísticas
  estatisticas: null
};

// ================= INICIALIZAÇÃO =================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initTrialSystem();
  initKeyboardShortcuts();
  carregarContadorVisitas();
  carregarFiltrosDropdown();
  carregarQuestoes();
  carregarEstatisticas();
  carregarListaEditais();
});

// ================= TEMA ESCURO / CLARO =================
function initTheme() {
  const salvo = localStorage.getItem('aprovaquest_theme');
  if (salvo === 'dark' || (!salvo && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('aprovaquest_theme', isDark ? 'dark' : 'light');
  if (window.lucide) lucide.createIcons();
}

// ================= NAVEGAÇÃO SPA =================
function navegarPara(visaoId) {
  state.visao = visaoId;
  
  // Atualizar botões de navegação no topo e mobile
  document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
  const navBtn = document.getElementById(`nav-${visaoId}`);
  if (navBtn) navBtn.classList.add('active');

  document.querySelectorAll('.mobile-nav-btn').forEach(el => el.classList.remove('text-brand-600', 'dark:text-indigo-400'));

  // Ocultar todas as seções e exibir a selecionada
  document.querySelectorAll('.view-panel').forEach(el => el.classList.add('hidden'));
  const painel = document.getElementById(`view-${visaoId}`);
  if (painel) painel.classList.remove('hidden');

  // Carregamentos sob demanda
  if (visaoId === 'estatisticas') carregarEstatisticas();
  if (visaoId === 'edital') carregarEditalSelecionado();
  if (visaoId === 'caderno') carregarCadernoErros();

  if (window.lucide) lucide.createIcons();
}

// ================= ATALHOS DE TECLADO (PC / NOTEBOOK) =================
function initKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    // Ignorar se o usuário estiver digitando em campos de texto
    const tag = e.target.tagName.toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select') return;

    if (state.visao === 'questoes' && state.questoes.length > 0) {
      const key = e.key.toUpperCase();
      
      // Teclas A, B, C, D, E
      if (['A', 'B', 'C', 'D', 'E'].includes(key)) {
        e.preventDefault();
        selecionarAlternativa(key);
      }
      // Atalhos Certo / Errado para Cebraspe
      if (key === 'C' && document.getElementById('alt-opt-C')) {
        selecionarAlternativa('C');
      }
      // Enter para Responder
      if (e.key === 'Enter') {
        e.preventDefault();
        confirmarResposta();
      }
      // Seta Direita para Próxima
      if (e.key === 'ArrowRight') {
        e.preventDefault();
        irProximaQuestao();
      }
      // Seta Esquerda para Anterior
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        irQuestaoAnterior();
      }
    }
  });
}

// ================= BANCO DE QUESTÕES & API =================
async function carregarFiltrosDropdown() {
  try {
    const res = await fetch('/api/filtros');
    const data = await res.parseJSON ? await res.parseJSON() : await res.json();
    
    preencherSelect('filtro-banca', data.bancas);
    preencherSelect('filtro-materia', data.materias);
    preencherSelect('filtro-assunto', data.assuntos);
  } catch (err) {
    console.error('Erro ao carregar filtros:', err);
  }
}

function preencherSelect(selectId, itens) {
  const el = document.getElementById(selectId);
  if (!el) return;
  const atual = el.value;
  el.innerHTML = `<option value="">Todos(as)</option>`;
  itens.forEach(item => {
    const opt = document.createElement('option');
    opt.value = item;
    opt.textContent = item;
    el.appendChild(opt);
  });
  el.value = atual;
}

async function carregarQuestoes() {
  try {
    const params = new URLSearchParams();
    if (state.filtros.busca) params.append('busca', state.filtros.busca);
    if (state.filtros.banca) params.append('banca', state.filtros.banca);
    if (state.filtros.materia) params.append('materia', state.filtros.materia);
    if (state.filtros.assunto) params.append('assunto', state.filtros.assunto);
    if (state.filtros.tipo) params.append('tipo', state.filtros.tipo);
    if (state.filtros.so_lei) params.append('so_lei', 'true');
    if (state.filtros.so_sumula) params.append('so_sumula', 'true');
    if (state.filtros.nao_resolvidas) params.append('nao_resolvidas', 'true');
    if (state.filtros.somente_erradas) params.append('somente_erradas', 'true');
    if (state.filtros.favoritas) params.append('favoritas', 'true');
    if (state.filtros.caderno_erros) params.append('caderno_erros', 'true');

    const res = await fetch(`/api/questoes?${params.toString()}`);
    const data = await res.json();
    state.questoes = data.questoes || [];
    state.indiceAtual = 0;

    renderizarQuestaoAtual();
    renderizarGridQuestoes();
    atualizarContadorGrid();
  } catch (err) {
    console.error('Erro ao buscar questões:', err);
  }
}

function renderizarQuestaoAtual() {
  const container = document.getElementById('card-questao');
  const comContainer = document.getElementById('card-comentario');
  
  if (state.questoes.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12">
        <i data-lucide="inbox" class="w-12 h-12 text-slate-400 mx-auto mb-3"></i>
        <h4 class="font-bold text-lg text-slate-700 dark:text-slate-300">Nenhuma questão encontrada</h4>
        <p class="text-xs text-slate-500 mt-1 mb-4">Tente afrouxar os filtros ou buscar por outro termo.</p>
        <button onclick="limparFiltros()" class="px-4 py-2 rounded-xl bg-brand-600 text-white text-xs font-bold">Limpar Filtros</button>
      </div>
    `;
    comContainer.classList.add('hidden');
    if (window.lucide) lucide.createIcons();
    return;
  }

  const q = state.questoes[state.indiceAtual];
  state.opcaoSelecionada = q.usuario_escolha || null;
  state.questaoRespondida = q.usuario_ja_respondeu || false;

  // Atualizar Metadados
  document.getElementById('badge-q-indice').textContent = `Questão ${state.indiceAtual + 1} de ${state.questoes.length}`;
  document.getElementById('badge-q-banca').textContent = q.banca || 'Geral';
  document.getElementById('badge-q-ano').textContent = q.ano || '2024';
  document.getElementById('badge-q-orgao').textContent = q.orgao || q.concurso || 'Concurso';

  // Badges de Lei Seca e Súmula
  const bLei = document.getElementById('badge-q-lei');
  if (q.eh_lei_seca) bLei.classList.remove('hidden'); else bLei.classList.add('hidden');
  
  const bSum = document.getElementById('badge-q-sumula');
  if (q.eh_sumula) bSum.classList.remove('hidden'); else bSum.classList.add('hidden');

  // Botões Favorita / Caderno de Erros
  const btnFav = document.getElementById('btn-fav-atual');
  if (q.favorita) {
    btnFav.classList.add('text-amber-500', 'fill-current');
  } else {
    btnFav.classList.remove('text-amber-500', 'fill-current');
  }

  const btnCad = document.getElementById('btn-caderno-atual');
  if (q.no_caderno_erros) {
    btnCad.classList.add('text-rose-500', 'fill-current');
  } else {
    btnCad.classList.remove('text-rose-500', 'fill-current');
  }

  // Título e Enunciado
  document.getElementById('q-materia').textContent = q.materia;
  document.getElementById('q-assunto').textContent = q.assunto;
  document.getElementById('q-enunciado').textContent = q.enunciado;

  // Renderizar Alternativas
  const altContainer = document.getElementById('q-alternativas');
  altContainer.innerHTML = '';

  const alternativas = q.alternativas || {};
  Object.keys(alternativas).forEach(letra => {
    const texto = alternativas[letra];
    const item = document.createElement('div');
    item.id = `alt-opt-${letra}`;
    item.className = 'opcao-resposta p-3.5 sm:p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800/60 flex items-start gap-3';
    
    // Se o usuário já respondeu anteriormente
    if (state.questaoRespondida) {
      if (letra === q.gabarito) {
        item.classList.add('correta');
      } else if (letra === q.usuario_escolha && !q.usuario_acertou) {
        item.classList.add('errada');
      }
    } else if (state.opcaoSelecionada === letra) {
      item.classList.add('selecionada');
    }

    item.onclick = () => {
      if (!state.questaoRespondida) {
        selecionarAlternativa(letra);
      }
    };

    item.innerHTML = `
      <span class="w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
        state.opcaoSelecionada === letra ? 'bg-brand-600 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
      }">${letra}</span>
      <span class="text-sm sm:text-base leading-relaxed text-slate-800 dark:text-slate-200">${texto}</span>
    `;

    altContainer.appendChild(item);
  });

  // Atualizar estado do botão Responder
  const btnResp = document.getElementById('btn-responder');
  if (state.questaoRespondida) {
    btnResp.classList.add('opacity-50', 'cursor-not-allowed');
    btnResp.textContent = 'Respondida';
    exibirComentario(q);
  } else {
    btnResp.classList.remove('opacity-50', 'cursor-not-allowed');
    btnResp.innerHTML = `<i data-lucide="check-circle" class="w-4 h-4"></i> Responder`;
    comContainer.classList.add('hidden');
  }

  // Atualizar estado dos botões Anterior/Próxima
  document.getElementById('btn-anterior').disabled = (state.indiceAtual === 0);
  document.getElementById('btn-proxima').disabled = (state.indiceAtual >= state.questoes.length - 1);

  destacarQuestaoNoGrid();
  if (window.lucide) lucide.createIcons();
}

function selecionarAlternativa(letra) {
  if (state.questaoRespondida) return;
  state.opcaoSelecionada = letra;
  
  // Atualizar estilos visuais das alternativas
  const q = state.questoes[state.indiceAtual];
  Object.keys(q.alternativas).forEach(l => {
    const el = document.getElementById(`alt-opt-${l}`);
    if (el) {
      if (l === letra) {
        el.classList.add('selecionada');
        el.querySelector('span:first-child').className = 'w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 bg-brand-600 text-white';
      } else {
        el.classList.remove('selecionada');
        el.querySelector('span:first-child').className = 'w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300';
      }
    }
  });
}

async function confirmarResposta() {
  if (state.questaoRespondida) return;
  if (!state.opcaoSelecionada) {
    alert('Por favor, selecione uma alternativa antes de responder.');
    return;
  }

  const q = state.questoes[state.indiceAtual];
  try {
    const res = await fetch('/api/questoes/responder', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        questao_id: q.id,
        alternativa_escolhida: state.opcaoSelecionada,
        tempo_gasto_segundos: 30
      })
    });
    const data = await res.json();
    
    // Atualizar estado local da questão
    q.usuario_ja_respondeu = true;
    q.usuario_acertou = data.acertou;
    q.usuario_escolha = state.opcaoSelecionada;
    q.no_caderno_erros = data.no_caderno_erros;
    state.questaoRespondida = true;

    // Atualizar visual das alternativas com cores de acerto/erro
    Object.keys(q.alternativas).forEach(l => {
      const el = document.getElementById(`alt-opt-${l}`);
      if (el) {
        if (l === data.gabarito) {
          el.classList.add('correta');
        } else if (l === state.opcaoSelecionada && !data.acertou) {
          el.classList.add('errada');
        }
      }
    });

    // Exibir comentário
    exibirComentario(q, data.acertou, data.gabarito);
    renderizarGridQuestoes();
    carregarEstatisticas();
  } catch (err) {
    console.error('Erro ao responder questão:', err);
  }
}

function exibirComentario(q, acertou = q.usuario_acertou, gabarito = q.gabarito) {
  const comContainer = document.getElementById('card-comentario');
  comContainer.classList.remove('hidden');

  const banner = document.getElementById('banner-resultado');
  const icone = document.getElementById('icon-resultado');
  const titulo = document.getElementById('titulo-resultado');
  const subtitulo = document.getElementById('subtitulo-resultado');

  if (acertou) {
    banner.className = 'mb-5 p-4 rounded-xl flex items-center gap-3 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-200';
    icone.className = 'w-10 h-10 rounded-full flex items-center justify-center font-bold text-xl bg-emerald-500 text-white';
    icone.innerHTML = '✓';
    titulo.textContent = 'Parabéns, você acertou!';
    subtitulo.textContent = `Gabarito Oficial: Letra ${gabarito}`;
  } else {
    banner.className = 'mb-5 p-4 rounded-xl flex items-center gap-3 bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-800 text-rose-800 dark:text-rose-200';
    icone.className = 'w-10 h-10 rounded-full flex items-center justify-center font-bold text-xl bg-rose-500 text-white';
    icone.innerHTML = '✕';
    titulo.textContent = 'Atenção, você errou esta questão!';
    subtitulo.textContent = `Resposta correta: Letra ${gabarito} (Adicionada ao seu Caderno de Erros)`;
  }

  // Preencher abas do comentário
  const com = q.comentario || {};
  document.getElementById('conteudo-tab-resumo').innerHTML = `
    <p class="font-medium">${com.resumo || 'Sem resumo disponível.'}</p>
  `;

  // Análise das alternativas
  const analiseEl = document.getElementById('conteudo-tab-alternativas');
  analiseEl.innerHTML = '';
  const analises = com.analise_alternativas || {};
  Object.keys(analises).forEach(l => {
    const div = document.createElement('div');
    const isCorreta = (l === gabarito);
    div.className = `p-3 rounded-xl border ${isCorreta ? 'border-emerald-200 dark:border-emerald-800/80 bg-emerald-50/50 dark:bg-emerald-950/30 font-semibold' : 'border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/40'}`;
    div.innerHTML = `<span class="font-bold text-brand-600 dark:text-indigo-400 mr-1">${l})</span> ${analises[l]}`;
    analiseEl.appendChild(div);
  });

  // Legislação / Súmula
  document.getElementById('conteudo-tab-legislacao').innerHTML = `
    <div class="p-3.5 rounded-xl bg-amber-50/60 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800">
      <span class="font-bold text-amber-800 dark:text-amber-300 block mb-1">⚖️ Fundamento Legal / Jurisprudência:</span>
      <p class="text-amber-950 dark:text-amber-200">${com.fundamentacao_legal || 'Fundamentação na jurisprudência das bancas examinadoras.'}</p>
    </div>
  `;

  // Pegadinha da Banca
  document.getElementById('conteudo-tab-pegadinha').innerHTML = `
    <div class="p-3.5 rounded-xl bg-purple-50/60 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800">
      <span class="font-bold text-purple-800 dark:text-purple-300 block mb-1">⚠️ Como a banca costuma derrubar o candidato:</span>
      <p class="text-purple-950 dark:text-purple-200">${com.pegadinha_da_banca || 'Atenção aos detalhes dos enunciados e prazos legais!'}</p>
    </div>
  `;

  trocarAbaComentario('resumo');
}

function trocarAbaComentario(abaId) {
  document.querySelectorAll('.tab-comentario').forEach(el => {
    el.classList.remove('border-brand-600', 'text-brand-600', 'dark:text-indigo-400');
    el.classList.add('border-transparent');
  });
  document.querySelectorAll('.aba-conteudo').forEach(el => el.classList.add('hidden'));

  const btn = document.getElementById(`tab-${abaId}`);
  if (btn) {
    btn.classList.add('border-brand-600', 'text-brand-600', 'dark:text-indigo-400');
    btn.classList.remove('border-transparent');
  }

  const conteudo = document.getElementById(`conteudo-tab-${abaId}`);
  if (conteudo) conteudo.classList.remove('hidden');
}

function irProximaQuestao() {
  if (state.indiceAtual < state.questoes.length - 1) {
    state.indiceAtual++;
    renderizarQuestaoAtual();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function irQuestaoAnterior() {
  if (state.indiceAtual > 0) {
    state.indiceAtual--;
    renderizarQuestaoAtual();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function pularParaQuestao(idx) {
  if (idx >= 0 && idx < state.questoes.length) {
    state.indiceAtual = idx;
    renderizarQuestaoAtual();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

// ================= GRADE DE QUESTÕES =================
function renderizarGridQuestoes() {
  const grid = document.getElementById('grid-questoes');
  if (!grid) return;
  grid.innerHTML = '';

  state.questoes.forEach((q, idx) => {
    const btn = document.createElement('button');
    btn.className = 'grid-q-btn';
    btn.textContent = idx + 1;
    
    if (q.usuario_ja_respondeu) {
      if (q.usuario_acertou) btn.classList.add('acerto');
      else btn.classList.add('erro');
    }

    if (idx === state.indiceAtual) {
      btn.classList.add('atual');
    }

    btn.onclick = () => pularParaQuestao(idx);
    grid.appendChild(btn);
  });
}

function destacarQuestaoNoGrid() {
  const buttons = document.querySelectorAll('.grid-q-btn');
  buttons.forEach((btn, idx) => {
    if (idx === state.indiceAtual) btn.classList.add('atual');
    else btn.classList.remove('atual');
  });
}

function atualizarContadorGrid() {
  const el = document.getElementById('grid-contador-total');
  if (el) el.textContent = `${state.questoes.length} no filtro`;
}

// ================= FILTROS =================
function togglePainelFiltros() {
  const painel = document.getElementById('painel-filtros-avancados');
  painel.classList.toggle('hidden');
}

function toggleFiltroRapido(chave) {
  state.filtros[chave] = !state.filtros[chave];
  
  // Atualizar visual do botão
  const mapaIds = {
    so_lei: 'btn-filtro-lei',
    so_sumula: 'btn-filtro-sumula',
    nao_resolvidas: 'btn-filtro-nao-resolvidas',
    somente_erradas: 'btn-filtro-erradas',
    favoritas: 'btn-filtro-favoritas'
  };
  const btn = document.getElementById(mapaIds[chave]);
  if (btn) {
    btn.classList.toggle('active', state.filtros[chave]);
  }
  
  carregarQuestoes();
}

function aplicarFiltros() {
  state.filtros.busca = document.getElementById('filtro-busca').value.trim();
  state.filtros.banca = document.getElementById('filtro-banca').value;
  state.filtros.materia = document.getElementById('filtro-materia').value;
  state.filtros.assunto = document.getElementById('filtro-assunto').value;
  state.filtros.tipo = document.getElementById('filtro-tipo').value;

  carregarQuestoes();
}

function limparFiltros() {
  state.filtros = {
    busca: '',
    banca: '',
    materia: '',
    assunto: '',
    tipo: '',
    so_lei: false,
    so_sumula: false,
    nao_resolvidas: false,
    somente_erradas: false,
    favoritas: false,
    caderno_erros: false
  };

  document.getElementById('filtro-busca').value = '';
  document.getElementById('filtro-banca').value = '';
  document.getElementById('filtro-materia').value = '';
  document.getElementById('filtro-assunto').value = '';
  document.getElementById('filtro-tipo').value = '';

  document.querySelectorAll('.badge-quick').forEach(el => el.classList.remove('active'));
  carregarQuestoes();
}

// ================= FAVORITAS & CADERNO DE ERROS =================
async function toggleFavoritaAtual() {
  const q = state.questoes[state.indiceAtual];
  if (!q) return;

  try {
    const res = await fetch('/api/favoritas/toggle', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ questao_id: q.id })
    });
    const data = await res.json();
    q.favorita = data.favorita;
    
    const btn = document.getElementById('btn-fav-atual');
    btn.classList.toggle('text-amber-500', q.favorita);
    btn.classList.toggle('fill-current', q.favorita);
    carregarEstatisticas();
  } catch (err) {
    console.error('Erro ao alternar favorita:', err);
  }
}

async function toggleCadernoErrosAtual() {
  const q = state.questoes[state.indiceAtual];
  if (!q) return;

  try {
    const res = await fetch('/api/caderno-erros/toggle', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ questao_id: q.id })
    });
    const data = await res.json();
    q.no_caderno_erros = data.no_caderno;
    
    const btn = document.getElementById('btn-caderno-atual');
    btn.classList.toggle('text-rose-500', q.no_caderno_erros);
    btn.classList.toggle('fill-current', q.no_caderno_erros);
    carregarEstatisticas();
  } catch (err) {
    console.error('Erro ao alternar caderno de erros:', err);
  }
}

// ================= TUTOR IA =================
function abrirTutorIA() {
  const modal = document.getElementById('modal-tutor-ia');
  modal.classList.remove('hidden');
  document.getElementById('tutor-pergunta-input').focus();
  if (window.lucide) lucide.createIcons();
}

function fecharTutorIA() {
  document.getElementById('modal-tutor-ia').classList.add('hidden');
}

async function solicitarAjudaTutor(modo) {
  const q = state.questoes[state.indiceAtual];
  if (!q) return;

  const box = document.getElementById('tutor-resposta-box');
  const pergunta = document.getElementById('tutor-pergunta-input').value.trim();

  box.innerHTML = `<span class="flex items-center gap-2"><i data-lucide="loader" class="w-4 h-4 animate-spin text-brand-600"></i> Consultando Mentor Concurseiro IA...</span>`;
  if (window.lucide) lucide.createIcons();

  try {
    const res = await fetch('/api/ia/tutor', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        questao_id: q.id,
        modo: modo,
        pergunta: pergunta
      })
    });
    const data = await res.json();
    box.innerHTML = data.resposta.replace(/\n/g, '<br>');
  } catch (err) {
    box.textContent = 'Erro ao consultar o Tutor. Tente novamente.';
  }
}

// ================= MODO SIMULADO =================
function atualizarFocoSimulado() {
  const selecionado = document.querySelector('input[name="tipo_simulado"]:checked').value;
  document.querySelectorAll('.simulado-tipo-card').forEach(card => {
    const radio = card.querySelector('input');
    if (radio.checked) {
      card.classList.add('border-brand-500', 'bg-brand-50/40', 'dark:bg-indigo-950/30');
      card.classList.remove('border-slate-200', 'dark:border-slate-800');
    } else {
      card.classList.remove('border-brand-500', 'bg-brand-50/40', 'dark:bg-indigo-950/30');
      card.classList.add('border-slate-200', 'dark:border-slate-800');
    }
  });
}

async function iniciarSimulado() {
  const tipo = document.querySelector('input[name="tipo_simulado"]:checked').value;
  const qtd = parseInt(document.getElementById('sim-qtd').value);
  const tempo = parseInt(document.getElementById('sim-tempo').value);

  try {
    const res = await fetch('/api/simulado/gerar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tipo: tipo,
        quantidade: qtd,
        tempo_minutos: tempo
      })
    });
    const data = await res.json();

    state.simulado = {
      ativo: true,
      id: data.simulado_id,
      questoes: data.questoes,
      indice: 0,
      respostas: {},
      segundosRestantes: data.tempo_segundos,
      tempoTotal: data.tempo_segundos,
      intervaloTimer: null
    };

    document.getElementById('config-simulado').classList.add('hidden');
    document.getElementById('resultado-simulado').classList.add('hidden');
    document.getElementById('arena-simulado').classList.remove('hidden');

    iniciarCronometroSimulado();
    renderizarQuestaoSimulado();
  } catch (err) {
    console.error('Erro ao gerar simulado:', err);
  }
}

function iniciarCronometroSimulado() {
  if (state.simulado.segundosRestantes <= 0) {
    document.getElementById('sim-tempo-restante').textContent = 'Livre';
    return;
  }

  atualizarDisplayCronometro();
  state.simulado.intervaloTimer = setInterval(() => {
    state.simulado.segundosRestantes--;
    atualizarDisplayCronometro();

    if (state.simulado.segundosRestantes <= 0) {
      clearInterval(state.simulado.intervaloTimer);
      alert('⏰ O tempo do simulado encerrou! Enviando suas respostas agora...');
      finalizarSimulado();
    }
  }, 1000);
}

function atualizarDisplayCronometro() {
  const s = state.simulado.segundosRestantes;
  const min = Math.floor(s / 60);
  const sec = s % 60;
  const display = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
  document.getElementById('sim-tempo-restante').textContent = display;
}

function renderizarQuestaoSimulado() {
  const q = state.simulado.questoes[state.simulado.indice];
  if (!q) return;

  document.getElementById('sim-progresso-txt').textContent = `Questão ${state.simulado.indice + 1} de ${state.simulado.questoes.length}`;
  document.getElementById('sim-q-materia').textContent = `${q.materia} • ${q.assunto}`;
  document.getElementById('sim-q-info').textContent = `${q.banca} (${q.ano})`;
  document.getElementById('sim-q-enunciado').textContent = q.enunciado;

  const containerAlt = document.getElementById('sim-q-alternativas');
  containerAlt.innerHTML = '';

  const respondidaLetra = state.simulado.respostas[q.id];

  Object.keys(q.alternativas).forEach(l => {
    const item = document.createElement('div');
    item.className = `opcao-resposta p-3.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-800 flex items-start gap-3 ${
      respondidaLetra === l ? 'selecionada' : ''
    }`;
    item.onclick = () => {
      state.simulado.respostas[q.id] = l;
      renderizarQuestaoSimulado();
      renderizarBolinhasNavegacaoSimulado();
    };

    item.innerHTML = `
      <span class="w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
        respondidaLetra === l ? 'bg-brand-600 text-white' : 'bg-slate-100 dark:bg-slate-700'
      }">${l}</span>
      <span class="text-sm text-slate-800 dark:text-slate-200">${q.alternativas[l]}</span>
    `;
    containerAlt.appendChild(item);
  });

  renderizarBolinhasNavegacaoSimulado();
}

function renderizarBolinhasNavegacaoSimulado() {
  const container = document.getElementById('sim-indicadores-navegacao');
  container.innerHTML = '';
  state.simulado.questoes.forEach((q, idx) => {
    const dot = document.createElement('button');
    const respondida = !!state.simulado.respostas[q.id];
    dot.className = `w-7 h-7 rounded-lg font-bold text-xs flex items-center justify-center transition-all ${
      idx === state.simulado.indice ? 'ring-2 ring-brand-500 scale-110' : ''
    } ${
      respondida ? 'bg-indigo-600 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
    }`;
    dot.textContent = idx + 1;
    dot.onclick = () => {
      state.simulado.indice = idx;
      renderizarQuestaoSimulado();
    };
    container.appendChild(dot);
  });
}

function simuladoProxima() {
  if (state.simulado.indice < state.simulado.questoes.length - 1) {
    state.simulado.indice++;
    renderizarQuestaoSimulado();
  }
}

function simuladoAnterior() {
  if (state.simulado.indice > 0) {
    state.simulado.indice--;
    renderizarQuestaoSimulado();
  }
}

function solicitarFinalizarSimulado() {
  const respondidas = Object.keys(state.simulado.respostas).length;
  const total = state.simulado.questoes.length;
  if (respondidas < total) {
    if (!confirm(`Você respondeu ${respondidas} de ${total} questões. Deseja realmente entregar a prova agora?`)) {
      return;
    }
  }
  finalizarSimulado();
}

async function finalizarSimulado() {
  if (state.simulado.intervaloTimer) clearInterval(state.simulado.intervaloTimer);
  const tempoGasto = state.simulado.tempoTotal - state.simulado.segundosRestantes;

  try {
    const res = await fetch('/api/simulado/finalizar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        simulado_id: state.simulado.id,
        respostas: state.simulado.respostas,
        tempo_gasto_segundos: tempoGasto,
        data: new Date().toLocaleDateString('pt-BR')
      })
    });
    const data = await res.json();
    exibirResultadoSimulado(data);
  } catch (err) {
    console.error('Erro ao finalizar simulado:', err);
  }
}

function exibirResultadoSimulado(data) {
  document.getElementById('arena-simulado').classList.add('hidden');
  const resContainer = document.getElementById('resultado-simulado');
  resContainer.classList.remove('hidden');

  const aprovado = data.porcentagem >= 75;
  resContainer.innerHTML = `
    <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 sm:p-8 border border-slate-200 dark:border-slate-800 shadow-sm text-center">
      <div class="w-16 h-16 rounded-full mx-auto flex items-center justify-center text-3xl font-black mb-3 ${
        aprovado ? 'bg-emerald-100 text-emerald-600' : 'bg-amber-100 text-amber-600'
      }">
        ${aprovado ? '🏆' : '🎯'}
      </div>
      <h3 class="text-2xl font-black text-slate-900 dark:text-white">Simulado Concluído!</h3>
      <p class="text-sm text-slate-500 mt-1">${
        aprovado ? 'Excelente resultado! Você atingiu pontuação compatível com vagas de ampla concorrência.' : 'Bom treino! Revise os pontos fracos apontados no relatório abaixo.'
      }</p>

      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 my-6">
        <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800">
          <span class="text-xs text-slate-500">Taxa de Acerto</span>
          <h4 class="text-2xl font-black text-brand-600 dark:text-indigo-400 mt-1">${data.porcentagem}%</h4>
        </div>
        <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800">
          <span class="text-xs text-slate-500">Acertos</span>
          <h4 class="text-2xl font-black text-emerald-600 mt-1">${data.acertos}/${data.total}</h4>
        </div>
        <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800">
          <span class="text-xs text-slate-500">Erros</span>
          <h4 class="text-2xl font-black text-rose-600 mt-1">${data.erros}</h4>
        </div>
        <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800">
          <span class="text-xs text-slate-500">Tempo Gasto</span>
          <h4 class="text-2xl font-black text-slate-700 dark:text-slate-300 mt-1">${Math.round(data.tempo_gasto_segundos / 60)} min</h4>
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-3">
        <button onclick="novoSimulado()" class="px-6 py-2.5 rounded-xl bg-brand-600 text-white font-bold text-sm">Fazer Novo Simulado</button>
        <button onclick="navegarPara('caderno')" class="px-6 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 font-bold text-sm">Ver Caderno de Erros</button>
      </div>
    </div>

    <!-- Lista de Revisão de Questões do Simulado -->
    <div class="space-y-4">
      <h4 class="text-lg font-bold text-slate-900 dark:text-white">Gabarito Comentado do Simulado</h4>
      ${data.detalhes.map((item, idx) => `
        <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 border ${
          item.acertou ? 'border-emerald-200 dark:border-emerald-900/60' : 'border-rose-200 dark:border-rose-900/60'
        }">
          <div class="flex items-center justify-between text-xs mb-2">
            <span class="font-bold">Questão ${idx + 1} • ${item.materia}</span>
            <span class="font-bold px-2 py-0.5 rounded-full ${
              item.acertou ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'
            }">${item.acertou ? 'Você Acertou' : `Você Marcou ${item.escolhida} (Gabarito ${item.gabarito})`}</span>
          </div>
          <p class="text-sm text-slate-800 dark:text-slate-200 mb-3">${item.enunciado}</p>
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800 text-xs text-slate-700 dark:text-slate-300">
            <strong>Comentário:</strong> ${item.comentario?.resumo || 'Comentário disponível no banco de questões.'}
          </div>
        </div>
      `).join('')}
    </div>
  `;
  if (window.lucide) lucide.createIcons();
}

function novoSimulado() {
  document.getElementById('resultado-simulado').classList.add('hidden');
  document.getElementById('config-simulado').classList.remove('hidden');
}

// ================= EDITAL VERTICALIZADO =================
async function carregarListaEditais() {
  try {
    const res = await fetch('/api/editais');
    const editais = await res.json();
    state.editaisDisponiveis = editais;

    const select = document.getElementById('seletor-edital');
    select.innerHTML = '';
    editais.forEach(ed => {
      const opt = document.createElement('option');
      opt.value = ed.id;
      opt.textContent = `${ed.nome} (${ed.cargo})`;
      select.appendChild(opt);
    });

    if (editais.length > 0) {
      state.editalAtivoId = editais[0].id;
      carregarEditalSelecionado();
    }
  } catch (err) {
    console.error('Erro ao carregar editais:', err);
  }
}

async function carregarEditalSelecionado() {
  const select = document.getElementById('seletor-edital');
  const editalId = select.value || state.editalAtivoId;
  if (!editalId) return;
  state.editalAtivoId = editalId;

  try {
    const res = await fetch(`/api/edital/detalhe?id=${editalId}`);
    const data = await res.json();
    renderizarArvoreEdital(data.edital, data.progresso || {});
  } catch (err) {
    console.error('Erro ao carregar detalhe do edital:', err);
  }
}

function renderizarArvoreEdital(edital, progresso) {
  const container = document.getElementById('conteudo-edital-arvore');
  container.innerHTML = '';

  let totalTopicos = 0;
  let concluidos = 0;

  edital.modulos.forEach(mod => {
    const modEl = document.createElement('div');
    modEl.className = 'bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm';
    
    let htmlMod = `
      <h3 class="font-bold text-base text-brand-600 dark:text-indigo-400 mb-4 pb-2 border-b border-slate-100 dark:border-slate-800">
        ${mod.nome}
      </h3>
      <div class="space-y-5">
    `;

    mod.disciplinas.forEach(disc => {
      htmlMod += `
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="font-extrabold text-sm text-slate-800 dark:text-slate-200">${disc.nome}</span>
            <button onclick="filtrarBancoPorDisciplina('${disc.nome}')" class="text-xs text-brand-600 hover:underline font-semibold flex items-center gap-1">
              🎯 Praticar Questões
            </button>
          </div>
          <div class="space-y-1.5 pl-2 border-l-2 border-slate-200 dark:border-slate-800">
      `;

      disc.topicos.forEach(topico => {
        totalTopicos++;
        const chave = `${disc.nome}::${topico}`;
        const p = progresso[chave] || { teoria: false, resumo: false, questoes: false };
        const is100 = p.teoria && p.questoes;
        if (is100) concluidos++;

        htmlMod += `
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 p-2 rounded-xl hover:bg-slate-50 dark:hover:bg-slate-800/40 text-xs">
            <span class="text-slate-700 dark:text-slate-300 font-medium ${is100 ? 'line-through text-slate-400' : ''}">${topico}</span>
            
            <div class="flex items-center gap-3 shrink-0">
              <label class="flex items-center gap-1 cursor-pointer">
                <input type="checkbox" ${p.teoria ? 'checked' : ''} onchange="salvarCheckEdital('${edital.id}', '${chave}', 'teoria', this.checked)" class="rounded text-brand-600">
                <span class="text-[11px] text-slate-500">Teoria</span>
              </label>
              <label class="flex items-center gap-1 cursor-pointer">
                <input type="checkbox" ${p.resumo ? 'checked' : ''} onchange="salvarCheckEdital('${edital.id}', '${chave}', 'resumo', this.checked)" class="rounded text-brand-600">
                <span class="text-[11px] text-slate-500">Resumo</span>
              </label>
              <label class="flex items-center gap-1 cursor-pointer">
                <input type="checkbox" ${p.questoes ? 'checked' : ''} onchange="salvarCheckEdital('${edital.id}', '${chave}', 'questoes', this.checked)" class="rounded text-brand-600">
                <span class="text-[11px] text-slate-500">Questões</span>
              </label>
            </div>
          </div>
        `;
      });

      htmlMod += `</div></div>`;
    });

    htmlMod += `</div>`;
    modEl.innerHTML = htmlMod;
    container.appendChild(modEl);
  });

  // Atualizar Barra Superior
  const pct = totalTopicos > 0 ? Math.round((concluidos / totalTopicos) * 100) : 0;
  document.getElementById('edital-porcentagem-topo').textContent = `${pct}%`;
  document.getElementById('edital-barra-topo').style.width = `${pct}%`;
  document.getElementById('edital-topicos-concluidos-txt').textContent = `${concluidos} de ${totalTopicos} tópicos concluídos`;
}

async function salvarCheckEdital(editalId, chave, tipo, valor) {
  try {
    await fetch('/api/edital/progresso', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        edital_id: editalId,
        chave_topico: chave,
        tipo: tipo,
        valor: valor
      })
    });
    carregarEditalSelecionado();
  } catch (err) {
    console.error('Erro ao salvar progresso:', err);
  }
}

function filtrarBancoPorDisciplina(disciplina) {
  limparFiltros();
  state.filtros.materia = disciplina;
  const select = document.getElementById('filtro-materia');
  if (select) select.value = disciplina;
  navegarPara('questoes');
  carregarQuestoes();
}

// ================= CADERNO DE ERROS =================
async function carregarCadernoErros() {
  try {
    const res = await fetch('/api/questoes?caderno_erros=true');
    const data = await res.json();
    const lista = document.getElementById('lista-caderno-erros');
    lista.innerHTML = '';

    if (!data.questoes || data.questoes.length === 0) {
      lista.innerHTML = `
        <div class="bg-white dark:bg-slate-900 rounded-2xl p-12 text-center border border-slate-200 dark:border-slate-800">
          <i data-lucide="check-circle-2" class="w-12 h-12 text-emerald-500 mx-auto mb-3"></i>
          <h4 class="font-bold text-lg text-slate-800 dark:text-slate-200">Seu Caderno de Erros está Limpo!</h4>
          <p class="text-xs text-slate-500 mt-1">Quando você errar alguma questão no treino ou no simulado, ela será salva aqui automaticamente para você revisar.</p>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    data.questoes.forEach((q, idx) => {
      const card = document.createElement('div');
      card.className = 'bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm';
      card.innerHTML = `
        <div class="flex items-center justify-between text-xs mb-2">
          <span class="font-bold text-brand-600 dark:text-indigo-400">${q.materia} • ${q.assunto}</span>
          <div class="flex items-center gap-2">
            <span class="text-slate-400">${q.banca} (${q.ano})</span>
            <button onclick="removerDoCaderno(${q.id})" title="Remover do Caderno" class="text-slate-400 hover:text-rose-500">
              <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
          </div>
        </div>
        <p class="text-sm text-slate-800 dark:text-slate-200 mb-3">${q.enunciado}</p>
        <div class="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/40 text-xs text-rose-900 dark:text-rose-200 mb-3">
          <strong>Atenção ao Gabarito (${q.gabarito}):</strong> ${q.comentario?.resumo || ''}
        </div>
        <button onclick="treinarQuestaoEspecifica(${q.id})" class="px-4 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-brand-600 hover:text-white font-bold text-xs transition-colors">
          Resolver Esta Questão Novamente
        </button>
      `;
      lista.appendChild(card);
    });

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    console.error('Erro ao carregar caderno de erros:', err);
  }
}

async function removerDoCaderno(qid) {
  await fetch('/api/caderno-erros/toggle', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ questao_id: qid })
  });
  carregarCadernoErros();
  carregarEstatisticas();
}

function iniciarTreinoCadernoErros() {
  limparFiltros();
  state.filtros.caderno_erros = true;
  navegarPara('questoes');
  carregarQuestoes();
}

function treinarQuestaoEspecifica(qid) {
  limparFiltros();
  navegarPara('questoes');
  // Buscar no array e selecionar
  carregarQuestoes().then(() => {
    const idx = state.questoes.findIndex(q => q.id === qid);
    if (idx !== -1) pularParaQuestao(idx);
  });
}

// ================= ESTATÍSTICAS =================
async function carregarEstatisticas() {
  try {
    const res = await fetch('/api/estatisticas');
    const data = await res.json();
    state.estatisticas = data;

    // Atualizar Topo & Card Lateral
    document.getElementById('meta-hoje').textContent = data.total_respondidas;
    document.getElementById('card-prod-taxa').textContent = `${data.taxa_acerto}%`;
    document.getElementById('card-prod-progresso').style.width = `${data.taxa_acerto}%`;
    document.getElementById('card-prod-acertos').textContent = data.total_acertos;
    document.getElementById('card-prod-erros').textContent = data.total_erros;

    // Atualizar Badge do Caderno de Erros no Topo
    const badgeCaderno = document.getElementById('badge-caderno-topo');
    if (data.total_caderno_erros > 0) {
      badgeCaderno.textContent = data.total_caderno_erros;
      badgeCaderno.classList.remove('hidden');
    } else {
      badgeCaderno.classList.add('hidden');
    }

    // Tela de Estatísticas Completa
    const statTotal = document.getElementById('stat-total');
    if (statTotal) statTotal.textContent = data.total_respondidas;
    const statTaxa = document.getElementById('stat-taxa');
    if (statTaxa) statTaxa.textContent = `${data.taxa_acerto}%`;
    const statErros = document.getElementById('stat-erros');
    if (statErros) statErros.textContent = data.total_caderno_erros;
    const statSim = document.getElementById('stat-simulados');
    if (statSim) statSim.textContent = data.simulados_feitos_qtd;

    // Lista por Matéria
    const listaMat = document.getElementById('stats-lista-materias');
    if (listaMat) {
      listaMat.innerHTML = '';
      const materias = Object.keys(data.por_materia || {});
      if (materias.length === 0) {
        listaMat.innerHTML = `<p class="text-xs text-slate-400">Responda questões para gerar o gráfico por matéria.</p>`;
      } else {
        materias.forEach(m => {
          const item = data.por_materia[m];
          listaMat.innerHTML += `
            <div>
              <div class="flex items-center justify-between text-xs font-semibold mb-1">
                <span>${m}</span>
                <span class="text-brand-600 dark:text-indigo-400">${item.taxa}% (${item.acertos}/${item.total})</span>
              </div>
              <div class="w-full bg-slate-100 dark:bg-slate-800 rounded-full h-2">
                <div class="bg-brand-600 h-2 rounded-full" style="width: ${item.taxa}%"></div>
              </div>
            </div>
          `;
        });
      }
    }

    // Lista por Banca
    const listaBan = document.getElementById('stats-lista-bancas');
    if (listaBan) {
      listaBan.innerHTML = '';
      const bancas = Object.keys(data.por_banca || {});
      if (bancas.length === 0) {
        listaBan.innerHTML = `<p class="text-xs text-slate-400">Responda questões para gerar o gráfico por banca examinadora.</p>`;
      } else {
        bancas.forEach(b => {
          const item = data.por_banca[b];
          listaBan.innerHTML += `
            <div>
              <div class="flex items-center justify-between text-xs font-semibold mb-1">
                <span>${b}</span>
                <span class="text-emerald-600 dark:text-emerald-400">${item.taxa}% (${item.acertos}/${item.total})</span>
              </div>
              <div class="w-full bg-slate-100 dark:bg-slate-800 rounded-full h-2">
                <div class="bg-emerald-500 h-2 rounded-full" style="width: ${item.taxa}%"></div>
              </div>
            </div>
          `;
        });
      }
    }

  } catch (err) {
    console.error('Erro ao buscar estatísticas:', err);
  }
}

// ================= MODAL CRIAR QUESTÃO =================
function abrirModalCriarQuestao() {
  document.getElementById('modal-criar-questao').classList.remove('hidden');
}

function fecharModalCriarQuestao() {
  document.getElementById('modal-criar-questao').classList.add('hidden');
}

async function salvarNovaQuestao(e) {
  e.preventDefault();
  const nova = {
    materia: document.getElementById('novo-materia').value.trim(),
    assunto: document.getElementById('novo-assunto').value.trim(),
    banca: document.getElementById('novo-banca').value.trim(),
    enunciado: document.getElementById('novo-enunciado').value.trim(),
    alternativas: {
      A: document.getElementById('novo-alt-a').value.trim(),
      B: document.getElementById('novo-alt-b').value.trim(),
      C: document.getElementById('novo-alt-c').value.trim(),
      D: document.getElementById('novo-alt-d').value.trim(),
      E: document.getElementById('novo-alt-e').value.trim()
    },
    gabarito: document.getElementById('novo-gabarito').value,
    fundamentacao_legal: document.getElementById('novo-artigo').value.trim(),
    comentario_resumo: document.getElementById('novo-comentario').value.trim()
  };

  try {
    await fetch('/api/questoes/criar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nova)
    });
    alert('Questão cadastrada com sucesso no seu banco local!');
    fecharModalCriarQuestao();
    document.getElementById('form-criar-questao').reset();
    carregarFiltrosDropdown();
    carregarQuestoes();
  } catch (err) {
    alert('Erro ao cadastrar questão.');
  }
}

// ================= COMPARTILHAR APP =================
function compartilharApp() {
  const url = window.location.href;
  const texto = '🚀 Estou estudando para concursos no AprovaQuest: 100% grátis, sem anúncios, com questões comentadas, simulados e caderno de erros! Acesse: ' + url;

  if (navigator.share) {
    navigator.share({
      title: 'AprovaQuest - Concursos Públicos Sem Anúncios',
      text: texto,
      url: url
    }).catch(() => {});
  } else if (navigator.clipboard) {
    navigator.clipboard.writeText(url).then(() => {
      alert('📋 Link do AprovaQuest copiado com sucesso! Agora é só colar no seu grupo de concurseiros.');
    }).catch(() => {
      prompt('Copie o link abaixo para enviar ao grupo:', url);
    });
  } else {
    prompt('Copie o link abaixo para enviar ao grupo:', url);
  }
}

// ================= SISTEMA DE PERÍODO DE TESTE (5 DIAS) =================
const TRIAL_CONFIG = {
  DIAS_TESTE: 5,
  CHAVE_STORAGE_INICIO: 'aprovaquest_trial_start_v1',
  CHAVE_STORAGE_VIP: 'aprovaquest_vip_unlocked_v1',
  CHAVES_VALIDAS: ['VIP2026', 'APROVA2026', 'ADMIN2026', 'CONCURSEIRO2026']
};

function initTrialSystem() {
  const badge = document.getElementById('badge-trial');
  const txt = document.getElementById('trial-tempo-txt');

  // 1. Verificar se possui chave VIP desbloqueada
  if (localStorage.getItem(TRIAL_CONFIG.CHAVE_STORAGE_VIP) === 'true') {
    if (badge) {
      badge.classList.remove('hidden');
      badge.className = 'flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-full text-[11px] sm:text-xs font-bold bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800 shadow-sm';
      badge.innerHTML = '<i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-500"></i><span>Acesso VIP Vitalício</span>';
      if (window.lucide) lucide.createIcons();
    }
    return;
  }

  // 2. Verificar primeiro acesso
  let inicio = localStorage.getItem(TRIAL_CONFIG.CHAVE_STORAGE_INICIO);
  if (!inicio) {
    inicio = Date.now().toString();
    localStorage.setItem(TRIAL_CONFIG.CHAVE_STORAGE_INICIO, inicio);
  }

  const tempoInicio = parseInt(inicio, 10);
  const agora = Date.now();
  const limiteMs = TRIAL_CONFIG.DIAS_TESTE * 24 * 60 * 60 * 1000;
  const decorridoMs = agora - tempoInicio;
  const restanteMs = limiteMs - decorridoMs;

  if (restanteMs <= 0) {
    // EXPIRADO!
    exibirTelaBloqueioTrial();
  } else {
    // ATIVO DENTRO DOS 5 DIAS
    const dias = Math.ceil(restanteMs / (24 * 60 * 60 * 1000));
    const horas = Math.ceil(restanteMs / (60 * 60 * 1000));

    if (badge && txt) {
      badge.classList.remove('hidden');
      if (dias > 1) {
        txt.textContent = `Acesso VIP: ${dias} dias restantes`;
      } else {
        txt.textContent = `Acesso VIP: ${horas}h restantes`;
      }
      if (window.lucide) lucide.createIcons();
    }
  }
}

function exibirTelaBloqueioTrial() {
  const modal = document.getElementById('modal-trial-expirado');
  if (modal) {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.lucide) lucide.createIcons();
  }
}

function validarChaveVIP() {
  const input = document.getElementById('input-chave-vip');
  const chave = (input ? input.value : '').trim().toUpperCase();

  if (TRIAL_CONFIG.CHAVES_VALIDAS.includes(chave)) {
    localStorage.setItem(TRIAL_CONFIG.CHAVE_STORAGE_VIP, 'true');
    alert('🎉 Parabéns! Sua Chave VIP foi validada com sucesso. O seu acesso ao AprovaQuest agora é ILIMITADO!');
    const modal = document.getElementById('modal-trial-expirado');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = '';
    window.location.reload();
  } else {
    alert('❌ Chave VIP não reconhecida. Envie uma mensagem no WhatsApp do desenvolvedor para receber seu acesso.');
  }
}

function abrirWhatsAppFeedback() {
  const msg = encodeURIComponent('Olá! Participei do teste de 5 dias do AprovaQuest no grupo de concurseiros. Gostei muito da ferramenta e gostaria de dar meu feedback para continuar com acesso!');
  window.open(`https://wa.me/?text=${msg}`, '_blank');
}

function copiarFeedbackTexto() {
  const texto = '🚀 Avaliação do Teste AprovaQuest:\n\n1. O que mais gostei no app: \n2. O que senti falta / sugestão de melhoria: \n3. Recomendo para amigos concurseiros? (Sim/Não): \n\nParabéns pelo projeto!';
  if (navigator.clipboard) {
    navigator.clipboard.writeText(texto).then(() => {
      alert('📋 Modelo de avaliação copiado! Basta colar no WhatsApp e nos enviar seu feedback.');
    }).catch(() => {
      prompt('Copie o texto abaixo para enviar:', texto);
    });
  } else {
    prompt('Copie o texto abaixo para enviar:', texto);
  }
}

// ================= CONTADOR DE VISITAS =================
async function carregarContadorVisitas() {
  const el = document.getElementById('contador-visitas-num');
  if (!el) return;
  try {
    const res = await fetch('/api/visitas');
    if (res.ok) {
      const data = await res.json();
      if (data && data.total_visitas) {
        el.textContent = Number(data.total_visitas).toLocaleString('pt-BR');
        return;
      }
    }
  } catch (e) {}

  let local = parseInt(localStorage.getItem('aprovaquest_visitas_total') || '1', 10);
  el.textContent = local.toLocaleString('pt-BR');
}

// ================= BACKUP & SINCRONIZAÇÃO =================
async function exportarBackupAluno() {
  try {
    let dados = {
      respostas: {},
      caderno_erros: [],
      favoritas: [],
      simulados_feitos: [],
      edital_progresso: {},
      metas: { diaria: 20, hoje_respondidas: 0 }
    };

    const rawLocal = localStorage.getItem('aprovaquest_user_data_v1');
    if (rawLocal) {
      dados = JSON.parse(rawLocal);
    }
    dados.exportado_em = new Date().toISOString();
    dados.versao = "1.2";

    const blob = new Blob([JSON.stringify(dados, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `aprovaquest_backup_${new Date().toISOString().slice(0,10)}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    alert('✅ Backup baixado com sucesso! Guarde este arquivo para restaurar em qualquer aparelho.');
  } catch (err) {
    alert('Erro ao gerar arquivo de backup: ' + err.message);
  }
}

function importarBackupAluno(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const parsed = JSON.parse(e.target.result);
      if (!parsed || (!parsed.respostas && !parsed.caderno_erros)) {
        throw new Error('Arquivo de backup inválido ou incompatível.');
      }
      localStorage.setItem('aprovaquest_user_data_v1', JSON.stringify(parsed));
      alert('🎉 Dados restaurados com sucesso! O aplicativo será recarregado.');
      window.location.reload();
    } catch (err) {
      alert('❌ Erro ao restaurar arquivo: ' + err.message);
    }
  };
  reader.readAsText(file);
}
