import random

def escolherPalavra(dificuldade, dicionario) :
    lista = dicionario[dificuldade]
    num = random.randint(0, len(lista) - 1)
    return lista[num]

def receberLetra() :
    while True :
        letra = input("\nInsira uma letra: ").upper()
        
        if len(letra) > 1 : continue
        else : return letra