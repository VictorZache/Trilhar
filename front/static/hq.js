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

  function svgCena(src) {
    if (src === "escritorio_boas_vindas") {
      return (
        '<svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
        '<rect x="16" y="16" width="608" height="188" rx="14" fill="#ffffff" stroke="#030213" stroke-width="3"/>' +
        '<rect x="60" y="135" width="520" height="16" rx="4" fill="#cbd5e1" stroke="#030213" stroke-width="2"/>' +
        '<rect x="240" y="55" width="140" height="80" rx="8" fill="#0f172a" stroke="#030213" stroke-width="3"/>' +
        '<circle cx="155" cy="72" r="24" fill="#fde68a" stroke="#030213" stroke-width="2.5"/>' +
        '<path d="M125 135 C125 102, 185 102, 185 135 Z" fill="#2563eb" stroke="#030213" stroke-width="2.5"/>' +
        '<circle cx="485" cy="64" r="24" fill="#fed7aa" stroke="#030213" stroke-width="2.5"/>' +
        '<path d="M452 135 C452 96, 518 96, 518 135 Z" fill="#030213" stroke="#030213" stroke-width="2.5"/>' +
        '<rect x="415" y="114" width="22" height="21" rx="4" fill="#ef4444" stroke="#030213" stroke-width="2"/>' +
        "</svg>"
      );
    }
    return (
      '<svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<rect x="16" y="16" width="608" height="188" rx="14" fill="#ecfdf5" stroke="#030213" stroke-width="3"/>' +
      '<rect x="60" y="135" width="520" height="16" rx="4" fill="#cbd5e1" stroke="#030213" stroke-width="2"/>' +
      '<rect x="230" y="50" width="160" height="85" rx="8" fill="#1e293b" stroke="#030213" stroke-width="3"/>' +
      '<text x="310" y="97" text-anchor="middle" fill="#34d399" font-size="16" font-family="monospace" font-weight="bold">git clone OK!</text>' +
      '<circle cx="155" cy="72" r="24" fill="#fde68a" stroke="#030213" stroke-width="2.5"/>' +
      '<path d="M125 135 C125 102, 185 102, 185 135 Z" fill="#059669" stroke="#030213" stroke-width="2.5"/>' +
      "</svg>"
    );
  }

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
      if (app === "navegador_github") estado.appAberto = "navegador_github";
      if (app === "assistente_ia") estado.appAberto = "assistente_ia";
      if (app === "terminal") estado.appAberto = "terminal";
      if (app === "vscode") estado.appAberto = "vscode";

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

  function renderJanelaComputador(cena) {
    var repo = cena.repositorio_alvo || {};
    var app = estado.appAberto;
    if (app === "desktop") {
      return (
        '<div class="pc-window-header"><span>Área de Trabalho</span><span>Selecione um aplicativo ao lado</span></div>' +
        '<p style="color: var(--muted-foreground); font-size: 0.925rem;">Clique nos aplicativos na barra lateral seguindo a investigação descrita no balão acima.</p>'
      );
    }
    if (app === "navegador_github") {
      return (
        '<div class="pc-window-header"><span>Navegador — GitHub</span><span class="lp-tag">' + (repo.nome || "") + "</span></div>" +
        '<p style="font-size: 0.9rem;">Repositório oficial do projeto. Para conectar sua máquina, copie a URL HTTPS:</p>' +
        '<div style="display:flex; gap:0.5rem; flex-wrap:wrap; align-items:center;">' +
        '<code style="padding:0.5rem 0.75rem; background:var(--secondary); border-radius:8px; font-size:0.82rem;">' + (repo.url_https || "") + "</code>" +
        '<button type="button" class="btn btn-primary btn-sm" data-acao="navegador_github:btn_copiar_https">' +
        (estado.urlCopiada ? "URL HTTPS Copiada ✓" : "<> Code: Copiar HTTPS") +
        "</button></div>"
      );
    }
    if (app === "assistente_ia") {
      return (
        '<div class="pc-window-header"><span>Assistente de IA</span><span class="lp-tag">Use com senso crítico</span></div>' +
        '<p style="font-size: 0.9rem;">Qual comando você confirma para baixar o repositório sem apagar dados locais?</p>' +
        '<div style="display:flex; flex-direction:column; gap:0.625rem;">' +
        '<button type="button" class="btn btn-outline" style="justify-content:flex-start;" data-acao="assistente_ia:btn_validar_comando_ia">' +
        (estado.comandoValidado ? "✓ Validado: git clone <url> (baixa uma cópia local)" : "Validar: git clone <url> (baixa uma cópia local)") +
        "</button>" +
        '<button type="button" class="btn btn-outline" style="justify-content:flex-start;" data-acao="assistente_ia:btn_comando_perigoso">Executar: git reset --hard (apaga alterações locais)</button>' +
        "</div>"
      );
    }
    if (app === "terminal") {
      var cmd = "git clone " + (repo.url_https || "");
      return (
        '<div class="pc-window-header"><span>Terminal</span><span class="lp-tag">bash</span></div>' +
        '<div class="pc-terminal-box">$ ' + (estado.repoClonado ? cmd + "<br>Cloning into 'projeto-trilhar'... done." : "aguardando comando...") + "</div>" +
        '<button type="button" class="btn btn-primary btn-sm" data-acao="terminal:btn_executar_clone">' +
        (estado.repoClonado ? "Repositório Clonado ✓" : "Executar: " + cmd) +
        "</button>"
      );
    }
    if (app === "vscode") {
      return (
        '<div class="pc-window-header"><span>VS Code — projeto-trilhar</span><span class="lp-tag">Conectado</span></div>' +
        '<div style="padding:1rem; background:var(--secondary); border-radius:10px; font-size:0.9rem;">' +
        (estado.repoClonado
          ? "<strong>Pasta aberta:</strong> projeto-trilhar/<br>Arquivos prontos para edição na branch <code>main</code>."
          : "Nenhuma pasta clonada ainda.") +
        "</div>"
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
      html += '<div class="hq-scene-art">' + svgCena(cena.visual && cena.visual.src) + "</div>";
      html += '<div class="hq-baloes">' + (cena.baloes || []).map(renderBalao).join("") + "</div>";
      html += '<div class="hq-actions"><button type="button" class="btn btn-primary" id="btn-avancar-hq">' + (cena.acao_avancar || "Continuar") + "</button></div>";
      html += "</div>";
      root.innerHTML = html;

      document.getElementById("btn-avancar-hq").onclick = function () {
        if (estado.cenasConcluidas.indexOf(cena.id) === -1) {
          estado.cenasConcluidas.push(cena.id);
        }
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

    if (etapaAtual && etapaAtual.balao) {
      html += renderBalao(etapaAtual.balao);
    }
    if (estado.feedback) {
      html += '<div class="pc-feedback pc-feedback--' + estado.feedback.tipo + '">' + estado.feedback.texto + "</div>";
    }

    html +=
      '<div class="pc-shell">' +
      '<div class="pc-desktop-bar"><span>Estação Trilhar OS</span><span>Etapa ' + Math.min(estado.etapaIdx + 1, etapas.length) + " de " + etapas.length + "</span></div>" +
      '<div class="pc-workspace">' +
      '<div class="pc-dock">' +
      '<button type="button" class="pc-app-btn ' + (estado.appAberto === "navegador_github" ? "ativo" : "") + '" data-acao="navegador_github:icone_navegador">Navegador<br>(GitHub)</button>' +
      '<button type="button" class="pc-app-btn ' + (estado.appAberto === "assistente_ia" ? "ativo" : "") + '" data-acao="assistente_ia:icone_ia">Assistente<br>de IA</button>' +
      '<button type="button" class="pc-app-btn ' + (estado.appAberto === "terminal" ? "ativo" : "") + '" data-acao="terminal:icone_terminal">Terminal</button>' +
      '<button type="button" class="pc-app-btn ' + (estado.appAberto === "vscode" ? "ativo" : "") + '" data-acao="vscode:icone_vscode">VS Code</button>' +
      "</div>" +
      '<div class="pc-window">' + renderJanelaComputador(cena) + "</div>" +
      "</div></div>";

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
      blocos.map(function (b) {
        return '<div class="alura-card"><h4>' + b.titulo + "</h4><p>" + b.texto + "</p></div>";
      }).join("") +
      '<div style="display:flex; justify-content:flex-end;"><button type="button" class="btn btn-primary" id="btn-ir-quiz">Ir para o Quiz</button></div>' +
      "</div>";
    root.innerHTML = html;
    document.getElementById("btn-ir-quiz").onclick = function () {
      estado.fase = "quiz";
      render();
    };
  }

  function renderQuiz() {
    var questoes = (fechamento.quiz && fechamento.quiz.questoes) || [];
    var html =
      '<div class="hq-topbar"><strong>Quiz Complementar</strong><span class="hq-step-pill">Etapa 2 de 3: Quiz</span></div>' +
      '<div class="alura-section">';

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
      '<button type="button" class="btn btn-primary" id="btn-ir-refs">Avançar para Referências</button>' +
      "</div></div>";

    root.innerHTML = html;

    questoes.forEach(function (q) {
      root.querySelectorAll('input[name="hq_' + q.id + '"]').forEach(function (radio) {
        radio.onchange = function () {
          estado.respostasQuiz[q.id] = parseInt(radio.value, 10);
        };
      });
    });

    document.getElementById("btn-conferir-quiz").onclick = function () {
      estado.quizConferido = true;
      render();
    };

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
      '<div class="alura-section">' +
      '<p style="color:var(--muted-foreground);">Quer aprofundar? Salve estes materiais oficiais e gratuitos:</p>' +
      refs.map(function (r) {
        return '<a class="alura-ref-link" href="' + r.url + '" target="_blank" rel="noopener noreferrer"><span><strong>' + r.titulo + '</strong><br><small style="color:var(--muted-foreground);">' + r.fonte + "</small></span><span>Abrir ↗</span></a>";
      }).join("") +
      '<div style="display:flex; justify-content:flex-end; margin-top:0.5rem;">' +
      '<button type="button" class="btn btn-primary" id="btn-finalizar-hq">Concluir Missão</button>' +
      "</div></div>";

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