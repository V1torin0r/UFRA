# Dada uma lista com números repetidos, crie uma nova lista sem valores duplicados, preservando a ordem dos elementos
numeross = [3, 5, 7, 7, 2, 8, 9, 4]

numeros_s = []

for num in numeross:
    if num not in numeros_s:
        numeros_s.append(num)
        
        
print(numeros_s)