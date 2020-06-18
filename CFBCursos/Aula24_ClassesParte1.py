# Criação de uma Classe:

class Carro:
    velMax = 0
    ligado = False
    cor = ""


c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False

print(f"Velocidade Máxima: {c1.velMax}\nCor do Carro: {c1.cor}\nO Carro está ligado: {c1.ligado}")

