from selenium import webdriver
import time
from auth_data import vk_password
from selenium.webdriver.common.keys import Keys




# options
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')


driver = webdriver.Chrome(
    executable_path=r'C:\projects\Selenium\cromedriver\chromedriver.exe',
    options=options
)

try:

    driver.get('https://vk.com')
    time.sleep(5)

    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys('geos79@tut.by')
    time.sleep(2)
    
    pass_input = driver.find_element_by_id('index_pass')
    pass_input.clear()
    pass_input.send_keys(vk_password)
    time.sleep(2)
    pass_input.send_keys(Keys.Enter)
    
    # login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(2)

    news_link = driver.find_element_by_id('l_nwsf').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()