#para faer tabuada usando o for deve se criar uma variavel para entrada
#usando o for ficaria mais ou menos (numero da tabuada, numero da tabuada * 10 + 1 pois se colocar 10 vai ate nove,
#somando numero da tabuada ao numero da tabuada inicial)

n = int(input("Informe a tauada desejada ..."))
for contadora in range(n, n * 10 + 1, n):
    print (contadora)