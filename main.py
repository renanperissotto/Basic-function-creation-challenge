# Desafio 4: Crie uma função que receba uma lista de números como parâmetro e retorne o valor máximo e mínimo da lista.



def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [5,2,9,10,30,4,81,]

maximo, minimo = encontrar_maximo_minimo(numeros)
print("valor máximo é:", maximo)
print("valor mínimo é:", minimo)

