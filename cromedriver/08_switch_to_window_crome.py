from selenium import webdriver
import time
import datetime

# options
options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument('--disable-blink-features=AutomationControlled')

# headless mode
# options.headless = True

options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')

driver = webdriver.Chrome(
    executable_path=r'C:\projects\Selenium\cromedriver\chromedriver',
    options=options
)

try:
    start_time = datetime.datetime.now()

    driver.get('https://avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty')
    print(f'Currently URL is: {driver.current_url}')
    # time.sleep(2)
    driver.implicitly_wait(2)

    items = driver.find_elements_by_xpath('//div[@data-marker="item-photo"]')
    items[0].click()
    # time.sleep(2)
    driver.implicitly_wait(2)


    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)
    driver.implicitly_wait(5)

    print(f'Currently URL is: {driver.current_url}')

    username = driver.find_element_by_class_name('seller-info-name')
    print(f'User name is : {username.text} ')
    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(5)
    driver.implicitly_wait(5)
    print(f'Currently URL is: {driver.current_url}')
    print('#'*20)

    items[1].click()
    #time.sleep(3)
    driver.implicitly_wait(3)

    driver.switch_to.window(driver.window_handles[1])
    #time.sleep(5)
    driver.implicitly_wait(5)
    print(f'Currently URL is: {driver.current_url}')
    username = driver.find_element_by_xpath('//div[@data-marker="seller-info/name"]')
    print(f'User name is : {username.text} ')

    ad_date = driver.find_element_by_class_name('title-info-metadata-item-redesign')
    print(f'An ad date is {ad_date.text} ')
    print('-'*20)

    joined_date = driver.find_elements_by_class_name('seller-info-value')[1]
    print(f'User since: {joined_date.text} ')
    print('#'*20)


    finish_time = datetime.datetime.now()
    spend_time = finish_time - start_time
    print(spend_time)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    '0:00:35.570598'
    '0:00:13.612163'