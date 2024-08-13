import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import datetime
import random

def enviar_mensagem(driver, mensagem, contador):
    try:
        # Localiza o campo de comentario pelo nome da Classe 
        comentario = driver.find_element(By.CLASS_NAME, "xaqnwrm")
        comentario.click()
        sleep(5)
        comentario = driver.find_element(By.CLASS_NAME, "xaqnwrm")
        comentario.send_keys(mensagem)
        sleep(10)
        # Clicando em enviar
        enviar = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37"]')
        enviar.click()
        sleep(8)
        driver.refresh()
    except NoSuchElementException as e:
        print(f"não encontrei o campo: {e}")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

def main():
    option = Options()
    option.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=option)
    driver.get('https://instagram.com')
    sleep(15)

    # Login do Instagram
    while True:
        try:
            #inserindo login
            login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            login.send_keys("Seu login")
            #inserindo senha
            senha = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            senha.send_keys("Senha")
            # localizando o botão entrar e clicando em entrar
            entrar = driver.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]')
            entrar.click()
            print("login efetuado")
            break
        except NoSuchElementException as e:
            print(f"não foi possivel logar: {e}")
        except Exception as e:
            print(f"Erro ao Logar: {e}")    

    # Aguardar a pagina carregar
    sleep(10)

    # acessando a postagem
    while True:
        try:
            postagem = driver.get('https://www.instagram.com/p/C95sbWrpG7E/')
            print("encontrei a postagem!")
            break
        except NoSuchElementException as e:
            print(f"Não encontrei a postagem")
        except	Exception as e:    
            print(f"Não encontrei a postagem {e}")

    # Esperando a pagina carregar
    sleep(10)

    # Definindo o tempo e a mensagem, contador, rondom mensagem
    tempo_intervalo = random.randint(10, 20)  # Intervalo de tempo em segundos random
    sleep(tempo_intervalo)
    mensagens = [
        "Dá um salve fafa",
        "essa e minha",
        "Cofia em Deus",
        "Sonhei com essa",
        "meu dia vai chegar"
]                                               # Mensagem random 

    contador = 0 # Inicializar contador
    # Loop de envio de mensagens
    while True:
        contador += 1 # roda toda vez que enviar a mensagem
        mensagem = random.choice(mensagens)
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        enviar_mensagem(driver, mensagem,contador)
        print(f"A mensagem foi enviada {contador} vezes proxima mensagem em {tempo_intervalo} segundos, mensagem enviada as {hora}")
        sleep(tempo_intervalo)

if __name__ == "__main__":
    main()