from tkinter import *

app = Tk()
app.title("CFB Cursos")  # titulo da janela
app.geometry("500x300")  # configuração do tamanho da janela
app.configure(background="#008")  # mudando a cor da janela

txt1 = Label(app, text="Curso de Python", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=30)

txt2 = Label(app, text="Curso de Java", background="#ff0", foreground="#000")
txt2.place(x=10, y=50, width=150, height=30)

txt3 = Label(app, text="Curso de C++", background="#ff0", foreground="#000")
txt3.place(x=10, y=90, width=150, height=30)

txt2 = Label(app, text="Curso de PHP", background="#ff0", foreground="#000")
txt2.place(x=10, y=130, width=150, height=30)

vtxt = "Módulo Tkinter"
vbg = "#008"
vfg = "#fff"
txt2 = Label(app, text=vtxt, background=vbg, foreground=vfg)

app.mainloop()
