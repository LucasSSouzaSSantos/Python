carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion"]

itCarros = iter(carros)

print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))

print("----------------------")

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break
