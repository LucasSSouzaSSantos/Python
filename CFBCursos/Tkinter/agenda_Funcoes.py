import sqlite3
from sqlite3 import Error


def abrirConexao():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Tkinter//agenda"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def menuPrincipal():
    print("1 - Inserir Novo Registro ")
    print("2 - Deletar Registro ")
    print("3 - Atualizar Registro ")
    print("4 - Consultar Registro")
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
    c.execute(sql)
    res = c.fetchall()
    return res


def menuAtualizar():
    vcon = abrirConexao()
    vid = input("Digite o ID do registro a ser alterado:")
    vsql = "SELECT * FROM tb_contatos WHERE n_IDCONTATOS = " + vid
    r = consultar(vcon, vsql)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome: ").strip()
    vtelefone = input("Digite o telefone: ").strip()
    vemail = input("Digite o email: ").strip()
    if len(vnome) == 0:
        vnome = rnome
    if len(vtelefone) == 0:
        vtelefone = rtelefone
    if len(vemail) == 0:
        vemail = remail

    vsql = "UPDATE tb_contatos SET t_NOMECONTATO = '"+vnome+"', t_TELEFONECONTATO = '"+vtelefone+"'," \
           " t_EMAILCONTATO = '"+vemail+"' WHERE n_IDCONTATO = " + vid
    query(vcon, vsql)


def menuConsultar():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(abrirConexao(), vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"ID: {r[0]:<3} Nome: {r[1]:<30} Telefone: {r[2]:<14} E-mail: {r[3]:<30}")
        vcont += 1
        if vcont >= vlim:
            vcont = 0
    print("Fim da lista")
    abrirConexao().close()


def menuConsultarNomes():
    vnome = input("Digite o nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE t_NOMECONTATO LIKE '%"+vnome+"%'"
    res = consultar(abrirConexao(), vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"ID: {r[0]:<3} Nome: {r[1]:<30} Telefone: {r[2]:<14} E-mail: {r[3]:<30}")
        vcont += 1
        if vcont >= vlim:
            vcont = 0
    print("Fim da lista")
    abrirConexao().close()


def menuDeletar():
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = "DELETE FROM tb_contatos WHERE n_IDCONTATO = " + vid
    query(abrirConexao(), vsql)
    abrirConexao().close()


def menuInserir():
    abrirConexao()
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vobs = input("Observação: ")
    vsql = "INSERT INTO tb_contatos (t_NOMECONTATO, t_TELEFONECONTATO, t_EMAILCONTATO, t_OBS)" \
           " VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"', '"+vobs+"')"
    query(abrirConexao(), vsql)
    abrirConexao().close()
