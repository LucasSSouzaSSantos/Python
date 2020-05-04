"""
EXERCÍCIO 042: Analisando Triângulos v2.0
Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print("Digite o comprimento das TRÊS retas: ")
reta1 = float(input("Reta 1: "))
reta2 = float(input("Reta 2: "))
reta3 = float(input("Reta 3: "))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):

    print("As retas informadas formam um triângulo")
    if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print("O triângulo formado é Escaleno:\npois todos seus lados são diferentes.")
    elif reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print("O triangulo informado é Equilátero:\npois tem os três lados iguais.")
    else:
        print("O triângulo informado é Isósceles:\npois dois dos lados são iguais.")
else:
    print("As retas informadas não formam um triângulo")
