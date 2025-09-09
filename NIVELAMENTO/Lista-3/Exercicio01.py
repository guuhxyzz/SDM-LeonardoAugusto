produtos = [ 
{"id": 1, "nome": "Teclado", "preco": 99.90}, 
{"id": 2, "nome": "Mouse", "preco": 59.50}, 
{"id": 3, "nome": "Monitor", "preco": 899.00}, 
] 

for name in produtos:
    print(f"Produto {name['nome']}")