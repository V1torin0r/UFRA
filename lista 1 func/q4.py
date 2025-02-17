#  Crie uma função que use uma variável global para acumular o resultado de diversas somas (quantas você desejar).

counter = 0

def somar(val):
    global counter  
    counter += val
    return counter

somar(5)
somar(3)
somar(6)
somar(7)
somar(12)


print("Resultado acumulado:", counter)  