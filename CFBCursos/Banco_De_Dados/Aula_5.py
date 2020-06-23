import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Banco_De_Dados//Agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
        print("Conexão Com Sucesso!")
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    print(res)


def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print("Registro finalizado")


vsql = "SELECT * FROM tb_contatos WHERE n_IdContatos = 1"
consultar(vcon, vsql)
