## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    dias = int(input("Insira a quantidade de dias: "))
    km = float(input("Insira a quantidade de kms percorridos: "))

    print("Por dias deu um total de:",60*dias)
    print("Por kms rodados deu um total de:",0.15*km)
    
if __name__ == '__main__':
    main()
