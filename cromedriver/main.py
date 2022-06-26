# from selenium import webdriver
from seleniumwire import webdriver
import time
#import random
from fake_useragent import UserAgent

#url = 'https://www.instagram.com/'
"""user_agent_list = [
    'hello_world',
    'best_of_the_best',
    'vanvala'
]
useragent = UserAgent()

#options
options = webdriver.ChromeOptions()
#options.add_argument('user-agent=HelloWorld:')
#options.add_argument(f'user-agent={random.choice(user_agent_list)}')
options.add_argument(f'user-agent={useragent.random}')

#set proxy you need to get proxy https://proxy6.net/
options.add_argument('--proxy-server=138.128.91.65:8000')"""

driver = webdriver.Chrome(
    executable_path=r'C:\projects\Selenium\cromedriver\chromedriver.exe',
    options=options
)

try:
    driver.get(url='http://www.whatismybrowser.com/detect/what-is-my-user-agent')
    time.sleep(2)

   """ driver.refresh()
    time.sleep(2)
    driver.get_screenshot_as_file('1.png')
    driver.get(url='https://www.stackoverflow.com')
    time.sleep(5)
    driver.save_screenshot('2.png')
    time.sleep(2)"""
    driver.get('https://2ip.ru')
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()