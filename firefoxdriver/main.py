from selenium import webdriver
import time
from fake_useragent import UserAgent


useragent = UserAgent()
options = webdriver.FirefoxOptions()

#change useragent
options.set_preference('general.useragent.override', useragent.random)
#url = 'https://www.vk.com/'
driver = webdriver.Firefox(
    executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver.exe', options=options
    )

try:
    driver.get(url='http://www.whatismybrowser.com/detect/what-is-my-user-agent')
    #driver.save_screenshot('vk.png')
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
