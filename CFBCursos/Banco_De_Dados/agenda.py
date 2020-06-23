from CFBCursos.Banco_De_Dados.agenda_Funcoes import menuPrincipal, menuAtualizar, menuInserir
from CFBCursos.Banco_De_Dados.agenda_Funcoes import menuConsultarId, menuConsultarNomes, menuDeletar


while True:
    menuPrincipal()
    opc = int(input("Digite uma opção: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarId()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        print("Programa finalizado!")
        break
    else:
        print("Opção Invalida")
