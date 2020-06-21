f = open("teste.txt", "at")
"""
r - read - Leitura
a - append - anexar
w - write   - Escrita
x - create  - criar
t - text - texto
b - binary  - binario
"""
f.write("CFB Cursos")

txt = input("Digite um texto: ")
f.write("\n" + txt + "\n")

f.close()


