import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2, values_only=True):
    nome, valor, cpf, vencimento = linha

    drive = webdriver.Chrome()
    drive.get('https://consultcpf-devaprender.netlify.app/')
    sleep(5)

    campo_pesquisa = drive.find_element(By.XPATH, "//input[@id='cpfInput']")
    campo_pesquisa.send_keys(cpf)
    sleep(2)

    botao_pesquisa = drive.find_element(
        By.XPATH, "//button[@class='btn btn-custom btn-lg btn-block mt-3']")
    sleep(1)
    botao_pesquisa.click()
    sleep(4)
