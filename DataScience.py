import pandas
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

#coleta informações do produto
# coleta de info na web
browser = webdriver.Chrome(executable_path=r"C:\\Users\\vaisefode\\PycharmProjects\\Programs\\chromedriver.exe")
browser.get("https://www.karsten.com.br/")
browser.find_element_by_class_name('menu-item-texto').send_keys(Keys.ARROW_RIGHT)
browser.find_element_by_class_name('menu-item-texto').send_keys(Keys.RETURN)
browser.find_element_by_link_text("https://www.karsten.com.br/lencol-com-elastico-casal-karsten-150-fios-100-algodao-com-fronha-rael-3674925/p" + Keys.RETURN)
#criaa catálogos e gráficos de cor para itens

#gerenciamento de clientes, coletando informações de endereço e contato (banco de dados)
#
#gerenciamento de produtos não vendidos, mais vendidos, menos vendidos

#lembretes de follow ups e cria listas de produtos famosos
