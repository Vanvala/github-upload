from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from time import sleep


def login(username, password):
    browser = webdriver.Chrome(executable_path=r'C:\projects\Selenium\Instabot\chromedriver\chromedriver.exe')

    try:
        browser.get('https://www.instagram.com')
        browser.implicitly_wait(5)

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)
        browser.implicitly_wait(5)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(10)

        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()



login(username, password)
