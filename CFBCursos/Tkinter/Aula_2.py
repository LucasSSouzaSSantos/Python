from tkinter import *

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")
"""
anchor => N = Norte, S = Sul, E = Leste, W = Oeste
NE => Nordeste, SE => Sudeste, SO => Sudoeste, NO => Noroeste
anchor=W => Ele pega o texto e joga para a esquerda, já que o anchor
foi definido como W.
+----------------+
|Nome            |  
+----------------+
O anchor jogaria para direita se eu definisse ele como anchor=E
+----------------+
|            Nome|  
+----------------+

"""
txt1 = Label(app, text="Nome", background="#dde", foreground="#000", anchor=W)
txt1.place(x=10, y=10, width=100, height=20)

"""
Componente de Texto
Entry => É um componente de Texto!
É preciso indicar quem é seu master, no caso o objeto criado
o "app"
"""
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

vfaleConosco = Text(app, background="#fff", foreground="#000")
vfaleConosco.place(x=10, y=185, width=150, height=50)

app.mainloop()
