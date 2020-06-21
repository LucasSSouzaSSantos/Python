import re
f = open("teste.txt", "rt")

#for x in f:
#    print(f"x = {x}")

res = re.sub("\s","-",f.readline())

# O res vai sair vázio pq o ler todos os dados dentro 
# do arquivo.

print(f"res = {res}")


f.close()
