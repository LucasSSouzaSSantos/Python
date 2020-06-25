from tkinter import *
import os
pastaApp = os.path.dirname(__file__)


def semComando():
    print()


def novoContato():
    exec(open(pastaApp+"//NovoContato.py").read())


app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)

menuContatos.add_command(label="Novo", command=novoContato)
menuContatos.add_command(label="Pesquisar", command="semComando")
menuContatos.add_command(label="Deletar", command="semComando")
menuContatos.add_separator()
menuContatos.add_command(label="Sair", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

app.config(menu=barraDeMenus)

app.mainloop()
