def tres_maiores(valores):
    # Inicializa uma lista para armazenar os três maiores valores
    maiores = [float('-inf')] * 3  # Começa com valores muito baixos

    for numero in valores:
        # Verifica se o número atual é maior que o menor dos três maiores
        if numero > maiores[2]:
            maiores[2] = numero  # Substitui o menor dos três maiores
            # Ordena a lista dos três maiores
            if maiores[2] > maiores[1]:
                maiores[2], maiores[1] = maiores[1], maiores[2]
                if maiores[1] > maiores[0]:
                    maiores[1], maiores[0] = maiores[0], maiores[1]

    return maiores

# Exemplo de uso
numeros = [10, 4, 3, 50, 23, 90, 5]
resultados = tres_maiores(numeros)
print("Os três maiores valores são:", resultados)