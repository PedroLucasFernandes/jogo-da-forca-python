import json
import funcoes

repita = True

while repita :

    with open("palavras.json", "r", encoding="utf-8") as json_file :
        dicionario = json.load(json_file)

    valido = True
    tentativas = 6
    acertos = []

    dificuldade = input('Em qual dificuldade você quer jogar?\n'
                        'Digite "1" para infantil\n'
                        'Digite "2" para fácil\n'
                        'Digite "3" para difícil\n'
                        'Digite "4" para inglês (básico)\n')

    match dificuldade : 
        
        case "1" : dificuldade = "infantil"
        
        case "2" : dificuldade = "fácil"
        
        case "3" : dificuldade = "difícil"

        case "4" : dificuldade = "inglês"

        case _:
            print("Valor inválido, insira um número correspondente: ")
            valido = False

    while valido :
            
        print(f'Você jogará no modo: {dificuldade}\n')
        palavra = funcoes.escolherPalavra(dificuldade, dicionario).upper()

        for letra in range(0, len(palavra)) :
            acertos.append("_")
            print(acertos[letra], end = " ")

        while tentativas > 0 :
            letra = funcoes.receberLetra()
            
            if letra in palavra :
                for l in range(0, len(palavra)) :
                    if letra == palavra[l] :
                        acertos[l] = letra
            else :
                tentativas -= 1

                if tentativas == 0 :
                    print("Fim de jogo, suas tentativas acabaram.\n"
                          f"A palavra correta era {palavra}")
                elif tentativas == 1 :
                    print("Esta é a sua última tentativa!")
                else : 
                    print(f"Você errou, restam {tentativas} tentativas")

            if "".join(acertos) == palavra :
                print("\nParabéns! Você venceu o jogo!\n")
                print(acertos)
                break    
            print(acertos)
        
        valido = False
        print("Deseja jogar mais uma vez?")
        resposta = input('Digite "s" para SIM ou qualquer outro valor para NÃO:\n').lower()
        repita = True if resposta == "s" else False

print("Obrigado por jogar, até mais!")