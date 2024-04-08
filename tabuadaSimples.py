#i quer dizer iteração ou seja, a quantidade de voltas que o programa da
#então sempre que aparecer i sera uma volta que o programa dei no while
i = 1
numero = int(input("Digite um numero de tabuada"))

while i <= 10:
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    i = i + 1