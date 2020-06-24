from tkinter import *
import os


c = os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"


def impDados():  # para quando apertar o botao
    arquivo = open(nomeArquivo, "a")
    arquivo.write(f"Nome: {vnome.get()}")
    arquivo.write(f"\nTelefone: {vtelefone.get()}")
    arquivo.write(f"\nEmail: {vemail.get()}")
    arquivo.write(f"\nObs: {vobs.get(1.0, END)}")
    arquivo.write("\n\n")
    print("??????")


app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

txt1 = Label(app, text="Nome", background="#dde", foreground="#000", anchor=W)
txt1.place(x=10, y=10, width=100, height=20)

vnome = Entry(app, background="#fff", foreground="#000")
vnome.place(x=10, y=35, width=100, height=20)

txt2 = Label(app, text="Telefone", background="#dde", foreground="#000", anchor=W)
txt2.place(x=10, y=60, width=100, height=20)

vtelefone = Entry(app, background="#fff", foreground="#000")
vtelefone.place(x=10, y=85, width=100, height=20)

txt3 = Label(app, text="E-mail", background="#dde", foreground="#000", anchor=W)
txt3.place(x=10, y=110, width=100, height=20)

vemail = Entry(app, background="#fff", foreground="#000")
vemail.place(x=10, y=135, width=100, height=20)

txt4 = Label(app, text="Fale Conosco", background="#dde", foreground="#000", anchor=W)
txt4.place(x=10, y=160, width=100, height=20)

vobs = Text(app, background="#fff", foreground="#000")
vobs.place(x=10, y=185, width=150, height=50)

btn1 = Button(app, text="Imprimir", command=impDados)
btn1.place(x=10, y=240, width=100, height=20)

app.mainloop()
