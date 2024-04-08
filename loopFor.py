#a variael no for fica dentro do proprio for
#o range é o especifico de 0 ate um numero antes da variavel colocada no range se eu coloco 10 vai gerar de 0 à 9
#como a variavel e criada pelo for ela não precisa ser criada antes de ser chamada
#caso seja necessario ela pode começar de outro numero sempre colocando assim (2, 10) para que ela inicie em dois e va ate 9
#para alterar o incremento você precisa adicionar mais uma variavel dentro do range#
# no terceiro lugar para que o incremento tenha intervalo diferente de 1

for contadora in range(2, 11, 2):
    print(contadora)