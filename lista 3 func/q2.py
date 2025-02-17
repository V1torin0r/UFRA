# Um banco analisa a solicitação de crédito de um cliente. Para ser aprovado, ele deve ter uma renda mensal de pelo menos R$ 2000,00 e não ter mais de R$ 5000,00 em dívidas.
# Escreva uma função em Python que recebe a renda mensal e o valor da dívida e retorna se o crédito foi aprovado ou não.


def cred(renda, divida):
    renda = float(input("digite sua renda mensal:\n"))
    divida = float(input("Digite o valor da sua dívida:\n"))
    
    if renda >= 2000 and divida <= 5000:
        print("Seu crédito foi aprovado, parabéns")
        
    else:
        print("Seu crédito não foi aprovado!")
        
cred(renda=True, divida=True)