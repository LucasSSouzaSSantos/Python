# fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print("a = ", a + " b = ", b)
    a, b = b, a + b

# 4. Mais ferramentas de controle de fluxo

# 4.1 if Declaraçoes

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# 4.2 for Declaraçoes

"""
A "for" instrução Python itera sobre os itens de qualquer sequência
(uma lista ou uma string), na ordem em que aparecem na sequência.
"""

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(f" word = {w}, len of word = {len(w)}")
    
# 4.3 A range() funçao
for i in range(5):
    print(i)

# range começa em 5 e termina em 9
range(5, 10)

# range começa em 0, termina em 9 e pula de 3 em 3
for i in range(0, 10, 3):
    print(f"{x} ", end=" ")

# range começa em -10, termina em -100 e pula de -30 em -30
for i in range(-10, -100, -30):
    print(f"{x} ", end=" ")

# Para iterar sobre os índices de uma sequência, você pode combinar
# range()e len()como segue:

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

"""
De muitas maneiras, o objeto retornado range()se comporta como se fosse
uma lista, mas na verdade não é. É um objeto que retorna os itens sucessivos
da sequência desejada quando você itera sobre ele, mas na verdade não faz
parte da lista, economizando espaço.
"""


# 4.4 Declarações break, continue e cláusulas else sobre loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        else:
            # loop fell through without finding a factor
            print(n, ' is a prime number')

# Obs: o else não pertence ao if e sim ao for. Esse tipo de declaração é chamado
# de claúsura

# 4.5 Declarações pass
"""
A passafirmação não faz nada. Pode ser usada quando uma declaração é necessária
sintaticamente, mas o programa não requer nenhuma ação. Por exemplo:
"""

while True:
    pass
"""
Isso é usado para criar classe mínimas.
Outro local que passpode ser usado é como um espaço reservado para uma função ou
corpo condicional quando você estiver trabalhando em um novo código, permitindo
que você continue pensando em um nível mais abstrato. O passsilenciosamente é
ignorado:
def initlog(*args):
    pass # Remember to implement this!
"""

# 4.6 Definindo funções
"""
A palavra-chave defintroduz uma definição de função . Deve ser seguido pelo nome
da função e pela lista entre parênteses de parâmetros formais. As instruções que
formam o corpo da função começam na próxima linha e devem ser recuadas.
"""

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(20)
fib

# 4.7 Mais sobre a definição de funçoes
"""
Também é possível definir funções com um número variável de argumentos.
Existem três formas, que podem ser combinadas.
"""

# 4.7.1 Valores de argumento padrao

def asK_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def soma( * num):
    s = 0
    s += num
    print(s)

soma(1, 2, 3)
soma(1, 4, 5, 6, 7)




































