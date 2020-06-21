import re
import os

if os.path.exists("texto.txt"):
    print("Arquivo existente.")
else:
    f = open("texto.txt", "w")
    f.close()

# os.remove("texto1.txt")

f = open("texto.txt", "w")

f.write("Curso de Python 3")

f.close()
