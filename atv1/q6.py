print("qual operação você deseja fazer?\n")
n1 = float(input("primeiro diga qual o primeiro número\n"))
n2 = float(input("agora diga qual o segundo número\n"))
choice = int(input("\n1.soma\n2.subtração\n3.multiplicação\n4.divisão\n"))

if choice == 1:
    print ("sua escolha foi soma, então o resultado da operação relacionada com os números supracitados é: ", n1+n2)

elif choice == 2:
    print ("sua escolha foi subtração, então o resultado da operação relacionada com os números supracitados é: ", n1-n2)

elif choice == 3:
    print ("sua escolha foi multiplicação, então o resultado da operação relacionada com os números supracitados é: ", n1*n2)

elif choice == 4:
    print ("sua escolha foi divisão, então o resultado da operação relacionada com os números supracitados é: ", n1/n2)