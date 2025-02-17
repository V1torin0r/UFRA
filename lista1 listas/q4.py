# Crie uma lista de números aleatórios e encontre o maior e o menor valor sem usar as funções max() e min().

lisa = [1, 2, 5, 8, 6, 9, 4, 3, 6, 4]

valoor = lisa [0]
valor = lisa [0]

for num in lisa:
    if num > valoor:
        valoor = num
    if num < valor:
        valor = num
        
print(f"A lista: {lisa}, tem por\nMaior Valor: {valoor}\nMenor Valor: {valor}")

