import os
os.system('pip install requests undetected_chromedriver webdriver_manager selenium')
os.system('clear')
os.system('cls')
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import requests





info = {}

print("loading...")
time.sleep(3)
os.system('cls')
views = int(input("enter no. of view: "))
time.sleep(0)
os.system('cls')
view_time = float(input('enter time for each view: '))
time.sleep(0)
os.system('cls')
username = (input("plase put your your email: "))
time.sleep(0)
os.system('cls')
password = (input("plase put your password: "))
time.sleep(0)
os.system('cls')
url1 = (input("enter reel or photo url or all link on instagram: "))
time.sleep(0)
os.system('cls')
print("loading...")
time.sleep(3)
os.system('cls')








chrome_options = uc.ChromeOptions()
proxy = 'http://viaduct.proxy.rlwy.net:34152'
chrome_options.add_argument('--headless')
chrome_options.add_argument('--proxy-server='+str(proxy))
driver = uc.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")
print("your page is loading your account please wait...")
time.sleep(4)
os.system('cls')
enter_username = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
enter_username.send_keys(username)
print("your email or username is successful put...")
time.sleep(4)
os.system('cls')
enter_password = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
enter_password.send_keys(password)
time.sleep(random.randint(1,4))
print("your password is successful put...")
time.sleep(4)
os.system('cls')
print("thanks your instagram account is successful loading...")
time.sleep(4)
os.system('cls')

for i in range(views):
        print("Your site is on status load please wait for the view successful...")
        time.sleep(4)
        os.system('cls')
        driver.get(url1)
        time.sleep(view_time)
        print("Your view is successful sent...")
        time.sleep(4)
        os.system('cls')
        print("reloading page...")
        time.sleep(4)
        os.system('cls')
