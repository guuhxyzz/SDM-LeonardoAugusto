nome = input("Digite o seu nome: ")
protocolo = input("Digite número do protocolo: ")
data = input("Digite data do protocolo (DD/MM/AAAA): ")

letras = ''.join([parte[-1].lower() for parte in nome.split()])

ano = data.split('/')[-1]

identificador = f"{protocolo}-{letras}-{ano}"

sobrenome = nome.split()[-1]

validade = 2025 - int(ano)

print(f"Sr(a). {sobrenome}, o seu identificador é: {identificador}.")
print(f"Seu protocolo irá perder a validade em {validade} anos!")