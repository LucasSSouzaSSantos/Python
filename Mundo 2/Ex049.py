"""
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
print(" TABUADA ".center(30, '-'))
numero = int(input("Digite um Número: "))
print(" ".center(30, '-'))
for x in range(1, 11, 1):
    print(f"{x} x {numero} = {x * numero}".center(30, ' '))
print(" ".center(30, '-'))
