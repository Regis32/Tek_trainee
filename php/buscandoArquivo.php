<?php
// Função para somar os valores de uma coluna específica em um arquivo CSV
function somarColunaCSV($caminhoArquivo, $indiceColuna) {
    // Verifica se o arquivo existe
    if (!file_exists($caminhoArquivo) || !is_readable($caminhoArquivo)) {
        return "Arquivo não encontrado ou não é legível.";
    }

    $total = 0; // Inicializa o total

    // Abre o arquivo CSV
    if (($handle = fopen($caminhoArquivo, 'r')) !== false) {
        // Lê cada linha do arquivo
        while (($dados = fgetcsv($handle, 1000, ',')) !== false) {
            // Verifica se a coluna existe na linha
            if (isset($dados[$indiceColuna])) {
                // Adiciona o valor da coluna ao total
                $total += floatval($dados[$indiceColuna]);
            }
        }
        fclose($handle); // Fecha o arquivo
    }

    return $total; // Retorna o total
}

// Exemplo de uso
$caminhoArquivo = 'caminho/para/seu/arquivo.csv'; // Substitua pelo caminho do seu arquivo CSV

$indiceColuna = 1; // Substitua pelo índice da coluna que você deseja somar (0 para a primeira coluna)

$total = somarColunaCSV($caminhoArquivo, $indiceColuna);
echo "O total da coluna é: " . $total;