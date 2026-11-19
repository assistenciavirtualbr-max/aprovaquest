# -*- coding: utf-8 -*-
import json
import os

QUESTOES_FILE = os.path.join(os.path.dirname(__file__), 'data', 'questoes.json')

with open(QUESTOES_FILE, 'r', encoding='utf-8') as f:
    questoes = json.load(f)

current_id = max([q['id'] for q in questoes]) + 1

NOVAS_QUESTOES = [
    # ==================== DIREITO ADMINISTRATIVO (NOVA LEI DE LICITAÇÕES & IMPROBIDADE) ====================
    {
        "concurso": "Concurso Público Nacional Unificado (CPNU)",
        "orgao": "MGI / Órgãos Federais",
        "cargo": "Analista Técnico-Administrativo",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Direito Administrativo",
        "assunto": "Nova Lei de Licitações - Modalidades e Inovações",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lei 14.133/2021, Art. 6º, XLII e Art. 28",
        "sumula_ref": "",
        "enunciado": "De acordo com a Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos Administrativos), a modalidade de licitação voltada para a contratação de obras, serviços e compras em que a Administração Pública realiza diálogos com licitantes previamente selecionados mediante critérios objetivos, com o intuito de desenvolver uma ou mais alternativas capazes de atender às suas necessidades, denomina-se:",
        "alternativas": {
            "A": "Concurso especial.",
            "B": "Tomada de preços simplificada.",
            "C": "Diálogo competitivo.",
            "D": "Pregão internacional.",
            "E": "Consulta pública vinculante."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "O Diálogo Competitivo é a nova modalidade introduzida pela Lei 14.133/2021 para inovações tecnológicas ou complexidades técnicas onde o Estado dialoga antes da proposta final.",
            "analise_alternativas": {
                "A": "Incorreta. Concurso destina-se à escolha de trabalho técnico, científico ou artístico.",
                "B": "Incorreta. Tomada de preços e Convite foram EXTINTOS na Lei 14.133/2021.",
                "C": "CORRETA. Definição literal do Art. 6º, XLII da Lei 14.133/2021.",
                "D": "Incorreta. O pregão destina-se a bens e serviços comuns.",
                "E": "Incorreta. Consulta pública é procedimento auxiliar/participativo, não modalidade de licitação."
            },
            "fundamentacao_legal": "Art. 6º, XLII c/c Art. 28 da Lei 14.133/2021.",
            "pegadinha_da_banca": "Lembre-se: 'Convite e Tomada de Preços NÃO existem na Nova Lei de Licitações; a grande novidade é o Diálogo Competitivo'."
        }
    },
    {
        "concurso": "Tribunal de Justiça de São Paulo",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "banca": "Vunesp",
        "materia": "Direito Administrativo",
        "assunto": "Improbidade Administrativa - Exigência de Dolo",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lei 8.429/1992 (com redação dada pela Lei 14.230/2021), Art. 1º, §§ 1º e 2º",
        "sumula_ref": "",
        "enunciado": "A respeito dos atos de improbidade administrativa disciplinados pela Lei nº 8.429/1992, com as alterações profundas promovidas pela Lei nº 14.230/2021, é correto afirmar que:",
        "alternativas": {
            "A": "Configura ato de improbidade a conduta culposa grave devidamente comprovada em processo administrativo.",
            "B": "Exige-se a demonstração de dolo específico para a configuração de qualquer ato de improbidade administrativa, sendo revogada a modalidade culposa.",
            "C": "A divergência na interpretação de lei autoriza, por si só, a punição por improbidade do agente público causador do prejuízo.",
            "D": "O mero exercício da função pública com negligência inescusável caracteriza dano ao erário com aplicação das sanções da lei.",
            "E": "O prazo prescricional para ajuizamento da ação de improbidade é de cinco anos contados da cessação do mandato eletivo."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "A Reforma da Lei de Improbidade (Lei 14.230/2021) aboliu expressamente os atos de improbidade na forma CULPOSA (mesmo culpa grave). Hoje exige-se estritamente o DOLO.",
            "analise_alternativas": {
                "A": "Incorreta. Atos culposos deixaram de caracterizar improbidade.",
                "B": "CORRETA. O Art. 1º, § 1º exige a vontade livre e consciente de alcançar o resultado ilícito (dolo).",
                "C": "Incorreta. Art. 1º, § 8º: divergência interpretativa NÃO configura ato de improbidade.",
                "D": "Incorreta. Negligência é culpa; logo, não configura improbidade.",
                "E": "Incorreta. O novo prazo prescricional é de 8 (oito) anos, contados da ocorrência do fato (Art. 23)."
            },
            "fundamentacao_legal": "Art. 1º, §§ 1º, 2º e 8º c/c Art. 23 da Lei 8.429/1992 (redação da Lei 14.230/2021).",
            "pegadinha_da_banca": "Atenção: 'NÃO existe mais improbidade culposa no ordenamento jurídico brasileiro. Todo ato de improbidade agora exige dolo'."
        }
    },
    {
        "concurso": "Tribunal Regional Federal",
        "orgao": "TRF",
        "cargo": "Técnico Judiciário",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Direito Administrativo",
        "assunto": "Poderes Administrativos - Poder de Polícia",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": False,
        "eh_sumula": True,
        "dificuldade": "Médio",
        "artigo_lei": "CTN, Art. 78; Jurisprudência do STF (Tema 532)",
        "sumula_ref": "Tema 532 STF",
        "enunciado": "Julgue o item a seguir com base no entendimento pacificado do Supremo Tribunal Federal (STF):\n\nÉ constitucional a delegação do poder de polícia, inclusive no que concerne à aplicação de sanções administrativas (multas), a pessoas jurídicas de direito privado integrantes da Administração Pública Indireta de capital social majoritariamente público que prestem exclusivamente serviço público de atuação própria do Estado e em regime não concorrencial.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "O STF fixou a tese de que estatais de capital majoritário público, prestadoras de serviços públicos não concorrenciais (ex: BHTrans), podem exercer e aplicar multas de poder de polícia.",
            "analise_alternativas": {
                "C": "CORRETA. Transcrição exata da tese de repercussão geral firmada pelo STF no Tema 532.",
                "E": "Incorreta. O STF superou o antigo entendimento que vedava a fase sancionatória para estatais não concorrenciais."
            },
            "fundamentacao_legal": "STF - RE 633782 (Tema 532 de Repercussão Geral).",
            "pegadinha_da_banca": "Antigamente dizia-se que estatal NUNCA podia multar. O STF autorizou, DESDE QUE seja capital público majoritário, não concorra no mercado e preste serviço público exclusivo."
        }
    },

    # ==================== CONHECIMENTOS BANCÁRIOS (CAIXA / BB / BACEN) ====================
    {
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário Novo",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Moeda Digital do Banco Central - DREX",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Diretrizes do Banco Central do Brasil para o Real Digital / Drex",
        "sumula_ref": "",
        "enunciado": "O Banco Central do Brasil desenvolveu o projeto da moeda digital brasileira oficial soberana, denominada DREX. A respeito do DREX e de suas características operacionais, assinale a opção correta:",
        "alternativas": {
            "A": "O DREX é uma criptomoeda descentralizada e não regulamentada, cuja cotação varia livremente de acordo com a oferta e a demanda internacional.",
            "B": "Trata-se de uma Central Bank Digital Currency (CBDC), sendo uma representação digital da moeda oficial brasileira com paridade direta de 1:1 com o Real convencional.",
            "C": "O objetivo primordial do DREX é substituir integralmente o papel-moeda e extinguir o sistema de transferências instantâneas PIX até o ano de 2026.",
            "D": "A emissão do DREX pode ser realizada privativamente por qualquer instituição bancária autorizada pelo Conselho Monetário Nacional.",
            "E": "O DREX impede o uso de contratos inteligentes (smart contracts) por razões de sigilo bancário e segurança da informação."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "O Drex é a CBDC brasileira. Não é criptomoeda volátil como Bitcoin; é o próprio Real em formato digital, emitido e custodiado exclusivamente pelo Banco Central (1 Drex = R$ 1,00).",
            "analise_alternativas": {
                "A": "Incorreta. O Drex é centralizado, regulado e emitido pelo Banco Central.",
                "B": "CORRETA. É uma CBDC oficial com valor fixado e garantido na proporção de 1 para 1 com o Real.",
                "C": "Incorreta. O Drex não substitui o PIX nem extingue o papel-moeda; são ferramentas complementares.",
                "D": "Incorreta. Apenas o Banco Central tem a prerrogativa constitucional de emitir a moeda.",
                "E": "Incorreta. Uma das maiores vantagens do Drex é exatamente viabilizar contratos inteligentes (smart contracts) em blockchain."
            },
            "fundamentacao_legal": "Comunicação nº 40.528/2023 do Banco Central do Brasil.",
            "pegadinha_da_banca": "Não confunda DREX com criptomoeda (Bitcoin/Ethereum). O DREX tem valor estável e soberania do Estado brasileiro."
        }
    },
    {
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário Novo",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Prevenção à Lavagem de Dinheiro - COAF e Comunicações Obrigatórias",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lei nº 9.613/1998, Art. 10 e 11; Circular Bacen 3.978/2020",
        "sumula_ref": "",
        "enunciado": "No contexto da Lei nº 9.613/1998 (Crimes de Lavagem ou Ocultação de Bens, Direitos e Valores), as instituições financeiras e bancárias têm o dever legal de comunicar às autoridades reguladoras operações suspeitas. Sobre esse dever, é correto afirmar:",
        "alternativas": {
            "A": "A comunicação ao COAF deve ser previamente notificada ao cliente para que ele exerça o contraditório e a ampla defesa.",
            "B": "As comunicações de boa-fé feitas na forma da lei ao COAF não acarretam responsabilidade civil ou administrativa para a instituição financeira ou seus prepostos.",
            "C": "Operações em espécie de valor igual ou superior a R$ 2.000,00 devem ser obrigatoriamente comunicadas ao Ministério Público Federal.",
            "D": "O cliente que constatar erro na comunicação feita pelo banco ao COAF poderá exigir indenização por dano moral in re ipsa da instituição.",
            "E": "Apenas operações que resultem em denúncia criminal do Ministério Público geram a obrigação de registro cadastral no banco."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "A Lei 9.613/98 protege expressamente o funcionário e o banco que comunicam ao COAF de boa-fé, isentando-os de processos de reparação civil e garantindo sigilo absoluto da comunicação.",
            "analise_alternativas": {
                "A": "Incorreta. A comunicação é estritamente SIGILOSA; avisar o cliente é crime/falta grave.",
                "B": "CORRETA. Literalidade do Art. 11, § 2º da Lei 9.613/1998.",
                "C": "Incorreta. A comunicação é feita ao COAF/Bacen, e o limite geral de espécie para registro obrigatório é de R$ 50.000,00.",
                "D": "Incorreta. As comunicações de boa-fé não geram dever de indenizar (Art. 11, § 2º).",
                "E": "Incorreta. O dever de cadastro e registro independe de qualquer investigação criminal prévia."
            },
            "fundamentacao_legal": "Art. 11, § 2º da Lei nº 9.613/1998.",
            "pegadinha_da_banca": "Lembre-se: 'O cliente NUNCA pode ser avisado de que sua transação foi reportada ao COAF'."
        }
    },
    {
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário - Agente Comercial",
        "ano": 2023,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Open Finance - Compartilhamento de Dados",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Resolução Conjunta nº 1/2020 CMN e BCB",
        "sumula_ref": "",
        "enunciado": "O ecossistema do Open Finance (Sistema Financeiro Aberto) no Brasil permite o compartilhamento padronizado de dados, produtos e serviços entre instituições autorizadas pelo Banco Central. O pilar fundamental que rege esse compartilhamento é:",
        "alternativas": {
            "A": "O envio compulsório dos dados cadastrais e financeiros de todos os correntistas para uma base única do governo.",
            "B": "O consentimento prévio, livre, informado, inequívoco e revogável do titular dos dados para finalidades determinadas.",
            "C": "A venda de dados pessoais financeiros para empresas de publicidade e redes sociais.",
            "D": "A proibição do cliente de cancelar ou revogar o compartilhamento antes do prazo mínimo de 2 anos.",
            "E": "A exclusividade do compartilhamento apenas entre bancos públicos e sociedades de economia mista."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "No Open Finance, os dados pertencem ao CLIENTE, não ao banco. O compartilhamento só ocorre se o cliente autorizar expressamente (consentimento), podendo revogar a qualquer momento.",
            "analise_alternativas": {
                "A": "Incorreta. Não há compartilhamento compulsório sem consentimento.",
                "B": "CORRETA. Alinhado com as normas do Bacen e com a LGPD (Lei Geral de Proteção de Dados).",
                "C": "Incorreta. Totalmente vedada a comercialização de dados.",
                "D": "Incorreta. O consentimento pode ser revogado a qualquer instante pelo cliente no app.",
                "E": "Incorreta. O Open Finance abrange bancos públicos, privados, cooperativas, fintechs e instituições de pagamento."
            },
            "fundamentacao_legal": "Resolução Conjunta CMN/Bacen nº 1/2020 c/c LGPD (Lei 13.709/2018).",
            "pegadinha_da_banca": "O cliente é o dono dos seus dados bancários. Ele decide com quem, para quê e por quanto tempo compartilha."
        }
    },

    # ==================== SEGURIDADE SOCIAL (INSS / PREVIDÊNCIA) ====================
    {
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Seguridade Social",
        "assunto": "Reforma da Previdência - Pensão por Morte (EC 103/2019)",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Emenda Constitucional nº 103/2019, Art. 23",
        "sumula_ref": "",
        "enunciado": "Julgue o item subsequente com relação às regras instituídas pela Emenda Constitucional nº 103/2019 (Reforma da Previdência):\n\nA pensão por morte concedida a dependente de segurado do Regime Geral de Previdência Social (RGPS) será equivalente a uma cota familiar de 50% do valor da aposentadoria recebida pelo segurado ou daquela a que teria direito se fosse aposentado por incapacidade permanente na data do óbito, acrescida de cotas de 10% por dependente, até o limite máximo de 100%.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "A EC 103/2019 alterou a pensão por morte: agora é cota familiar de 50% + 10% por dependente (viúva sem filhos = 60%; viúva com 1 filho = 70%; viúva com 5 filhos = 100%).",
            "analise_alternativas": {
                "C": "CORRETA. Redação literal do Art. 23, caput da EC nº 103/2019.",
                "E": "Incorreta. Essa é a regra exata e vigente da reforma."
            },
            "fundamentacao_legal": "Art. 23 da Emenda Constitucional nº 103/2019.",
            "pegadinha_da_banca": "A antiga regra pagava 100% integralmente. A nova regra é 50% (cota base) + 10% por dependente, não revertendo a cota do dependente que atinge 21 anos."
        }
    },
    {
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Seguridade Social",
        "assunto": "Segurados Obrigatórios - Contribuinte Individual e Empregado",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Lei nº 8.213/1991, Art. 11, V",
        "sumula_ref": "",
        "enunciado": "Julgue o item a seguir referente aos segurados do RGPS:\n\nO padre, o pastor evangélico e os membros de instituto de vida consagrada que prestam serviços religiosos à sua congregação eclesiástica são enquadrados perante o RGPS, obrigatoriamente, na categoria de contribuintes individuais.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Líderes religiosos (padres, pastores, rabinos) são considerados contribuintes individuais pelo Art. 11, V, alínea 'c' da Lei 8.213/91, não possuindo vínculo de emprego com a igreja.",
            "analise_alternativas": {
                "C": "CORRETA. Previsão expressa do Art. 11, V, 'c' da Lei 8.213/1991 e Decreto 3.048/1999.",
                "E": "Incorreta. Eles não são empregados nem facultativos, e sim contribuintes individuais obrigatórios."
            },
            "fundamentacao_legal": "Art. 11, inciso V, alínea 'c' da Lei nº 8.213/1991.",
            "pegadinha_da_banca": "Ministros de confissão religiosa são segurados OBRIGATÓRIOS na categoria CONTRIBUINTE INDIVIDUAL."
        }
    },

    # ==================== DIREITO CONSTITUCIONAL ====================
    {
        "concurso": "Polícia Federal",
        "orgao": "PF",
        "cargo": "Agente de Polícia Federal",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Direito Constitucional",
        "assunto": "Inviolabilidade de Domicílio - Tema 280 STF",
        "nivel": "Superior",
        "tipo": "certo_errado",
        "eh_lei_seca": False,
        "eh_sumula": True,
        "dificuldade": "Difícil",
        "artigo_lei": "CF/88, Art. 5º, XI; Tema 280 STF",
        "sumula_ref": "Tema 280 STF (RE 603616)",
        "enunciado": "Acerca dos direitos e garantias fundamentais previstos na CF/88 e da jurisprudência do STF, julgue o item seguinte:\n\nA entrada forçada em domicílio sem mandado judicial, no período noturno, só é lícita quando amparada em fundadas razões, devidamente justificadas a posteriori, que indiquem que dentro da casa ocorre situação de flagrante delito, sob pena de responsabilidade disciplinar, civil e penal do agente ou da autoridade e de nulidade dos atos praticados.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "O STF fixou a tese de que a mera suspeita ou fuga para dentro da casa sem elementos prévios objetivos não autoriza arrombamento de domicílio sem mandado.",
            "analise_alternativas": {
                "C": "CORRETA. Tese exata fixada pelo STF no Tema 280 de repercussão geral.",
                "E": "Incorreta. A tese exige 'fundadas razões justificadas pelas circunstâncias do caso concreto'."
            },
            "fundamentacao_legal": "STF - RE 603616 (Tema 280).",
            "pegadinha_da_banca": "O flagrante nos crimes permanentes (ex: tráfico/depósito de drogas) exige 'justa causa anterior' à invasão; a polícia não pode invadir 'para ver se acha drogas' e justificar depois."
        }
    },
    {
        "concurso": "Tribunal de Contas da União",
        "orgao": "TCU",
        "cargo": "Auditor Federal de Controle Externo",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Direito Constitucional",
        "assunto": "Remédios Constitucionais - Habeas Data vs Mandado de Segurança",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": True,
        "dificuldade": "Médio",
        "artigo_lei": "CF/88, Art. 5º, LXXII; Súmula 2 do STJ",
        "sumula_ref": "Súmula 2 do STJ",
        "enunciado": "Cidadão solicita perante determinado órgão público federal certidão com cópia integral de processo licitatório em que não figura como parte, visando exercer fiscalização cidadã sobre os gastos públicos. A repartição indefere o pedido imotivadamente. Para obter a documentação pleiteada, a ação constitucional cabível é o:",
        "alternativas": {
            "A": "Habeas Data, por se tratar de pedido de informação perante banco de dados de entidade governamental.",
            "B": "Mandado de Injunção, ante a ausência de norma regulamentadora sobre transparência governamental.",
            "C": "Mandado de Segurança, pois a pretensão visa à obtenção de informação de interesse coletivo ou geral, e não de dados pessoais do impetrante.",
            "D": "Ação Popular, sendo privativa e exclusiva para o fornecimento de certidões administrativas.",
            "E": "Habeas Corpus coletivo, em razão da violação à liberdade de manifestação e pensamento."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Habeas Data só serve para informações relativas à PESSOA DO IMPETRANTE (dados personalíssimos). Para informações gerais, certidões ou dados de terceiros, o remédio correto é o Mandado de Segurança.",
            "analise_alternativas": {
                "A": "Incorreta. Habeas Data exige que a informação seja sobre a pessoa do próprio requerente.",
                "B": "Incorreta. Não há omissão legislativa (a LAI regulamenta o tema).",
                "C": "CORRETA. Direito líquido e certo de obter certidão de interesse geral (Art. 5º, XXXIII e XXXIV, 'b') tutelado por Mandado de Segurança.",
                "D": "Incorreta. Ação Popular serve para anular ato lesivo ao patrimônio, não para obter certidão.",
                "E": "Incorreta. Habeas Corpus protege exclusivamente a liberdade de locomoção."
            },
            "fundamentacao_legal": "Art. 5º, XXXIII, XXXIV 'b' e LXIX da CF/88 c/c Lei 12.016/2009.",
            "pegadinha_da_banca": "Clássica pegadinha: 'Pediu informação sua? Habeas Data. Pediu certidão ou informação geral/de interesse público? Mandado de Segurança'."
        }
    },

    # ==================== LÍNGUA PORTUGUESA ====================
    {
        "concurso": "Receita Federal do Brasil",
        "orgao": "RFB",
        "cargo": "Auditor-Fiscal da Receita Federal",
        "ano": 2023,
        "banca": "FGV",
        "materia": "Língua Portuguesa",
        "assunto": "Sintaxe de Concordância - Partícula 'SE'",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Difícil",
        "artigo_lei": "Gramática Normativa (Concordância Verbal e Voz Passiva)",
        "sumula_ref": "",
        "enunciado": "Assinale a opção em que a concordância verbal foi construída em estrita observância à norma-padrão da língua portuguesa:",
        "alternativas": {
            "A": "Tratam-se de questões de alta complexidade tributária levantadas pelos auditores fiscais.",
            "B": "Identificou-se, nos relatórios financeiros preliminares, diversas inconsistências orçamentárias.",
            "C": "Alugam-se salas comerciais no edifício central para escritórios de assessoria aduaneira.",
            "D": "Precisa-se de novos técnicos capacitados para atuarem na fiscalização de fronteiras.",
            "E": "Deve haverem muitos recursos administrativos aguardando julgamento no conselho."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Em 'Alugam-se salas comerciais', o verbo é Transitivo Direto (VTD) acompanhado do pronome apassivador 'se'. O sujeito paciente é 'salas comerciais' (plural), exigindo o verbo no plural ('salas comerciais são alugadas').",
            "analise_alternativas": {
                "A": "Incorreta. 'Trata-se de' é VTI com Índice de Indeterminação do Sujeito. O verbo fica OBRIGATORIAMENTE no singular ('Trata-se de questões').",
                "B": "Incorreta. O sujeito é 'diversas inconsistências' (plural), logo o correto é 'Identificaram-se diversas inconsistências'.",
                "C": "CORRETA. 'Alugam-se salas' = 'Salas são alugadas'. Voz passiva sintética com sujeito no plural.",
                "D": "Incorreta. Embora a oração principal esteja certa, a opção C é o exemplo clássico de concordância perfeita, enquanto em 'precisa-se de... para atuarem' há oscilação de infinitivo flexionado.",
                "E": "Incorreta. O verbo 'haver' no sentido de existir é impessoal e transmite a impessoalidade ao auxiliar: 'Deve haver' (singular)."
            },
            "fundamentacao_legal": "Norma Gramatical - Voz Passiva Sintética vs Índice de Indeterminação do Sujeito.",
            "pegadinha_da_banca": "VTD + SE = Partícula Apassivadora (concorda com o sujeito). VTI / VI / VL + SE = Índice de Indeterminação (verbo sempre no singular)."
        }
    },
    {
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário",
        "ano": 2023,
        "banca": "Cesgranrio",
        "materia": "Língua Portuguesa",
        "assunto": "Regência Verbal e Emprego do Pronome Oblíquo",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Gramática Normativa (Regência Verbal)",
        "sumula_ref": "",
        "enunciado": "A frase que apresenta regência verbal e substituição pronominal adequadas segundo a norma culta é:",
        "alternativas": {
            "A": "O gerente assistiu o cliente durante o atendimento e assistiu-lhe com dedicação.",
            "B": "O assessor informou os novos correntistas sobre as taxas, informando-os de suas vantagens.",
            "C": "O candidato aspira ao cargo de chefia bancária e aspira-o desde o início da carreira.",
            "D": "O banco obedece os regulamentos do Banco Central sem questioná-los.",
            "E": "Ele visou o cheque com a assinatura e visou-lhe para liberação imediata."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "O verbo 'informar' é bitransitivo (VTDI): quem informa, informa algo a alguém (ou informa alguém de/sobre algo). 'Informando-os (objeto direto) de suas vantagens (objeto indireto)' está impecável.",
            "analise_alternativas": {
                "A": "Incorreta. No sentido de prestar ajuda, 'assistir' é VTD ('assistiu-o', não 'assistiu-lhe').",
                "B": "CORRETA. Regência clássica: 'informar alguém (os) de/sobre algo'.",
                "C": "Incorreta. No sentido de almejar/pretender, 'aspirar' é VTI regido por 'a' ('aspira a ele', e não aceita 'o').",
                "D": "Incorreta. O verbo 'obedecer' é VTI, exige a preposição 'a' ('obedece aos regulamentos').",
                "E": "Incorreta. No sentido de colocar visto/rubrica, 'visar' é VTD ('visou-o', não 'visou-lhe')."
            },
            "fundamentacao_legal": "Gramática Normativa - Regência dos verbos Informar, Assistir, Aspirar e Obedecer.",
            "pegadinha_da_banca": "Cuidado com o verbo 'obedecer': no dia a dia as pessoas usam sem preposição, mas para a banca examinadora ele é estritamente VTI ('obedecer A alguém / A algo')."
        }
    },

    # ==================== SEGURANÇA DA INFORMAÇÃO & LGPD ====================
    {
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário Novo - Tecnologia da Informação",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Segurança da Informação",
        "assunto": "Golpes Cibernéticos e Engenharia Social - Phishing e Ransomware",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Cartilha de Segurança para a Internet (CERT.br)",
        "sumula_ref": "",
        "enunciado": "Um colaborador de instituição financeira recebe uma mensagem eletrônica fraudulenta com logotipo idêntico ao da intranet corporativa, solicitando a atualização urgente de sua senha de acesso sob pena de bloqueio da conta. Ao clicar no link, ele é direcionado a uma página clonada que captura suas credenciais. Esse tipo de ataque cibernético de engenharia social é classificado como:",
        "alternativas": {
            "A": "Ransomware criptográfico.",
            "B": "Ataque de negação de serviço distribuído (DDoS).",
            "C": "Phishing.",
            "D": "Buffer overflow.",
            "E": "Cavalo de Troia (Trojan) do tipo backdoor."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Phishing é a técnica de engenharia social que 'pesca' dados e credenciais do usuário induzindo-o ao erro por meio de e-mails, mensagens ou páginas falsas que imitam instituições legítimas.",
            "analise_alternativas": {
                "A": "Incorreta. Ransomware é o malware que sequestra arquivos criptografando-os e exigindo resgate.",
                "B": "Incorreta. DDoS visa sobrecarregar servidores para tirá-los do ar.",
                "C": "CORRETA. Definição exata de ataque de Phishing.",
                "D": "Incorreta. Buffer overflow é falha de estouro de memória em programas.",
                "E": "Incorreta. Trojan backdoor abre portas secretas para controle remoto do sistema."
            },
            "fundamentacao_legal": "Cartilha de Segurança do CERT.br - Capítulo Ataques na Internet.",
            "pegadinha_da_banca": "Phishing = pescar credenciais por engano do usuário. Ransomware = criptografar e cobrar resgate."
        }
    },

    # ==================== RACIOCÍNIO LÓGICO-MATEMÁTICO ====================
    {
        "concurso": "Polícia Rodoviária Federal",
        "orgao": "PRF",
        "cargo": "Policial Rodoviário Federal",
        "ano": 2023,
        "banca": "Cebraspe",
        "materia": "Raciocínio Lógico-Matemático",
        "assunto": "Lógica Proposicional - Equivalência da Condicional",
        "nivel": "Superior",
        "tipo": "certo_errado",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lógica Sentencial e Proposicional",
        "sumula_ref": "",
        "enunciado": "Considerando a proposição P: 'Se o motorista consumiu bebida alcoólica, então sua capacidade psicomotora está alterada', julgue o item a seguir:\n\nA proposição 'Se a capacidade psicomotora do motorista não está alterada, então ele não consumiu bebida alcoólica' é logicamente equivalente à proposição P.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Equivalência contrapositiva da condicional: 'P -> Q' é logicamente idêntico a '~Q -> ~P' (inverte as duas proposições e nega ambas).",
            "analise_alternativas": {
                "C": "CORRETA. A contrapositiva de 'Se bebeu -> alterou' é 'Se NÃO alterou -> NÃO bebeu'.",
                "E": "Incorreta. Essa é uma das principais leis de equivalência lógica mais cobradas pelo Cebraspe."
            },
            "fundamentacao_legal": "Regra da Contrapositiva da Implicação Lógica: (P -> Q) <==> (~Q -> ~P).",
            "pegadinha_da_banca": "Não confunda com inverter sem negar! 'Se alterou, então bebeu' NÃO é equivalente."
        }
    },

    # ==================== ÉTICA NO SERVIÇO PÚBLICO ====================
    {
        "concurso": "Instituto Nacional do Seguro Social",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2023,
        "banca": "Cebraspe",
        "materia": "Ética no Serviço Público",
        "assunto": "Decreto nº 1.171/1994 - Código de Ética Profissional",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Decreto nº 1.171/1994, Seção I, Capítulo I, Item IX",
        "sumula_ref": "",
        "enunciado": "A respeito das regras deontológicas constantes do Código de Ética Profissional do Servidor Público Civil do Poder Executivo Federal (Decreto nº 1.171/1994), julgue o item:\n\nA dignidade, o decoro, o zelo, a eficácia e a consciência dos princípios morais são primados maiores que devem nortear o servidor público, seja no exercício do cargo ou função, ou fora dele, já que seus atos na vida particular poderão acrescer ou diminuir o seu bom conceito na vida funcional.",
        "alternativas": {
            "C": "Certo",
            "E": "Errado"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "A conduta ética do servidor público federal transcende o horário de trabalho. O que ele faz na vida privada reflete diretamente no prestígio do cargo público.",
            "analise_alternativas": {
                "C": "CORRETA. Texto literal do inciso I das Regras Deontológicas do Decreto nº 1.171/1994.",
                "E": "Incorreta. A banca costuma tentar limitar a ética apenas ao ambiente da repartição."
            },
            "fundamentacao_legal": "Decreto nº 1.171/1994, Capítulo I, Seção I, Inciso I.",
            "pegadinha_da_banca": "A banca tenta afirmar que a vida privada do servidor não importa para a Comissão de Ética. ERRADO! A vida particular reflete sim no conceito funcional."
        }
    }
]

for item in NOVAS_QUESTOES:
    item["id"] = current_id
    current_id += 1
    questoes.append(item)

with open(QUESTOES_FILE, 'w', encoding='utf-8') as f:
    json.dump(questoes, f, indent=2, ensure_ascii=False)

print(f"Sucesso! Banco expandido para {len(questoes)} questões.")
