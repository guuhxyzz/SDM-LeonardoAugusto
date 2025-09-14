frase = input("Digite uma frase: ")

qtd_caracteres = len(frase)

vogais = "aeiouAEIOU"
qtd_vogais = sum(1 for c in frase if c in vogais)

percentual_vogais = (qtd_vogais / qtd_caracteres) * 100 if qtd_caracteres > 0 else 0

palavras = frase.split()
qtd_palavras = len(palavras)

media_caracteres = qtd_caracteres / qtd_palavras if qtd_palavras > 0 else 0

print(f"Quantidade de caracteres : {qtd_caracteres}")
print(f"percentual de vogais {percentual_vogais:.2f} %")
print(f"sua frase contém: {qtd_palavras} palavras.")
print(f"em média temos {media_caracteres:.2f} caracteres por palavra")