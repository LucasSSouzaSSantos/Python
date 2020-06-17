# Herança
# O que é herança ?
class NPC: # Base, Pai, Super classe
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


    class soldado(NPC):
        def __init__(self, nome, time):
            self.forca = 200
            self.municao = 200
            super().__init__(nome, time,self.forca, self.municao)

    
    class Guarda(NPC):
        def __init__(self, nome, time):
            self.forca = 100
            self.municao = 20
            super().__init__(nome, time, self.forca, self.municao)
        def inf(self):
            super().info()
    
    class Elite(NPC):
        def __init__(self, nome, time):    
            self.forca = 300
            self.municao = 500
            super().__init(nome, time, self.forca, self.municao)
        def inf(self):
            super().info()



