import random

cor = ['\033[31m', '\033[32m', '\033[34m', '\033[33m', '\033[0m']
    #  vermelho     verde       azul       amarelo     fim

def escolherPalavra(dificuldade, dicionario) :
    lista = dicionario[dificuldade]
    num = random.randint(0, len(lista) - 1)
    return lista[num]

def receberLetra() :
    while True :
        letra = input("\nInsira uma letra: ").upper()

        if len(letra) > 1 : continue
        else : return letra

def letraCerta(palavra, letra, acertos) :
    for l in range(0, len(palavra)) :
        if letra == palavra[l] :
            acertos[l] = letra

def letraErrada(tentativas, palavra) :
    if tentativas == 0 :
        print(f"\n{cor[0]}Fim de jogo, suas tentativas acabaram.\n{cor[-1]}"
                f"A palavra correta era {palavra}\n")
    elif tentativas == 1 :
        print("Esta é a sua última tentativa!")
    else : 
        print(f"Você errou, restam {tentativas} tentativas")

def jogarNovamente() :
    print("\nDeseja jogar mais uma vez?")
    resposta = input(f'Digite "s" para {cor[1]}SIM{cor[-1]} ou qualquer outro valor para {cor[0]}NÃO{cor[-1]}:\n').lower()
    repita = True if resposta == "s" else False
    return repita