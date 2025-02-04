def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1  # Inicializa os dois primeiros números da sequência

    for _ in range(n):
        fib_sequence.append(a)  # Adiciona o número atual à lista
        a, b = b, a + b  # Atualiza a e b para os próximos números

    return fib_sequence

# Chama a função para obter os 10 primeiros números da sequência de Fibonacci
result = fibonacci(10)
print(result)