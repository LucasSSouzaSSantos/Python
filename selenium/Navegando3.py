from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("file:///home/lucas/Documentos/GitHub/Python/selenium/teste.html")
"""
Como a maneira vista no arquivo Navengando2.py não é melhor maneira de navegar entre os select,
vamos tentar um nova abordagem. As classes de suporte do webDriver incluem uma chamada "select",
que fornece métodos úteis para interagir com estes(select):

"""
#################################################################################################
# Criado um objeto Select e passando um método como parâmetro
sel = Select(driver.find_element_by_name('carros'))
sele1 = sel.select_by_index(0)
# sele2 = sel.select_by_visible_text("volvo")
# sele3 = sel.select_by_value("volvo")
print(sele1)
# print(sele2)
# print(sele3)

driver.close()
