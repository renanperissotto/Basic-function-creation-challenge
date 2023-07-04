
def destacar_maior_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for palavra in lista:
        if len(palavra)> len(maior):
            maior = palavra
        if len(palavra) < len(menor):
            menor = palavra
        
    return maior, menor

palavras = ['renan', 'café', 'paralelepipedo', 'anarquia']
maior, menor = destacar_maior_menor(palavras)
print('A maior palavra é:', maior)
print('A menor palavra é:', menor)