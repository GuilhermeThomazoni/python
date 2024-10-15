#Desafio vocês a desenvolverem um programa que inclua as seguintes funcionalidades:

#Verificação de paridade: O programa deve permitir que o usuário forneça uma lista de números e, em seguida, verificar se cada número é par ou ímpar.
#Cálculo da soma: O programa deve solicitar ao usuário uma quantidade específica de números e calcular a soma desses números.
#Verificação de números primos: Permita que o usuário insira um número e, em seguida, verifique se é primo ou não.
#Contagem de vogais: Peça ao usuário que digite uma palavra e conte quantas vogais ela possui.
#Garanta que o programa seja interativo, solicitando entrada do usuário conforme necessário. Além disso, vocês devem incluir pelo menos 4 loops for e 4 condicionais if relevantes para as tarefas das funções.
#As entradas devem ser validadas e todo código devve ser comentado





def retorna_opcao():
    while True:
        try:
            print("BEM-VINDO AO PROGRAMA DOS CARA!")
            print("[1] - Verificação de Paridade")
            print("[2] - Cálculo de Soma")
            print("[3] - Verificação de Primos")
            print("[4] - Contagem de Vogais")
            opcao = int(input("Insira sua opção: "))
            return opcao
        except ValueError:
            print("Insira uma opção válida. ")


def verifica_par():
    while True:
        try:
            numero = int(input("Insira um número inteiro. Será verificado se o mesmo é par: "))
            if numero % 2 == 0:
                print("O número é par. ")
            else:
                print("O número é ímpar. ")
            return numero
        except ValueError:
            print("Insira um número válido. ")
   
def soma():
    while True:
        try:
            num1 = int(input("Insira o primeiro valor inteiro da soma: "))
            num2 = int(input("Insira o segundo valor inteiro da soma: "))
            soma = num1 + num2
            print("O resultado da soma é: ", soma)
            return soma
        except ValueError:
            print("Insira valores válidos. ")


def verifica_primo():
    while True:
        try:
           
            #Não achei nenhum meio de fazer essa função sem que virasse uma bomba relógio!
       
        except ValueError:
            print("Insira um número inteiro válido. ")


def conta_vogal():
    while True:
        try:
            numvogais = 0
            texto = str(input("Insira um texto. Serão contadas as vogais. "))
            vogais = ["a", "e", "i", "o", "u"]
            for letra in texto:
                for vogal in vogais:
                    if letra == vogal:
                        numvogais = numvogais + 1
            return numvogais      
        except ValueError:
            print("Insira um texto válido. ")


opcao = retorna_opcao()


if opcao == 1:
    numero_par = verifica_par()
    print(numero_par)


elif opcao == 2:
   res_soma = soma()


elif opcao == 3:
    numero_primo = verifica_primo()
    print(numero_primo)


elif opcao == 4:
    numvogais = conta_vogal()
    print(numvogais)



