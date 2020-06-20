# Criação de uma Classe:


class Carro:
    velMax = 0
    ligado = ""
    cor = ""

    def __init__(self, v, li, c):
        # O parâmetro self é uma referência para a própria classe
        self.velMax = v
        self.ligado = li
        self.cor = c

    def ligar(self):
        self.ligado = "Sim"

    def desligar(self):
        self.ligado = "Não"

    def andar(self):
        if self.ligado.upper() == "Sim":
            print("Carro em movimento")
        else:
            print("Carro Parado")

    def mostrar(self):
        print(f"Velocidade Máxima:................ {self.velMax}")
        print(f"Cor do Carro:..................... {self.cor}")
        print(f"Ligado:........................... {self.ligado}")
        print("--------------------------------------------------")


print(50 * "-")
print(" Carro 1")
c1 = Carro(200, "Não", "Preto")  # Construção do primeiro objeto chamado c1
c1.ligar()
c1.mostrar()  # Chamada do método mostrar() para mostrar os parâmetro do objeto c1
c1.andar()

print(" Carro 2")
c2 = Carro(120, "Não", "Branco")
c2.ligar()
c2.desligar()
c2.mostrar()

print(" Carro 3")
c3 = Carro(350, "Não", "Vermelho")
c3.ligar()
c3.desligar()
c3.mostrar()
