valorTotal = input("Qual o valor total da sua compra? ")
cupom = input("Possui cupom de desconto? ")

if cupom == "NIVER10":
    valorFinal = float(valorTotal) * 0.9
else :
    valorFinal = float(valorTotal)
    print("Cupom inválido")

print("O valor final da sua compra foi de {}, Esperamos ve-lo novamente".format(valorFinal))