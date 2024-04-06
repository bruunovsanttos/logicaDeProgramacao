#verificaão de batimentos cardiacos
#devese perguntar idade
#deve se perguntar numero de batimentos
#fazer calculo para o resultado final
idade = input("Qual sua idade?" )
batimentos = input("QUal a medição de batimentos?" )

if float(idade) <=2 and float(batimentos) <120 :
    print("Batimentos abaixo do normal.")
elif float(idade) <=2 and float(batimentos) <=140:
    print("Batimentos normais.")
elif float(idade) <=2 and float(batimentos) >140:
    print("Batimentos acima do normal, se estiver fazendo atividade fisica ok, caso não ir ao medico.")
elif float(idade) >=8 <=17 and float(batimentos) <=80:
    print("Batimentos abaixo do normal")
elif float(idade) >=8 <=17 and float(batimentos) <=100:
    print("Batimentos normais.")
elif float(idade) >=8 <=17 and float(batimentos) >100:
    print("Batimentos acima do normal, se estiver fazendo atividade fisica ok, caso não ir ao medico.")
elif float(idade) >=18 <59 and float(batimentos) <= 70:
    print("Batimentos abaixo do normal")
elif float(idade) >=18 <59 and float(batimentos) <= 80:
    print("Batimentos normais.")
elif float(idade) >=18 <59 and float(batimentos) > 80:
    print("Batimentos acima do normal, se estiver fazendo atividade fisica ok, caso não ir ao medico.")
elif float(idade) >=60 and float(batimentos) <=50:
    print("Batimentos abaixo do normal")
elif float(idade) >=60 and float(batimentos) <60:
    print("Batimentos normais.")
elif float(idade) >=60 and float(batimentos) >60:
    print("Batimentos acima do normal, se estiver fazendo atividade fisica ok, caso não ir ao medico.")