# Um produto comprado pelo valor X é vendido por Y% do valor de compra. Escreva uma função em Python que recebe o valor de compra e a porcentagem de lucro e retorna o valor de venda.

def valor(comp, perc):
    
    perc = float(input("insira a porcentagem:\n1. 10%\n2. 20%\n"))
         
    if perc == 1:
        perc = 0.10
        
    elif perc == 2:
        perc = 0.20
    
    venda = comp + (comp*perc)

    return venda
        
        
print (valor(10, perc= True))