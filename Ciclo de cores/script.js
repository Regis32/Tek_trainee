// Array de cores
const cores = ['red', 'green', 'blue'];
let indiceCor = 0; // Índice da cor atual

// Função para mudar a cor do botão
function mudarCor() {
    // Muda a cor do botão
    const botao = document.getElementById('botao');
    botao.style.backgroundColor = cores[indiceCor];

    // Atualiza o índice da cor
    indiceCor = (indiceCor + 1) % cores.length; // Ciclo entre as cores
}

// Adiciona o evento de clique ao botão
document.getElementById('botao').addEventListener('click', mudarCor);