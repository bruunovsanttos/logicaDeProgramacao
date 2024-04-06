#pedir valor bruto da compra
#colocar desconto no valor total da compra
#os descontos são dados conforme a quantiade e clase escolhida


valorBruto = int(input("Qual o valor total da sua compra?"))
categoria = int(input("Em qual classe você deseja viajar? Economica=1 Executiva=2 Primeira Classe=3"))
qtdViajantes = int(input("Quantas pessoas ? "))
valorDesconto = 0

if categoria == 1:
    if qtdViajantes ==2:
        valorDesconto = valorBruto * 0.03
    elif qtdViajantes == 3:
        valorDesconto = valorBruto * 0.04
    elif qtdViajantes >= 4:
        valorDesconto = valorBruto * 0.05
elif categoria == 2:
    if qtdViajantes ==2:
        valorDesconto = valorBruto * 0.05
    elif qtdViajantes == 3:
        valorDesconto = valorBruto * 0.07
    elif qtdViajantes >= 4:
        valorDesconto = valorBruto * 0.08
elif categoria == 3:
    if qtdViajantes ==2:
        valorDesconto = valorBruto * 0.10
    elif qtdViajantes == 3:
        valorDesconto = valorBruto * 0.15
    elif qtdViajantes >= 4:
        valorDesconto = valorBruto * 0.20

valorLiquido = valorBruto - valorDesconto
mediaViajante= valorBruto / qtdViajantes

print("O valor da sua viagem é de R${}, com desconto no valor de R${}, e o valor final da sua viagem "
      "com desconto é de R${}, e a media de valor pago por viajante e de R${}."
      .format(valorBruto,valorDesconto, valorLiquido, mediaViajante ))