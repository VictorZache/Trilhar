(function () {
  var root = document.getElementById("hq-app");
  if (!root) return;

  var dadosEl = document.getElementById("hq-dados-json");
  if (!dadosEl) return;

  var dados = JSON.parse(dadosEl.textContent);
  var cenas = dados.cenas || [];
  var fechamento = dados.fechamento || {};

  var estado = {
    fase: "cenas",
    cenaIdx: 0,
    etapaIdx: 0,
    appAberto: "desktop",
    urlCopiada: false,
    comandoValidado: false,
    repoClonado: false,
    feedback: null,
    cenasConcluidas: [],
    respostasQuiz: {},
    quizConferido: false
  };

  var ICONS = {
    win: '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M3 3h8v8H3V3zm10 0h8v8h-8V3zM3 13h8v8H3v-8zm10 0h8v8h-8v-8z"/></svg>',
    browser: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" fill="#3b82f6"/><circle cx="12" cy="12" r="4" fill="#ffffff"/><path d="M12 2a10 10 0 0 1 8.66 5H12V2z" fill="#ef4444"/><path d="M3.34 7A10 10 0 0 0 12 22l4-6.93A4 4 0 0 1 8 12H3.34z" fill="#22c55e"/></svg>',
    ia: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="6" fill="#7c3aed"/><path d="M12 5l1.6 4.4L18 11l-4.4 1.6L12 17l-1.6-4.4L6 11l4.4-1.6L12 5z" fill="#ffffff"/></svg>',
    cmd: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="2" y="4" width="20" height="16" rx="3" fill="#0c0c0c" stroke="#94a3b8" stroke-width="1.5"/><path d="M6 10l3 2.5L6 15M11 15h5" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    vscode: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="5" fill="#1e293b"/><path d="M17.5 4.5L10 11.2 6.5 8.5 5 9.6l3.3 2.4L5 14.4l1.5 1.1 3.5-2.7 7.5 6.7 2.5-1.2V5.7l-2.5-1.2z" fill="#38bdf8"/></svg>',
    octocat: '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>'
  };

  function renderBalao(b) {
    var cls = "hq-balao hq-balao--" + (b.tipo || "fala");
    var autor = b.personagem ? '<span class="hq-balao-autor">' + b.personagem + "</span>" : "";
    return '<div class="' + cls + '">' + autor + b.texto + "</div>";
  }

  function tentarAcao(app, elemento) {
    var cena = cenas[estado.cenaIdx];
    var etapa = cena.etapas[estado.etapaIdx];
    if (!etapa) return;

    if (etapa.alvo.app === app && etapa.alvo.elemento === elemento) {
      estado.appAberto = app;
      if (elemento === "btn_copiar_https") estado.urlCopiada = true;
      if (elemento === "btn_validar_comando_ia") estado.comandoValidado = true;
      if (elemento === "btn_executar_clone") estado.repoClonado = true;

      estado.feedback = { tipo: "sucesso", texto: etapa.feedback_sucesso };
      estado.etapaIdx += 1;

      if (estado.etapaIdx >= cena.etapas.length) {
        if (estado.cenasConcluidas.indexOf(cena.id) === -1) {
          estado.cenasConcluidas.push(cena.id);
        }
      }
    } else {
      estado.feedback = { tipo: "erro", texto: etapa.feedback_erro };
    }
    render();
  }

  function renderJanelaSO(cena) {
    var repo = cena.repositorio_alvo || {};
    var app = estado.appAberto;
    if (app === "desktop") return "";

    if (app === "navegador_github") {
      return (
        '<div class="pc-app-window">' +
        '<div class="pc-win-titlebar"><span>Navegador — GitHub</span><button type="button" class="pc-win-close" data-minimizar="1">✕</button></div>' +
        '<div class="pc-win-body">' +
        '<div class="gh-urlbar"><span>🔒</span><span class="gh-url-pill">https://github.com/' + (repo.nome || "") + "</span></div>" +
        '<div class="gh-header">' + ICONS.octocat + "<span>" + (repo.nome || "") + "</span></div>" +
        '<div class="gh-content">' +
        '<div class="gh-repo-bar">' +
        '<span style="font-size:0.7rem;color:#57606a;">Branch: <strong>' + (repo.branch || "main") + "</strong></span>" +
        '<button type="button" class="gh-code-btn" data-acao="navegador_github:btn_copiar_https">' +
        (estado.urlCopiada ? "HTTPS Copiado ✓" : "<> Code (HTTPS)") +
        "</button></div>" +
        '<div style="font-size:0.65rem;background:#f6f8fa;padding:0.35rem 0.5rem;border:1px solid #d0d7de;border-radius:6px;word-break:break-all;">' +
        (repo.url_https || "") + "</div>" +
        '<div class="gh-files">' +
        '<div class="gh-file-row"><span>📁 backend/</span><span>app inicial</span></div>' +
        '<div class="gh-file-row"><span>📄 README.md</span><span>instruções</span></div>' +
        '<div class="gh-file-row"><span>📄 requirements.txt</span><span>dependências</span></div>' +
        "</div></div></div></div>"
      );
    }

    if (app === "assistente_ia") {
      return (
        '<div class="pc-app-window">' +
        '<div class="pc-win-titlebar"><span>Assistente de IA</span><button type="button" class="pc-win-close" data-minimizar="1">✕</button></div>' +
        '<div class="pc-win-body" style="padding:0.65rem; gap:0.5rem;">' +
        '<p style="font-size:0.74rem;"><strong>Sugestão gerada:</strong> leia com atenção e valide apenas o comando seguro para baixar o repositório.</p>' +
        '<button type="button" class="btn btn-outline btn-sm" style="justify-content:flex-start;font-size:0.72rem;" data-acao="assistente_ia:btn_validar_comando_ia">' +
        (estado.comandoValidado ? "✓ Validado: git clone <url>" : "Validar: git clone <url> (baixa cópia local)") +
        "</button>" +
        '<button type="button" class="btn btn-outline btn-sm" style="justify-content:flex-start;font-size:0.72rem;" data-acao="assistente_ia:btn_comando_perigoso">Executar: git reset --hard (apaga alterações locais)</button>' +
        "</div></div>"
      );
    }

    if (app === "terminal") {
      var cmd = "git clone " + (repo.url_https || "");
      return (
        '<div class="pc-app-window">' +
        '<div class="pc-win-titlebar"><span>Prompt de Comando (cmd.exe)</span><button type="button" class="pc-win-close" data-minimizar="1">✕</button></div>' +
        '<div class="cmd-body">' +
        "<div>Microsoft Windows [Versão 10.0]<br>C:\\Users\\Estagiario\\Projetos> " +
        (estado.repoClonado ? cmd + "<br>Cloning into 'projeto-trilhar'...<br>Receiving objects: 100%, done." : "_") +
        "</div>" +
        '<button type="button" class="cmd-run-btn" data-acao="terminal:btn_executar_clone">' +
        (estado.repoClonado ? "Clonado com sucesso ✓" : "Executar: " + cmd) +
        "</button></div></div>"
      );
    }

    if (app === "vscode") {
      return (
        '<div class="pc-app-window">' +
        '<div class="pc-win-titlebar pc-win-titlebar--dark"><span>Visual Studio Code — projeto-trilhar</span><button type="button" class="pc-win-close" data-minimizar="1">✕</button></div>' +
        '<div class="vscode-shell">' +
        '<div class="vscode-activity"><span>📁</span><span>🔍</span><span>🌿</span></div>' +
        '<div class="vscode-sidebar"><div style="font-size:0.6rem;color:#9ca3af;margin-bottom:0.35rem;">EXPLORADOR</div><div>▾ projeto-trilhar</div><div style="padding-left:0.5rem;">📄 app.py<br>📄 README.md</div></div>' +
        '<div class="vscode-editor"><span style="color:#60a5fa;"># projeto-trilhar (main)</span><br>' +
        (estado.repoClonado ? '<span style="color:#34d399;">print("Repositório conectado!")</span>' : "<span>Nenhuma pasta aberta.</span>") +
        "</div></div></div>"
      );
    }
    return "";
  }

  function renderCena() {
    var cena = cenas[estado.cenaIdx];
    var html =
      '<div class="hq-topbar">' +
      "<strong>" + cena.titulo + "</strong>" +
      '<span class="hq-step-pill">Cena ' + (estado.cenaIdx + 1) + " de " + cenas.length + "</span>" +
      "</div>";

    if (cena.tipo_cena === "hq") {
      html += '<div class="hq-panel">';
      html += '<div class="hq-scene-art"><img src="' + cena.visual.src + '" alt="' + cena.titulo + '"></div>';
      html += '<div class="hq-baloes">' + (cena.baloes || []).map(renderBalao).join("") + "</div>";
      html += '<div class="hq-actions"><button type="button" class="btn btn-primary" id="btn-avancar-hq">' + (cena.acao_avancar || "Continuar") + "</button></div>";
      html += "</div>";
      root.innerHTML = html;

      document.getElementById("btn-avancar-hq").onclick = function () {
        if (estado.cenasConcluidas.indexOf(cena.id) === -1) estado.cenasConcluidas.push(cena.id);
        if (estado.cenaIdx + 1 < cenas.length) {
          estado.cenaIdx += 1;
          estado.etapaIdx = 0;
          estado.feedback = null;
        } else {
          estado.fase = "leitura";
        }
        render();
      };
      return;
    }

    var etapas = cena.etapas || [];
    var concluida = estado.etapaIdx >= etapas.length;
    var etapaAtual = concluida ? null : etapas[estado.etapaIdx];

    if (etapaAtual && etapaAtual.balao) html += renderBalao(etapaAtual.balao);
    if (estado.feedback) {
      html += '<div class="pc-feedback pc-feedback--' + estado.feedback.tipo + '">' + estado.feedback.texto + "</div>";
    }

    html +=
      '<div class="pc-stage">' +
      '<img class="pc-stage-bg" src="' + cena.visual.src + '" alt="Mesa de trabalho">' +
      '<div class="pc-screen-overlay">' +
      '<div class="pc-desktop-area">' +
      '<div class="pc-icons-grid">' +
      '<button type="button" class="pc-desktop-icon" data-acao="navegador_github:icone_navegador">' + ICONS.browser + "<span>Navegador</span></button>" +
      '<button type="button" class="pc-desktop-icon" data-acao="assistente_ia:icone_ia">' + ICONS.ia + "<span>IA</span></button>" +
      '<button type="button" class="pc-desktop-icon" data-acao="terminal:icone_terminal">' + ICONS.cmd + "<span>Prompt</span></button>" +
      '<button type="button" class="pc-desktop-icon" data-acao="vscode:icone_vscode">' + ICONS.vscode + "<span>VS Code</span></button>" +
      "</div>" +
      renderJanelaSO(cena) +
      "</div>" +
      '<div class="pc-taskbar">' +
      '<div class="pc-taskbar-apps">' +
      '<span style="color:#60a5fa;display:inline-flex;margin-right:4px;">' + ICONS.win + "</span>" +
      '<button type="button" class="pc-task-btn ' + (estado.appAberto === "navegador_github" ? "ativo" : "") + '" data-acao="navegador_github:icone_navegador" title="Navegador">' + ICONS.browser + "</button>" +
      '<button type="button" class="pc-task-btn ' + (estado.appAberto === "assistente_ia" ? "ativo" : "") + '" data-acao="assistente_ia:icone_ia" title="Assistente de IA">' + ICONS.ia + "</button>" +
      '<button type="button" class="pc-task-btn ' + (estado.appAberto === "terminal" ? "ativo" : "") + '" data-acao="terminal:icone_terminal" title="Prompt de Comando">' + ICONS.cmd + "</button>" +
      '<button type="button" class="pc-task-btn ' + (estado.appAberto === "vscode" ? "ativo" : "") + '" data-acao="vscode:icone_vscode" title="VS Code">' + ICONS.vscode + "</button>" +
      "</div>" +
      '<span style="font-size:0.65rem;color:#cbd5e1;">Etapa ' + Math.min(estado.etapaIdx + 1, etapas.length) + "/" + etapas.length + " · 09:14</span>" +
      "</div></div></div>";

    if (concluida) {
      html += '<div style="display:flex; justify-content:flex-end;"><button type="button" class="btn btn-primary" id="btn-proxima-cena">Continuar história</button></div>';
    }

    root.innerHTML = html;

    root.querySelectorAll("[data-acao]").forEach(function (btn) {
      btn.onclick = function () {
        var partes = btn.getAttribute("data-acao").split(":");
        tentarAcao(partes[0], partes[1]);
      };
    });
    root.querySelectorAll("[data-minimizar]").forEach(function (btn) {
      btn.onclick = function () {
        estado.appAberto = "desktop";
        render();
      };
    });

    var btnProx = document.getElementById("btn-proxima-cena");
    if (btnProx) {
      btnProx.onclick = function () {
        estado.cenaIdx += 1;
        estado.feedback = null;
        render();
      };
    }
  }

  function renderLeitura() {
    var blocos = fechamento.leitura || [];
    var html =
      '<div class="hq-topbar"><strong>Revisão — O que você aprendeu</strong><span class="hq-step-pill">Etapa 1 de 3: Leitura</span></div>' +
      '<div class="alura-section">' +
      blocos.map(function (b) { return '<div class="alura-card"><h4>' + b.titulo + "</h4><p>" + b.texto + "</p></div>"; }).join("") +
      '<div style="display:flex; justify-content:flex-end;"><button type="button" class="btn btn-primary" id="btn-ir-quiz">Ir para o Quiz</button></div></div>';
    root.innerHTML = html;
    document.getElementById("btn-ir-quiz").onclick = function () { estado.fase = "quiz"; render(); };
  }

  function renderQuiz() {
    var questoes = (fechamento.quiz && fechamento.quiz.questoes) || [];
    var html = '<div class="hq-topbar"><strong>Quiz Complementar</strong><span class="hq-step-pill">Etapa 2 de 3: Quiz</span></div><div class="alura-section">';
    questoes.forEach(function (q, idx) {
      html += '<div class="alura-card"><h4>' + (idx + 1) + ". " + q.pergunta + '</h4><div class="quiz-options" style="margin-top:0.75rem;">';
      q.opcoes.forEach(function (op, opIdx) {
        var checked = estado.respostasQuiz[q.id] === opIdx ? "checked" : "";
        html += '<label class="quiz-option"><input type="radio" name="hq_' + q.id + '" value="' + opIdx + '" ' + checked + "> " + op + "</label>";
      });
      html += "</div>";
      if (estado.quizConferido) {
        var acertou = estado.respostasQuiz[q.id] === q.correta_idx;
        html += '<div class="pc-feedback pc-feedback--' + (acertou ? "sucesso" : "erro") + '" style="margin-top:0.75rem;">' + q.explicacao + "</div>";
      }
      html += "</div>";
    });
    html +=
      '<div style="display:flex; justify-content:space-between; gap:0.75rem; flex-wrap:wrap;">' +
      '<button type="button" class="btn btn-outline" id="btn-conferir-quiz">Conferir explicações</button>' +
      '<button type="button" class="btn btn-primary" id="btn-ir-refs">Avançar para Referências</button></div></div>';
    root.innerHTML = html;

    questoes.forEach(function (q) {
      root.querySelectorAll('input[name="hq_' + q.id + '"]').forEach(function (radio) {
        radio.onchange = function () { estado.respostasQuiz[q.id] = parseInt(radio.value, 10); };
      });
    });
    document.getElementById("btn-conferir-quiz").onclick = function () { estado.quizConferido = true; render(); };
    document.getElementById("btn-ir-refs").onclick = function () {
      if (Object.keys(estado.respostasQuiz).length < questoes.length) {
        alert("Responda todas as perguntas do quiz antes de avançar.");
        return;
      }
      estado.fase = "referencias";
      render();
    };
  }

  function renderReferencias() {
    var refs = fechamento.referencias || [];
    var html =
      '<div class="hq-topbar"><strong>Referências de Estudo</strong><span class="hq-step-pill">Etapa 3 de 3: Referências</span></div>' +
      '<div class="alura-section"><p style="color:var(--muted-foreground);">Quer aprofundar? Salve estes materiais oficiais e gratuitos:</p>' +
      refs.map(function (r) {
        return '<a class="alura-ref-link" href="' + r.url + '" target="_blank" rel="noopener noreferrer"><span><strong>' + r.titulo + '</strong><br><small style="color:var(--muted-foreground);">' + r.fonte + "</small></span><span>Abrir ↗</span></a>";
      }).join("") +
      '<div style="display:flex; justify-content:flex-end; margin-top:0.5rem;"><button type="button" class="btn btn-primary" id="btn-finalizar-hq">Concluir Missão</button></div></div>';
    root.innerHTML = html;
    document.getElementById("btn-finalizar-hq").onclick = function () {
      document.getElementById("resposta-hidden").value = JSON.stringify({
        cenas_concluidas: estado.cenasConcluidas,
        respostas_quiz: estado.respostasQuiz
      });
      document.getElementById("jogo-form").submit();
    };
  }

  function render() {
    if (estado.fase === "cenas") return renderCena();
    if (estado.fase === "leitura") return renderLeitura();
    if (estado.fase === "quiz") return renderQuiz();
    return renderReferencias();
  }

  render();
})();