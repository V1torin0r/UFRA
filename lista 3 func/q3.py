# Um motorista deseja calcular o tempo necessário para viajar uma distância D a uma velocidade V constante.
# Escreva uma função em Python que recebe a distância e a velocidade e retorna o tempo necessário (em horas).

def tempo(velocidade, distancia):
    velocidade = float(input("Insira a velocidade em km/h\n"))
    distancia = float(input("Insira a sua distância em km\n"))   
    tmp = distancia/velocidade
    
    return tmp

tmpo = tempo(velocidade=True, distancia= True)
print (f"o tempo de percurso é de: {tmpo} Horas")