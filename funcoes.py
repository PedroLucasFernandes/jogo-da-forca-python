import random

cor = ['\033[31m', '\033[32m', '\033[34m', '\033[33m', '\033[0m']
    #  vermelho     verde       azul       amarelo     fim

def escolherPalavra(dificuldade, dicionario) :

    if dificuldade == "HARDCORE" :

        categorias = ["Fruta", "Feriado", "Animal", "País", "Esporte"]
        tema = random.choice(categorias)
        lista = dicionario[tema]
        num = random.randint(0, len(lista) - 1)

        print(f'O tema da palavra é: {tema}!')

        return lista[num]
    
    else :
        lista = dicionario[dificuldade]
        num = random.randint(0, len(lista) - 1)
        return lista[num]

def removerAcentos(letra) :
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'â': 'a', 'ê': 'e', 'ô': 'o', 'à': 'a',
        'ã': 'a', 'õ': 'o',
        'ç': 'c'
    }
    
    for item in acentos.keys():
        
        if item.upper() == letra : letra = acentos[item].upper()
    
    return letra

def modoHardcore() :
    print(f'\nVocê jogará no modo: {cor[0]}HARDCORE!!!{cor[-1]}')
    print(f'Você só tem {cor[0]}UMA{cor[-1]} tentativa.')
    print("Iremos falar o tema da palavra para te dar uma mãozinha... Boa sorte!\n")

def receberLetra() :
    while True :
        letra = input("\nInsira uma letra: ").upper()

        if len(letra) > 1 : continue
        else : return letra

def letraCerta(palavra, letra, acertos) :
    for l in range(0, len(palavra)) :
        if letra == palavra[l] :
            acertos[l] = letra

def letraErrada(tentativas, palavraSecreta) :
    if tentativas == 0 :
        print(f"\n{cor[0]}Fim de jogo, suas tentativas acabaram.\n{cor[-1]}"
                f"A palavra correta era {palavraSecreta}\n")
    elif tentativas == 1 :
        print("Esta é a sua última tentativa!")
    else : 
        print(f"Você errou, restam {tentativas} tentativas")

def exibirPalavra(palavraSecreta, palavra, acertos) :
    aux = []    
    
    for i, letra in enumerate(palavra) :
        if letra == acertos[i] :
            aux.append(palavraSecreta[i])
        else :
            aux.append("_")
    
    print(aux)

def jogarNovamente() :
    print("\nDeseja jogar mais uma vez?")
    resposta = input(f'Digite "s" para {cor[1]}SIM{cor[-1]} ou qualquer outro valor para {cor[0]}NÃO{cor[-1]}:\n').lower()
    repita = True if resposta == "s" else False
    return repita