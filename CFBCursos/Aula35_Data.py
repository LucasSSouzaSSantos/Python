import datetime

data = datetime.datetime.now()

print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

nasc = datetime.datetime(1992,2, 21)

print(nasc.strftime("%A"))

# %a dia da semana resulmido
# %A dia da semana completo
# %w número do dia da semana domingo - 0, segunda - 1
# %d númedo do dia do mês
# 