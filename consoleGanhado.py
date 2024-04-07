#5 colaboradores ganharam 1 console
#os consoles são olaystation, xbox, nintendo
#o programa precisa mostrar os votos de cada um dos cinco membors
#e no final exibir o console escohido e com quantos votos

print("Ganhando um console")

colaborador1 = input("Qual console você prefere? 1- Playstation 2-XBOX 3-Nintendo Switch")
colaborador2 = input("Qual console você prefere? 1- Playstation 2-XBOX 3-Nintendo Switch")
colaborador3 = input("Qual console você prefere? 1- Playstation 2-XBOX 3-Nintendo Switch")
colaborador4 = input("Qual console você prefere? 1- Playstation 2-XBOX 3-Nintendo Switch")
colaborador5 = input("Qual console você prefere? 1- Playstation 2-XBOX 3-Nintendo Switch")

playstation = 0
xbox = 0
nintendo = 0

if int(colaborador1) == 1:
    playstation = playstation + 1
elif int(colaborador1) == 2:
    xbox = xbox + 1
elif int(colaborador1) == 3:
    nintendo = nintendo + 1

if int(colaborador2) == 1:
    playstation = playstation + 1
elif int(colaborador2) == 2:
    xbox = xbox + 1
elif int(colaborador2) == 3:
    nintendo = nintendo + 1

if int(colaborador3) == 1:
    playstation = playstation + 1
elif int(colaborador3) == 2:
    xbox = xbox + 1
elif int(colaborador3) == 3:
    nintendo = nintendo + 1

if int(colaborador4) == 1:
    playstation = playstation + 1
elif int(colaborador4) == 2:
    xbox = xbox + 1
elif int(colaborador4) == 3:
    nintendo = nintendo + 1

if int(colaborador5) == 1:
    playstation = playstation + 1
elif int(colaborador5) == 2:
    xbox = xbox + 1
elif int(colaborador5) == 3:
    nintendo = nintendo + 1

print("\nA votação terminou assim: \n Playstation: {} \n XBOX: {} \n Nintendo: {}".format(playstation, xbox, nintendo))


if playstation > xbox and playstation > nintendo:
    print("\nO console escolhido foi o Plastation")
elif xbox > playstation and xbox > nintendo:
    print("\nO console escolhido foi o XBOX")
elif nintendo > playstation and nintendo > xbox :
    print("\nO console escolhido foi o Nintendo Switch")
else:
    print("\nHouve empate na esolha, conversar entre si para uma escolha melhor para todos.")