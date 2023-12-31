import json
import funcoes
import os

repita = True

while repita :

    with open("palavras.json", "r", encoding="utf-8") as json_file :
        dicionario = json.load(json_file)

    valido = True
    tentativas = 6
    acertos = []

    os.system("cls")

    dificuldade = input('Em qual dificuldade você quer jogar?\n'
                        'Digite "1" para infantil\n'
                        'Digite "2" para fácil\n'
                        'Digite "3" para difícil\n'
                        'Digite "4" para HARDCORE (apenas UMA tentativa)\n'
                        'Digite "5" para inglês (básico)\n')

    match dificuldade : 
        
        case "1" : dificuldade = "infantil"
        
        case "2" : dificuldade = "fácil"
        
        case "3" : dificuldade = "difícil"

        case "4" : dificuldade = "HARDCORE"

        case "5" : dificuldade = "inglês"

        case _:
            print(f"\n{funcoes.cor[0]}Valor inválido, insira um número correspondente: {funcoes.cor[-1]}")
            valido = False

    while valido :

        if dificuldade == "HARDCORE" :
            funcoes.modoHardcore()
            tentativas = 1
        
        else :
            print(f'Você jogará no modo: {dificuldade}\n')

        palavraSecreta = funcoes.escolherPalavra(dificuldade, dicionario).upper()
        palavra = list(map(funcoes.removerAcentos, palavraSecreta))
        
        for letra in range(0, len(palavra)) :
            acertos.append("_")
            print(acertos[letra], end = " ")

        while tentativas > 0 :
            letra = funcoes.removerAcentos(funcoes.receberLetra())
            
            if letra in palavra :
               funcoes.letraCerta(palavra, letra, acertos)

            else :
                tentativas -= 1
                funcoes.letraErrada(tentativas, palavraSecreta)
            
            if acertos == palavra :
                print(f"{funcoes.cor[1]}\nParabéns! Você venceu o jogo!\n{funcoes.cor[-1]}")
                print(acertos)
                break    
            funcoes.exibirPalavra(palavraSecreta, palavra, acertos)
        
        valido = False
        repita = funcoes.jogarNovamente()

print("Obrigado por jogar, até mais!")