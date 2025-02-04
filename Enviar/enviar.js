document.getElementById('meuFormulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    const botao = document.getElementById('botaoEnviar');
    
    botao.textContent = 'Processando...'; // Altera o texto do botão
    botao.disabled = true; // Desabilita o botão para evitar múltiplos cliques

    // Simula um atraso para o processamento (exemplo)
    setTimeout(() => {
        // Aqui você pode adicionar a lógica para enviar o formulário
        alert('Formulário enviado com sucesso!'); // Exemplo de ação após o envio
        botao.textContent = 'Enviar'; // Restaura o texto do botão
        botao.disabled = false; // Habilita o botão novamente
    }, 2000); // 2 segundos de atraso
});
