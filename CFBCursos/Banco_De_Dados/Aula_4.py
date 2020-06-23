import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Banco_De_Dados//Agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
        print("Conexão Com Sucesso!")
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados deletado com sucesso!")
    except Error as ex:
        print(ex)


vsql = "DELETE FROM tb_contatos WHERE n_IdContatos=1"
deletar(vcon, vsql)
