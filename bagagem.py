cliente = input("Possui vippass?")
if cliente == str("sim") :
    peso = input("Qual o peso da sua bagagem?")
    if int(peso) <=32:
        print("Bagagem permitida")
    else: print("Bagagem não permitida, favor dirigir-se ao guiche de embarque...")
else:
    peso = input("Qual o peso da sua bagagem?")

    if int(peso) <= 25:
        print("Bagagem permitida")
    else :
        print("Bagagem não permitida, favor dirigir-se ao guiche de embarque...")
