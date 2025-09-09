def cadastrar_cliente(clientes, nome, email):
    while '@' not in email:
        print("E-mail inválido! Deve conter '@'.")
        email = input("Digite um e-mail válido: ")

    for cliente in clientes:
        if cliente["email"] == email:
            print("E-mail já cadastrado. Cadastro não realizado.")
            return

    novo_id = len(clientes) + 1 # gerador de id

    novo_cliente = {"id": novo_id, "nome": nome, "email": email}
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

clientes = []
cadastrar_cliente(clientes, "Ana", "ana@ex.com") # salvo com sucesso
cadastrar_cliente(clientes, "João", "joaoex.com")  # vai pedir para escrever o email novamente
cadastrar_cliente(clientes, "Maria", "ana@ex.com") # exemplo de teste de email duplicado

for i in clientes:
    print(f"ID: {i['id']}\nNome: {i['nome']}\nEmail: {i['email']}")