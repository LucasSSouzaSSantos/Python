x = 10
try:
    # verifica se um bloco tem um erro
    print(x)
except:
    # caso tenha ele execulta o except
    print ("X não definido")
else:
    # caso não o código não tenha erro ele cai nesse bloco
    print("Tudo certo!")
finally:
    # Independente se deu erro ou não, o bloco finally
    # será execultado.
    print("Fim do tratamento")
