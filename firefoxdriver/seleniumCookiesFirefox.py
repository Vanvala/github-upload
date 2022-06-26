from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import insta_password, insta_login
import pickle

options = webdriver.FirefoxOptions()

# change useragent
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')
# url = 'https://www.vk.com/'
driver = webdriver.Firefox(
    executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver.exe', options=options
)

try:
    driver.get(url='https://instagram.com/')
    time.sleep(3)

    """username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(insta_login)
    time.sleep(2)

    pass_input = driver.find_element_by_name('password')
    pass_input.clear()
    pass_input.send_keys(insta_password)
    time.sleep(2)

    pass_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # cookies
    pickle.dump(driver.get_cookies(), open(f'{insta_login}_cookies', 'wb'))"""


    for cookie in pickle.load(open(f'{insta_login}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()