compras = [
    {"itens": [{"produto_id": 1, "qtd": 2}, {"produto_id": 2, "qtd": 1}]},
    {"itens": [{"produto_id": 1, "qtd": 1}, {"produto_id": 3, "qtd": 4}]},
    {"itens": [{"produto_id": 2, "qtd": 3}, {"produto_id": 3, "qtd": 2}]},
]

# a
vendas_por_produto = {}
for compra in compras:
    for item in compra["itens"]:
        pid = item["produto_id"]
        qtd = item["qtd"]
        vendas_por_produto[pid] = vendas_por_produto.get(pid, 0) + qtd

# b
ordenada = sorted(vendas_por_produto.items(), key=lambda x: x[1], reverse=True)

# c
top3 = ordenada[:3]

print("Vendas por produto:", vendas_por_produto)
print("Ordenada:", ordenada)
print("Top 3:", top3)