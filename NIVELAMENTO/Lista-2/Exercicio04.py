palavra = input("Digite uma palavra: ")

palavra_normalizada = palavra.lower()
if palavra_normalizada == palavra_normalizada[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")