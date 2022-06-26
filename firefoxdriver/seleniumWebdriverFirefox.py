from selenium import webdriver
import time


options = webdriver.FirefoxOptions()

# change useragent
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')

# disable webdriver mode
options.set_preference('dom.webdriver.enabled', False)

driver = webdriver.Firefox(
    executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver.exe', options=options
)

try:
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    time.sleep(10)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()