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

time.sleep(3)
driver.close()
