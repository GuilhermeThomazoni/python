#Escreva um programa em Python que atenda às seguintes especificações:O programa deve conter funções para:
#Verificar se uma palavra é um palíndromo.(Palavra perguntada ao usuário)
#Verificar se um número é primo.
#Calcular o fatorial de um número.
#Calcular a raiz quadrada de um número.
#O programa deve interagir com o usuário para:
#Solicitar e verificar a idade do usuário, informando se ele é maior ou menor de idade.
#Solicitar um número inteiro para calcular seu fatorial.
#Solicitar um número para verificar se é primo.
#Solicitar uma palavra para verificar se é um palíndromo.
#Além disso, o programa deve incluir um loop que acumula a soma dos números de 1 a 5.




import math


def retorna_opcao():
    while True:
        try:
            print("Seja bem-vindo à terra do sexo!")
            print("[1] - Verificação de idade")
            print("[2] - Verificação de palíndromo")
            print("[3] - Verificação de número primo")
            print("[4] - Cálculo de fatorial")
            print("[5] - Cálculo de raiz")
            print("[6] - Encerrar programa")

            opcao = int(input("Insira sua opção: "))
            return opcao
        except ValueError:
            print("Insira uma opção válida. ")


def obter_pali():
    while True:
        try:
            pali = str(input("Insira uma palavra. Será verificado se a mesma é um palíndromo: "))
            return pali
        except ValueError:
            print("Por favor, insira uma palavra válida. ")


def verificar_pali():
    palavra = obter_pali()
    palavra = palavra.lower()
    palavra = palavra.replace(" ", "")
    palavra_inversa = palavra[::-1]
    if palavra_inversa == palavra:
        print("A palavra inserida é um palíndromo. ")
    else:
        print("A palavra inserida não é um palíndromo. ")






def obter_primo():
    while True:
        try:
            primo = int(input("Insira um número inteiro. Será verificado se o mesmo é primo: "))
            return primo
        except ValueError:
            print("Insira um número inteiro válido. ")




def verificar_primo():
    num = obter_primo()
    if num == 1:
        print(num, " é um número primo.")
    elif num < 1:
        print(num, " não é um número primo. ")
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print(num, " não é um número primo. ")
                break
            else:
                print(num, " não é um número primo. ")


def receber_fatorial():
    while True:
        try:
            numfatorial = int(input("Insira um número inteiro. Será calculado o fatorial do mesmo: "))
            return numfatorial
        except ValueError:
            print("Insira um número inteiro válido. ")


def calcular_fatorial():
    fatorial = receber_fatorial()
    fator = 1
    for i in range(fatorial):
        fator = fator * (i+1)


    print(fator, " é o resultado do fatorial do número ", fatorial)




def receber_raiz():
    while True:
        try:
            raiz = int(input("Insira um número inteiro. Será calculada a raiz quadrada do mesmo: "))
            return raiz
        except ValueError:
            print("Insira um número válido. ")


def calcular_raiz():
    numraiz = receber_raiz()
    raizqd = math.sqrt(numraiz)
    print("A raiz quadrada de ", numraiz, "é igual a", raizqd)




def receber_idade():
    while True:
        try:
            idade = int(input("Insira sua idade. Será calculado se você é maior de idade: "))
            return idade
        except ValueError:
            print("Insira uma idade válida. ")


def calcular_idade():
    numidade = receber_idade()
    if numidade < 0:
        print("Idade inválida. ")
    elif numidade < 18:
        print("Você é menor de idade.")
    else:
        print("Você é maior de idade. ")




opcao = retorna_opcao()


def geral():
    while True:
        if opcao == 1:
            age = calcular_idade()
            print(age)
        elif opcao == 2:
            pali = verificar_pali()
            print(pali)
        elif opcao == 3:
            cousin = verificar_primo()
            print(cousin)
        elif opcao == 4:
            factorial = calcular_fatorial()
            print(factorial)
        elif opcao == 5:
            source = calcular_raiz()
            print(source)
        elif opcao == 6:
            print("Encerrando programa.")
            break


