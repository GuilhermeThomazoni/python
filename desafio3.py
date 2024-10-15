#Escreva um programa em Python que apresente um menu com as seguintes opções:
#Validar número inteiro positivo
#Validar string não vazia
#Validar e-mailValidar data no formato DD/MM/AAAA
#Validar número dentro de um intervalo
#Validar CPF - Colocar 9 digito e descobrir o outros 2 verificaores
#Calcular soma de uma lista de números (interativa)
#Contar ocorrências de um caractere em uma string
#Converter temperatura de Celsius para Fahrenheit
#Encontrar o maior número em uma lista (interativa)
#Reverter uma stringCalcular fatorial de um número
#Sair do programa
#Cada opção deve chamar uma função correspondente que realiza a validação ou
#operação desejada. As funções devem ser definidas sem parâmetros e devem receber
#as entradas necessárias do usuário dentro delas. O programa deve limpar a tela após cada seleção de opção.

import re
from datetime import datetime
from os import *


def menu():
    while True:
        try:
            print("SEJA BEM-VINDO AO CAPS!")
            print("[0] - Sair do programa")
            print("[1] - Validar número inteiro positivo")
            print("[2] - Validar string não vazia")
            print("[3] - Validar e-mail")
            print("[4] - Validar data DD/MM/AAAA")
            print("[5] - Validar número dentro de um intervalo")
            print("[6] - Descobrir dois últimos dígitos do CPF")
            print("[7] - Calcular a soma de uma lista")
            print("[8] - Contar ocorrências de caractere")
            print("[9] - Converter Celsius para Fahrenheit")
            print("[10] - Encontrar o maior número da lista")
            print("[11] - Inverter texto")
            print("[12] - Calcular fatorial de um número")

            escolha = int(input("Selecione uma opção: "))
            return escolha
        except ValueError:
            print("Selecione uma opção válida. ")




def geral():
    while True:
        escolha = menu()
        if escolha == 1:
            valorpositivo = verifica_positivo()
            print(valorpositivo)


        elif escolha == 2:
                string = str(input("Insira um texto. Será verificado se está vazio: "))
                return string
                if len(string) == 0:
                    print("Lista vazia!")
                else:
                    print("Lista com conteúdo!")


        elif escolha == 3:
            email = verifica_email()
            print(email)


        elif escolha == 4:
            desgraca = valida_data()
            print(desgraca)


        elif escolha == 5:
            minimo = recebe_minintervalo()
            maximo = recebe_maxintervalo()
            valorInterv = recebe_valorintervalo()


            if valorInterv >= minimo & valorInterv <= maximo:
                print(f"O número {valorInterv} está DENTRO do intervalo {minimo} - {maximo}.")
            else:
                print(f"O número {valorInterv} está FORA do intervalo {minimo} - {maximo}.")


        elif escolha == 6:
            print(f"O primeiro dígito verificador do CPF é: {digito1}")
            print(f"O segundo dígito verificador do CPF é: {digito2}")


        elif escolha == 7:
            listaStr = recebe_lista()
            lista = listaStr.split(",")
            somaLista = somar_lista()
            print(f"A soma dos números da lista é {somaLista}.")


        elif escolha == 8:
            texto = texto_ocorrencia()
            caractere = char_ocorrencia()
            print(f"O caractere '{caractere}' aparece {texto.count(caractere)} vezes no texto.")


        elif escolha == 9:
            celsius = recebe_celsius()
            fahren = celsius_fahrenheit()
            print(f"A temperatura de {celsius}°C equivale a {fahren}°F.")


        elif escolha == 10:
            listaSexo = recebe_listamaior()
            lista2 = listaSexo.split(",")
            maiorLista = calcula_listamaior()
            print(f"O maior item da lista {lista2} é {maiorLista}.")


        elif escolha == 11:
            texto = recebe_textoinverter()
            print(' Você digitou: {}'.format(texto))
            string = texto[::-1]
            print('A frase que você digitou invertida fica: {}'.format(string))


        elif escolha == 12:
            numFator = recebe_fatorial()
            resuFator = calcula_fatorial()
            print(f"O fatorial de {numFator} é igual a {resuFator}.")


        elif escolha == 0:
            break






def recebe_positivo():
    numeroposi = int(input("Insira um número inteiro: "))
    return numeroposi


def verifica_positivo():
    numposi = recebe_positivo()
    if numposi > 0:
        print("O número", numposi, "é positivo!")
    elif numposi < 0:
        print("O número", numposi, "é negativo!")
    else:
        print("O número", numposi, "é neutro!")






def recebe_email():
    while True:
        try:
            email = str(input("Insira seu e-mail. Será verificado se o mesmo é válido: "))
            return email
        except ValueError:
            print("Informação inválida.")


def verifica_email():
    email = recebe_email()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        print("E-mail válido.")
    else:
        print("E-mail inválido.")






def recebe_data():
    while True:
        try:
            data = str(input("Insira uma data no formato DD/MM/AAAA. Será validado se a mesma confere com o formato: "))
            return data
        except ValueError:
            print("Informação inválida.")


def valida_data():
    data = recebe_data()
    try:
       datetime.strptime(data, "%D/%M/%Y")
       print(data)
    except ValueError:
        print("Formato incorreto, deve ser DD/MM/AAAA. ")






def recebe_lista():
    while True:
        try:
            return input("Digite uma lista de números separados por vírgula: ")
        except ValueError:
            print("Lista inválida.")





def somar_lista():
    soma = 0
    for item in lista:
        soma += int(item)
    return soma






def texto_ocorrencia():
    while True:
        try:
            textoContar = str(input("Digite um texto para contar a ocorrência de um caractere: "))
            return textoContar
        except ValueError:
            print("Informação inválida.")


def char_ocorrencia():
    while True:
        try:
            charContar = str(input("Digite o caractere cuja ocorrência será contada: "))
            return charContar
        except ValueError:
            print("Informação inválida.")






def recebe_celsius():
    while True:
        try:
            celsius = float(input("Insira a temperatura em Celsius. Será convertida para Fahrenheit: "))
            return celsius
        except ValueError:
            print("Insira uma entrada válida.")


def celsius_fahrenheit():
    celsius = recebe_celsius()
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit






def recebe_listamaior():
    while True:
        try:
            return input("Digite uma lista de números separados por vírgula ")
        except ValueError:
            print("Lista inválida.")



def calcula_listamaior():
    maior_lista = max(lista2)
    return maior_lista






def recebe_textoinverter():
    while True:
        try:
            textoprainv = str(input("Insira um texto. O mesmo será invertido: "))
            return textoprainv
        except ValueError:
            print("Insira um texto válido.")






def recebe_minintervalo():
    while True:
        try:
            minimo = int(input("Insira um número inteiro como valor mínimo do intervalo: "))
            return minimo
        except ValueError:
            print("Número inválido.")


def recebe_maxintervalo():
    while True:
        try:
            maximo = int(input("Insira um número inteiro como valor máximo do intervalo: "))
            return maximo
        except ValueError:
            print("Número inválido.")


def recebe_valorintervalo():
    while True:
        try:
            valorInterv = int(input("Insira um valor inteiro para calcular se está dentro do intervalo: "))
            return valorInterv
        except ValueError:
            print("Número inválido.")






def digite_os_primeiros9():
    while True:
        try:
            primeiros9 = int(input("Insira os primeiros 9 dígitos do seu CPF sem pontuação: "))
            if primeiros9(len = 9):
                return primeiros9
            else:
                print("Entrada inválida.")
        except ValueError:
            print("Entrada inválida.")


def calcular_digito(cpf, multiplicadores):
    soma = 0
    for i in range(len(cpf)):
        produto = int(cpf[i]) * multiplicadores[i]
        soma = soma + produto
    resto = soma % 11
    if resto < 2:
        return '0'  # Se o resto for menor que 2, retorna '0'
    else:
        return str(11 - resto)  # Caso contrário, retorna a diferença entre 11 e o resto, convertida para string

def validar_cpf():
    cpf = digite_os_primeiros9()
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 9 or not cpf.isdigit():  # Verifica se o CPF tem 9 dígitos e é composto apenas de números
        print("CPF inválido.")
        return

    lista10 = []
    for i in range(10, 1, -1):
        lista10.append(i)
    lista11 = []
    for i in range(11, 1, -1):
        lista11.append(i)

    digito1 = calcular_digito(cpf, lista10)
    digito2 = calcular_digito(cpf + digito1, lista11)


def recebe_fatorial():
    while True:
        try:
            numfatorial = int(input("Insira um número inteiro. Será calculado o fatorial do mesmo: "))
            return numfatorial
        except ValueError:
            print("Insira um número inteiro válido. ")

def calcula_fatorial():
    fatorial = recebe_fatorial()
    fator = 1
    for i in range(fatorial):
        fator = fator * (i+1)

geral()

