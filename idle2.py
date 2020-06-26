# Estruturas de Dados

# 5.1 Mais sobre lista

list = []  # lista vázia para usar como exemplo
list.append(2) # adiciona um intem no final da lista. Equivalente a list[len(list):] = [x]

list.extend(range(2, 5)) # ou a[len(a):] = range(2, 5)

list.insert(i, x)
# i é o índice antes do qual inserir equivalente a a.insert(0, x) a.insert(len(a), x) a.append(x)

list.remove(x) 

list.pop([I])  # [I] indica que o parametro é opção

list.index(x)

list.count(x)

list.sort(chave = Nenhum, reverso = Falso)

list.reverse()
list.copy()

# 5.1.1 Usando listas como pilhas


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()
stack.pop()

# 5.1.2 Usando listas como filas

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
queue

# 5.4 Conjuntos
"""
Um conjunto é uma coleção não ordenada sem elementos duplicados.
para criar um conjunto vazio, você deve usar set(), não {}; o último cria um
dicionário vazio, uma estrutura de dados que discutiremos na próxima seção.
"""

# 5.5 Dicionários

# 5.6 Técnicas de looping

knights = {'gallahad' : 'the pure', 'robin' : 'the brave'}

for k, v in knights.items():
    print(k, v)

for i, v in enumerate([]):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))



















