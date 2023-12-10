from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
from random import randint

class Setup:
    def init(self):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        proxy = 'http://viaduct.proxy.rlwy.net:34152'
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--proxy-server='+str(proxy))
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )

    def close_browser(self):
        self.browser.close()