# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);



# Ao final do processamento, qual será o valor da variável SOMA?
def soma():
    i = 13; soma = 0; k = 0

    while (k<i):
        k = k+1
        soma = soma + k

    print(soma)

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci():

    userInput = int(input("Insert a number to check if it belongs to the Fibonacci sequence: "))

    fibo = 0
    aux = 1


    if userInput == 1 or userInput == 0:
        print(f"The number {userInput} belongs to the Fibonacci sequence")

    else:
        while fibo < userInput:
           print(fibo)

           prox = fibo + aux
           fibo = aux
           aux = prox
    
    if fibo == userInput:
        print(f"{userInput} belongs to the sequence")

    else:
        print(f"{userInput} {fibo} doesn't belong to the sequence")

# 3) Descubra a lógica e complete o próximo elemento:



# a) 1, 3, 5, 7, _9__

# b) 2, 4, 8, 16, 32, 64, __128__

# c) 0, 1, 4, 9, 16, 25, 36, __48__

# d) 4, 16, 36, 64, __100__

# e) 1, 1, 2, 3, 5, 8, __13__

# f) 2,10, 12, 16, 17, 18, 19, __20__
        


# 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

# R: Primeiro eu ligaria um interruptor (a) e a manteria acesa tempo o suficiente para esquentar a lampada. Logo em seguida
# eu desligaria esse interruptor e manteria um outro (b) ligado. Então eu iria checar a primeira sala. Caso essa lampada esteja quente, 
# ela é ativada pelo interruptor a, se estiver acesa, é interruptor b, se nenhuma das duas, então é c. Vamos dizer que ela esta apagada e quente
# então foi ativada por a. Logo, eu iria para a outra sala. Se a lampada está acesa, ela é ativada por b, se estiver apagada, é ativada por c. 
# Essa é a lógica que eu usaria para resolver essa situação.
        

# 5) Escreva um programa que inverta os caracteres de um string.


# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;
        
def revertString():
    stringInput = input("Enter a word:\n")
    length = len(stringInput) - 1
    auxWord = ''
    
    while length >= 0:
       auxWord += stringInput[length] 
       length -= 1
    
    print(auxWord)

revertString()
