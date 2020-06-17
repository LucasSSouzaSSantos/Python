# Herança
# O que é herança ?
class NPD: # Base, Pai, Super classe
    def __init__(self, nome, time, forca, munnicao)
    self.nome = nome 
    self.time = time 
    self.forca = forca
    self.municao = municao
    self.vivo = True
    self.energia = 100

    def info(self):
        print("Nome:        "  + self.nome)
        print("Time:        "  + str(self.time))
        print("Força:       " + self.forca)
        print("munição:     " + self.municao)
        print("Vivo:        " + "Sim" if self.vivo else "Não")
        print("Energia:     " + str(self.energia))
        print("---------------------------------------")


