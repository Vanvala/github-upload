from selenium import webdriver
import time
from auth_data import vk_password, email
from selenium.webdriver.common.keys import Keys



# options
options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument('--disable-blink-features=AutomationControlled')

# headless mode
options.headless = True

options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')

driver = webdriver.Chrome(
    executable_path=r'C:\projects\Selenium\cromedriver\chromedriver.exe',
    options=options
)

try:

    driver.get('https://vk.com')
    time.sleep(2)

    print('Passing authentification...')
    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(2)

    pass_input = driver.find_element_by_id('index_pass')
    pass_input.clear()
    pass_input.send_keys(vk_password)
    time.sleep(3)
    pass_input.send_keys(Keys.ENTER)

    # login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(5)

    print('Going to the profile page...')
    profile_link = driver.find_element_by_id('l_pr').click()
    time.sleep(5)

    print('Start watching video...')
    video_block = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/a[5]').click()
    time.sleep(10)
    print('Finito la comedia!')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()