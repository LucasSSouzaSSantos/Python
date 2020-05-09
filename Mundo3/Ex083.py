"""
EXERCÍCIO 083: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
parenteseAberto = 0
parenteseFechado = 0
expressao = []
while True:
    valor = str(input(": "))
    expressao.append(valor)
    if valor == '(':
        parenteseAberto += 1
        print(f"Parentese Aberto {parenteseAberto} vez")
    if valor == ')':
        parenteseFechado += 1
        print(f"Parentese fechado {parenteseFechado} vez")
    if parenteseAberto == parenteseFechado:
        opcao = str(input("Deseja Continuar ")).upper().strip()
        if opcao[0] == 'N':
            break
print(f"Expressão: ")
for x in expressao:
    print(f"{x}", end=' ')
