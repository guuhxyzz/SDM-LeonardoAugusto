def calcular_resumo(catalogo, carrinho):
    itens = []
    total = 0.0

    for id_produto, qtd in carrinho:
        preco = catalogo.get(id_produto, 0)
        subtotal = preco * qtd
        itens.append({"id": id_produto, "qtd": qtd, "subtotal": subtotal})
        total += subtotal

    resumo = {"items": itens, "total": total}
    return resumo

catalogo = {1: 99.90, 2: 59.50, 3: 899.00}
carrinho = [(1, 2), (3, 1)]

resumo = calcular_resumo(catalogo, carrinho)
print(resumo)