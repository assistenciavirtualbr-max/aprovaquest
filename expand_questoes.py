import json
import os

QUESTOES_PATH = os.path.join(os.path.dirname(__file__), 'data', 'questoes.json')

with open(QUESTOES_PATH, 'r', encoding='utf-8') as f:
    questoes = json.load(f)

# Normalize existing 8 questions with tags
for q in questoes:
    q.setdefault('eh_lei_seca', True if 'Art' in q.get('comentario', {}).get('fundamentacao_legal', '') or 'Lei' in q.get('comentario', {}).get('fundamentacao_legal', '') else False)
    q.setdefault('eh_sumula', True if 'Súmula' in q.get('comentario', {}).get('fundamentacao_legal', '') or 'Súmula' in q.get('assunto', '') else False)
    q.setdefault('dificuldade', 'Médio')

novas_questoes = [
    {
        "id": 9,
        "concurso": "Tribunal Regional do Trabalho",
        "orgao": "TRT 2ª Região",
        "cargo": "Técnico Judiciário",
        "ano": 2024,
        "banca": "FCC",
        "materia": "Direito Constitucional",
        "assunto": "Eficácia e Aplicabilidade das Normas Constitucionais",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "CF/88, Art. 5º, XIII",
        "sumula_ref": "Súmula Vinculante 70 STF (conceito correlato)",
        "enunciado": "O artigo 5º, inciso XIII, da Constituição Federal dispõe que 'é livre o exercício de qualquer trabalho, ofício ou profissão, atendidas as qualificações profissionais que a lei estabelecer'. Quanto à classificação clássica de José Afonso da Silva sobre a aplicabilidade das normas constitucionais, trata-se de norma de eficácia:",
        "alternativas": {
            "A": "Plena, pois produz todos os seus efeitos imediatamente sem possibilidade de qualquer restrição legislativa posterior.",
            "B": "Contida (ou prospectiva), que nasce com plena eficácia, mas pode ter seu alcance restringido por lei ordinária futura.",
            "C": "Limitada de princípio institutivo, que depende de lei futura para começar a produzir seus efeitos essenciais.",
            "D": "Limitada de princípio programático, pois apenas traça uma diretriz ou meta social a ser alcançada pelo Estado.",
            "E": "Diferida ou inoperante, sem qualquer eficácia jurídica até a sua regulamentação pelo Congresso Nacional."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Norma de eficácia contida: tem aplicabilidade direta e imediata, mas NÃO INTEGRAL (pode ser contida/restringida por lei posterior).",
            "analise_alternativas": {
                "A": "Incorreta. A norma de eficácia plena NÃO admite restrição por lei ordinária.",
                "B": "CORRETA. O exercício da profissão é livre imediatamente. Caso o legislador queira restringir (ex: exigir OAB para advogados ou CRM para médicos), ele cria lei. Sem lei, a liberdade é plena.",
                "C": "Incorreta. Normas de eficácia limitada dependem de regulamentação para surtirem efeitos; a contida já produz efeitos desde o primeiro momento.",
                "D": "Incorreta. Princípios programáticos traçam metas sociais e políticas públicas (ex: erradicação da pobreza).",
                "E": "Incorreta. Não existe classificação de norma 'inoperante' na doutrina de José Afonso da Silva."
            },
            "fundamentacao_legal": "Doutrina de Direito Constitucional (José Afonso da Silva) e Art. 5º, XIII da CF/88.",
            "pegadinha_da_banca": "Grave o mnemônico: 'CONTIDA já nasce viva e pode ser RESTRINGIDA'. Já a 'LIMITADA nasce magrinha e precisa de lei para engordar'."
        }
    },
    {
        "id": 10,
        "concurso": "Polícia Rodoviária Federal",
        "orgao": "PRF",
        "cargo": "Policial Rodoviário Federal",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Direito Administrativo",
        "assunto": "Poderes Administrativos - Poder de Polícia",
        "nivel": "Superior",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "CTN, Art. 78",
        "sumula_ref": "",
        "enunciado": "Julgue o item subsequente acerca dos poderes da Administração Pública:\n\nSão atributos do poder de polícia administrativa a discricionariedade, a autoexecutoriedade e a coercibilidade, estando presente a autoexecutoriedade em todos os atos praticados com base nesse poder, inclusive na cobrança coercitiva imediata de multas pecuniárias aplicadas pela autoridade fiscalizadora.",
        "alternativas": {
            "C": "CERTO",
            "E": "ERRADO"
        },
        "gabarito": "E",
        "comentario": {
            "resumo": "A cobrança de MULTA NÃO é autoexecutória! A administração não pode penhorar bens por conta própria; precisa executar em juízo.",
            "analise_alternativas": {
                "C": "Incorreto. A assertiva peca ao generalizar dizendo que a autoexecutoriedade existe em TODOS os atos, especialmente na cobrança de multa.",
                "E": "CORRETO. A autoexecutoriedade consiste na faculdade de a Administração executar diretamente suas decisões sem intervenção do Judiciário (ex: apreender mercadoria estragada, interditar estabelecimento). Porém, a MULTA pecuniária é a clássica EXCEÇÃO à autoexecutoriedade: se o administrado não pagar, o Estado tem que inscrever em dívida ativa e ajuizar execução fiscal perante o Judiciário."
            },
            "fundamentacao_legal": "Código Tributário Nacional, Art. 78; Doutrina de Hely Lopes Meirelles / Maria Sylvia Zanella Di Pietro.",
            "pegadinha_da_banca": "Pegadinha clássica e implacável em provas de polícia: 'A multa pecuniária NÃO possui autoexecutoriedade'."
        }
    },
    {
        "id": 11,
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário - Agente Comercial",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Política Monetária e Taxa Selic",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Regulamento do Copom / Resoluções Bacen",
        "sumula_ref": "",
        "enunciado": "No Brasil, a taxa básica de juros da economia, que baliza as taxas de juros cobradas em empréstimos e investimentos e serve de principal instrumento de controle inflacionário, é a taxa Selic Meta. O órgão colegiado responsável por definir periodicamente a meta da taxa Selic é o:",
        "alternativas": {
            "A": "Comitê de Política Monetária (Copom), vinculado ao Banco Central do Brasil.",
            "B": "Conselho Monetário Nacional (CMN), exclusivamente.",
            "C": "Conselho de Controle de Atividades Financeiras (Coaf).",
            "D": "Comitê de Estabilidade Financeira (Comef).",
            "E": "Tesouro Nacional, por meio da Secretaria de Orçamento Federal."
        },
        "gabarito": "A",
        "comentario": {
            "resumo": "Meta de Inflação = CMN. Taxa Selic Meta = Copom (órgão do Banco Central).",
            "analise_alternativas": {
                "A": "CORRETA. O Copom (Comitê de Política Monetária), criado em 1996 e integrado pela Diretoria Colegiada do Banco Central, reúne-se a cada 45 dias para fixar a Meta da Taxa Selic.",
                "B": "Incorreta. O CMN fixa a META DE INFLAÇÃO, e não a Taxa Selic Meta.",
                "C": "Incorreta. O Coaf atua na prevenção e combate à lavagem de dinheiro e financiamento ao terrorismo.",
                "D": "Incorreta. O Comef monitora os riscos do sistema financeiro, sem competência para fixar a Selic.",
                "E": "Incorreta. O Tesouro Nacional administra a dívida pública e as contas fiscais da União."
            },
            "fundamentacao_legal": "Circular Bacen nº 3.868/2017 e Lei Complementar nº 179/2021 (Autonomia do Banco Central).",
            "pegadinha_da_banca": "Não confunda: O CMN define a META DE INFLAÇÃO (ex: 3% ao ano). O COPOM define a TAXA SELIC necessária para alcançar essa meta!"
        }
    },
    {
        "id": 12,
        "concurso": "Tribunal de Justiça",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "banca": "Vunesp",
        "materia": "Direito Penal",
        "assunto": "Crimes Praticados por Funcionário Público contra a Administração",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Código Penal, Art. 317 e 316",
        "sumula_ref": "",
        "enunciado": "Um funcionário público, em razão de sua função pública, SOLICITOU diretamente a um particular o pagamento de R$ 5.000,00 para agilizar a emissão de uma certidão de regularidade fundiária. O particular recusou o pagamento e denunciou o fato à corregedoria. Nesse caso, a conduta praticada pelo servidor configura o crime de:",
        "alternativas": {
            "A": "Corrupção passiva consumada.",
            "B": "Corrupção passiva tentada, já que o particular não pagou o valor solicitado.",
            "C": "Concussão consumada.",
            "D": "Prevaricação consumada.",
            "E": "Advocacia administrativa consumada."
        },
        "gabarito": "A",
        "comentario": {
            "resumo": "Solicitou = Corrupção Passiva. O crime é FORMAL e consuma-se com o mero ato de solicitar, independentemente de receber o dinheiro.",
            "analise_alternativas": {
                "A": "CORRETA. O crime de corrupção passiva (art. 317 do CP) possui os núcleos verbais: solicitar, receber ou aceitar promessa de vantagem indevida. Sendo crime formal, consuma-se no momento da solicitação, sendo o recebimento mero exaurimento.",
                "B": "Incorreta. Como é crime formal, a recusa do particular não torna o crime tentado; ele já está plenamente consumado.",
                "C": "Incorreta. Na Concussão (art. 316 do CP), o verbo típico é EXIGIR (sob tom de imposição ou temor), e não apenas solicitar.",
                "D": "Incorreta. Prevaricação (art. 319 do CP) consiste em retardar ou deixar de praticar ato de ofício para satisfazer interesse ou sentimento pessoal, sem solicitar propina.",
                "E": "Incorreta. Advocacia administrativa consiste em patrocinar interesse privado perante a administração pública valendo-se da qualidade de funcionário."
            },
            "fundamentacao_legal": "Código Penal, Artigo 317 (Corrupção Passiva) e Artigo 316 (Concussão).",
            "pegadinha_da_banca": "Mnemônico de ouro: 'EXIGIR = CONCUSSÃO' | 'SOLICITAR / RECEBER = CORRUPÇÃO PASSIVA'."
        }
    },
    {
        "id": 13,
        "concurso": "Tribunal de Justiça",
        "orgao": "TJ",
        "cargo": "Analista Judiciário",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Direito Administrativo",
        "assunto": "Responsabilidade Civil do Estado",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": True,
        "dificuldade": "Difícil",
        "artigo_lei": "CF/88, Art. 37, § 6º",
        "sumula_ref": "Tema 940 STF (Repercussão Geral)",
        "enunciado": "Um motorista de viatura policial oficial, durante o exercício de sua função, colidiu culposamente contra o veículo particular de João, causando-lhe danos materiais de grande monta. À luz do art. 37, § 6º, da Constituição da República e da jurisprudência vinculante fixada pelo STF no Tema 940 de Repercussão Geral, João:",
        "alternativas": {
            "A": "Pode ajuizar a ação indenizatória diretamente e exclusivamente contra o policial motorista causador do dano.",
            "B": "Pode escolher livremente se ajuíza a ação apenas contra o Estado, contra o policial motorista ou contra ambos em litisconsórcio passivo facultativo.",
            "C": "Deve ajuizar a ação indenizatória exclusivamente contra o Estado, sendo vedado o ajuizamento direto ou litisconsórcio contra o agente público.",
            "D": "Deve ajuizar a ação contra o policial e o Estado conjuntamente em regime de litisconsórcio passivo necessário obrigatório.",
            "E": "Não tem direito à indenização pelo Estado se demonstrado que o policial agiu apenas com culpa simples (imprudência leve)."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Tema 940 STF: Teoria da dupla garantia. A vítima processa o ESTADO. O Estado, se condenado, move ação de regresso contra o servidor.",
            "analise_alternativas": {
                "A": "Incorreta. O STF proibiu a ação direta da vítima contra o agente público causador do dano.",
                "B": "Incorreta. A tese da escolha livre (litisconsórcio facultativo) foi expressamente superada e rejeitada pelo STF no Tema 940.",
                "C": "CORRETA. Tese do Tema 940 do STF: 'A teor do disposto no art. 37, § 6º, da Constituição Federal, a ação por danos causados por agente público deve ser ajuizada contra o Estado ou a pessoa jurídica de direito privado prestadora de serviço público, sendo parte ilegítima para a lide o autor do ato, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa'.",
                "D": "Incorreta. O servidor é parte ilegítima no polo passivo da ação indenizatória movida pelo particular.",
                "E": "Incorreta. A responsabilidade do Estado perante o particular é objetiva (independe de dolo ou culpa do agente)."
            },
            "fundamentacao_legal": "CF/88, Art. 37, § 6º e STF RE 1.027.633/SP (Tema 940 da Repercussão Geral).",
            "pegadinha_da_banca": "A FGV adora cobrar teses antigas do STJ. Fique atento: o STF pacificou que o particular NÃO PODE colocar o servidor no polo passivo!"
        }
    },
    {
        "id": 14,
        "concurso": "Concurso Público Nacional Unificado",
        "orgao": "CNU",
        "cargo": "Especialista em Políticas Públicas e Gestão Governamental",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Língua Portuguesa",
        "assunto": "Concordância Verbal e Partícula 'Se'",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "",
        "sumula_ref": "",
        "enunciado": "Assinale a alternativa que atende rigorosamente às regras de concordância verbal estabelecidas pela norma-padrão da Língua Portuguesa:",
        "alternativas": {
            "A": "Aluga-se salas comerciais mobiliadas na região central da capital.",
            "B": "Precisa-se de analistas qualificados para a execução das auditorias tributárias.",
            "C": "Tratam-se de questões prioritárias para o desenvolvimento sustentável do país.",
            "D": "Construiu-se, ao longo dos últimos anos, várias pontes e viadutos modernos.",
            "E": "Haviam muitos inscritos no concurso para as vagas de nível superior."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Com verbo transitivo indireto (quem precisa, precisa DE) + 'se', o 'se' é Índice de Indeterminação do Sujeito e o verbo fica SEMPRE no singular.",
            "analise_alternativas": {
                "A": "Incorreta. 'Salas comerciais mobiliadas' é o sujeito paciente. O verbo deve concordar no plural: 'Alugam-se salas'.",
                "B": "CORRETA. O verbo 'precisar' rege preposição ('de'). O 'se' funciona como Índice de Indeterminação do Sujeito (IIS), tornando o verbo obrigatoriamente singular: 'Precisa-se de analistas'.",
                "C": "Incorreta. O verbo 'tratar-se de' não vai para o plural com preposição: o correto é 'Trata-se de questões prioritárias'.",
                "D": "Incorreta. O sujeito é plural ('várias pontes e viadutos'). O correto é 'Construíram-se (...) várias pontes e viadutos'.",
                "E": "Incorreta. O verbo 'haver' no sentido de existir é impessoal e não tem plural: o correto é 'Havia muitos inscritos'."
            },
            "fundamentacao_legal": "Gramática Normativa (Celso Cunha & Lindley Cintra / Evanildo Bechara).",
            "pegadinha_da_banca": "Macetão: Verbo com preposição + SE = Verbo SEMPRE no singular (IIS). Verbo direto sem preposição + SE = Concorda com o sujeito (Pronome Apassivador)."
        }
    },
    {
        "id": 15,
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Open Finance e Pix",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Resoluções Conjuntas CMN/Bacen nº 1/2020 e BCB nº 1/2020",
        "sumula_ref": "",
        "enunciado": "O Open Finance (Sistema Financeiro Aberto), regulamentado pelo Banco Central do Brasil em conjunto com o Conselho Monetário Nacional, baseia-se no princípio de que os dados bancários pertencem ao cliente e não às instituições financeiras. Sobre as regras de compartilhamento de dados no Open Finance, é correto afirmar que:",
        "alternativas": {
            "A": "O compartilhamento pode ser realizado automaticamente pelas instituições sem a anuência prévia do correntista para viabilizar melhores taxas de crédito.",
            "B": "O consentimento do cliente é dispensado caso a troca de dados ocorra entre instituições financeiras pertencentes ao mesmo conglomerado econômico.",
            "C": "O compartilhamento de dados e serviços depende de consentimento prévio, livre, informado, inequívoco e com prazo de validade determinado dado pelo cliente.",
            "D": "Uma vez autorizado pelo cliente, o consentimento torna-se irrevogável pelo período mínimo estipulado de dois anos.",
            "E": "Apenas dados de pessoas físicas podem ser compartilhados, ficando as pessoas jurídicas excluídas do ecossistema do Open Finance."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Open Finance: consentimento obrigatório, prévio, específico, com prazo delimitado e revogável a qualquer momento pelo cliente.",
            "analise_alternativas": {
                "A": "Incorreta. Jamais há compartilhamento automático sem anuência prévia.",
                "B": "Incorreta. O consentimento é indispensável mesmo entre empresas de um mesmo conglomerado financeiro.",
                "C": "CORRETA. Conforme a Resolução Conjunta nº 1/2020 do CMN e BCB, o consentimento deve ser prévio, livre, informado, inequívoco, para finalidades determinadas e com prazo de vigência (geralmente até 12 meses), podendo ser revogado a qualquer momento pelo cliente.",
                "D": "Incorreta. O consentimento pode ser revogado a qualquer instante pelo cliente nos canais da instituição.",
                "E": "Incorreta. O Open Finance abrange amplamente pessoas físicas e pessoas jurídicas."
            },
            "fundamentacao_legal": "Resolução Conjunta nº 1/2020 (CMN/Bacen) e Lei Geral de Proteção de Dados (LGPD - Lei 13.709/18).",
            "pegadinha_da_banca": "A Cesgranrio costuma trocar 'revogável a qualquer momento' por 'irrevogável' ou afirmar que as instituições podem compartilhar dados por conta própria."
        }
    },
    {
        "id": 16,
        "concurso": "Tribunal de Contas da União",
        "orgao": "TCU",
        "cargo": "Auditor Federal de Controle Externo",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Direito Constitucional",
        "assunto": "Controle de Constitucionalidade e Súmula Vinculante 10 (Cláusula de Reserva de Plenário)",
        "nivel": "Superior",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": True,
        "dificuldade": "Difícil",
        "artigo_lei": "CF/88, Art. 97",
        "sumula_ref": "Súmula Vinculante nº 10 do STF",
        "enunciado": "Julgue o item a seguir com fulcro na jurisprudência do STF e na ordem constitucional vigente:\n\nViola a cláusula de reserva de plenário a decisão de órgão fracionário de tribunal que, embora não declare expressamente a inconstitucionalidade de lei ou ato normativo do poder público, afasta sua incidência, no todo ou em parte.",
        "alternativas": {
            "C": "CERTO",
            "E": "ERRADO"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Súmula Vinculante 10 do STF: Órgão fracionário (Turma/Câmara) NÃO pode afastar lei, mesmo sem usar a palavra 'inconstitucional'.",
            "analise_alternativas": {
                "C": "CORRETO. Este item é a transcrição literal da Súmula Vinculante nº 10 do STF. Para declarar a inconstitucionalidade ou afastar a incidência de uma lei, é obrigatório o voto da maioria absoluta dos membros do tribunal Pleno ou do seu Órgão Especial (art. 97 da CF/88).",
                "E": "Incorreto. A assertiva é exatamente o texto vinculante da SV nº 10."
            },
            "fundamentacao_legal": "Constituição Federal de 1988, Artigo 97 e Súmula Vinculante nº 10 do STF.",
            "pegadinha_da_banca": "A Cebraspe e a FCC tentam fazer o candidato achar que, se o juiz ou turma não usou a palavra 'inconstitucional', não viola o Plenário. Viola SIM!"
        }
    },
    {
        "id": 17,
        "concurso": "Receita Federal",
        "orgao": "RFB",
        "cargo": "Analista Tributário",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Raciocínio Lógico-Matemático",
        "assunto": "Equivalência Lógica e Negação da Condicional (Se...Então)",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "",
        "sumula_ref": "",
        "enunciado": "Considere a seguinte afirmação feita por um auditor fiscal: 'Se o contribuinte entregou a declaração com omissão de rendimentos, então ele será autuado pela fiscalização'. A negação lógica correta dessa afirmação é:",
        "alternativas": {
            "A": "Se o contribuinte não entregou a declaração com omissão de rendimentos, então ele não será autuado pela fiscalização.",
            "B": "O contribuinte não entregou a declaração com omissão de rendimentos ou ele não será autuado pela fiscalização.",
            "C": "O contribuinte entregou a declaração com omissão de rendimentos e não será autuado pela fiscalização.",
            "D": "Se o contribuinte for autuado pela fiscalização, então ele entregou a declaração com omissão de rendimentos.",
            "E": "O contribuinte não entregou a declaração com omissão e foi autuado pela fiscalização."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Negação do 'Se P então Q' = Regra do MANÉ (MAntém a primeira E NEga a segunda: P e ~Q).",
            "analise_alternativas": {
                "A": "Incorreta. A negação de uma condicional NÃO é outra condicional.",
                "B": "Incorreta. Aqui usou-se conectivo 'ou' e negou-se a primeira parte.",
                "C": "CORRETA. A negação da condicional (P -> Q) é dada por: P ^ ~Q. Mantém a primeira: 'O contribuinte entregou a declaração com omissão' E nega a segunda: 'não será autuado'.",
                "D": "Incorreta. Esta é a recíproca, que sequer é equivalente lógica.",
                "E": "Incorreta. Negou a primeira e manteve a segunda, que viola a regra."
            },
            "fundamentacao_legal": "Lógica Proposicional Formal (Tabela-Verdade da Condicional e Regras de De Morgan).",
            "pegadinha_da_banca": "Lembre-se do 'MANÉ': MAntém o P E NEga o Q. E jamais responda a negação de um 'Se...então' com outro 'Se...então'!"
        }
    },
    {
        "id": 18,
        "concurso": "Polícia Federal",
        "orgao": "PF",
        "cargo": "Escrivão de Polícia Federal",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Segurança da Informação",
        "assunto": "Criptografia Simétrica vs Assimétrica",
        "nivel": "Superior",
        "tipo": "certo_errado",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "",
        "sumula_ref": "",
        "enunciado": "Julgue o item no que se refere aos conceitos de segurança cibernética e criptografia:\n\nNos sistemas de criptografia assimétrica, utiliza-se um par de chaves matematicamente correlacionadas, denominadas chave pública e chave privada. A mensagem cifrada com a chave pública de um destinatário só pode ser decifrada mediante o emprego da chave privada correspondente desse mesmo destinatário.",
        "alternativas": {
            "C": "CERTO",
            "E": "ERRADO"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Criptografia assimétrica = par de chaves (pública para cifrar, privada para decifrar).",
            "analise_alternativas": {
                "C": "CORRETO. É a definição exata de criptografia de chave pública (assimétrica, como RSA e ECC). A chave pública é distribuída livremente para qualquer pessoa cifrar a mensagem, mas apenas quem detém a respectiva chave privada exclusiva consegue decifrá-la e ler o conteúdo.",
                "E": "Incorreto. A descrição do enunciado está perfeita."
            },
            "fundamentacao_legal": "Cartilha de Segurança para a Internet (CERT.br) e Padrões Criptográficos ICP-Brasil.",
            "pegadinha_da_banca": "A Cebraspe tenta inverter: dizer que se cifra com a privada e decifra com a pública para sigilo. Cifrar com a privada serve para ASSINATURA DIGITAL (autenticidade), enquanto para SIGILO/CONFIDENCIALIDADE cifra-se com a PÚBLICA do destinatário!"
        }
    },
    {
        "id": 19,
        "concurso": "Tribunal de Justiça",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "banca": "Vunesp",
        "materia": "Direito Processual Civil",
        "assunto": "Prazos Processuais e Contagem em Dias Úteis",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "Código de Processo Civil (CPC/2015), Art. 219",
        "sumula_ref": "",
        "enunciado": "Nos termos do Código de Processo Civil de 2015 (Lei nº 13.105/2015), na contagem de prazo em dias, estabelecido por lei ou pelo juiz, para a prática de ato processual:",
        "alternativas": {
            "A": "Computar-se-ão exclusivamente os dias corridos, incluindo-se sábados, domingos e feriados.",
            "B": "Computar-se-ão somente os dias úteis, aplicando-se essa regra apenas aos prazos processuais.",
            "C": "Computar-se-ão os dias úteis tanto para os prazos processuais quanto para os prazos de prescrição e decadência do direito material.",
            "D": "Computar-se-ão os sábados e excluir-se-ão apenas os domingos e feriados forenses.",
            "E": "Suspender-se-á a contagem no primeiro dia do ano novo até o final do primeiro semestre forense."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "CPC/2015 Art. 219: Na contagem de prazos em dias computam-se APENAS DIAS ÚTEIS (aplica-se somente aos prazos processuais).",
            "analise_alternativas": {
                "A": "Incorreta. Dias corridos era a sistemática do antigo CPC de 1973.",
                "B": "CORRETA. Art. 219 do CPC: 'Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar-se-ão somente os dias úteis. Parágrafo único: O disposto neste artigo aplica-se somente aos prazos processuais'.",
                "C": "Incorreta. Prazos de direito material (prescrição, decadência do Código Civil) continuam correndo de forma contínua/ininterrupta.",
                "D": "Incorreta. Sábados não são dias úteis forenses.",
                "E": "Incorreta. O recesso forense suspende prazos entre 20 de dezembro e 20 de janeiro (art. 220)."
            },
            "fundamentacao_legal": "CPC/2015, Art. 219, caput e parágrafo único.",
            "pegadinha_da_banca": "A Vunesp tenta estender a contagem em dias úteis para o direito material (como prescrição e decadência). Fique atento: dias úteis é SOMENTE para prazo processual!"
        }
    },
    {
        "id": 20,
        "concurso": "INSS",
        "orgao": "INSS",
        "cargo": "Técnico do Seguro Social",
        "ano": 2024,
        "banca": "Cebraspe",
        "materia": "Seguridade Social",
        "assunto": "Princípios Constitucionais da Seguridade Social",
        "nivel": "Médio",
        "tipo": "certo_errado",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "CF/88, Art. 195, § 5º",
        "sumula_ref": "",
        "enunciado": "Julgue o item à luz dos princípios constitucionais que regem a Seguridade Social no Brasil:\n\nEm atenção ao princípio da contrapartida ou precedência da fonte de custeio, nenhum benefício ou serviço da seguridade social poderá ser criado, majorado ou estendido sem a correspondente fonte de custeio total.",
        "alternativas": {
            "C": "CERTO",
            "E": "ERRADO"
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Princípio da Contrapartida (Art. 195, § 5º da CF): Para criar ou aumentar benefício, TEM que indicar de onde virá o dinheiro (custeio total).",
            "analise_alternativas": {
                "C": "CORRETO. Reproduz textualmente o art. 195, § 5º, da CF/88: 'Nenhum benefício ou serviço da seguridade social poderá ser criado, majorado ou estendido sem a correspondente fonte de custeio total'. Trata-se da pedra angular do equilíbrio atuarial e financeiro da seguridade.",
                "E": "Incorreto. A assertiva é a própria letra da Constituição Federal."
            },
            "fundamentacao_legal": "Constituição Federal de 1988, Artigo 195, § 5º.",
            "pegadinha_da_banca": "A banca adora trocar 'custeio total' por 'custeio parcial' ou tentar dizer que esse princípio se aplica somente à Previdência e não à Saúde ou Assistência Social."
        }
    },
    {
        "id": 21,
        "concurso": "Ministério Público da União",
        "orgao": "MPU",
        "cargo": "Técnico do MPU - Administração",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Direito Administrativo",
        "assunto": "Atos Administrativos - Motivação e Teoria dos Motivos Determinantes",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Lei 9.784/99, Art. 50",
        "sumula_ref": "",
        "enunciado": "Uma autoridade pública praticou ato discricionário exonerando um servidor ocupante de cargo em comissão, justificando expressamente no termo de exoneração que o motivo da dispensa foi 'a necessidade inadiável de redução de 20% das despesas de pessoal para cumprimento da Lei de Responsabilidade Fiscal'. Dias depois, restou comprovado mediante auditoria que as contas do órgão estavam com folga orçamentária e que tal redução nunca foi necessária nem planejada. Diante disso, segundo a Teoria dos Motivos Determinantes:",
        "alternativas": {
            "A": "O ato de exoneração é perfeitamente válido, pois cargos em comissão são de livre nomeação e exoneração ('ad nutum'), sendo a motivação irrelevante.",
            "B": "O ato de exoneração torna-se nulo, uma vez que, tendo a Administração optado por motivar o ato, a validade deste vincula-se à veracidade e legalidade do motivo declarado.",
            "C": "O servidor exonerado adquire automaticamente estabilidade excepcional no serviço público por desvio de finalidade.",
            "D": "O ato de exoneração converte-se de ofício em demissão por infração disciplinar praticada pela autoridade signatária.",
            "E": "O ato é anulável somente se a autoridade ratificar o erro e emitir nova portaria substitutiva."
        },
        "gabarito": "B",
        "comentario": {
            "resumo": "Teoria dos Motivos Determinantes: Se a administração alegou um motivo, ela fica AMARRADA a ele! Se o motivo for falso ou inexistente, o ato é NULO.",
            "analise_alternativas": {
                "A": "Incorreta. Embora o cargo seja em comissão (não exigindo motivação obrigatória), ao declarar um motivo, o ato fica a ele subordinado.",
                "B": "CORRETA. Conforme a consagrada Teoria dos Motivos Determinantes, quando a autoridade explicita os motivos de sua decisão (mesmo em ato discricionário), a validade do ato fica vinculada à comprovação real e verídica desses motivos. Motivo falso = ato nulo.",
                "C": "Incorreta. O servidor comissionado não adquire estabilidade.",
                "D": "Incorreta. Exoneração não se confunde com punição disciplinar de demissão.",
                "E": "Incorreta. O vício no motivo contamina a própria existência jurídica do ato."
            },
            "fundamentacao_legal": "Lei nº 9.784/1999, Art. 50; Doutrina pacífica de Direito Administrativo (Celso Antônio Bandeira de Mello).",
            "pegadinha_da_banca": "Lembre-se sempre: Se o gestor não era obrigado a motivar mas resolveu motivar, a mentira contamina o ato e anula tudo!"
        }
    },
    {
        "id": 22,
        "concurso": "Banco do Brasil",
        "orgao": "BB",
        "cargo": "Escriturário - Agente de Tecnologia",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Língua Portuguesa",
        "assunto": "Pontuação e Emprego da Vírgula",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": False,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "",
        "sumula_ref": "",
        "enunciado": "A pontuação de um texto reflete a estrutura sintática das orações e a hierarquia dos termos. O uso da vírgula está plenamente de acordo com as normas gramaticais em:",
        "alternativas": {
            "A": "Os clientes do banco com renda mais elevada, costumam aplicar seus recursos em títulos de renda fixa isentos de imposto de renda.",
            "B": "O gerente da agência informou, que o prazo para renegociação de dívidas terminaria na próxima sexta-feira.",
            "C": "Diante das novas diretrizes divulgadas pelo Banco Central, as instituições financeiras atualizaram seus sistemas tecnológicos.",
            "D": "Os investimentos em títulos públicos federais proporcionam, alta rentabilidade com liquidez diária aos poupadores.",
            "E": "O Conselho de Administração da empresa aprovou com louvor, o plano estratégico de expansão internacional."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Vírgula separa adjunto adverbial deslocado ('Diante das novas diretrizes...'). NUNCA se separa sujeito de predicado nem verbo de seu objeto!",
            "analise_alternativas": {
                "A": "Incorreta. Separou incorretamente o sujeito ('Os clientes...') do verbo ('costumam').",
                "B": "Incorreta. Separou indevidamente o verbo ('informou') da oração subordinada substantiva objetiva direta ('que o prazo...').",
                "C": "CORRETA. 'Diante das novas diretrizes divulgadas pelo Banco Central' é uma oração subordinada adverbial ou adjunto adverbial extenso antecipado/deslocado, exigindo vírgula obrigatória.",
                "D": "Incorreta. Separou indevidamente o verbo transitivo direto ('proporcionam') do seu objeto direto ('alta rentabilidade').",
                "E": "Incorreta. O verbo 'aprovou' não pode ser separado com vírgula do objeto direto 'o plano estratégico'."
            },
            "fundamentacao_legal": "Gramática Normativa da Língua Portuguesa (Regra de proibição da vírgula entre termos imediatos da oração).",
            "pegadinha_da_banca": "Regra número um de pontuação de concurso: JAMAIS ponha vírgula entre Sujeito e Verbo, nem entre Verbo e Objeto Direto/Indireto!"
        }
    },
    {
        "id": 23,
        "concurso": "Caixa Econômica Federal",
        "orgao": "CEF",
        "cargo": "Técnico Bancário",
        "ano": 2024,
        "banca": "Cesgranrio",
        "materia": "Conhecimentos Bancários",
        "assunto": "Garantias do Sistema Financeiro Nacional - Aval vs Fiança",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Médio",
        "artigo_lei": "Código Civil, Art. 818 e Lei Uniforme de Genebra (LUG)",
        "sumula_ref": "Súmula 26 STJ",
        "enunciado": "No âmbito das garantias pessoais (fidejussórias) utilizadas nas operações de crédito bancário, a distinção entre fiança e aval é fundamental. Assinale a afirmativa correta a respeito dessas modalidades de garantia:",
        "alternativas": {
            "A": "O aval é uma garantia tipicamente contratual que confere ao avalista o benefício de ordem para exigir que os bens do devedor principal sejam executados primeiro.",
            "B": "A fiança é prestada exclusivamente em títulos de crédito cambiários, como notas promissórias e duplicatas.",
            "C": "O aval é ato unilateral e autônomo prestado em títulos de crédito, gerando responsabilidade solidária sem benefício de ordem.",
            "D": "A fiança subsiste plenamente mesmo que a obrigação principal que lhe deu origem seja declarada nula de pleno direito.",
            "E": "Tanto no aval quanto na fiança, a outorga conjugal (vênia uxória) é sempre dispensável caso o cônjuge do garante exerça profissão liberal."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Aval = Título de crédito, autônomo, solidário (SEM benefício de ordem). Fiança = Contrato, acessório (COM benefício de ordem).",
            "analise_alternativas": {
                "A": "Incorreta. O aval NÃO tem benefício de ordem; a fiança é que tem em regra.",
                "B": "Incorreta. Fiança é garantia contratual (contratos bancários, locação, mútuo). Quem é exclusivo de título de crédito é o AVAL.",
                "C": "CORRETA. O aval é declaração cambial unilateral, abstrata e autônoma. O avalista equipara-se ao devedor principal e responde solidariamente perante o credor.",
                "D": "Incorreta. Como a fiança é garantia ACESSÓRIA, a nulidade da obrigação principal acarreta a nulidade da fiança (o acessório segue o principal). Já a obrigação do avalista é autônoma.",
                "E": "Incorreta. A regra geral do Código Civil (art. 1.647, III) exige vênia conjugal para a fiança."
            },
            "fundamentacao_legal": "Lei Uniforme de Genebra (Decreto 57.663/66) e Código Civil, artigos 818 a 839 e art. 897 a 900.",
            "pegadinha_da_banca": "Cesgranrio e FCC adoram inverter: dizer que 'aval tem benefício de ordem' ou que 'fiança é em título de crédito'. Guarde a dupla: Aval = Título / Fiança = Contrato."
        }
    },
    {
        "id": 24,
        "concurso": "Tribunal de Justiça",
        "orgao": "TJ-SP",
        "cargo": "Escrevente Técnico Judiciário",
        "ano": 2024,
        "banca": "Vunesp",
        "materia": "Direito Constitucional",
        "assunto": "Nacionalidade e Cargos Privativos de Brasileiro Nato",
        "nivel": "Médio",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Fácil",
        "artigo_lei": "CF/88, Art. 12, § 3º",
        "sumula_ref": "",
        "enunciado": "A Constituição Federal de 1988 estabelece que a lei não poderá estabelecer distinção entre brasileiros natos e naturalizados, salvo nos casos expressamente previstos pelo texto constitucional. Dentre os cargos a seguir relacionados, aquele que é privativo de brasileiro nato é o de:",
        "alternativas": {
            "A": "Ministro da Justiça e Segurança Pública.",
            "B": "Governador de Estado federado.",
            "C": "Presidente da Câmara dos Deputados.",
            "D": "Procurador-Geral da República.",
            "E": "Embaixador do Brasil em organismos multilaterais."
        },
        "gabarito": "C",
        "comentario": {
            "resumo": "Mnemônico clássico MP3.COM: Ministros do STF, Presidente da República e Vice, Presidente da Câmara, Presidente do Senado, Carreira diplomática, Oficial das FA, Ministro de Estado da Defesa.",
            "analise_alternativas": {
                "A": "Incorreta. O único Ministro de Estado que precisa ser nato é o Ministro de Estado da DEFESA (art. 12, § 3º, VII).",
                "B": "Incorreta. Governadores e Prefeitos podem ser naturalizados.",
                "C": "CORRETA. Conforme art. 12, § 3º, II, da CF/88, o cargo de Presidente da Câmara dos Deputados é privativo de brasileiro nato (pois integra a linha sucessória imediata da Presidência da República).",
                "D": "Incorreta. O PGR não exige natividade expressa no rol do art. 12, § 3º.",
                "E": "Incorreta. A carreira diplomática exige brasileiro nato para os cargos de diplomata, mas chefes de missão extraordinária temporária podem ser designados por lei."
            },
            "fundamentacao_legal": "Constituição Federal de 1988, Art. 12, § 3º.",
            "pegadinha_da_banca": "Mnemônico obrigatório: MP3.COM -> M (Ministro do STF) | P3 (Pres. da República, Pres. da Câmara, Pres. do Senado) | C (Carreira diplomática) | O (Oficial das Forças Armadas) | M (Ministro da Defesa)."
        }
    },
    {
        "id": 25,
        "concurso": "Controladoria-Geral da União",
        "orgao": "CGU",
        "cargo": "Auditor Federal de Finanças e Controle",
        "ano": 2024,
        "banca": "FGV",
        "materia": "Direito Administrativo",
        "assunto": "Lei de Improbidade Administrativa - Alterações da Lei 14.230/21",
        "nivel": "Superior",
        "tipo": "multipla_escolha",
        "eh_lei_seca": True,
        "eh_sumula": False,
        "dificuldade": "Difícil",
        "artigo_lei": "Lei 8.429/92 com redação da Lei 14.230/21, Art. 1º, §§ 1º e 2º",
        "sumula_ref": "Tema 1199 STF",
        "enunciado": "Com o advento da expressiva reforma promovida pela Lei nº 14.230/2021 na Lei de Improbidade Administrativa (Lei nº 8.429/1992), o elemento subjetivo necessário para a configuração dos atos de improbidade administrativa que causam prejuízo ao erário (art. 10) passou a ser:",
        "alternativas": {
            "A": "Apenas o dolo específico, não mais se admitindo a modalidade culposa em nenhuma hipótese de improbidade administrativa.",
            "B": "Tanto o dolo quanto a culpa grave (culpa temerária) devidamente atestada pelo Tribunal de Contas.",
            "C": "A culpa estrita, desde que decorrente de negligência continuada na fiscalização dos recursos públicos.",
            "D": "O dolo genérico, consistente na simples voluntariedade de praticar o ato formal sem intenção de fim ilícito.",
            "E": "A culpa presumida com inversão do ônus da prova em desfavor do gestor público ordenador de despesas."
        },
        "gabarito": "A",
        "comentario": {
            "resumo": "A Lei 14.230/21 EXTINGUIU a improbidade culposa! Agora TODOS os atos de improbidade exigem DOLO ESPECÍFICO.",
            "analise_alternativas": {
                "A": "CORRETA. Art. 1º, § 1º da Lei 8.429/92 (com redação dada pela Lei 14.230/21): 'Consideram-se atos de improbidade administrativa apenas as condutas dolosas tipificadas nos arts. 9º, 10 e 11'. O § 2º reforça que se exige o dolo específico (vontade livre e consciente de alcançar o resultado ilícito).",
                "B": "Incorreta. A culpa grave foi banida da tipificação de improbidade.",
                "C": "Incorreta. Negligência ou imperícia constituem culpa, que não configuram mais improbidade (podem configurar no máximo infração disciplinar).",
                "D": "Incorreta. O art. 1º, § 3º expressamente rejeita o mero dolo genérico ou voluntariedade.",
                "E": "Incorreta. Não existe presunção de culpa em improbidade administrativa."
            },
            "fundamentacao_legal": "Lei nº 8.429/1992, Art. 1º, §§ 1º, 2º e 3º e Tema 1199 do STF (ARE 843.989).",
            "pegadinha_da_banca": "Essa foi a maior mudança dos últimos 30 anos no Direito Administrativo: NÃO EXISTE MAIS IMPROBIDADE CULPOSA NO BRASIL!"
        }
    }
]

questoes.extend(novas_questoes)

with open(QUESTOES_PATH, 'w', encoding='utf-8') as f:
    json.dump(questoes, f, indent=2, ensure_ascii=False)

print(f"Total de questões agora no banco: {len(questoes)}")
