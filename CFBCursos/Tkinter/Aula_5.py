from tkinter import *
# Como criar menu

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)

menuContatos.add_command(label="Novo", command="semComando")
menuContatos.add_command(label="Pesquisar", command="semComando")
menuContatos.add_command(label="Deletar", command="semComando")
menuContatos.add_separator()
menuContatos.add_command(label="Sair", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

app.config(menu=barraDeMenus)

app.mainloop()
