from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import insta_password



options = webdriver.FirefoxOptions()

#change useragent
options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')
#url = 'https://www.vk.com/'
driver = webdriver.Firefox(
    executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver.exe', options=options
    )

try:
    driver.get(url='https://instagram.com/')
    time.sleep(3)
    
    username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys('vanvala2014')
    time.sleep(2)

    pass_input = driver.find_element_by_name('password')
    pass_input.clear()
    pass_input.send_keys(insta_password)
    time.sleep(2)
    
    pass_input.send_keys(Keys.ENTER)
    time.sleep(5)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()