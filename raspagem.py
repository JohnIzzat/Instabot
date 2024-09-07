import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Configuração do Selenium WebDriver
option = Options()
option.add_argument('--start-maximized')
driver = webdriver.Chrome(options=option)
print('[AVISO] Aguarde 10 segundos que será informado seu login e senha automaticamente.')
driver.get('https://instagram.com')
sleep(10)

# Tentativa de Login
while True:
    try:
        login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys("achaadinhoshopeeapp")  # Substitua por seu login
        senha = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        senha.send_keys("989182159")  # Substitua por sua senha
        entrar = driver.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')
        entrar.click()
        print("Login efetuado")
        break
    except Exception as e:
        print(f"Erro ao tentar logar: {e}")

# Aguardar a página carregar
sleep(15)

# Navegar até o perfil do usuário
driver.get('https://www.instagram.com/johnizzat_/')
sleep(6)

# Clicar em seguidores
while True:
    try:
        seguidores = driver.find_element(By.XPATH, "//a[contains(@href, 'followers')]")
        seguidores.click()
        print("Consegui Clicar!")
        break
    except Exception as e:
        print(f"Erro ao tentar clicar em seguidores: {e}")

# Esperar o modal carregar
sleep(8)

# Lista para armazenar os nomes dos seguidores
dados_usuarios = []

# Raspagem de dados sem rolagem
try:
    # Encontrar todos os nomes de seguidores carregados inicialmente
    nomes = driver.find_elements(By.XPATH, "//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")
    for nome in nomes:
        texto_nome = nome.text.strip()
        if texto_nome and texto_nome not in dados_usuarios:  # Verificar se o nome não está vazio e evitar duplicados
            dados_usuarios.append(texto_nome)
            print(texto_nome) # Mostra os dados que foram pegos
except Exception as e:
    print(f"Erro durante a raspagem: {e}")
    print("Raspagem de dados concluída ou interrompida pelo usuário.")

# Realizar o Scroll

# Salvando dados em um arquivo txt
nome_arquivo = "dados.txt"
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    for nome in dados_usuarios:
        arquivo.write(nome + '\n')
print(f"Dados salvos no arquivo {nome_arquivo}.")

input('')
