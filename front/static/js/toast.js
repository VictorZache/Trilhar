window.Toast = (function() {
  var container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  function mostrar(tipo, mensagem, duracao) {
    duracao = duracao || 5000;
    var toast = document.createElement('div');
    toast.className = 'toast ' + tipo;

    var icone = tipo === 'sucesso' ? '✓' : tipo === 'erro' ? '✕' : 'ℹ';
    toast.innerHTML =
      '<div class="toast-icon">' + icone + '</div>' +
      '<div class="toast-mensagem">' + mensagem + '</div>' +
      '<button class="toast-fecha" aria-label="Fechar notificação">×</button>';

    container.appendChild(toast);

    var btnFecha = toast.querySelector('.toast-fecha');
    btnFecha.onclick = function() {
      remover(toast);
    };

    setTimeout(function() {
      remover(toast);
    }, duracao);

    return toast;
  }

  function remover(toast) {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    setTimeout(function() {
      if (toast.parentNode) {
        toast.parentNode.removeChild(toast);
      }
    }, 300);
  }

  return {
    sucesso: function(msg, d) { return mostrar('sucesso', msg, d); },
    erro: function(msg, d) { return mostrar('erro', msg, d); },
    info: function(msg, d) { return mostrar('info', msg, d); }
  };
})();
