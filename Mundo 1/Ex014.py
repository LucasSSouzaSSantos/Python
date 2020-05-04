"""
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
temperatura = float(input("Digite uma temperatura em °C: "))

print(f"{temperatura}°C = {(9 * temperatura / 5) + 32}°F")
print(f"{temperatura}°C = {temperatura + 273}K")
