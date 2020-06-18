import datetime

data = datetime.datetime.now()

print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

nasc = datetime.datetime(1992,2, 21)

print(nasc.strftime("%A"))

# %a dia da semana resulmido
# %A dia da semana completo
# %w número do dia da semana domingo - 0, segunda - 1
# %d númedo do dia do mês
# %b nome do mês abreviado
# %B nome do mês completo
# %n número do mês
# %y ano com dois dígitos
# %Y ano com quatro dígitos
# %H hora de 00 à 23
# %I hora de 00 à 12
 