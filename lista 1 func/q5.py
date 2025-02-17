
# Fatorial: Escreva uma função que calcule o fatorial de um número recebido como argumento.


def fatorial(n):
    if n < 0:
        return "fatorial não definido (número menor que 0)"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):  
            result *= i
        return result

num = int(input("Insira um número para o calculo fatorial: "))


print(f"O fatorial de {num} é: {fatorial(num)}")