import sqlite3
from sqlite3 import Error


def abrirConexao():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Banco_De_Dados//Agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        print("Conexao realizada com sucesso! ")
    return con


def fecharConexao(conexao):
    conexao.close()


def menuPrincipal():
    print("1 - Inserir Novo Registro ")
    print("2 - Deletar Registro ")
    print("3 - Atualizar Registro ")
    print("4 - Consultar Registro por ID ")
    print("5 - Consultar Resgistro por Nome ")
    print("6 - Sair")


def query(conexao, sql):
    try:
        c = conexao.cursor()
        print("Objeto: ", c)
        conexao.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print("OK")


def consultar(conexao, sql):
    c = conexao.cursor()
    conexao.execute(sql)
    res = c.fetchall
    return res


def menuAtualizar():
    print()


def menuConsultarId():
    print()


def menuConsultarNomes():
    print()


def menuDeletar():
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = "DELETE tb_contatos WHERE"


def menuInserir():
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql = "INSERT INTO tb_contatos (t_NomeContato, t_TelefoneContato, t_EmailContato)" \
           " VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(abrirConexao(), vsql)
    abrirConexao().close()
