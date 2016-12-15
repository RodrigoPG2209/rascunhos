from math import sqrt

def sqrt_int_noint():
    print(" ")
    print(" ")
    print("Digite valores para descobrir quantos e quais sao os numeros que resultam em raiz quadrada exata.")
    print(" ")

    loop = 1

    while loop == 1:
        inicio = int(input("Digite um numero inteiro inicial: "))
        final = int(input("Digite um numero inteiro final: "))

        if final < inicio:
            print("O valor inicial deve ser menor que o final. A operacao sera reiniciada.")
            print("   ")
        elif inicio < 0 or final < 0:
            print("Tanto o valor inicial quanto o final devem ser maiores que zero.")
            print("   ")
        else:
            break

#                       x: valor a ser inserido na lista
#                                                               for: instrução de loop. O início e final do loop é definido pelas variáveis 'inicio' e 'final' dentro de range()
#                                                               for: o range não considera ir até o valor final, por isso é necessário somar
#                                                                                                if: cláusula para inclusão de x à lista
    valores_inteiros = [str(x) + " (" + str(int(sqrt(x))) + ")" for x in range(inicio, final +1) if x % sqrt(x) == 0]
    valores_nao_inteiros = [x for x in range(inicio, final +1) if x not in valores_inteiros]

    print("Quantidade de valores cuja raiz quadrada resulta em numeros inteiros:", str(len(valores_inteiros)))
    print("Quais sao:", valores_inteiros)
    print(" ")
    print("Quantidade de valores cuja raiz quadrada nao resulta em numeros inteiros:", str(len(valores_nao_inteiros)))
    print("Quais sao:", valores_nao_inteiros)
