import os
os.system('pip install requests undetected_chromedriver webdriver_manager selenium')
os.system('clear')
os.system('cls')
#importing required python packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


username= "pon_tu_nombre_de_usuario_aqui" #Instagram Username
password= "pon_tu_clave_aqui" #Instagram Password

chrome_options = uc.ChromeOptions()
proxy = 'http://viaduct.proxy.rlwy.net:34152'
chrome_options.add_argument('--headless')
chrome_options.add_argument('--proxy-server='+str(proxy))
driver = uc.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")
enter_username = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'username')))
enter_username.send_keys(username)
   
enter_password = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
enter_password.send_keys(password)
enter_password.send_keys(Keys.RETURN)
time.sleep(random.randint(1,4))

try:
  	not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mt3GC')))
  	a= not_now.find_elements_by_tag_name("button")[1]
  	actions = ActionChains(driver)
  	actions.click(a)
  	actions.perform()
except:
   	pass
   
finally:
	for i in range(20000): #Number of views
            driver.get("https://www.instagram.com/reel/") #Reel link
            time.sleep(random.randint(1,4))
