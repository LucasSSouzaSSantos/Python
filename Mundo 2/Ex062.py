"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print(" PROGRESSÃO ARITMETRICA ".center(30, '-'))
opcao = str(input("Deseja começar[Ss/Nn]: ")).upper().strip()
while opcao not in 'nNsS':
    opcao = str(input("Erro: Deseja começar[Ss/Nn]: ")).upper().strip()

if opcao in 'sS':
    a1 = int(input("a1 = "))
    r = int(input("r = "))
    cont = 0
    numero = 10
    print("".center(30, '-'))
    while opcao not in 'Nn':
        while cont <= numero:
            if cont == 0:
                print(f"a{cont + 1} = {a1}")
            else:
                print(f"a{cont + 1} = {a1 + r * cont} ")
            cont += 1
        print("".center(30, '-'))

        opcao = str(input("Deseja continuar[Ss/Nn]: ")).upper().strip()
        while opcao not in ['N', 'S']:
            opcao = str(input("Erro: Digite novamente[Ss/Nn]: ")).upper().strip()
        print("".center(30, '-'))
        if opcao in 'Ss':
            num = int(input("Deseja mais quantos elementos: "))
            numero += num
        print("".center(30, '-'))

print(" FIM ".center(30, '-'))
print("".center(30, '-'))
