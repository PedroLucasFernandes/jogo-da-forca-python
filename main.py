repita = True
while repita :
    palavra = list(input("Insira a palavra secreta: ").upper());
    vidas = 5;

    for letra in palavra :
        print("_", end = " ");

    while vidas > 0 :
        print("");
        letra = input("Insira uma letra: ").upper();
        if letra in palavra :
            print("Parabéns, você acertou uma letra");    
        else :
            vidas -= 1;
            print(f"Você errou, restam {vidas} vidas");

    print("Game Over!");
    print("Deseja jogar mais uma vez?");
    resposta = input('Digite "s" para SIM ou qualquer outro valor para NÃO: ');
    repita = False if resposta != "s" else True;

print("Obrigado por jogar, até mais!");