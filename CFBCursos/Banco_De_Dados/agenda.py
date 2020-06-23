import sqlite3
from sqlite3 import Error
from CFBCursos.Banco_De_Dados.agenda_Funcoes import menuPrincipal
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
    opc = int(input("Digite uma opção: "))
    if opc == 1:
        print("opc 1")
    elif opc == 2:
        print("opc 2")
    elif opc == 3:
        print("opc 3")
    elif opc == 4:
        print("opc 4")
    elif opc == 5:
        print("opc 5")
    elif opc == 6:
        print("Programa finalizado!")
        break
    else:
        print("Opção Invalida")
