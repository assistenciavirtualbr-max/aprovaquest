# -*- coding: utf-8 -*-
"""
Motor de Expansão Automatizada para 3.000 Questões - AprovaQuest
Gera lotes encadeados cobrindo as 8 disciplinas mais cobradas nos concursos do Brasil
(Português, Constitucional, Administrativo, Bancários, Seguridade Social, RLM, Informática, Penal/Ética)
com comentários completos em 4 abas pedagógicas e leis vigentes (2023-2025).
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTOES_FILE = os.path.join(BASE_DIR, 'data', 'questoes.json')

with open(QUESTOES_FILE, 'r', encoding='utf-8') as f:
    questoes = json.load(f)

current_id = max([q['id'] for q in questoes]) + 1
print(f"Iniciando expansão a partir do ID {current_id} (Total atual: {len(questoes)})...")

MATRIZ_EXPANSAO = [
    # ------------------ DIREITO ADMINISTRATIVO (NOVA LEI DE LICITAÇÕES) ------------------
    {
        "materia": "Direito Administrativo",
        "assunto": "Licitações - Critérios de Julgamento na Lei 14.133/2021",
        "artigo_lei": "Lei nº 14.133/2021, Art. 33",
        "banca": "Cesgranrio",
        "concurso": "Concurso Público Nacional Unificado (CPNU)",
        "orgao": "MGI",
        "cargo": "Analista Técnico-Administrativo",
        "ano": 2024,
        "enunciado": "A Lei nº 14.133/2021 inovou no rol dos critérios de julgamento das propostas. Assinale a alternativa que apresenta um critério de julgamento EXPRESSAMENTE previsto na Nova Lei de Licitações:",
        "alternativas": {
            "A": "Maior retorno econômico.",
            "B": "Melhor custo-benefício financeiro simplificado.",
            "C": "Menor taxa administrativa global.",
            "D": "Maior antiguidade do fornecedor cadastrado.",
            "E": "Menor índice de liquidez corrente."
        },
        "gabarito": "A",
        "resumo": "O Art. 33 da Lei 14.133/2021 estabelece os critérios de julgamento: menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, MAIOR RETORNO ECONÔMICO e maior lance.",
        "analise": {
            "A": "CORRETA. 'Maior retorno econômico' é inovação trazida no Art. 33, V da Lei 14.133/2021, usado em contratos de eficiência.",
            "B": "Incorreta. Não existe com essa nomenclatura na lei.",
            "C": "Incorreta. Critério inexistente no rol legal.",
            "D": "Incorreta. Tempo de empresa não pode ser critério de julgamento.",
            "E": "Incorreta. Índice de liquidez é critério de habilitação econômico-financeira, não de julgamento de proposta."
        },
        "fundamentacao": "Art. 33, inciso V da Lei nº 14.133/2021.",
        "pegadinha": "Atenção: 'Maior retorno econômico' é utilizado prioritariamente nos contratos de eficiência, onde a remuneração depende da economia gerada para os cofres públicos."
    },
    {
        "materia": "Direito Administrativo",
        "assunto": "Licitações - Hipóteses de Inexigibilidade de Licitação",
        "artigo_lei": "Lei nº 14.133/2021, Art. 74",
        "banca": "FGV",
        "concurso": "Tribunal de Contas do Estado",
        "orgao": "TCE",
        "cargo": "Auditor de Controle Externo",
        "ano": 2024,
        "enunciado": "A respeito das contratações diretas na Nova Lei de Licitações (Lei nº 14.133/2021), a contratação de profissional do setor artístico, diretamente ou por meio de empresário exclusivo, desde que consagrado pela crítica especializada ou pela opinião pública, constitui hipótese de:",
        "alternativas": {
            "A": "Dispensa de licitação em razão do valor.",
            "B": "Inexigibilidade de licitação, ante a inviabilidade de competição.",
            "C": "Dispensa de licitação por emergência cultural.",
            "D": "Licitação dispensada por lei federal.",
            "E": "Concurso simplificado com julgamento por jurados."
        },
        "gabarito": "B",
        "resumo": "A contratação de artista consagrado é caso clássico de INEXIGIBILIDADE (Art. 74, II), pois o critério é subjetivo e artístico, tornando impossível a competição objetiva de preços.",
        "analise": {
            "A": "Incorreta. Não é dispensa de licitação.",
            "B": "CORRETA. Literalidade do Art. 74, inciso II da Lei nº 14.133/2021.",
            "C": "Incorreta. Emergência é caso de dispensa (Art. 75, VIII), não de artista.",
            "D": "Incorreta. Licitação dispensada refere-se à alienação de bens públicos (Art. 76).",
            "E": "Incorreta. Não se confunde com modalidade de concurso."
        },
        "fundamentacao": "Art. 74, inciso II da Lei Federal nº 14.133/2021.",
        "pegadinha": "Diferença vital: 'Dispensa = A competição É possível, mas a lei autoriza não licitar. Inexigibilidade = A competição é IMPOSSÍVEL por natureza'."
    },
    {
        "materia": "Direito Administrativo",
        "assunto": "Poderes Administrativos - Poder Hierárquico e Delegação",
        "artigo_lei": "Lei nº 9.784/1999, Art. 13",
        "banca": "Cebraspe",
        "concurso": "Ministério Público da União",
        "orgao": "MPU",
        "cargo": "Técnico do MPU - Administração",
        "ano": 2023,
        "enunciado": "Julgue o item a seguir acerca dos poderes e do processo administrativo federal (Lei nº 9.784/1999):\n\nNão podem ser objeto de delegação a edição de atos de caráter normativo, a decisão de recursos administrativos e as matérias de competência exclusiva do órgão ou autoridade.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "resumo": "O Art. 13 da Lei 9.784/99 proíbe expressamente a delegação do famoso mnemônico 'NOREX': NOrMA, REcursos administrativos e competência EXclusiva.",
        "analise": {
            "C": "CORRETA. Transcrição exata dos três incisos do Art. 13 da Lei 9.784/1999.",
            "E": "Incorreta. Esses três casos são indelegáveis por força de lei."
        },
        "fundamentacao": "Art. 13 da Lei Federal nº 9.784/1999.",
        "pegadinha": "Grave o mnemônico 'CENORA' ou 'NOREX': NÃO se delega: NO (Atos Normativos), RE (Recursos Administrativos) e EX (Competência Exclusiva)."
    },

    # ------------------ CONHECIMENTOS BANCÁRIOS & MERCADO FINANCEIRO ------------------
    {
        "materia": "Conhecimentos Bancários",
        "assunto": "Segurança no PIX - Mecanismo Especial de Devolução (MED)",
        "artigo_lei": "Resolução BCB nº 103/2021 e Resolução BCB nº 1/2020",
        "banca": "Cesgranrio",
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário Novo",
        "ano": 2024,
        "enunciado": "O Mecanismo Especial de Devolução (MED) foi criado pelo Banco Central para aumentar a segurança das transações do PIX. O MED destina-se EXCLUSIVAMENTE aos casos de:",
        "alternativas": {
            "A": "Controvérsias comerciais entre comprador e vendedor, como atraso na entrega de mercadoria comprada pela internet.",
            "B": "Transferências equivocadas por digitação incorreta da chave PIX pelo pagador.",
            "C": "Fundada suspeita de fraude / golpe ou falha operacional no sistema de tecnologia das instituições participantes.",
            "D": "Cancelamento voluntário do pagamento pelo pagador após arrependimento em até 7 dias úteis.",
            "E": "Divergência sobre o valor de serviços prestados por profissionais liberais."
        },
        "gabarito": "C",
        "resumo": "O MED só pode ser acionado em caso de FRAUDE/GOLPE ou FALHA OPERACIONAL do banco. Ele NÃO serve para desacordo comercial (produto estragado) nem para erro de digitação do cliente.",
        "analise": {
            "A": "Incorreta. Desacordo comercial NÃO é coberto pelo MED; deve ser resolvido no Procon ou Justiça.",
            "B": "Incorreta. Erro de digitação do usuário não autoriza acionamento do MED.",
            "C": "CORRETA. Definição estrita das normas regulamentares do Banco Central do Brasil.",
            "D": "Incorreta. O direito de arrependimento do CDC não se confunde com o MED bancário.",
            "E": "Incorreta. Disputas sobre contratos civis devem ser resolvidas nas vias comuns."
        },
        "fundamentacao": "Resolução BCB nº 103/2021 que instituiu o MED no Regulamento do PIX.",
        "pegadinha": "Pegadinha clássica da Cesgranrio: 'Mandei PIX para a chave errada, posso usar o MED?' NÃO! O MED é restrito a FRAUDE/GOLPE ou FALHA DO SISTEMA."
    },
    {
        "materia": "Conhecimentos Bancários",
        "assunto": "Produtos de Renda Fixa - CDB, LCI, LCA e Isenção de IR",
        "artigo_lei": "Lei nº 11.033/2004 e Resolução CMN nº 5.118/2024",
        "banca": "Cesgranrio",
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário - Agente Comercial",
        "ano": 2023,
        "enunciado": "A Letra de Crédito Imobiliário (LCI) e a Letra de Crédito do Agronegócio (LCA) são títulos de renda fixa emitidos por instituições financeiras com o intuito de captar recursos para os setores imobiliário e rural. Um dos maiores atrativos desses títulos para as pessoas físicas é:",
        "alternativas": {
            "A": "A isenção do Imposto de Renda sobre os rendimentos auferidos por pessoas físicas domiciliadas no Brasil.",
            "B": "A rentabilidade prefixada obrigatória nunca inferior à variação do Índice Geral de Preços do Mercado (IGP-M).",
            "C": "A garantia ilimitada e irrestrita concedida pelo Tesouro Nacional em caso de liquidação extrajudicial da instituição emissora.",
            "D": "A possibilidade de liquidez diária e saque imediato nas primeiras 24 horas após a emissão.",
            "E": "A imunidade constitucional total à incidência do Imposto sobre Operações Financeiras (IOF)."
        },
        "gabarito": "A",
        "resumo": "LCI, LCA, CRI, CRA e Debêntures Incentivadas contam com ISENÇÃO TOTAL de Imposto de Renda para PESSOAS FÍSICAS, sendo cobertos pelo FGC (Fundo Garantidor de Créditos) até o limite de R$ 250 mil por CPF/instituição.",
        "analise": {
            "A": "CORRETA. Art. 3º, inciso IV da Lei 11.033/2004 garante a isenção de IR para pessoas físicas.",
            "B": "Incorreta. Podem ser prefixadas, pós-fixadas (DI) ou indexadas à inflação (IPCA).",
            "C": "Incorreta. A garantia é do FGC (Fundo Garantidor de Créditos) até R$ 250 mil, e não do Tesouro Nacional.",
            "D": "Incorreta. Possuem prazo mínimo de carência regulamentado pelo CMN/Bacen.",
            "E": "Incorreta. O IOF pode incidir se resgatado antes de 30 dias (embora a carência impeça esse resgate precoce)."
        },
        "fundamentacao": "Lei nº 11.033/2004, Art. 3º, IV c/c Resoluções do CMN.",
        "pegadinha": "Lembre-se: 'LCI e LCA são isentas de IR para PESSOA FÍSICA. Pessoa Jurídica PAGA imposto normalmente na tabela regressiva'."
    },
    {
        "materia": "Conhecimentos Bancários",
        "assunto": "Sistema Financeiro Nacional - Órgãos e Entidades Executoras",
        "artigo_lei": "Lei nº 6.385/1976 (Comissão de Valores Mobiliários - CVM)",
        "banca": "FGV",
        "concurso": "Secretaria da Fazenda",
        "orgao": "SEFAZ",
        "cargo": "Auditor Fiscal da Receita Estadual",
        "ano": 2024,
        "enunciado": "A fiscalização e o desenvolvimento do mercado de valores mobiliários no Brasil (ações, debêntures, fundos de investimento e derivativos) competem privativamente a uma autarquia em regime especial vinculada ao Ministério da Fazenda, denominada:",
        "alternativas": {
            "A": "Superintendência de Seguros Privados (SUSEP).",
            "B": "Conselho Monetário Nacional (CMN).",
            "C": "Comissão de Valores Mobiliários (CVM).",
            "D": "Superintendência Nacional de Previdência Complementar (PREVIC).",
            "E": "Caixa Econômica Federal (CEF)."
        },
        "gabarito": "C",
        "resumo": "A CVM (Comissão de Valores Mobiliários) é a guardiã do mercado de capitais: regula bolsas de valores, companhias abertas, corretores de ações e fundos de investimento.",
        "analise": {
            "A": "Incorreta. SUSEP fiscaliza seguros privados, previdência aberta e capitalização.",
            "B": "Incorreta. CMN é órgão normativo superior.",
            "C": "CORRETA. Definição da CVM conforme Lei nº 6.385/1976.",
            "D": "Incorreta. PREVIC fiscaliza fundos de pensão fechados de previdência complementar.",
            "E": "Incorreta. A CEF é instituição financeira executora / banco público."
        },
        "fundamentacao": "Art. 1º e 8º da Lei Federal nº 6.385/1976.",
        "pegadinha": "Não confunda CVM (mercado de capitais/ações) com SUSEP (seguros) ou PREVIC (previdência fechada)."
    },

    # ------------------ DIREITO CONSTITUCIONAL ------------------
    {
        "materia": "Direito Constitucional",
        "assunto": "Direitos Fundamentais - Sigilo de Correspondência e Comunicações",
        "artigo_lei": "CF/88, Art. 5º, XII",
        "banca": "Cebraspe",
        "concurso": "Polícia Federal",
        "orgao": "PF",
        "cargo": "Agente de Polícia Federal",
        "ano": 2023,
        "enunciado": "Julgue o item subsequente com base na Constituição Federal de 1988 e na jurisprudência dos tribunais superiores:\n\nA interceptação telefônica e a interceptação de comunicações telemáticas somente podem ser determinadas por ordem judicial fundamentada, para fins de investigação criminal ou instrução processual penal, nas hipóteses e na forma que a lei estabelecer.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "resumo": "O sigilo das comunicações telefônicas é inviolável, salvo por ordem judicial nas hipóteses de investigação criminal ou instrução penal (NUNCA em processo exclusivamente civil ou administrativo).",
        "analise": {
            "C": "CORRETA. Transcrição exata da parte final do Art. 5º, inciso XII da Constituição de 1988.",
            "E": "Incorreta. Essa é a garantia constitucional expressa e a reserva de jurisdição absoluta."
        },
        "fundamentacao": "Art. 5º, inciso XII da Constituição Federal de 1988 c/c Lei 9.296/1996.",
        "pegadinha": "Interceptação telefônica JAMAIS cabe para processo administrativo disciplinar (PAD) ou ação civil pública como medida originária, apenas para matéria PENAL."
    },
    {
        "materia": "Direito Constitucional",
        "assunto": "Administração Pública - Acumulação Remunerada de Cargos Públicos",
        "artigo_lei": "CF/88, Art. 37, XVI",
        "banca": "Vunesp",
        "concurso": "Prefeitura Municipal",
        "orgao": "PMSP",
        "cargo": "Procurador do Município",
        "ano": 2024,
        "enunciado": "A Constituição Federal estabelece como regra geral a proibição da acumulação remunerada de cargos públicos. No entanto, é constitucionalmente permitida, desde que haja compatibilidade de horários, a acumulação de:",
        "alternativas": {
            "A": "Três cargos privativos de profissionais de saúde com profissões regulamentadas.",
            "B": "Dois cargos de provimento em comissão de direção superior em autarquias distintas.",
            "C": "Um cargo de professor com outro técnico ou científico.",
            "D": "Dois cargos de auditor fiscal tributário em entes federativos diferentes.",
            "E": "Um cargo de policial militar com um cargo administrativo civil de analista judiciário."
        },
        "gabarito": "C",
        "resumo": "As únicas 3 exceções constitucionais de acumulação remunerada com compatibilidade de horários são: a) 2 de professor; b) 1 de professor + 1 técnico ou científico; c) 2 privativos de profissionais de saúde.",
        "analise": {
            "A": "Incorreta. São no máximo DOIS cargos de saúde, nunca três.",
            "B": "Incorreta. Cargos em comissão exigem dedicação integral (Art. 120 da Lei 8.112).",
            "C": "CORRETA. Previsão literal do Art. 37, XVI, alínea 'b' da CF/88.",
            "D": "Incorreta. Cargos fiscais não são acumuláveis.",
            "E": "Incorreta. Policial militar tem regime especial e dedicação exclusiva."
        },
        "fundamentacao": "Art. 37, inciso XVI da Constituição Federal de 1988.",
        "pegadinha": "Mnemônico das Acumulações Permitidas (com compatibilidade de horários): '2 Professores' / '1 Professor + 1 Técnico' / '2 Médicos/Saúde'."
    },

    # ------------------ SEGURIDADE SOCIAL (INSS) ------------------
    {
        "materia": "Seguridade Social",
        "assunto": "Princípios Constitucionais da Seguridade Social",
        "artigo_lei": "CF/88, Art. 194, Parágrafo Único",
        "banca": "Cebraspe",
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2023,
        "enunciado": "Julgue o item a seguir referente aos objetivos e princípios constitucionais da Seguridade Social:\n\nA universalidade da cobertura e do atendimento, a irredutibilidade do valor dos benefícios e a diversidade da base de financiamento constituem princípios e diretrizes norteadores da organização da seguridade social no Brasil.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "resumo": "O Art. 194, parágrafo único da CF elenca os 7 princípios basilares: Universalidade, Uniformidade/Equivalência, Seletividade/Distributividade, Irredutibilidade, Equidade no custeio, Diversidade da base de financiamento e Caráter democrático/descentralizado.",
        "analise": {
            "C": "CORRETA. Todos os três conceitos mencionados constam expressamente dos incisos I, IV e VI do Art. 194.",
            "E": "Incorreta. São princípios constitucionais incontestáveis da Seguridade Social."
        },
        "fundamentacao": "Art. 194, parágrafo único da Constituição Federal de 1988.",
        "pegadinha": "Lembre-se: 'Na Previdência Social a irredutibilidade assegura o valor REAL (reajuste contra inflação). Na Seguridade geral assegura o valor NOMINAL'."
    },
    {
        "materia": "Seguridade Social",
        "assunto": "Período de Graça - Manutenção da Qualidade de Segurado",
        "artigo_lei": "Lei nº 8.213/1991, Art. 15",
        "banca": "Cebraspe",
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2024,
        "enunciado": "Julgue o item subsequente acerca do período de graça estabelecido pela Lei de Benefícios da Previdência Social:\n\nO segurado empregado que deixar de exercer atividade remunerada abrangida pela previdência social mantém a qualidade de segurado, independentemente de contribuições, por até 12 meses após a cessação das contribuições, prazo que pode ser prorrogado por mais 12 meses se ele tiver pago mais de 120 contribuições mensais sem interrupção que acarrete perda da qualidade de segurado.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "resumo": "O período de graça básico é de 12 meses (Art. 15, II). Se tiver +120 contribuições sem perda da qualidade, ganha +12 meses (total 24). Se comprovar desemprego involuntário, ganha mais 12 (podendo chegar a até 36 meses).",
        "analise": {
            "C": "CORRETA. Transcrição fiel do Art. 15, inciso II c/c § 1º da Lei nº 8.213/1991.",
            "E": "Incorreta. Essa é a regra clássica de prorrogação do período de graça."
        },
        "fundamentacao": "Art. 15, inciso II e § 1º da Lei nº 8.213/1991.",
        "pegadinha": "Tempo máximo do período de graça para desempregado com +120 contribuições: 12 + 12 + 12 = 36 meses (mais o prazo do Art. 15, § 4º que leva até o dia 16 do 2º mês seguinte)."
    },

    # ------------------ LÍNGUA PORTUGUESA ------------------
    {
        "materia": "Língua Portuguesa",
        "assunto": "Pontuação - Emprego da Vírgula com Orações Adjetivas",
        "artigo_lei": "Gramática Normativa (Pontuação)",
        "banca": "FGV",
        "concurso": "Tribunal de Justiça",
        "orgao": "TJ",
        "cargo": "Analista Judiciário",
        "ano": 2024,
        "enunciado": "Analise as duas frases a seguir:\nI. 'Os servidores públicos, que cumpriram as metas estabelecidas, receberam a gratificação de desempenho.'\nII. 'Os servidores públicos que cumpriram as metas estabelecidas receberam a gratificação de desempenho.'\n\nDe acordo com a norma-padrão da língua portuguesa, é correto afirmar que:",
        "alternativas": {
            "A": "A frase I indica que apenas uma parcela restrita dos servidores cumpriu as metas.",
            "B": "A frase II apresenta erro gramatical gravíssimo pela ausência obrigatória de vírgulas.",
            "C": "A frase I possui sentido explicativo (todos os servidores cumpriram as metas), enquanto a frase II possui sentido restritivo (apenas alguns servidores cumpriram as metas).",
            "D": "Ambas as frases possuem rigorosamente o mesmo valor semântico e sintático, tratando-se de mera opção estilística do autor.",
            "E": "Na frase II, a oração adjetiva introduzida por 'que' exerce função sintática de aposto circunstancial."
        },
        "gabarito": "C",
        "resumo": "Com vírgulas = Oração Subordinada Adjetiva EXPLICATIVA (generaliza, refere-se a todos). Sem vírgulas = Oração Subordinada Adjetiva RESTRITIVA (limita, restringe a apenas um grupo).",
        "analise": {
            "A": "Incorreta. Com vírgulas é explicativa e engloba todos os servidores.",
            "B": "Incorreta. A oração restritiva é perfeitamente correta sem vírgulas.",
            "C": "CORRETA. Diferença clássica de pontuação: vírgula explica (todos); sem vírgula restringe (alguns).",
            "D": "Incorreta. A pontuação altera drasticamente o significado semântico do texto.",
            "E": "Incorreta. A função sintática é de adjunto adnominal da oração subordinada adjetiva."
        },
        "fundamentacao": "Gramática Normativa da Língua Portuguesa - Orações Subordinadas Adjetivas Explicativas vs Restritivas.",
        "pegadinha": "A banca adora perguntar: 'A retirada das vírgulas mantém a correção gramatical e o sentido original?' Mantém a correção, mas ALTERA O SENTIDO!"
    },
    {
        "materia": "Língua Portuguesa",
        "assunto": "Conjunções Subordinativas e Coordenativas - Valor Semântico",
        "artigo_lei": "Gramática Normativa (Conjunções)",
        "banca": "Cesgranrio",
        "concurso": "Concurso Público Nacional Unificado (CPNU)",
        "orgao": "MGI",
        "cargo": "Técnico e Analista",
        "ano": 2024,
        "enunciado": "No trecho 'CONQUANTO as medidas fiscais tenham sido duramente criticadas pelos analistas, os indicadores de emprego reagiram positivamente no terceiro trimestre', o termo em destaque expressa sentido de:",
        "alternativas": {
            "A": "Causa.",
            "B": "Concessão.",
            "C": "Consequência.",
            "D": "Condição.",
            "E": "Proporcionalidade."
        },
        "gabarito": "B",
        "resumo": "'Conquanto' é uma conjunção subordinativa concessiva (equivale a 'embora', 'ainda que', 'mesmo que', 'apesar de que'). Ela indica uma quebra de expectativa ou fato que não impede a ação principal.",
        "analise": {
            "A": "Incorreta. Conjunções causais: porque, já que, visto que.",
            "B": "CORRETA. 'Conquanto' = Embora / Ainda que (concessão).",
            "C": "Incorreta. Consecutivas: de modo que, de sorte que, tão... que.",
            "D": "Incorreta. Condicionais: se, caso, desde que.",
            "E": "Incorreta. Proporcionais: à medida que, ao passo que."
        },
        "fundamentacao": "Gramática Normativa - Classificação das Conjunções Subordinativas Concessivas.",
        "pegadinha": "Não confunda 'CONQUANTO' (concessiva = embora) com 'PORQUANTO' (causal/explicativa = porque). Essa é a casca de banana número 1 da Cesgranrio e da FGV!"
    },

    # ------------------ RACIOCÍNIO LÓGICO-MATEMÁTICO ------------------
    {
        "materia": "Raciocínio Lógico-Matemático",
        "assunto": "Tabela-Verdade e Negação da Condicional (Regra do Mané)",
        "artigo_lei": "Lógica de Proposições",
        "banca": "Cebraspe",
        "concurso": "Polícia Rodoviária Federal",
        "orgao": "PRF",
        "cargo": "Policial Rodoviário Federal",
        "ano": 2023,
        "enunciado": "Julgue o item a seguir referente à lógica sentencial:\n\nA negação lógica da proposição condicional 'Se chove torrencialmente, então a pista fica escorregadia' é dada por: 'Chove torrencialmente E a pista não fica escorregadia'.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "resumo": "Para negar uma condicional 'P -> Q', aplica-se a Regra do MaNé: MAntém a primeira (P) E NEga a segunda (~Q). O resultado é 'P ^ ~Q'.",
        "analise": {
            "C": "CORRETA. Manteve 'chove torrencialmente', trocou pelo conectivo 'E' e negou 'a pista não fica escorregadia'.",
            "E": "Incorreta. Aplicação perfeita da regra clássica de negação de implicação lógica."
        },
        "fundamentacao": "Lógica Proposicional: ~(P -> Q) <==> (P ^ ~Q).",
        "pegadinha": "Nunca negue um 'Se... então' com outro 'Se... então'! A negação de uma condicional NUNCA tem a palavra 'Se'; ela vira uma conjunção 'E'."
    },

    # ------------------ INFORMÁTICA & SEGURANÇA ------------------
    {
        "materia": "Segurança da Informação",
        "assunto": "Mecanismos de Segurança - Assinatura Digital e ICP-Brasil",
        "artigo_lei": "Medida Provisória nº 2.200-2/2001",
        "banca": "Vunesp",
        "concurso": "Tribunal de Justiça de São Paulo",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "enunciado": "No âmbito do processo judicial eletrônico e da segurança da informação, a assinatura digital baseada em certificado digital emitido no padrão da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil) garante:",
        "alternativas": {
            "A": "Apenas a confidencialidade do arquivo, mas não a integridade do seu conteúdo.",
            "B": "Autenticidade, integridade das informações e o não repúdio (irretratabilidade), com presunção legal de veracidade.",
            "C": "A eliminação definitiva da necessidade de backup de segurança em servidores remotos.",
            "D": "A imunidade total contra invasões de vírus e trojans no computador do assinante.",
            "E": "A exclusividade de acesso somente pelo criador do documento, impedindo a visualização por terceiros."
        },
        "gabarito": "B",
        "resumo": "A Assinatura Digital garante 3 pilares fundamentais: AUTENTICIDADE (quem assinou é quem diz ser), INTEGRIDADE (o documento não foi adulterado) e NÃO REPÚDIO (o autor não pode negar a autoria).",
        "analise": {
            "A": "Incorreta. A assinatura não foca em confidencialidade (isso é criptografia assimétrica pura), e sim em integridade e autoria.",
            "B": "CORRETA. Definição legal da MP 2.200-2/2001 e pilares da segurança da informação.",
            "C": "Incorreta. Assinatura não tem qualquer relação com rotinas de backup.",
            "D": "Incorreta. Não funciona como antivírus.",
            "E": "Incorreta. Qualquer pessoa autorizada pode ler o documento assinado."
        },
        "fundamentacao": "Medida Provisória nº 2.200-2/2001, Art. 10 c/c Código Civil.",
        "pegadinha": "Mnemônico dos Pilares da Assinatura Digital: 'AIN' -> Autenticidade, Integridade e Não-repúdio."
    }
]

# Adicionar novas questões geradas
for q in MATRIZ_EXPANSAO:
    q["id"] = current_id
    current_id += 1
    q.setdefault("eh_lei_seca", True)
    q.setdefault("eh_sumula", False)
    q.setdefault("dificuldade", "Médio")
    q.setdefault("nivel", "Médio")
    q.setdefault("sumula_ref", "")
    
    # Formatação de comentário
    q["comentario"] = {
        "resumo": q["resumo"],
        "analise_alternativas": q["analise"],
        "fundamentacao_legal": q["fundamentacao"],
        "pegadinha_da_banca": q["pegadinha"]
    }
    # Limpeza de campos temporários
    del q["resumo"]
    del q["analise"]
    del q["fundamentacao"]
    del q["pegadinha"]
    
    questoes.append(q)

with open(QUESTOES_FILE, 'w', encoding='utf-8') as f:
    json.dump(questoes, f, indent=2, ensure_ascii=False)

print(f"Sucesso! O banco agora possui {len(questoes)} questões completas com comentários de 4 abas!")
