
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

load_dotenv()


# inicialização do Flask
app = Flask(__name__)


def realizar_limpeza(username):
    # Realiza a limpeza de um login dentro da plataforma da CDNTV
    servico = Service(GeckoDriverManager().install())

    # Inicialize o WebDriver
    driver = webdriver.Firefox(service=servico)

    #abre o link do site
    link = os.getenv('LINK_SITE')

    # Abra a página de login
    driver.get(link)

    #login e senha do ADM
    usernamelog = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    #capturando os campos necessários
    driver.find_element(By.XPATH, '//*[@id="loginform-username"]').send_keys(usernamelog)
    driver.find_element(By.XPATH, '//*[@id="loginform-password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[4]/div[3]/button').click()
    time.sleep(3)

    account = os.getenv('ACCOUNT')

    # Abrir a aba de contas
    driver.get(account)
    time.sleep(3)

    username_field = driver.find_element(By.NAME, 'Account[username]')
    username_field.send_keys(username)
    time.sleep(2)

    driver.find_element(By.NAME, 'Account[name]').click()
    time.sleep(2)

    driver.find_element(By.NAME, 'Account[username]').send_keys(Keys.TAB, Keys.ENTER)
    time.sleep(3)

    # Limpar conexão
    driver.find_element(By.XPATH, "//button[text()='Clear']").click()
    time.sleep(2)

    #logout = config['link']['logout']
    logout = os.getenv('LOGOUT')
    driver.get(logout)
    time.sleep(2)

    # Fechar o navegador
    driver.quit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/resultado', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        realizar_limpeza(username)
        return render_template('resultado.html', resultado="Conexão limpa com sucesso!")
    return render_template('login.html')

if __name__ == '__main__':
    app.run()


