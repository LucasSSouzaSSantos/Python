from tkinter import *

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#008")

txt1 = Label(app, text="Curso de Python", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=120, height=20)

vtxt = "Módulo Tkinter"
cor_fundo = "#ff0"
cor_letra = "#000"
txt2 = Label(app, text=vtxt, bg=cor_fundo, fg=cor_letra)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True)
app.mainloop()
