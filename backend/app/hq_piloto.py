"""
Roteiro e dados da Missão Piloto em HQ Investigativa:
Trilha Introdutória de GitHub — "Primeiro Dia: Conectando ao Repositório".

Este arquivo segue o Contrato JSON v1 de `hq_investigacao` e será
serializado na coluna `missoes.dados_jogo` do SQLite.
"""

MISSAO_PILOTO_GITHUB = {
    "versao": 1,
    "meta": {
        "titulo": "Primeiro Dia: Conectando ao Repositório",
        "trilha": "Introdução ao GitHub",
        "protagonista": "Você (Estagiário)",
        "objetivo": "Conectar sua estação de trabalho ao repositório da empresa usando GitHub, Terminal e IA com senso crítico.",
    },
    "cenas": [
        {
            "id": "cena_1_chegada",
            "ordem": 1,
            "tipo_cena": "hq",
            "titulo": "Boas-vindas na Empresa",
            "visual": {
                "tipo": "svg_cena",
                "src": "escritorio_boas_vindas",
            },
            "baloes": [
                {
                    "tipo": "narracao",
                    "personagem": None,
                    "texto": "Segunda-feira, 9h00. Seu primeiro dia de estágio em tecnologia. O café está quente, o crachá é novo e a cadeira ainda tem cheiro de plástico.",
                },
                {
                    "tipo": "fala",
                    "personagem": "Gerente de Projetos",
                    "texto": "Seja muito bem-vindo(a) ao time! Sem pressão para o primeiro dia: sua missão inicial é se conectar ao repositório do nosso projeto no GitHub.",
                },
                {
                    "tipo": "pensamento",
                    "personagem": "Você",
                    "texto": "Beleza... 'se conectar ao repositório'. Parece simples, mas é melhor eu investigar passo a passo no computador antes de sair clicando em tudo!",
                },
            ],
            "acao_avancar": "Sentar e ligar a estação de trabalho",
        },
        {
            "id": "cena_2_computador",
            "ordem": 2,
            "tipo_cena": "computador",
            "titulo": "Estação de Trabalho",
            "apps": ["navegador_github", "assistente_ia", "terminal", "vscode"],
            "repositorio_alvo": {
                "nome": "empresa-tech/projeto-trilhar",
                "url_https": "https://github.com/empresa-tech/projeto-trilhar.git",
                "branch": "main",
            },
            "etapas": [
                {
                    "ordem": 1,
                    "balao": {
                        "tipo": "pensamento",
                        "personagem": "Você",
                        "texto": "Primeiro preciso achar o endereço do projeto. Onde fica hospedado o repositório da empresa?",
                    },
                    "alvo": {
                        "app": "navegador_github",
                        "elemento": "icone_navegador",
                    },
                    "feedback_erro": "Calma! Antes de abrir código ou terminal, você precisa buscar o link do repositório na internet.",
                    "feedback_sucesso": "Boa! Você abriu o navegador direto na página do projeto no GitHub.",
                },
                {
                    "ordem": 2,
                    "balao": {
                        "tipo": "narracao",
                        "personagem": None,
                        "texto": "Você encontrou o repositório 'empresa-tech/projeto-trilhar'. Agora precisa copiar o endereço dele para trazer uma cópia para o seu computador.",
                    },
                    "alvo": {
                        "app": "navegador_github",
                        "elemento": "btn_copiar_https",
                    },
                    "feedback_erro": "Procure o botão de 'Code (HTTPS)' no repositório para copiar o link de conexão.",
                    "feedback_sucesso": "URL HTTPS copiada! Agora você já tem o endereço exato do repositório.",
                },
                {
                    "ordem": 3,
                    "balao": {
                        "tipo": "pensamento",
                        "personagem": "Você",
                        "texto": "Tenho o link, mas esqueci qual comando baixa o repositório. Vou consultar o Assistente de IA — mas lendo com atenção antes de confiar!",
                    },
                    "alvo": {
                        "app": "assistente_ia",
                        "elemento": "icone_ia",
                    },
                    "feedback_erro": "Antes de digitar qualquer comando no terminal, confira com o Assistente de IA qual é o comando certo e o que ele faz.",
                    "feedback_sucesso": "Assistente de IA aberto! Veja a sugestão dele com senso crítico.",
                },
                {
                    "ordem": 4,
                    "balao": {
                        "tipo": "fala",
                        "personagem": "Assistente de IA",
                        "texto": "Sugiro rodar: git clone <url> (baixa uma cópia completa do repositório para uma pasta local) ou git reset --hard (apaga alterações locais). Qual você valida?",
                    },
                    "alvo": {
                        "app": "assistente_ia",
                        "elemento": "btn_validar_comando_ia",
                    },
                    "feedback_erro": "Cuidado! Nunca execute comandos destrutivos sem checar. Valide o comando que apenas clona (copia) o repositório.",
                    "feedback_sucesso": "Senso crítico em dia! Você confirmou o 'git clone' e descartou o comando perigoso.",
                },
                {
                    "ordem": 5,
                    "balao": {
                        "tipo": "pensamento",
                        "personagem": "Você",
                        "texto": "Agora que já conferi o comando 'git clone', preciso de um lugar para executá-lo e baixar o projeto.",
                    },
                    "alvo": {
                        "app": "terminal",
                        "elemento": "icone_terminal",
                    },
                    "feedback_erro": "Para rodar comandos Git como 'git clone', abra o Terminal na área de trabalho.",
                    "feedback_sucesso": "Terminal aberto! Agora cole a URL e execute a clonagem.",
                },
                {
                    "ordem": 6,
                    "balao": {
                        "tipo": "narracao",
                        "personagem": None,
                        "texto": "Tudo pronto no Terminal. Execute o comando git clone com a URL HTTPS que você copiou.",
                    },
                    "alvo": {
                        "app": "terminal",
                        "elemento": "btn_executar_clone",
                    },
                    "feedback_erro": "Clique no comando 'git clone https://github.com/empresa-tech/projeto-trilhar.git' para baixar o repositório.",
                    "feedback_sucesso": "Repositório clonado com sucesso! Pasta 'projeto-trilhar' criada na sua máquina.",
                },
                {
                    "ordem": 7,
                    "balao": {
                        "tipo": "pensamento",
                        "personagem": "Você",
                        "texto": "Quase lá! Só falta abrir a pasta do projeto no editor de código para confirmar que tudo veio certinho.",
                    },
                    "alvo": {
                        "app": "vscode",
                        "elemento": "icone_vscode",
                    },
                    "feedback_erro": "Abra o VS Code na área de trabalho para visualizar os arquivos clonados.",
                    "feedback_sucesso": "Projeto aberto no VS Code! Todos os arquivos da empresa estão conectados.",
                },
            ],
        },
        {
            "id": "cena_3_alivio",
            "ordem": 3,
            "tipo_cena": "hq",
            "titulo": "Primeira Demanda Concluída!",
            "visual": {
                "tipo": "svg_cena",
                "src": "escritorio_alivio",
            },
            "baloes": [
                {
                    "tipo": "pensamento",
                    "personagem": "Você",
                    "texto": "Ufa! Repositório clonado, VS Code aberto e nenhum comando perigoso executado por acidente. Sobrevivi ao primeiro dia!",
                },
                {
                    "tipo": "fala",
                    "personagem": "Gerente de Projetos",
                    "texto": "Mandou muito bem! Muita gente trava logo nessa primeira conexão. Agora vale revisar o que você acabou de fazer.",
                },
            ],
            "acao_avancar": "Ir para a revisão e quiz",
        },
    ],
    "fechamento": {
        "leitura": [
            {
                "titulo": "1. O que significa clonar um repositório (git clone)?",
                "texto": "No GitHub, o código do projeto fica salvo na nuvem. Quando você roda 'git clone <URL-HTTPS>', o Git cria uma cópia completa do projeto no seu computador já conectada ao repositório original, permitindo baixar atualizações e enviar suas contribuições depois.",
            },
            {
                "titulo": "2. Por que usar o Terminal no dia a dia?",
                "texto": "O Terminal permite conversar diretamente com ferramentas de desenvolvimento como Git, Python e Node.js por meio de comandos curtos e precisos. Mesmo em editores modernos como o VS Code, o terminal integrado é usado o tempo todo.",
            },
            {
                "titulo": "3. Usando a IA com senso crítico",
                "texto": "Assistentes de IA são ótimos para lembrar comandos e explicar erros, mas eles também podem sugerir opções desnecessárias ou destrutivas (como 'git reset --hard'). Sempre leia o que um comando faz antes de executá-lo no seu computador.",
            },
        ],
        "quiz": {
            "nota_minima": 2,
            "questoes": [
                {
                    "id": "q1",
                    "pergunta": "Qual comando usamos no Terminal para baixar uma cópia conectada de um repositório do GitHub?",
                    "opcoes": [
                        "git clone <url-do-repositorio>",
                        "git reset --hard",
                        "git delete <url-do-repositorio>",
                    ],
                    "correta_idx": 0,
                    "explicacao": "O comando 'git clone' cria uma cópia local do repositório remoto já configurada para se comunicar com o GitHub.",
                },
                {
                    "id": "q2",
                    "pergunta": "Onde encontramos a URL HTTPS para clonar um projeto no GitHub?",
                    "opcoes": [
                        "Na lixeira do computador",
                        "No botão 'Code' na página do repositório",
                        "Nas configurações de brilho do monitor",
                    ],
                    "correta_idx": 1,
                    "explicacao": "Na página principal de qualquer repositório no GitHub, o botão 'Code' exibe a URL HTTPS pronta para copiar.",
                },
                {
                    "id": "q3",
                    "pergunta": "Qual é a melhor postura quando uma IA sugere um comando de terminal?",
                    "opcoes": [
                        "Copiar e colar o mais rápido possível sem ler",
                        "Ler o que o comando faz e validar se ele resolve exatamente o seu problema",
                        "Nunca usar IA para aprender programação",
                    ],
                    "correta_idx": 1,
                    "explicacao": "A IA acelera o aprendizado, mas quem responde pelo código e pelo ambiente é quem executa o comando.",
                },
            ],
        },
        "referencias": [
            {
                "titulo": "Clonando um repositório (GitHub Docs)",
                "fonte": "Documentação Oficial do GitHub",
                "url": "https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository",
            },
            {
                "titulo": "Git — Guia Inicial em Português",
                "fonte": "Git SCM",
                "url": "https://git-scm.com/book/pt-br/v2",
            },
        ],
    },
}
