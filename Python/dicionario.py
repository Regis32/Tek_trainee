produtos = [
    {"nome": "Batata", "quantidade": 10, "preco": 5.0},
    {"nome": "Cebola", "quantidade": 1, "preco": 0.97},
    {"nome": "Cenoura", "quantidade": 3, "preco": 2.52},
    {"nome": "Banana", "quantidade": 1, "preco": 4.20},
]

# Calculando a quantidade total de produtos

quantidade_total = sum(produto["quantidade"] for produto in produtos)

# Exibindo o resultado
print(f"A quantidade total de produtos é: {quantidade_total}")
