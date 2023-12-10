from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
import json
from faker import Faker
import urllib3

playlist_url = 'https://open.spotify.com/playlist/<play_list_number>'

# Load secret data from JSON file
secret_file = open('secret.json')
data = json.load(secret_file)
user_name = data['username']
password = data['password']
secret_file.close()

# Initialize Faker for generating random data
fake = Faker()

# Set up HTTP proxy
proxy_url = 'http://viaduct.proxy.rlwy.net:34152'
proxy = urllib3.ProxyManager(proxy_url, cert_reqs='CERT_NONE', assert_hostname=False)

# Set up options for Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy_url)
chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL verification

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up WebDriver with Chrome options
browser = webdriver.Chrome(options=chrome_options)

# Set geolocation and time zone using Faker
geolocation = fake.local_latlng(country_code="US")
time_zone = fake.timezone()

# Set geolocation and time zone in browser
browser.execute_cdp_cmd('Emulation.setGeolocationOverride', {
    "latitude": geolocation[0],
    "longitude": geolocation[1],
    "accuracy": 100
})
browser.execute_cdp_cmd('Emulation.setTimezoneOverride', {
    "timezoneId": time_zone
})

# Open Spotify login page
spotify_url = 'https://www.spotify.com/login'
browser.get(spotify_url)

# Fill in login credentials
browser.find_element_by_id('login-username').send_keys(user_name)
browser.find_element_by_id('login-password').send_keys(password)
browser.find_element_by_id('login-button').click()
time.sleep(3)

# Print session information
print('Selenium Session id:', browser.session_id)
print('Logged In....')

# Open the playlist URL
browser.get(playlist_url)
time.sleep(3)

# Find play buttons and click them
play_button_xpath = "//button[@data-testid='play-button']"
play_buttons = browser.find_elements_by_xpath(play_button_xpath)

for i, button in enumerate(play_buttons):
    print("Clicking play button #", i)
    try:
        button.click()
    except ElementClickInterceptedException as ex:
        pass  # It's okay; try another play button

# Enjoy
