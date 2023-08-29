import random

def escolherPalavra(dificuldade, dicionario) :
    lista = dicionario[dificuldade]
    num = random.randint(0, len(lista) - 1)
    return lista[num]