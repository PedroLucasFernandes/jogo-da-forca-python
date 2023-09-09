# Jogo da Forca programado em Python
Jogo da Forca para se divertir em quatro modos diferentes.

***

## Autor
Pedro Lucas Fernandes Ferreira

## Proposta
Programar um Jogo da Forca funcional e intuitivo, com o objetivo educativo de colocar em prática meus conhecimentos de Programação em Python.

## Como utilizar o sistema
Abra o terminal na pasta onde os arquivos se encontram e utilize o comando ``python main.py``. Após isso a aplicação já estará em funcionamento.

Com isso, uma série de dificuldades aparecerão na tela, digite o número correspondente para selecionar o modo desejado. Confira abaixo:
- 'Digite "1" para infantil'
- 'Digite "2" para fácil'
- 'Digite "3" para difícil'
- 'Digite "4" para inglês (básico)'

Caso a sua resposta não seja nenhum dos números previstos, uma mensagem de valor inválido aparecerá, junto das instruções novamente. <br>
![Exemplo de valor inválido](https://i.imgur.com/yStVuDV.png)

Após inserir um valor válido, o programa irá imprimir um "_" para cada letra presente na palavra, e logo te pedirá para inserir uma letra.

Confira como a aplicação retorna o seu resultado parcial, baseado nas suas tentativas:
![Exemplo de uma partida em andamento](https://i.imgur.com/YEtMJhP.png)

Ao fim da partida, o jogo te mostra uma mensagem de Parabéns, em caso de vitória. Se você perder a partida, aparecerá uma mensagem de Fim de Jogo, informando que suas tentativas acabaram, também será informado qual era a palavra correta. 

Independente do seu resultado, temos a pergunta para jogar novamente, responda conforme a instrução abaixo para voltar ao menu de seleção de modo ou finalizar o programa.
- Deseja jogar mais uma vez?
- Digite "s" para SIM ou qualquer outro valor para NÃO.

Também colori palavras/frases em alguns prints para uma melhor qualidade e ilustração no jogo.
![exemplo de partida vencida](https://i.imgur.com/jgRC5LF.png)

## Como foi desenvolvido
Utilizei o Python como principal linguagem para o projeto, por meio do editor de código Visual Studio Code.

Arquivos necessários para o desenvolvimento do programa:
```bash
funcoes.py
main.py
palavras.json
```

O ``main.py`` é responsável pela execução do programa, e ``funcoes.py`` armazena as funções para uma melhor organização e otimização do código.

``palavras.json`` é o arquivo que contém o nosso dicionário, com todas as palavras possíveis para a partida, basicamente o dicionário é feito utilizando quatro keys, onde cada uma representa um modo de jogo (infantil, fácil, difícil, inglês), inseri uma lista de palavras para ser o valor de cada key.

### Explicando as funções
Até então existem sete funções para ajudar no processamento do jogo, e elas contêm um nome bem autoexplicativo para facilitar o entendimento. ``escolherPalavra(dificuldade, dicionario)`` irá acessar o dicionário em ``palavras.json`` e acessa a key correspondente a dificuldade fornecida pelo usuário, depois seleciona uma palavra aleatória que representa aquele modo.

Para desconsiderar acentos utilizamos ``removerAcentos(letra)``. Por exemplo, se a palavra secreta for "ÓCULOS" e o jogador inserir a letra "O", o programa naturalmente não iria reconhecer o "Ó", dificultando na adivinhação e tornando a partida inviável, por isso utilizamos essa função.

``receberLetra()``, ``letraCerta(palavra, letra, acertos)`` e ``letraErrada(tentativas, palavraSecreta)`` são responsáveis pelo recebimento da tentativa do usuário e por todo o processamento. Faz parte do processamento: a verificação da letra inserida pelo jogador e a resposta do programa conforme o resultado, indicando se ele acertou ou não essa letra, e claro, retirando uma tentativa (vida) em caso de erro.

Depois de todo esse processamento, ``exibirPalavra(palavraSecreta, palavra, acertos)`` irá printar os acertos atualizados a cada palpite do usuário. Ela leva duas palavras como parâmetro pois usa a palavra sem acentos (utilizando ``removerAcentos(letra)``) para a comparação, e depois printa a palavra com acento.

Por fim, ``jogarNovamente()`` será executado ao final de cada partida, perguntando ao usuário se ele pretende jogar mais uma vez, em caso de afirmação, o programa retorna ao menu inicial para que possa ser selecionado um modo, não será obrigatório repitir a dificuldade jogada anteriormente. Em caso de negação, o aplicativo será finalizado com a frase "Obrigado por jogar, até mais!.