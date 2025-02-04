function enviarFormulario() {
    // Mostra a mensagem "Processando..."
    document.getElementById("processando").style.display = "block";

    // Simula o envio do formulário (substitua por sua lógica real)
    setTimeout(function() {
      // Após o envio, oculta a mensagem e faz algo com os dados do formulário
      document.getElementById("processando").style.display = "none";
      alert("Formulário enviado com sucesso!");
    }, 2000); // Aguarda 2 segundos para simular o envio
  }