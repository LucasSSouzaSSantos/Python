"""
EXERCÍCIO 089: Boletim com Listas Compostas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
Nome = []
Notas = []
Media = []
Aluno = []
Boletim = []
for x in range(0, 4):
    nome = str(input("Nome: ")).capitalize().strip()
    Nome.append(nome)
    nota1 = float(input(f"Nota 1: "))
    Notas.append(nota1)
    nota2 = float(input(f"Nota 2: "))
    Notas.append(nota2)
    media = (nota1 + nota2) / 2
    Media.append(media)
    Aluno.append(Nome[:])
    Aluno.append(Notas[:])
    Aluno.append(Media[:])
    Boletim.append(Aluno[:])
    Nome.clear()
    Notas.clear()
    Media.clear()
    Aluno.clear()
print(f" BOLETIM ".center(41, "="))
print(f"| Id |".center(6) + f"Nome".center(25, ' ') + f"|".center(1, ' ') + f"Media".center(8) + f"|")
print("".center(41, '-'))
for c, v in enumerate(Boletim):
    print(
        f"| 0{c} |".center(6, ' ') + f"{v[0][0]}".center(25, ' ') + f"|".center(1) + f"{v[2][0]}".center(8, ' ') + "|")

print("".center(41, '-'))
detalhes = str(input("Você quer o detalhamento individualmente: ")).upper().strip()
print("".center(60, '-'))
print(f"| Id |".center(6) + f"Nome".center(25, ' ') + f"|".center(1, ' ') + f"Nota 1".center(8) + "|" +
      f"Nota 2".center(8) + "|" + f"Media".center(9) + f"|")
while True:
    print("".center(60, '-'))
    iden = int(input("Informe o Id do Aluno: "))
    print("".center(60, '-'))
    print(f"| {iden} |".center(6) + f"{Boletim[iden][0][0]}".center(25, ' ') + f"|".center(1, ' ') +
          f"{Boletim[iden][1][0]}".center(8) + "|" +
          f"{Boletim[iden][1][1]}".center(8) + "|" + f"{Boletim[iden][2][0]}".center(9) + f"|")
    print("".center(60, '-'))
    detalhes = str(input("Proximo[S/N]:")).upper().strip()
    print("".center(60, '-'))
    if detalhes == 'N':
        break
