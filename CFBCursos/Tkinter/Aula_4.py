from tkinter import *
import os
from CFBCursos.Tkinter.banco import dml
c = os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"


def gravarDados():  # para quando apertar o botao
    if tb_nome.get() != "":
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get("1.0", END)
        vquery = "INSERT INTO tb_contatos (t_NOMECONTATO, t_TELEFONECONTATO, t_EMAILCONTATO, t_OBS)" \
                 "VALUES ('"+vnome+"', '"+vfone+"', '"+vemail+"', '"+vobs+"')"
        dml(vquery)
        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete("1.0", END)
        print("Dados Gravados")
    else:
        print("Erro!")


app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

txt1 = Label(app, text="Nome", background="#dde", foreground="#000", anchor=W)
txt1.place(x=10, y=10, width=100, height=20)

tb_nome = Entry(app, background="#fff", foreground="#000")
tb_nome.place(x=10, y=35, width=100, height=20)

txt2 = Label(app, text="Telefone", background="#dde", foreground="#000", anchor=W)
txt2.place(x=10, y=60, width=100, height=20)

tb_fone = Entry(app, background="#fff", foreground="#000")
tb_fone.place(x=10, y=85, width=100, height=20)

txt3 = Label(app, text="E-mail", background="#dde", foreground="#000", anchor=W)
txt3.place(x=10, y=110, width=100, height=20)

tb_email = Entry(app, background="#fff", foreground="#000")
tb_email.place(x=10, y=135, width=100, height=20)

txt4 = Label(app, text="Fale Conosco", background="#dde", foreground="#000", anchor=W)
txt4.place(x=10, y=160, width=100, height=20)

tb_obs = Text(app, background="#fff", foreground="#000")
tb_obs.place(x=10, y=185, width=150, height=50)

btn1 = Button(app, text="Gravar", command=gravarDados)
btn1.place(x=10, y=240, width=100, height=20)

app.mainloop()
