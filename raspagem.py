import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup

option = Options()
option.add_argument('--start-maximized')
driver = webdriver.Chrome(options=option)
driver.get('https://instagram.com')

while True:
    try:
        login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        login.send_keys("seu login") #login
        senha = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        senha.send_keys("Senha") #senha
        entrar = driver.find_element(By.XPATH,'//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')
        entrar.click()
        print("login efetuado")
        break
        
    except:
        print("erro")
        sleep(1)

# Aguardar a pagina carregar
sleep(8)       

# Acessar a página do perfil
driver.get('https://www.instagram.com/johnizzat_/')
sleep(6)

# Clicar em seguidores
while True:
    try:
        seguidores = driver.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd']")
        seguidores.click()
        print("Consegui Clicar!")
        break
    except:
        print('elemento encontrado!!')
        sleep(6)

# Raspagem de dados
segudiores = driver.find_elements(class_="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3")
print(seguidores)




input('Z')