print("Bom dia dr sonic, hoje iremos solicitar a quilometragem do seu percurso")
inp = int(input("Por favor, insira quantos quilômetros você percorrerá\n"))

if inp <= 200:
    print("Ok seu percurso será de:", inp, "km, e o valor a ser pagado é de: R$", inp*1.5)

elif inp > 200:
    print("Ok seu percurso será de:", inp, "km, e o valor a ser pagado é de: R$", inp)