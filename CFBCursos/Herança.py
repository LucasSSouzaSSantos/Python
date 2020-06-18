class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome 
        self.time = time 
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome:...." + self.nome)
        print("Time:...." + str(self.time))
        print("Força:..." + str(self.forca))
        print("munição:." + str(self.municao))
        print("Vivo:...." + ("Sim" if self.vivo else "Não"))
        print("Energia:." + str(self.energia))
        print("-------------------------------------------")


class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super(Soldado, self).__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super(Soldado, self).info()


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super(Guarda, self).__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super(Guarda, self).info()


class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super(Elite, self).__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super(Elite, self).info()


s1 = Soldado("Olho Vivo", 1)
s2 = Guarda("Bala na Agulha", 1)
s3 = Elite("Ninja", 1)
s4 = Soldado("Super Atento", 2)
s5 = Guarda("Tiro Certo", 2)
s6 = Elite("Samurei", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
