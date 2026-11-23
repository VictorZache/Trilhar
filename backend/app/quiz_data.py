"""
Quiz de Orientação Vocacional - Área de TI
25 perguntas adaptadas para crianças e adolescentes do Ensino Fundamental
Cada resposta adiciona pontos a uma ou mais carreiras.
"""

CAREERS = [
    {
        "id": "desenvolvimento",
        "nome": "Desenvolvimento de Software",
        "descricao": "Cria programas, apps, jogos e sites. Ideal para quem gosta de lógica, programação e construir coisas do zero.",
        "icone": "code",
        "cor": "#0052ff",
        "conhecimento_necessario": [
            {
                "titulo": "Lógica de Programação",
                "descricao": "Aprenda a pensar como um programador: decompor problemas em passos menores, criar sequências lógicas e resolver desafios de forma sistemática. Este é o fundamento de toda programação.",
                "tipo_jogo": "sequencia",
                "descricao_jogo": "Arraste blocos de comandos na ordem correta para fazer o robô chegar até o destino final.",
                "dados": {"tipo": "sequencia", "tema": "logica_programacao"}
            },
            {
                "titulo": "Variáveis e Tipos de Dados",
                "descricao": "Aprenda a guardar informações na memória do computador: números (inteiros e decimais), textos (strings), verdadeiro/falso (booleanos) e mais.",
                "tipo_jogo": "caixa_memoria",
                "descricao_jogo": "Organize os dados nas caixas de armazenamento colocando cada dado no tipo correto.",
                "dados": {"tipo": "caixa_memoria", "tema": "variaveis"}
            },
            {
                "titulo": "Estruturas de Repetição (loops)",
                "descricao": "Aprenda a fazer o computador repetir ações várias vezes sem escrever tudo de novo, usando estruturas como for e while.",
                "tipo_jogo": "repeticao",
                "descricao_jogo": "Use blocos de repetição para fazer o robô completar tarefas repetitivas com menos comandos.",
                "dados": {"tipo": "repeticao", "tema": "loops"}
            },
            {
                "titulo": "Estruturas de Decisão (if/else)",
                "descricao": "Aprenda a fazer o programa tomar decisões: se acontecer X, faça Y; senão, faça Z.",
                "tipo_jogo": "decisao",
                "descricao_jogo": "Crie caminhos diferentes no labirinto baseado em condições verdadeiras ou falsas.",
                "dados": {"tipo": "decisao", "tema": "condicionais"}
            },
            {
                "titulo": "Funções e Parâmetros",
                "descricao": "Aprenda a criar blocos de código reutilizáveis que recebem entradas (parâmetros) e produzem saídas.",
                "tipo_jogo": "funcao",
                "descricao_jogo": "Crie receitas (funções) que o robô pode executar com diferentes ingredientes (parâmetros).",
                "dados": {"tipo": "funcao", "tema": "funcoes"}
            },
            {
                "titulo": "Arrays e Listas",
                "descricao": "Aprenda a armazenar múltiplos valores em uma única variável e acessar cada um por posição (índice).",
                "tipo_jogo": "lista",
                "descricao_jogo": "Organize itens em prateleiras (listas) e acesse cada um pelo número da posição.",
                "dados": {"tipo": "lista", "tema": "arrays"}
            },
            {
                "titulo": "Orientação a Objetos Básica",
                "descricao": "Aprenda a criar classes (modelos) e objetos (instâncias): entidades com características e comportamentos.",
                "tipo_jogo": "classe_objeto",
                "descricao_jogo": "Crie classes (modelos) e instancie objetos com características diferentes.",
                "dados": {"tipo": "classe_objeto", "tema": "oo"}
            },
            {
                "titulo": "Banco de Dados Simples (SQL)",
                "descricao": "Aprenda a guardar e consultar informações em tabelas usando linguagem SQL simples.",
                "tipo_jogo": "sql",
                "descricao_jogo": "Escreva comandos SQL simples para consultar dados em uma tabela simples.",
                "dados": {"tipo": "sql", "tema": "banco_dados"}
            },
            {
                "titulo": "Versionamento com Git",
                "descricao": "Aprenda a salvar versões do seu código e voltar no tempo se algo der errado, usando Git.",
                "tipo_jogo": "commit",
                "descricao_jogo": "Faça 'commits' para salvar versões do seu projeto e volte para versões anteriores.",
                "dados": {"tipo": "commit", "tema": "git"}
            },
            {
                "titulo": "HTML, CSS e JavaScript Básicos",
                "descricao": "Aprenda a criar páginas web: estrutura (HTML), estilo (CSS) e interatividade (JavaScript).",
                "tipo_jogo": "html_css_js",
                "descricao_jogo": "Monte uma página simples adicionando elementos HTML, estilo CSS e interatividade com JavaScript.",
                "dados": {"tipo": "html_css_js", "tema": "web"}
            },
        ]
    },
    {
        "id": "dados",
        "nome": "Análise de Dados",
        "descricao": "Transforma números em descobertas legais. Ideal para quem gosta de matemática, quebra-cabeça e encontrar padrões.",
        "icone": "chart",
        "cor": "#00d4ff",
        "conhecimento_necessario": [
            {
                "titulo": "Estatística Descritiva (média, mediana, moda)",
                "descricao": "Aprenda a resumir conjuntos de dados usando média, mediana e moda.",
                "tipo_jogo": "estatistica",
                "descricao_jogo": "Calcule a média, mediana e moda de um conjunto de números para resolver o desafio.",
                "dados": {"tipo": "estatistica", "tema": "estatistica_descritiva"}
            },
            {
                "titulo": "Gráficos e Visualizações",
                "descricao": "Aprenda a transformar dados em gráficos (barras, linhas, pizza) para entender melhor.",
                "tipo_jogo": "grafico",
                "descricao_jogo": "Crie o gráfico correto para representar os dados fornecidos.",
                "dados": {"tipo": "grafico", "tema": "visualizacao"}
            },
            {
                "titulo": "Planilhas (Excel/Google Sheets)",
                "descricao": "Aprenda a usar planilhas eletrônicas para organizar e calcular dados.",
                "tipo_jogo": "planilha",
                "descricao_jogo": "Preencha células de uma planilha com fórmulas simples (SOMA, MÉDIA, CONTAR).",
                "dados": {"tipo": "planilha", "tema": "planilhas"}
            },
            {
                "titulo": "Banco de Dados e Consultas SQL",
                "descricao": "Aprenda a buscar informações em bancos de dados usando linguagem SQL.",
                "tipo_jogo": "sql",
                "descricao_jogo": "Escreva consultas SQL para encontrar informações em uma tabela de dados.",
                "dados": {"tipo": "sql", "tema": "consultas"}
            },
            {
                "titulo": "Limpeza e Organização de Dados",
                "descricao": "Aprenda a tratar dados faltantes, duplicados e inconsistentes antes da análise.",
                "tipo_jogo": "limpeza",
                "descricao_jogo": "Identifique e corrija erros em um conjunto de dados sujo.",
                "dados": {"tipo": "limpeza", "tema": "limpeza_dados"}
            },
            {
                "titulo": "Interpretação de Gráficos",
                "descricao": "Aprenda a ler e interpretar diferentes tipos de gráficos para extrair insights.",
                "tipo_jogo": "interpretacao",
                "descricao_jogo": "Responda perguntas com base em gráficos de barras, linhas e setores.",
                "dados": {"tipo": "interpretacao", "tema": "graficos"}
            },
            {
                "titulo": "Probabilidade Básica",
                "descricao": "Aprenda a calcular a chance de eventos acontecerem.",
                "tipo_jogo": "probabilidade",
                "descricao_jogo": "Calcule a probabilidade de eventos simples (moeda, dado, cartas).",
                "dados": {"tipo": "probabilidade", "tema": "probabilidade"}
            },
            {
                "titulo": "Python para Análise (pandas)",
                "descricao": "Aprenda a usar a biblioteca pandas para manipular dados em Python.",
                "tipo_jogo": "pandas",
                "descricao_jogo": "Escreva comandos Python pandas para filtrar e agrupar dados.",
                "dados": {"tipo": "pandas", "tema": "pandas"}
            },
            {
                "titulo": "Storytelling com Dados",
                "descricao": "Aprenda a contar histórias com dados, contando uma história através de visualizações.",
                "tipo_jogo": "storytelling",
                "descricao_jogo": "Crie uma narrativa simples baseada em dados para explicar uma situação.",
                "dados": {"tipo": "storytelling", "tema": "storytelling"}
            },
            {
                "titulo": "Ética e Privacidade de Dados",
                "descricao": "Aprenda a proteger dados pessoais e usar informações de forma ética.",
                "tipo_jogo": "etica",
                "descricao_jogo": "Identifique quais dados são pessoais e como protegê-los adequadamente.",
                "dados": {"tipo": "etica", "tema": "etica_dados"}
            },
        ]
    },
    {
        "id": "seguranca",
        "nome": "Segurança da Informação",
        "descricao": "Protege sistemas e dados contra invasores. Ideal para quem é detalhista, curioso e gosta de resolver mistérios.",
        "icone": "shield",
        "cor": "#ff3b30",
        "conhecimento_necessario": [
            {
                "titulo": "O que é cibersegurança",
                "descricao": "Aprenda o que é cibersegurança e por que é importante proteger informações digitais.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é cibersegurança e por que é importante.",
                "dados": {"tipo": "conceito", "tema": "ciberseguranca"}
            },
            {
                "titulo": "Senhas fortes e autenticação",
                "descricao": "Aprenda a criar senhas seguras e entender autenticação de dois fatores.",
                "tipo_jogo": "senha",
                "descricao_jogo": "Crie senhas seguras e identifique senhas fracas em exemplos.",
                "dados": {"tipo": "senha", "tema": "senhas"}
            },
            {
                "titulo": "Phishing e engenharia social",
                "descricao": "Aprenda a identificar tentativas de enganar pessoas para roubar informações.",
                "tipo_jogo": "phishing",
                "descricao_jogo": "Identifique emails e mensagens suspeitas que são tentativas de phishing.",
                "dados": {"tipo": "phishing", "tema": "phishing"}
            },
            {
                "titulo": "Criptografia básica",
                "descricao": "Aprenda a cifrar e decifrar mensagens para mantê-las secretas.",
                "tipo_jogo": "criptografia",
                "descricao_jogo": "Codifique e decodifique mensagens usando cifras simples (César, substituição).",
                "dados": {"tipo": "criptografia", "tema": "criptografia"}
            },
            {
                "titulo": "Firewalls e redes seguras",
                "descricao": "Aprenda como firewalls protegem redes de acessos não autorizados.",
                "tipo_jogo": "firewall",
                "descricao_jogo": "Configure regras de firewall para permitir ou bloquear tráfego de rede.",
                "dados": {"tipo": "firewall", "tema": "rede_segura"}
            },
            {
                "titulo": "Vulnerabilidades comuns",
                "descricao": "Aprenda sobre falhas comuns de segurança (injeção SQL, XSS, etc).",
                "tipo_jogo": "vulnerabilidade",
                "descricao_jogo": "Identifique vulnerabilidades comuns em exemplos de código ou cenários.",
                "dados": {"tipo": "vulnerabilidade", "tema": "vulnerabilidades"}
            },
            {
                "titulo": "Leis de proteção de dados (LGPD)",
                "descricao": "Aprenda sobre a Lei Geral de Proteção de Dados e direitos dos titulares.",
                "tipo_jogo": "lgpd",
                "descricao_jogo": "Responda perguntas sobre direitos e deveres relacionados à LGPD.",
                "dados": {"tipo": "lgpd", "tema": "lgpd"}
            },
            {
                "titulo": "Auditoria de segurança",
                "descricao": "Aprenda a revisar sistemas para identificar falhas de segurança.",
                "tipo_jogo": "auditoria",
                "descricao_jogo": "Revise um sistema e identifique falhas de segurança.",
                "dados": {"tipo": "auditoria", "tema": "auditoria"}
            },
            {
                "titulo": "Resposta a incidentes",
                "descricao": "Aprenda o que fazer quando ocorre um incidente de segurança.",
                "tipo_jogo": "incidente",
                "descricao_jogo": "Siga os passos de resposta a incidente em um cenário de ataque.",
                "dados": {"tipo": "incidente", "tema": "incidente"}
            },
            {
                "titulo": "Hacking ético introdutório",
                "descricao": "Aprenda os princípios do hacking ético (testar sistemas com permissão).",
                "tipo_jogo": "hacking_etico",
                "descricao_jogo": "Simule um teste de invasão ético para encontrar e reportar vulnerabilidades.",
                "dados": {"tipo": "hacking_etico", "tema": "hacking_etico"}
            },
        ]
    },
    {
        "id": "cloud",
        "nome": "Computação em Nuvem",
        "descricao": "Cuida de arquivos e programas que ficam na internet. Ideal para quem gosta de organização e automação.",
        "icone": "cloud",
        "cor": "#8b5cf6",
        "conhecimento_necessario": [
            {
                "titulo": "O que é computação em nuvem",
                "descricao": "Aprenda o que é computação em nuvem e por que é usada.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é nuvem e por que é usada.",
                "dados": {"tipo": "conceito", "tema": "nuvem_conceito"}
            },
            {
                "titulo": "Modelos IaaS, PaaS, SaaS",
                "descricao": "Aprenda a diferença entre modelos de serviço em nuvem.",
                "tipo_jogo": "classificacao",
                "descricao_jogo": "Classifique serviços em IaaS, PaaS ou SaaS corretamente.",
                "dados": {"tipo": "classificacao", "tema": "modelos_nuvem"}
            },
            {
                "titulo": "Armazenamento em nuvem",
                "descricao": "Aprenda a armazenar e acessar arquivos na nuvem.",
                "tipo_jogo": "armazenamento",
                "descricao_jogo": "Envie e recupere arquivos de um armazenamento em nuvem simulado.",
                "dados": {"tipo": "armazenamento", "tema": "armazenamento_nuvem"}
            },
            {
                "titulo": "Máquinas virtuais",
                "descricao": "Aprenda o que são máquinas virtuais e como funcionam.",
                "tipo_jogo": "maquina_virtual",
                "descricao_jogo": "Crie e gerencie máquinas virtuais em um ambiente simulado.",
                "dados": {"tipo": "maquina_virtual", "tema": "maquina_virtual"}
            },
            {
                "titulo": "Banco de dados na nuvem",
                "descricao": "Aprenda a usar bancos de dados hospedados na nuvem.",
                "tipo_jogo": "banco_nuvem",
                "descricao_jogo": "Consulte e insira dados em um banco de dados hospedado na nuvem.",
                "dados": {"tipo": "banco_nuvem", "tema": "banco_nuvem"}
            },
            {
                "titulo": "Segurança na nuvem",
                "descricao": "Aprenda a proteger dados e recursos na nuvem.",
                "tipo_jogo": "seguranca_nuvem",
                "descricao_jogo": "Configure controles de segurança para proteger recursos na nuvem.",
                "dados": {"tipo": "seguranca_nuvem", "tema": "seguranca_nuvem"}
            },
            {
                "titulo": "Migração de sistemas",
                "descricao": "Aprenda a mover sistemas locais para a nuvem.",
                "tipo_jogo": "migracao",
                "descricao_jogo": "Planeje a migração de um sistema local para a nuvem.",
                "dados": {"tipo": "migracao", "tema": "migracao"}
            },
            {
                "titulo": "Custo e otimização",
                "descricao": "Aprenda a controlar custos e otimizar recursos na nuvem.",
                "tipo_jogo": "custo",
                "descricao_jogo": "Otimize recursos para reduzir custos na nuvem.",
                "dados": {"tipo": "custo", "tema": "custo_nuvem"}
            },
            {
                "titulo": "Provedores (AWS, Azure, Google Cloud)",
                "descricao": "Aprenda sobre os principais provedores de nuvem.",
                "tipo_jogo": "provedor",
                "descricao_jogo": "Identifique quais serviços pertencem a cada provedor de nuvem.",
                "dados": {"tipo": "provedor", "tema": "provedores"}
            },
            {
                "titulo": "Conceitos de servidor e cliente",
                "descricao": "Aprenda a diferença entre servidor e cliente na computação.",
                "tipo_jogo": "servidor_cliente",
                "descricao_jogo": "Identifique quem é servidor e quem é cliente em diferentes cenários.",
                "dados": {"tipo": "servidor_cliente", "tema": "servidor_cliente"}
            },
        ]
    },
    {
        "id": "redes",
        "nome": "Redes e Infraestrutura",
        "descricao": "Cuida de internet, roteadores e servidores. Ideal para quem gosta de hardware e consertar conexão.",
        "icone": "network",
        "cor": "#10b981",
        "conhecimento_necessario": [
            {
                "titulo": "O que é rede de computadores",
                "descricao": "Aprenda o que é rede de computadores e para que serve.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é rede de computadores.",
                "dados": {"tipo": "conceito", "tema": "rede_conceito"}
            },
            {
                "titulo": "Endereço IP e máscara de sub-rede",
                "descricao": "Aprenda como funcionam endereços IP e máscaras de sub-rede.",
                "tipo_jogo": "ip",
                "descricao_jogo": "Identifique endereços IP e máscaras de sub-rede corretos.",
                "dados": {"tipo": "ip", "tema": "ip"}
            },
            {
                "titulo": "Roteadores e switches",
                "descricao": "Aprenda a diferença entre roteadores e switches.",
                "tipo_jogo": "dispositivo",
                "descricao_jogo": "Identifique quando usar um roteador ou um switch em cenários de rede.",
                "dados": {"tipo": "dispositivo", "tema": "rede_dispositivos"}
            },
            {
                "titulo": "Protocolos (TCP/IP, HTTP, DNS)",
                "descricao": "Aprenda os principais protocolos de rede e para que servem.",
                "tipo_jogo": "protocolo",
                "descricao_jogo": "Associe protocolos (TCP/IP, HTTP, DNS) às suas funções.",
                "dados": {"tipo": "protocolo", "tema": "protocolos"}
            },
            {
                "titulo": "Cabo de rede e Wi-Fi",
                "descricao": "Aprenda sobre tipos de cabos de rede e redes sem fio.",
                "tipo_jogo": "cabo_wifi",
                "descricao_jogo": "Identifique tipos de cabos de rede e quando usar Wi-Fi vs cabo.",
                "dados": {"tipo": "cabo_wifi", "tema": "cabo_wifi"}
            },
            {
                "titulo": "Servidores e estações de trabalho",
                "descricao": "Aprenda a diferença entre servidores e estações de trabalho.",
                "tipo_jogo": "servidor_estacao",
                "descricao_jogo": "Classifique dispositivos como servidor ou estação de trabalho.",
                "dados": {"tipo": "servidor_estacao", "tema": "servidor_estacao"}
            },
            {
                "titulo": "Topologias de rede",
                "descricao": "Aprenda os principais tipos de topologia de rede (estrela, barramento, anel).",
                "tipo_jogo": "topologia",
                "descricao_jogo": "Identifique diferentes topologias de rede em diagramas.",
                "dados": {"tipo": "topologia", "tema": "topologia"}
            },
            {
                "titulo": "Segurança de rede básica",
                "descricao": "Aprenda princípios básicos de segurança de rede.",
                "tipo_jogo": "seguranca_rede",
                "descricao_jogo": "Aplique medidas básicas de segurança em uma rede.",
                "dados": {"tipo": "seguranca_rede", "tema": "seguranca_rede"}
            },
            {
                "titulo": "Sistemas operacionais de servidor",
                "descricao": "Aprenda sobre sistemas operacionais usados em servidores.",
                "tipo_jogo": "so_servidor",
                "descricao_jogo": "Identifique sistemas operacionais usados em servidores.",
                "dados": {"tipo": "so_servidor", "tema": "so_servidor"}
            },
            {
                "titulo": "Monitoramento de rede",
                "descricao": "Aprenda a monitorar redes para identificar problemas.",
                "tipo_jogo": "monitoramento",
                "descricao_jogo": "Monitore uma rede e identifique pontos de falha.",
                "dados": {"tipo": "monitoramento", "tema": "monitoramento_rede"}
            },
        ]
    },
    {
        "id": "banco",
        "nome": "Banco de Dados",
        "descricao": "Organiza e guarda informações de forma segura. Ideal para quem gosta de listas, planilhas e manter tudo no lugar.",
        "icone": "database",
        "cor": "#f59e0b",
        "conhecimento_necessario": [
            {
                "titulo": "O que é banco de dados",
                "descricao": "Aprenda o que é banco de dados e para que serve.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é banco de dados.",
                "dados": {"tipo": "conceito", "tema": "banco_conceito"}
            },
            {
                "titulo": "Tabelas, linhas e colunas",
                "descricao": "Aprenda a estrutura básica de tabelas em bancos de dados.",
                "tipo_jogo": "tabela",
                "descricao_jogo": "Identifique tabelas, linhas e colunas em um banco de dados.",
                "dados": {"tipo": "tabela", "tema": "tabelas"}
            },
            {
                "titulo": "Consultas SQL básicas (SELECT, INSERT, UPDATE, DELETE)",
                "descricao": "Aprenda os comandos básicos de SQL para manipular dados.",
                "tipo_jogo": "sql",
                "descricao_jogo": "Escreva consultas SQL simples para manipular dados.",
                "dados": {"tipo": "sql", "tema": "sql_basico"}
            },
            {
                "titulo": "Chave primária e chave estrangeira",
                "descricao": "Aprenda o que são chaves primárias e estrangeiras em bancos de dados.",
                "tipo_jogo": "chave",
                "descricao_jogo": "Identifique chaves primárias e estrangeiras em tabelas relacionadas.",
                "dados": {"tipo": "chave", "tema": "chaves"}
            },
            {
                "titulo": "Relacionamentos entre tabelas",
                "descricao": "Aprenda como tabelas se relacionam (1-para-1, 1-para-muitos, muitos-para-muitos).",
                "tipo_jogo": "relacionamento",
                "descricao_jogo": "Identifique o tipo de relacionamento entre tabelas.",
                "dados": {"tipo": "relacionamento", "tema": "relacionamentos"}
            },
            {
                "titulo": "Normalização de dados",
                "descricao": "Aprenda a organizar dados em tabelas para evitar redundância.",
                "tipo_jogo": "normalizacao",
                "descricao_jogo": "Normalize uma tabela simples seguindo regras de normalização.",
                "dados": {"tipo": "normalizacao", "tema": "normalizacao"}
            },
            {
                "titulo": "Backup e recuperação",
                "descricao": "Aprenda a fazer backup e restaurar dados em bancos de dados.",
                "tipo_jogo": "backup",
                "descricao_jogo": "Faça backup e restaure dados em um banco de dados.",
                "dados": {"tipo": "backup", "tema": "backup"}
            },
            {
                "titulo": "Segurança de dados",
                "descricao": "Aprenda a proteger dados em bancos de dados.",
                "tipo_jogo": "seguranca_dados",
                "descricao_jogo": "Aplique medidas de segurança para proteger dados em bancos.",
                "dados": {"tipo": "seguranca_dados", "tema": "seguranca_dados"}
            },
            {
                "titulo": "Modelagem entidade-relacionamento",
                "descricao": "Aprenda a criar diagramas entidade-relacionamento (ER).",
                "tipo_jogo": "modelagem",
                "descricao_jogo": "Crie um diagrama ER simples para um cenário dado.",
                "dados": {"tipo": "modelagem", "tema": "modelagem_er"}
            },
            {
                "titulo": "Bancos relacionais e não relacionais",
                "descricao": "Aprenda a diferença entre bancos relacionais (SQL) e não relacionais (NoSQL).",
                "tipo_jogo": "tipo_banco",
                "descricao_jogo": "Classifique bancos de dados como relacionais ou não relacionais.",
                "dados": {"tipo": "tipo_banco", "tema": "tipo_banco"}
            },
        ]
    },
    {
        "id": "devops",
        "nome": "DevOps",
        "descricao": "Une programação e operações para deixar tudo funcionando rápido. Ideal para quem gosta de eficiência e ferramentas.",
        "icone": "gear",
        "cor": "#6366f1",
        "conhecimento_necessario": [
            {
                "titulo": "O que é DevOps",
                "descricao": "Aprenda o que é DevOps e por que é importante.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é DevOps.",
                "dados": {"tipo": "conceito", "tema": "devops_conceito"}
            },
            {
                "titulo": "Integração Contínua (CI)",
                "descricao": "Aprenda o que é integração contínua e por que é importante.",
                "tipo_jogo": "ci",
                "descricao_jogo": "Entenda o fluxo de integração contínua em um projeto.",
                "dados": {"tipo": "ci", "tema": "ci"}
            },
            {
                "titulo": "Entrega Contínua (CD)",
                "descricao": "Aprenda o que é entrega contínua e como ela ajuda na entrega de software.",
                "tipo_jogo": "cd",
                "descricao_jogo": "Entenda o fluxo de entrega contínua em um projeto.",
                "dados": {"tipo": "cd", "tema": "cd"}
            },
            {
                "titulo": "Contêineres (Docker)",
                "descricao": "Aprenda o que são contêineres Docker e como funcionam.",
                "tipo_jogo": "docker",
                "descricao_jogo": "Entenda como contêineres empacotam aplicações e dependências.",
                "dados": {"tipo": "docker", "tema": "docker"}
            },
            {
                "titulo": "Orquestração (Kubernetes)",
                "descricao": "Aprenda o que é orquestração de contêineres com Kubernetes.",
                "tipo_jogo": "kubernetes",
                "descricao_jogo": "Entenda como Kubernetes gerencia contêineres.",
                "dados": {"tipo": "kubernetes", "tema": "kubernetes"}
            },
            {
                "titulo": "Versionamento com Git",
                "descricao": "Aprenda a usar Git para versionar código.",
                "tipo_jogo": "git",
                "descricao_jogo": "Use comandos Git básicos para versionar código.",
                "dados": {"tipo": "git", "tema": "git"}
            },
            {
                "titulo": "Automação de testes",
                "descricao": "Aprenda a automatizar testes de software.",
                "tipo_jogo": "teste_automatizado",
                "descricao_jogo": "Crie testes automatizados simples para validar código.",
                "dados": {"tipo": "teste_automatizado", "tema": "testes"}
            },
            {
                "titulo": "Monitoramento de aplicações",
                "descricao": "Aprenda a monitorar aplicações em produção.",
                "tipo_jogo": "monitoramento",
                "descricao_jogo": "Monitore métricas de uma aplicação e identifique problemas.",
                "dados": {"tipo": "monitoramento", "tema": "monitoramento_app"}
            },
            {
                "titulo": "Infraestrutura como código",
                "descricao": "Aprenda a definir infraestrutura como código.",
                "tipo_jogo": "iac",
                "descricao_jogo": "Escreva definições de infraestrutura como código.",
                "dados": {"tipo": "iac", "tema": "iac"}
            },
            {
                "titulo": "Colaboração entre desenvolvimento e operações",
                "descricao": "Aprenda como desenvolvedores e operações colaboram no DevOps.",
                "tipo_jogo": "colaboracao",
                "descricao_jogo": "Entenda como dev e ops trabalham juntos no DevOps.",
                "dados": {"tipo": "colaboracao", "tema": "colaboracao_devops"}
            },
        ]
    },
    {
        "id": "produto",
        "nome": "Product Owner / Scrum Master",
        "descricao": "Planeja o produto, decide o que fazer primeiro e ajuda o time. Ideal para quem gosta de liderar e organizar.",
        "icone": "users",
        "cor": "#ec4899",
        "conhecimento_necessario": [
            {
                "titulo": "O que é produto digital",
                "descricao": "Aprenda o que é produto digital e como ele difere de projetos tradicionais.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é produto digital.",
                "dados": {"tipo": "conceito", "tema": "produto_conceito"}
            },
            {
                "titulo": "Metodologias ágeis (Scrum, Kanban)",
                "descricao": "Aprenda sobre metodologias ágeis como Scrum e Kanban.",
                "tipo_jogo": "agile",
                "descricao_jogo": "Entenda como funcionam Scrum e Kanban.",
                "dados": {"tipo": "agile", "tema": "agile"}
            },
            {
                "titulo": "Histórias de usuário",
                "descricao": "Aprenda a escrever histórias de usuário para capturar requisitos.",
                "tipo_jogo": "historia",
                "descricao_jogo": "Escreva histórias de usuário seguindo o padrão: Como [persona], eu quero [objetivo] para [benefício].",
                "dados": {"tipo": "historia", "tema": "historias_usuario"}
            },
            {
                "titulo": "Backlog do produto",
                "descricao": "Aprenda a criar e gerenciar um backlog de produto.",
                "tipo_jogo": "backlog",
                "descricao_jogo": "Crie e organize um backlog de produto com itens de trabalho.",
                "dados": {"tipo": "backlog", "tema": "backlog"}
            },
            {
                "titulo": "Planejamento de sprint",
                "descricao": "Aprenda a planejar sprints em projetos ágeis.",
                "tipo_jogo": "sprint",
                "descricao_jogo": "Planeje uma sprint selecionando itens do backlog.",
                "dados": {"tipo": "sprint", "tema": "planejamento_sprint"}
            },
            {
                "titulo": "Análise de requisitos",
                "descricao": "Aprenda a coletar e analisar requisitos de stakeholders.",
                "tipo_jogo": "requisitos",
                "descricao_jogo": "Colete e analise requisitos de stakeholders para um produto.",
                "dados": {"tipo": "requisitos", "tema": "requisitos"}
            },
            {
                "titulo": "Comunicação com stakeholders",
                "descricao": "Aprenda a se comunicar efetivamente com stakeholders.",
                "tipo_jogo": "comunicacao",
                "descricao_jogo": "Escolha a melhor forma de comunicar com diferentes stakeholders.",
                "dados": {"tipo": "comunicacao", "tema": "comunicacao"}
            },
            {
                "titulo": "Priorização de funcionalidades",
                "descricao": "Aprenda a priorizar funcionalidades usando critérios como valor e esforço.",
                "tipo_jogo": "priorizacao",
                "descricao_jogo": "Priorize funcionalidades de um produto com base em valor e esforço.",
                "dados": {"tipo": "priorizacao", "tema": "priorizacao"}
            },
            {
                "titulo": "Métricas de produto",
                "descricao": "Aprenda a medir o sucesso de um produto com métricas.",
                "tipo_jogo": "metricas",
                "descricao_jogo": "Escolha e interprete métricas de produto relevantes.",
                "dados": {"tipo": "metricas", "tema": "metricas"}
            },
            {
                "titulo": "Facilitação de reuniões",
                "descricao": "Aprenda a facilitar reuniões produtivas em times ágeis.",
                "tipo_jogo": "reuniao",
                "descricao_jogo": "Planeje e conduza reuniões produtivas de time ágil.",
                "dados": {"tipo": "reuniao", "tema": "reunioes"}
            },
        ]
    },
    {
        "id": "qa",
        "nome": "QA / Testes de Software",
        "descricao": "Testa programas para encontrar erros e garantir que funcionem direito. Ideal para quem é detalhista e gosta de achar falhas.",
        "icone": "check",
        "cor": "#84cc16",
        "conhecimento_necessario": [
            {
                "titulo": "O que é teste de software",
                "descricao": "Aprenda o que é teste de software e por que é importante.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é teste de software.",
                "dados": {"tipo": "conceito", "tema": "teste_conceito"}
            },
            {
                "titulo": "Tipos de teste (funcional, não funcional)",
                "descricao": "Aprenda a diferença entre testes funcionais e não funcionais.",
                "tipo_jogo": "tipo_teste",
                "descricao_jogo": "Classifique testes como funcionais ou não funcionais.",
                "dados": {"tipo": "tipo_teste", "tema": "tipos_teste"}
            },
            {
                "titulo": "Casos de teste",
                "descricao": "Aprenda a escrever casos de teste eficazes.",
                "tipo_jogo": "caso_teste",
                "descricao_jogo": "Escreva casos de teste para diferentes cenários.",
                "dados": {"tipo": "caso_teste", "tema": "casos_teste"}
            },
            {
                "titulo": "Relato de bugs",
                "descricao": "Aprenda a reportar bugs de forma clara e eficaz.",
                "tipo_jogo": "bug",
                "descricao_jogo": "Escreva relatórios de bugs claros e úteis.",
                "dados": {"tipo": "bug", "tema": "bugs"}
            },
            {
                "titulo": "Teste de usabilidade",
                "descricao": "Aprenda a testar a usabilidade de interfaces.",
                "tipo_jogo": "usabilidade",
                "descricao_jogo": "Avalie a usabilidade de interfaces e sugira melhorias.",
                "dados": {"tipo": "usabilidade", "tema": "usabilidade"}
            },
            {
                "titulo": "Teste de regressão",
                "descricao": "Aprenda o que é teste de regressão e por que é importante.",
                "tipo_jogo": "regressao",
                "descricao_jogo": "Entenda por que é importante testar novamente após mudanças.",
                "dados": {"tipo": "regressao", "tema": "regressao"}
            },
            {
                "titulo": "Ferramentas de teste",
                "descricao": "Aprenda sobre ferramentas comuns de teste de software.",
                "tipo_jogo": "ferramenta",
                "descricao_jogo": "Identifique ferramentas comuns de teste de software.",
                "dados": {"tipo": "ferramenta", "tema": "ferramentas_teste"}
            },
            {
                "titulo": "Garantia de qualidade",
                "descricao": "Aprenda a diferença entre teste de software e garantia de qualidade.",
                "tipo_jogo": "qc",
                "descricao_jogo": "Entenda a diferença entre QA e teste de software.",
                "dados": {"tipo": "qc", "tema": "qc"}
            },
            {
                "titulo": "Ciclo de vida de software",
                "descricao": "Aprenda sobre o ciclo de vida de desenvolvimento de software (SDLC).",
                "tipo_jogo": "ciclo_vida",
                "descricao_jogo": "Identifique as fases do ciclo de vida de desenvolvimento de software.",
                "dados": {"tipo": "ciclo_vida", "tema": "sdlc"}
            },
            {
                "titulo": "Documentação de testes",
                "descricao": "Aprenda a documentar testes e planos de teste.",
                "tipo_jogo": "documentacao",
                "descricao_jogo": "Escreva planos de teste e documentação relacionada.",
                "dados": {"tipo": "documentacao", "tema": "documentacao_testes"}
            },
        ]
    },
    {
        "id": "design",
        "nome": "Design UX/UI",
        "descricao": "Cria a aparência e a experiência de apps e sites. Ideal para quem gosta de desenhar, cores e deixar bonito e fácil de usar.",
        "icone": "pencil",
        "cor": "#f43f5e",
        "conhecimento_necessario": [
            {
                "titulo": "O que é experiência do usuário (UX)",
                "descricao": "Aprenda o que é experiência do usuário e por que é importante.",
                "tipo_jogo": "conceito",
                "descricao_jogo": "Responda perguntas sobre o que é UX e por que é importante.",
                "dados": {"tipo": "conceito", "tema": "ux_conceito"}
            },
            {
                "titulo": "Interface do usuário (UI)",
                "descricao": "Aprenda o que é interface do usuário e seus elementos.",
                "tipo_jogo": "ui",
                "descricao_jogo": "Identifique elementos de interface em exemplos de interfaces.",
                "dados": {"tipo": "ui", "tema": "ui"}
            },
            {
                "titulo": "Teoria das cores",
                "descricao": "Aprenda sobre cores e como usá-las em design.",
                "tipo_jogo": "cores",
                "descricao_jogo": "Crie combinações de cores harmônicas para interfaces.",
                "dados": {"tipo": "cores", "tema": "teoria_cores"}
            },
            {
                "titulo": "Tipografia",
                "descricao": "Aprenda sobre fontes e como usá-las em design.",
                "tipo_jogo": "tipografia",
                "descricao_jogo": "Escolha fontes apropriadas para diferentes contextos de design.",
                "dados": {"tipo": "tipografia", "tema": "tipografia"}
            },
            {
                "titulo": "Wireframes e protótipos",
                "descricao": "Aprenda a criar wireframes e protótipos de interfaces.",
                "tipo_jogo": "wireframe",
                "descricao_jogo": "Crie wireframes simples para páginas ou telas.",
                "dados": {"tipo": "wireframe", "tema": "wireframe"}
            },
            {
                "titulo": "Design responsivo",
                "descricao": "Aprenda a criar interfaces que funcionam em diferentes dispositivos.",
                "tipo_jogo": "responsivo",
                "descricao_jogo": "Adapte interfaces para diferentes tamanhos de tela.",
                "dados": {"tipo": "responsivo", "tema": "responsivo"}
            },
            {
                "titulo": "Acessibilidade",
                "descricao": "Aprenda a tornar interfaces acessíveis para todos os usuários.",
                "tipo_jogo": "acessibilidade",
                "descricao_jogo": "Identifique barreiras de acessibilidade e sugira melhorias.",
                "dados": {"tipo": "acessibilidade", "tema": "acessibilidade"}
            },
            {
                "titulo": "Ferramentas de design (Figma, etc.)",
                "descricao": "Aprenda sobre ferramentas populares de design.",
                "tipo_jogo": "ferramenta",
                "descricao_jogo": "Identifique ferramentas comuns de design e seus usos.",
                "dados": {"tipo": "ferramenta", "tema": "ferramentas_design"}
            },
            {
                "titulo": "Pesquisa com usuários",
                "descricao": "Aprenda a realizar pesquisas com usuários para informar o design.",
                "tipo_jogo": "pesquisa",
                "descricao_jogo": "Planeje e execute pesquisas simples com usuários.",
                "dados": {"tipo": "pesquisa", "tema": "pesquisa_usuarios"}
            },
            {
                "titulo": "Testes de usabilidade",
                "descricao": "Aprenda a realizar testes de usabilidade com usuários reais.",
                "tipo_jogo": "teste_usabilidade",
                "descricao_jogo": "Planeje e conduza testes de usabilidade simples.",
                "dados": {"tipo": "teste_usabilidade", "tema": "testes_usabilidade"}
            },
        ]
    },
]

QUESTOES_TODAS = [
    {
        "id": 1,
        "pergunta": "Quando você precisa resolver um problema difícil, o que faz?",
        "opcoes": [
            ("Divido em partes pequenas e testo soluções", "desenvolvimento"),
            ("Procuro padrões e analiso antes de decidir", "dados"),
            ("Procuro falhas e erros", "seguranca"),
            ("Crio algo novo e criativo", "design"),
        ],
    },
    {
        "id": 2,
        "pergunta": "Qual atividade parece mais legal?",
        "opcoes": [
            ("Criar um jogo ou app", "desenvolvimento"),
            ("Analisar números e tirar conclusões", "dados"),
            ("Proteger um sistema contra ataques", "seguranca"),
            ("Deixar arquivos na internet (nuvem)", "cloud"),
        ],
    },
    {
        "id": 3,
        "pergunta": "Você se identifica com alguém que:",
        "opcoes": [
            ("Constrói coisas que funcionam", "desenvolvimento"),
            ("É detalhista e atento a riscos", "seguranca"),
            ("Organiza coisas e processos", "redes"),
            ("Gosta de números e análises", "dados"),
        ],
    },
    {
        "id": 4,
        "pergunta": "Em um trabalho em grupo, você prefere:",
        "opcoes": [
            ("Desenvolver as funções do projeto", "desenvolvimento"),
            ("Garantir a segurança de todos", "seguranca"),
            ("Organizar o ambiente e a internet", "redes"),
            ("Analisar dados para ajudar o time", "dados"),
        ],
    },
    {
        "id": 5,
        "pergunta": "Qual matéria você mais gosta na escola?",
        "opcoes": [
            ("Programação e lógica", "desenvolvimento"),
            ("Segurança digital e internet", "seguranca"),
            ("Informática e redes", "redes"),
            ("Matemática e estatística", "dados"),
        ],
    },
    {
        "id": 6,
        "pergunta": "Se um jogo ou programa parar de funcionar, você:",
        "opcoes": [
            ("Olha o programa para achar o erro", "desenvolvimento"),
            ("Investiga se foi algum ataque", "seguranca"),
            ("Vê se a internet está ok", "redes"),
            ("Olha relatórios e gráficos", "dados"),
        ],
    },
    {
        "id": 7,
        "pergunta": "Você prefere trabalhar com:",
        "opcoes": [
            ("Criar telas e funções de um app", "desenvolvimento"),
            ("Ficar de olho em ameaças", "seguranca"),
            ("Configurar a nuvem", "cloud"),
            ("Criar gráficos e análises", "dados"),
        ],
    },
    {
        "id": 8,
        "pergunta": "Qual frase combina mais com você?",
        "opcoes": [
            ("Quero criar soluções", "desenvolvimento"),
            ("Quero proteger informações", "seguranca"),
            ("Quero montar sistemas digitais", "redes"),
            ("Quero usar dados para decidir", "dados"),
        ],
    },
    {
        "id": 9,
        "pergunta": "Como você se descreve?",
        "opcoes": [
            ("Criativo e lógico", "desenvolvimento"),
            ("Estratégico e observador", "seguranca"),
            ("Organizado e técnico", "redes"),
            ("Analítico e curioso", "dados"),
        ],
    },
    {
        "id": 10,
        "pergunta": "O que mais te motiva?",
        "opcoes": [
            ("Criar algo novo", "desenvolvimento"),
            ("Defender sistemas e pessoas", "seguranca"),
            ("Organizar sistemas grandes", "redes"),
            ("Descobrir coisas nos dados", "dados"),
        ],
    },
    {
        "id": 11,
        "pergunta": "Quando pensa em guardar informações, você:",
        "opcoes": [
            ("Gosta de organizar em listas e tabelas", "banco"),
            ("Prefere não mexer com dados", "desenvolvimento"),
            ("Quer manter tudo seguro", "seguranca"),
            ("Quer fazer relatórios com dados", "dados"),
        ],
    },
    {
        "id": 12,
        "pergunta": "Sobre guardar arquivos na internet (nuvem), você:",
        "opcoes": [
            ("Gosta de tudo automático", "cloud"),
            ("Prefere guardar no computador", "redes"),
            ("Quer ligar nuvem com programas", "devops"),
            ("Não tem interesse específico", "design"),
        ],
    },
    {
        "id": 13,
        "pergunta": "Você gosta de criar atalhos para não repetir tarefas?",
        "opcoes": [
            ("Sim, criar automações", "devops"),
            ("Não, prefere fazer na mão", "qa"),
            ("Sim, com dados", "dados"),
            ("Sim, com internet e servidores", "redes"),
        ],
    },
    {
        "id": 14,
        "pergunta": "Qual sua melhor qualidade?",
        "opcoes": [
            ("Criatividade", "design"),
            ("Lógica", "desenvolvimento"),
            ("Detalhismo", "qa"),
            ("Saber conversar com as pessoas", "produto"),
        ],
    },
    {
        "id": 15,
        "pergunta": "Num projeto, você gosta de:",
        "opcoes": [
            ("Decidir o que será feito", "produto"),
            ("Escrever o programa", "desenvolvimento"),
            ("Testar se tudo funciona", "qa"),
            ("Colocar no ar para todos usarem", "devops"),
        ],
    },
    {
        "id": 16,
        "pergunta": "Você se sente mais à vontade com:",
        "opcoes": [
            ("Tela, cores e como a pessoa usa", "design"),
            ("Código e lógica", "desenvolvimento"),
            ("Planilhas e relatórios de dados", "dados"),
            ("Cabos, roteadores e equipamentos", "redes"),
        ],
    },
    {
        "id": 17,
        "pergunta": "Sobre proteger informações na internet, você:",
        "opcoes": [
            ("Gosta de investigar ataques", "seguranca"),
            ("Prefere não se preocupar com isso", "desenvolvimento"),
            ("Quer proteger dados das pessoas", "seguranca"),
            ("Acha importante, mas não é prioridade", "qa"),
        ],
    },
    {
        "id": 18,
        "pergunta": "Se fosse criar um jogo, você seria:",
        "opcoes": [
            ("Quem programa para tudo funcionar", "desenvolvimento"),
            ("Quem cuida da segurança dos dados", "seguranca"),
            ("Quem analisa dados dos jogadores", "dados"),
            ("Quem cria a aparência e a experiência", "design"),
        ],
    },
    {
        "id": 19,
        "pergunta": "Você prefere trabalhar com:",
        "opcoes": [
            ("Pessoas e o que o negócio precisa", "produto"),
            ("Código e tecnologia", "desenvolvimento"),
            ("Dados e métricas", "dados"),
            ("Segurança e proteção", "seguranca"),
        ],
    },
    {
        "id": 20,
        "pergunta": "Quando um programa tem erros, você:",
        "opcoes": [
            ("Quer achar e consertar cada um", "qa"),
            ("Quer entender por que aconteceu", "desenvolvimento"),
            ("Quer garantir que não haja perigo", "seguranca"),
            ("Quer anotar tudo para o time", "produto"),
        ],
    },
    {
        "id": 21,
        "pergunta": "Sobre organizar o trabalho em equipe, você:",
        "opcoes": [
            ("Gosta de organizar quem faz o quê", "produto"),
            ("Prefere focar na entrega técnica", "desenvolvimento"),
            ("Não tem certeza ainda", "devops"),
            ("Quer garantir qualidade nas entregas", "qa"),
        ],
    },
    {
        "id": 22,
        "pergunta": "Você gosta de criar telas bonitas?",
        "opcoes": [
            ("Sim, com foco em ser fácil de usar", "design"),
            ("Não, prefiro o lado de trás do programa", "desenvolvimento"),
            ("Sim, junto com dados", "dados"),
            ("Não é prioridade para mim", "redes"),
        ],
    },
    {
        "id": 23,
        "pergunta": "Se tivesse que escolher hoje:",
        "opcoes": [
            ("Criar produtos digitais bonitos", "design"),
            ("Proteger sistemas e dados", "seguranca"),
            ("Gerenciar muitas informações", "banco"),
            ("Construir aplicações", "desenvolvimento"),
        ],
    },
    {
        "id": 24,
        "pergunta": "Sobre internet e servidores, você:",
        "opcoes": [
            ("Gosta de manter servidores e redes", "redes"),
            ("Prefere software e código", "desenvolvimento"),
            ("Quer ligar programação com servidores", "devops"),
            ("Não se interessa por infraestrutura", "design"),
        ],
    },
    {
        "id": 25,
        "pergunta": "No tempo livre, você gosta de:",
        "opcoes": [
            ("Programar um projeto próprio", "desenvolvimento"),
            ("Analisar dados de algo que gosta", "dados"),
            ("Estudar sobre ataques de hackers", "seguranca"),
            ("Desenhar ou criar arte digital", "design"),
        ],
    },
    # --- Novas 50 perguntas ---
    {
        "id": 26,
        "pergunta": "Qual brinquedo ou app você mais gosta de criar?",
        "opcoes": [
            ("Um jogo de celular", "desenvolvimento"),
            ("Um app para organizar tarefas", "produto"),
            ("Um site divertido", "design"),
            ("Um jogo seguro sem trapaça", "seguranca"),
        ],
    },
    {
        "id": 27,
        "pergunta": "No celular, você costuma:",
        "opcoes": [
            ("Baixar muitos apps e testar todos", "desenvolvimento"),
            ("Ver quais apps são seguros antes de instalar", "seguranca"),
            ("Organizar pastas e arquivos", "redes"),
            ("Editar fotos e vídeos", "design"),
        ],
    },
    {
        "id": 28,
        "pergunta": "Quando a internet cai em casa, você:",
        "opcoes": [
            ("Tenta reiniciar o roteador", "redes"),
            ("Procura um jeito de usar offline", "desenvolvimento"),
            ("Se preocupa se alguém hackeou o Wi-Fi", "seguranca"),
            ("Acessa arquivos salvos na nuvem", "cloud"),
        ],
    },
    {
        "id": 29,
        "pergunta": "Você gosta de criar senhas?",
        "opcoes": [
            ("Sim, senhas complexas e seguras", "seguranca"),
            ("Não, prefiro usar o mesmo para tudo", "desenvolvimento"),
            ("Sim, para organizar minhas contas", "banco"),
            ("Não, não gosto disso", "qa"),
        ],
    },
    {
        "id": 30,
        "pergunta": "Se um amigo esquecer a senha, você:",
        "opcoes": [
            ("Ajuda a recuperar de forma segura", "seguranca"),
            ("Tenta adivinhar a senha", "qa"),
            ("Ensina a criar uma melhor", "produto"),
            ("Não se envolve", "desenvolvimento"),
        ],
    },
    {
        "id": 31,
        "pergunta": "Qual tipo de vídeo você mais assiste?",
        "opcoes": [
            ("Tutoriais de programação", "desenvolvimento"),
            ("Documentários sobre tecnologia", "dados"),
            ("Notícias sobre cibersegurança", "seguranca"),
            ("Canais de design e arte", "design"),
        ],
    },
    {
        "id": 32,
        "pergunta": "Em um jogo online, você:",
        "opcoes": [
            ("Cria mods ou personalizações", "desenvolvimento"),
            ("Denuncia jogadores suspeitos", "seguranca"),
            ("Organiza o time", "produto"),
            ("Analisa estatísticas de partida", "dados"),
        ],
    },
    {
        "id": 33,
        "pergunta": "Você gosta de montar o computador?",
        "opcoes": [
            ("Sim, monto peças e cabos", "redes"),
            ("Não, prefiro só usar o software", "desenvolvimento"),
            ("Sim, para rodar servidores caseiros", "cloud"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 34,
        "pergunta": "Qual rede social você usa mais?",
        "opcoes": [
            ("YouTube para aprender tecnologia", "desenvolvimento"),
            ("LinkedIn para ver vagas de TI", "produto"),
            ("Instagram para ver arte e design", "design"),
            ("Twitter/X para notícias de segurança", "seguranca"),
        ],
    },
    {
        "id": 35,
        "pergunta": "Se um site estiver lento, você:",
        "opcoes": [
            ("Verifica a conexão de internet", "redes"),
            ("Acha que o código está pesado", "desenvolvimento"),
            ("Se preocupa se está sendo atacado", "seguranca"),
            ("Acha que o banco de dados está lento", "banco"),
        ],
    },
    {
        "id": 36,
        "pergunta": "Você gosta de planilhas?",
        "opcoes": [
            ("Sim, adoro organizar dados", "dados"),
            ("Não, acho chato", "desenvolvimento"),
            ("Sim, para controlar senhas", "seguranca"),
            ("Não, prefiro visual", "design"),
        ],
    },
    {
        "id": 37,
        "pergunta": "Quando baixa um arquivo, você:",
        "opcoes": [
            ("Verifica se é seguro antes de abrir", "seguranca"),
            ("Abre logo para testar", "qa"),
            ("Organiza na pasta certa", "redes"),
            ("Não baixa nada da internet", "desenvolvimento"),
        ],
    },
    {
        "id": 38,
        "pergunta": "Qual tipo de loja você gosta?",
        "opcoes": [
            ("Loja de aplicativos", "desenvolvimento"),
            ("Loja de jogos", "qa"),
            ("Loja de arte digital", "design"),
            ("Loja de componentes de computador", "redes"),
        ],
    },
    {
        "id": 39,
        "pergunta": "Se pudesse criar um robô, ele faria:",
        "opcoes": [
            ("Tarefas de casa automaticamente", "devops"),
            ("Análise de dados científicos", "dados"),
            ("Vigiar a casa", "seguranca"),
            ("Desenhar e pintar", "design"),
        ],
    },
    {
        "id": 40,
        "pergunta": "Você gosta de ensinar os outros?",
        "opcoes": [
            ("Sim, explico como usar programas", "produto"),
            ("Não, prefiro fazer sozinho", "desenvolvimento"),
            ("Sim, ensino segurança na internet", "seguranca"),
            ("Não, prefiro criar sozinho", "design"),
        ],
    },
    {
        "id": 41,
        "pergunta": "Qual dispositivo você usa mais?",
        "opcoes": [
            ("Computador para programar", "desenvolvimento"),
            ("Tablet para desenhar", "design"),
            ("Servidor para testar", "redes"),
            ("Celular para tudo", "produto"),
        ],
    },
    {
        "id": 42,
        "pergunta": "Se um programa trava, você:",
        "opcoes": [
            ("Fecha e abre de novo", "qa"),
            ("Olha o código de erro", "desenvolvimento"),
            ("Verifica se é vírus", "seguranca"),
            ("Reinicia o computador", "redes"),
        ],
    },
    {
        "id": 43,
        "pergunta": "Você gosta de atualizar programas?",
        "opcoes": [
            ("Sim, sempre deixo tudo atualizado", "seguranca"),
            ("Não, nunca atualizo", "desenvolvimento"),
            ("Sim, para melhorar o desempenho", "devops"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 44,
        "pergunta": "Qual filme você mais gosta?",
        "opcoes": [
            ("Sobre hackers e tecnologia", "seguranca"),
            ("Sobre criação de apps", "desenvolvimento"),
            ("Sobre animação e arte", "design"),
            ("Sobre ciência de dados", "dados"),
        ],
    },
    {
        "id": 45,
        "pergunta": "Você gosta de testar coisas novas?",
        "opcoes": [
            ("Sim, sou o primeiro a experimentar", "qa"),
            ("Não, prefiro o que já conheço", "desenvolvimento"),
            ("Sim, se for seguro", "seguranca"),
            ("Sim, se for bonito", "design"),
        ],
    },
    {
        "id": 46,
        "pergunta": "Se criasse um site, ele seria sobre:",
        "opcoes": [
            ("Meus jogos e programas", "desenvolvimento"),
            ("Minha coleção de fotos", "design"),
            ("Meus dados e estatísticas", "dados"),
            ("Minhas senhas seguras", "seguranca"),
        ],
    },
    {
        "id": 47,
        "pergunta": "Você gosta de trabalhar sozinho ou em grupo?",
        "opcoes": [
            ("Sozinho, focado no código", "desenvolvimento"),
            ("Em grupo, planejando juntos", "produto"),
            ("Sozinho, analisando dados", "dados"),
            ("Em grupo, protegendo o sistema", "seguranca"),
        ],
    },
    {
        "id": 48,
        "pergunta": "Qual prêmio você gostaria de ganhar?",
        "opcoes": [
            ("Um notebook para programar", "desenvolvimento"),
            ("Um curso de segurança digital", "seguranca"),
            ("Um tablet para desenhar", "design"),
            ("Um servidor para testes", "redes"),
        ],
    },
    {
        "id": 49,
        "pergunta": "Você gosta de ler sobre tecnologia?",
        "opcoes": [
            ("Sim, blogs de programação", "desenvolvimento"),
            ("Sim, notícias de segurança", "seguranca"),
            ("Sim, revistas de design", "design"),
            ("Sim, sites de dados", "dados"),
        ],
    },
    {
        "id": 50,
        "pergunta": "Se pudesse criar um app para a escola, ele faria:",
        "opcoes": [
            ("Organizar tarefas e notas", "produto"),
            ("Ensinar programação", "desenvolvimento"),
            ("Proteger dados dos alunos", "seguranca"),
            ("Mostrar rankings e estatísticas", "dados"),
        ],
    },
    {
        "id": 51,
        "pergunta": "Qual tipo de música você ouve enquanto usa o computador?",
        "opcoes": [
            ("Música eletrônica para focar", "desenvolvimento"),
            ("Música calma para criar", "design"),
            ("Qualquer coisa, desde que seja seguro", "seguranca"),
            ("Não ouço nada", "qa"),
        ],
    },
    {
        "id": 52,
        "pergunta": "Você gosta de desmontar aparelhos?",
        "opcoes": [
            ("Sim, para ver como funcionam", "redes"),
            ("Não, prefiro software", "desenvolvimento"),
            ("Sim, para reaproveitar peças", "cloud"),
            ("Não, não gosto", "design"),
        ],
    },
    {
        "id": 53,
        "pergunta": "Se um amigo enviar um link estranho, você:",
        "opcoes": [
            ("Não clica e avisa o amigo", "seguranca"),
            ("Clica para ver o que é", "qa"),
            ("Denuncia o link", "produto"),
            ("Não abre links de ninguém", "desenvolvimento"),
        ],
    },
    {
        "id": 54,
        "pergunta": "Você gosta de criar senhas diferentes para cada site?",
        "opcoes": [
            ("Sim, uso gerenciador de senhas", "seguranca"),
            ("Não, uso a mesma para tudo", "desenvolvimento"),
            ("Sim, anoto em um caderno", "banco"),
            ("Não me preocupo com isso", "qa"),
        ],
    },
    {
        "id": 55,
        "pergunta": "Qual tipo de notificação você mais recebe?",
        "opcoes": [
            ("De apps e jogos", "desenvolvimento"),
            ("De alertas de segurança", "seguranca"),
            ("De atualizações de design", "design"),
            ("De relatórios automáticos", "dados"),
        ],
    },
    {
        "id": 56,
        "pergunta": "Você gosta de criar backups?",
        "opcoes": [
            ("Sim, salvo tudo na nuvem", "cloud"),
            ("Não, nunca faço", "desenvolvimento"),
            ("Sim, em disco externo", "redes"),
            ("Não sei o que é isso", "qa"),
        ],
    },
    {
        "id": 57,
        "pergunta": "Se pudesse automatizar uma coisa na escola, seria:",
        "opcoes": [
            ("O chamada dos alunos", "devops"),
            ("O boletim de notas", "banco"),
            ("O controle de entrada", "seguranca"),
            ("O cardápio da cantina", "design"),
        ],
    },
    {
        "id": 58,
        "pergunta": "Você gosta de criar vídeos?",
        "opcoes": [
            ("Sim, edito e publico", "design"),
            ("Não, não gosto", "desenvolvimento"),
            ("Sim, tutoriais de tecnologia", "produto"),
            ("Não, prefiro assistir", "qa"),
        ],
    },
    {
        "id": 59,
        "pergunta": "Qual loja de aplicativos você mais usa?",
        "opcoes": [
            ("Google Play ou App Store", "desenvolvimento"),
            ("Steam para jogos", "qa"),
            ("Outras lojas de arte digital", "design"),
            ("Não uso", "seguranca"),
        ],
    },
    {
        "id": 60,
        "pergunta": "Se pudesse criar uma ferramenta para ajudar pessoas, seria:",
        "opcoes": [
            ("Um app de acessibilidade", "desenvolvimento"),
            ("Um sistema de proteção de dados", "seguranca"),
            ("Uma plataforma de aprendizado", "produto"),
            ("Um site de arte digital", "design"),
        ],
    },
    {
        "id": 61,
        "pergunta": "Você gosta de criar lógica de programação?",
        "opcoes": [
            ("Sim, adoro desafios de código", "desenvolvimento"),
            ("Não, prefiro visual", "design"),
            ("Sim, para automatizar tarefas", "devops"),
            ("Não me interessa", "qa"),
        ],
    },
    {
        "id": 62,
        "pergunta": "Você gosta de participar de hackathons?",
        "opcoes": [
            ("Sim, adoro criar em pouco tempo", "desenvolvimento"),
            ("Não, prefiro trabalhar sozinho", "qa"),
            ("Sim, para criar soluções seguras", "seguranca"),
            ("Não, não sei o que é", "design"),
        ],
    },
    {
        "id": 63,
        "pergunta": "Você gosta de criar documentação?",
        "opcoes": [
            ("Sim, para explicar como usar", "produto"),
            ("Não, prefiro apenas fazer", "desenvolvimento"),
            ("Sim, para registrar segurança", "seguranca"),
            ("Não, prefiro criar", "design"),
        ],
    },
    {
        "id": 64,
        "pergunta": "Se pudesse criar um jogo educativo, ele ensinaria:",
        "opcoes": [
            ("Programação para crianças", "desenvolvimento"),
            ("Segurança na internet", "seguranca"),
            ("Matemática e dados", "dados"),
            ("Desenho e arte digital", "design"),
        ],
    },
    {
        "id": 65,
        "pergunta": "Você gosta de criar APIs?",
        "opcoes": [
            ("Sim, para conectar programas", "desenvolvimento"),
            ("Não, não sei o que é", "qa"),
            ("Sim, para integrar sistemas", "devops"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 66,
        "pergunta": "Você gosta de criar bancos de dados?",
        "opcoes": [
            ("Sim, para organizar informações", "banco"),
            ("Não, prefiro código", "desenvolvimento"),
            ("Sim, para armazenar de forma segura", "seguranca"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 67,
        "pergunta": "Você gosta de criar pipelines de CI/CD?",
        "opcoes": [
            ("Sim, para automatizar deploys", "devops"),
            ("Não, não sei o que é", "desenvolvimento"),
            ("Sim, para testar código", "qa"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 68,
        "pergunta": "Você gosta de criar interfaces de usuário?",
        "opcoes": [
            ("Sim, foco em experiência", "design"),
            ("Não, prefiro backend", "desenvolvimento"),
            ("Sim, para apps de dados", "dados"),
            ("Não me interessa", "redes"),
        ],
    },
    {
        "id": 69,
        "pergunta": "Você gosta de criar relatórios?",
        "opcoes": [
            ("Sim, com gráficos e dados", "dados"),
            ("Não, prefiro código", "desenvolvimento"),
            ("Sim, para segurança", "seguranca"),
            ("Não me interessa", "qa"),
        ],
    },
    {
        "id": 70,
        "pergunta": "Você gosta de criar redes sociais?",
        "opcoes": [
            ("Sim, para conectar pessoas", "produto"),
            ("Não, prefiro programas", "desenvolvimento"),
            ("Sim, com foco em privacidade", "seguranca"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 71,
        "pergunta": "Você gosta de criar jogos?",
        "opcoes": [
            ("Sim, adoro criar jogos", "desenvolvimento"),
            ("Não, prefiro jogar", "qa"),
            ("Sim, com foco em segurança", "seguranca"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 72,
        "pergunta": "Você gosta de criar apps mobile?",
        "opcoes": [
            ("Sim, para Android e iOS", "desenvolvimento"),
            ("Não, prefiro web", "desenvolvimento"),
            ("Sim, com foco em design", "design"),
            ("Não me interessa", "redes"),
        ],
    },
    {
        "id": 73,
        "pergunta": "Você gosta de criar sites?",
        "opcoes": [
            ("Sim, adoro criar sites", "desenvolvimento"),
            ("Não, prefiro apps", "desenvolvimento"),
            ("Sim, com foco em visual", "design"),
            ("Não me interessa", "redes"),
        ],
    },
    {
        "id": 74,
        "pergunta": "Você gosta de criar sistemas?",
        "opcoes": [
            ("Sim, sistemas completos", "desenvolvimento"),
            ("Não, prefiro partes pequenas", "qa"),
            ("Sim, com foco em dados", "dados"),
            ("Não me interessa", "design"),
        ],
    },
    {
        "id": 75,
        "pergunta": "Você gosta de criar soluções tecnológicas?",
        "opcoes": [
            ("Sim, para resolver problemas", "desenvolvimento"),
            ("Não, prefiro usar prontas", "qa"),
            ("Sim, com foco em segurança", "seguranca"),
            ("Não me interessa", "design"),
        ],
    },
]
