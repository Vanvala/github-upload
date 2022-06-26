from selenium import webdriver
import time
from auth_data import vk_password, email
from selenium.webdriver.common.keys import Keys
import pickle


# options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')

driver = webdriver.Chrome(
    executable_path=r'C:\projects\Selenium\cromedriver\chromedriver.exe',
    options=options
)

try:

    driver.get('https://vk.com')
    time.sleep(2)

    """email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(2)

    pass_input = driver.find_element_by_id('index_pass')
    pass_input.clear()
    pass_input.send_keys(vk_password)
    time.sleep(3)
    pass_input.send_keys(Keys.ENTER)

    # login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(15)

    news_link = driver.find_element_by_id('l_nwsf').click()
    time.sleep(5)
    # cookies
    pickle.dump(driver.get_cookies(), open(f'{email}_cookies', 'wb'))"""

    for cookie in pickle.load(open(f'{email}_cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()