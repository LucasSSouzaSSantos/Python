from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("file:///home/lucas/Documentos/GitHub/Python/selenium/teste.html")

element = driver.find_element_by_xpath("//select[@name='carros']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print(f'O valor é:  {option.get_attribute("value")}')
try:
    element2 = driver.find_element_by_xpath("//select[@name='comidas']")
    all_options2 = element2.find_elements_by_tag_name("option")
    for option in all_options:
        print(f"O valor é: {option.get_attribute('value')}")
except:
    print("Não pôde ser imprimido!")
