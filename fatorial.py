def fatorial(x):
    aux = 1
    while x > 0:
        aux = aux*x
        x=x-1
    return aux
    
print(fatorial(2))