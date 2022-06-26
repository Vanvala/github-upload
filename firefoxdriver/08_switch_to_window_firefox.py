from selenium import webdriver
import time


options = webdriver.FirefoxOptions()

# disable webdriver mode
options.set_preference('dom.webdriver.enabled', False)

# headless mode
options.headless = True

# change useragent
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')
# url = 'https://www.vk.com/'
driver = webdriver.Firefox(
    executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver', options=options
)

try:
    driver.get('https://avito.ru/moskva/transport')
    print(f'Currently URL is: {driver.current_url}')
    time.sleep(2)

    items = driver.find_elements_by_xpath('//div[@data-marker="item-photo"]')
    items[0].click()
    time.sleep(2)


    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f'Currently URL is: {driver.current_url}')

    username = driver.find_element_by_class_name('seller-info-name')
    print(f'User name is : {username.text} ')
    time.sleep(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    print(f'Currently URL is: {driver.current_url}')
    print('#'*20)

    items[1].click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f'Currently URL is: {driver.current_url}')
    username = driver.find_element_by_xpath('//div[@data-marker="seller-info/name"]')
    print(f'User name is : {username.text} ')

    ad_date = driver.find_element_by_class_name('title-info-metadata-item-redesign')
    print(f'An ad date is {ad_date.text} ')
    print('-'*20)

    joined_date = driver.find_elements_by_class_name('seller-info-value')[1]
    print(f'User since: {joined_date.text} ')
    print('#'*20)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()