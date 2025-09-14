entrada = input("Digite uma lista de números inteiros separados por espaço: ")

numeros = list(map(int, entrada.split()))
numeros_unicos = sorted(set(numeros))

print(numeros_unicos)