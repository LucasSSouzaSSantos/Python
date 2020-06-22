import sqlite3
from sqlite3 import Error

# Criar Conexão com  o banco de dados usando a função
################ Criar Conexão ######################
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

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vsql = "insert into tb_contatos (T_NomeContato, T_TelefoneContato, T_EmailContato) values ('"+nome+"','"+telefone+"','"+email+"')"


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Dados inseridos com sucesso!")
        conexao.commit()
    except Error as ex:
        print(ex)

inserir(vcon, vsql)
