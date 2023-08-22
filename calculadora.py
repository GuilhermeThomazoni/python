import time

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

def fatorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def elevacao(base, expoente):
    return base ** expoente

def raiz(numero, indice):
    return numero ** (1 / indice)

def porcentagem(valor, percentual):
    return (valor * percentual) / 100

def logaritmo(numero, base):
    result = 0
    while numero >= base:
        result += 1
        numero /= base
    return result

# Constantes
constante_pi = 3.141592653589793
constante_euler = 2.718281828459045


while True:
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Fatorial")
    print("6. Elevação")
    print("7. Raiz")
    print("8. Porcentagem")
    print("9. Logaritmo")
    print("10. Constante Pi")
    print("11. Constante Euler")
    print("0. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '0':
        print("Encerrando a calculadora.")
        break
    elif escolha in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num1 = float(input("Digite o primeiro número: "))

        if escolha in ['1', '2', '3', '4', '6', '7', '8', '9']:
            num2 = float(input("Digite o segundo número: "))
    elif escolha == '10' or escolha == '11':
        if escolha == '10':
            print("Valor de Pi:", constante_pi)
        else:
            print("Valor de Euler:", constante_euler)
        continue
    else:
        print("Escolha inválida. Por favor, escolha uma operação válida.")
        continue

    if escolha == '1':
        print("Resultado:", soma(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado:", divisao(num1, num2))
    elif escolha == '5':
        print("Resultado:", fatorial(int(num1)))
    elif escolha == '6':
        print("Resultado:", elevacao(num1, num2))
    elif escolha == '7':
        print("Resultado:", raiz(num1, num2))
    elif escolha == '8':
        print("Resultado:", porcentagem(num1, num2))
    elif escolha == '9':
        print("Resultado:", logaritmo(num1, num2))

        time.sleep(3)