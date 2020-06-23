import sqlite3
from sqlite3 import Error

# conexao


def ConexaoBanco():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Banco_De_Dados//Agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        print("Conexao realizada com sucesso! ")
    return con


vcon = ConexaoBanco()
opc = 0

while True:
    menuPrincipal()
    opc = input("Digite uma opção: ")
    if opc == 1:
        print()
    elif opc == 2:
        print()
    elif opc == 3:
        print()
    elif opc == 4:
        print()
    elif opc == 5:
        print()
    elif opc == 6:
        print("Programa finalizado!")
        break
    else:
        print("Opção Invalida")
