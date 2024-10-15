from datetime import date, timedelta #bibliotecas necessárias para lidar com datas

def calcula_idade(data_nascimento): # função que calcula a idade do usuário
    hoje = date.today() #define a variável hoje com a data atual
    idade = hoje - data_nascimento #define a variável idade com a data de hoje menos a data de nascimento

    anos = idade.days // 365  #define anos como 365 dias dentro da variável de idade
    idade -= timedelta(days=anos * 365) #cálculo matemático que mexe com a variação de data, onde os dias de x anos são x vezes 365

    meses = idade.days // 30 #define que o mês possui 30 dias
    idade -= timedelta(days=meses * 30) #define que os dias de x meses são x vezes 30

    dias = idade.days #dias são dias (risos)

    return anos, meses, dias #retorna as três variáveis, agora com parâmetro de idade

# Entrada do usuário
ano_nascimento = int(input("Digite o ano de nascimento: ")) #pede o ano de nascimento
mes_nascimento = int(input("Digite o mês de nascimento: ")) #pede o mês de nascimento
dia_nascimento = int(input("Digite o dia de nascimento: ")) #pede o dia de nascimento

# Cria a data de nascimento
data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)

# Calcula a idade
anos, meses, dias = calcula_idade(data_nascimento)

# Exibe a idade
print(f"Sua idade é {anos} anos, {meses} meses e {dias} dias.")


