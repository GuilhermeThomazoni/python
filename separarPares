def limit(): #Criação da função que define o número mais alto da lista
    while True: #Enquanto a função for verdadeira:
        try: #Tente:
            num = int(input("Digite um número inteiro limite para a lista: ")) #Cria-se a variável num, que recebe o número inserido pelo usuário.
            return num #Retorna a variável com o valor fornecido
        except ValueError: #Exceção para erro:
            print("Insira um número inteiro válido. ") #Imprime a mensagem de erro.

def listas(numero): #Criação da função que cria as listas.
    numeros_inferiores = [] #Lista dos inferiores
    numeros_pares = [] #Lista dos pares
    numeros_impares = [] #lista dos ímpares

    for aux in range(numero + 1): #Para a variável auxiliar no range da variável recebida em limit, somando 1 para que o número limite seja considerado
        numeros_inferiores.append(aux) #Append para que os números sejam adicionados à lista

        if aux % 2 == 0: #Se for par:
            numeros_pares.append(aux) #Adiciona à lista dos pares
        else: #Senão, é ímpar:
            numeros_impares.append(aux) #Adiciona à lista dos ímpares

    return numeros_inferiores, numeros_pares, numeros_impares #Retorna as variáveis

def imprimir(numeros_inferiores, numeros_pares, numeros_impares): #função para imprimir todas as listas
    print("Números inferiores: ", numeros_inferiores) #imprime os inferiores
    print("Números pares: ", numeros_pares) #imprime os pares
    print("Números ímpares: ", numeros_impares) #imprime o ímpares

numero = limit() #a variável recebe a função do número limite
numeros_inferiores, numeros_pares, numeros_impares = listas(numero) #as listas recebem a função que lhes dá o valor
imprimir(numeros_inferiores, numeros_pares, numeros_impares) #a função que imprime recebe as listas
