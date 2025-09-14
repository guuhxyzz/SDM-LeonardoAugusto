texto = input("Digite uma palavra ou frase: ")
resultado = ""

for char in texto:
    if 'a' <= char <= 'z':
        resultado += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        resultado += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
    else:
        resultado += char

print(resultado)