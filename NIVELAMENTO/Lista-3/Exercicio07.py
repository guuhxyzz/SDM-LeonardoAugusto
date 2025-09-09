clientes = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Bruno"}
]

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 99.90},
    {"id": 2, "nome": "Mouse", "preco": 59.50}
]

compras = [
    {"id": 100, "cliente_id": 1, "itens": [{"produto_id": 1, "qtd": 2}, {"produto_id": 2, "qtd": 1}]},
    {"id": 101, "cliente_id": 2, "itens": [{"produto_id": 2, "qtd": 3}, {"produto_id": 3, "qtd": 1}]}
]

# índices para acesso rápido
idx_clientes = {c["id"]: c["nome"] for c in clientes}
idx_produtos = {p["id"]: p["preco"] for p in produtos}

# a
faturamento_por_cliente = {}
for compra in compras:
    total = sum(
        item["qtd"] * idx_produtos.get(item["produto_id"], 0.0)
        for item in compra["itens"]
    )
    faturamento_por_cliente[compra["cliente_id"]] = faturamento_por_cliente.get(compra["cliente_id"], 0.0) + total

# b
lista_faturamento = [
    {"cliente": idx_clientes.get(cid, "desconhecido"), "total": total}
    for cid, total in faturamento_por_cliente.items()
]

# c
ranking = sorted(lista_faturamento, key=lambda d: d["total"], reverse=True)

from pprint import pprint
pprint(ranking)