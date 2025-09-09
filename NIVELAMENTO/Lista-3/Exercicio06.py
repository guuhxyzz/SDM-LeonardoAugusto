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

# a
idx_clientes = {c["id"]: c["nome"] for c in clientes}
idx_produtos = {p["id"]: {"nome": p["nome"], "preco": p["preco"]} for p in produtos}

# b
compras_detalhadas = []
for compra in compras:
    itens_detalhados = [
        {
            "nome_produto": idx_produtos.get(item["produto_id"], {"nome": "desconhecido", "preco": 0.0})["nome"],
            "qtd": item["qtd"],
            "preco": idx_produtos.get(item["produto_id"], {"nome": "desconhecido", "preco": 0.0})["preco"],
            "subtotal": item["qtd"] * idx_produtos.get(item["produto_id"], {"nome": "desconhecido", "preco": 0.0})["preco"]
        }
        for item in compra["itens"]
    ]
    total = sum(item["subtotal"] for item in itens_detalhados)
    compras_detalhadas.append({
        "cliente": idx_clientes.get(compra["cliente_id"], "desconhecido"),
        "itens": itens_detalhados,
        "total": total
    })

from pprint import pprint
pprint(compras_detalhadas)