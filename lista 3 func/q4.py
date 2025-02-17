# Um cliente recebe um desconto de X% em uma compra caso o valor total seja superior a R$ 500,00.
# Escreva uma função em Python que recebe o valor da compra e o percentual de desconto e retorna o valor final a pagar.

def compra(val, desc):
                
    val = float(input("diga qual o valor total da sua compra:\n"))
    
    if val < 500:
        print ("Com esse valor não podemos lhe dar desconto")
    
    elif val >= 500 and val <= 1000:
        desc = 0.1
        print ("Parabéns, você ganhou um descomto de 10% na compra")
        
    elif val > 1000:
        desc = 0.2
        print("Parabéns, você ganhou um desconto de 20% na compra")
        
    res = val - (val*desc)
    
    return res

valor = compra(val= True, desc=True)
print ("valor com desconto: ", valor)