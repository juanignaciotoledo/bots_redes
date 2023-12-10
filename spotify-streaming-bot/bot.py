from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
import json

playlist_url = 'https://open.spotify.com/playlist/<play_list_number>'


secret_file = open('secret.json')
data = json.load(secret_file)
user_name = data['username']
password = data['password']
secret_file.close()


spotify_url = 'https://www.spotify.com/login'

browser = webdriver.Chrome()
browser.get(spotify_url)

browser.find_element_by_id('login-username').send_keys(user_name)
browser.find_element_by_id('login-password').send_keys(password)
browser.find_element_by_id('login-button').click()
time.sleep(3)
spotify_player_url = 'https://open.spotify.com/genre/recommended-stations'
print('Selenium Seesion id: ', browser.session_id)
print('Logged In....')
browser.get(playlist_url)

time.sleep(3)

play_button_xpath = "//button[@data-testid='play-button']"
play_buttons = browser.find_elements_by_xpath(play_button_xpath)


# there are multiple play buttons found. Try and click all of them.
for i, button in enumerate(play_buttons):
    print("clicking play button # " ,i)
    try:
        button.click()
    except ElementClickInterceptedException as ex:
        pass # It's ok we will try another play button

# enjoy

