def filtrar_compras(compras, cliente_id, data_ini, data_fim):
    return [
        compra for compra in compras
        if compra["cliente_id"] == cliente_id
        and data_ini <= compra["data"] <= data_fim
    ]

compras = [
    {"cliente_id": 1, "data": "2025-09-01", "valor": 150.0},
    {"cliente_id": 2, "data": "2025-09-03", "valor": 99.9},
    {"cliente_id": 1, "data": "2025-09-08", "valor": 300.0},
]

resultado = filtrar_compras(compras, 1, "2025-09-01", "2025-09-08")
print(resultado)