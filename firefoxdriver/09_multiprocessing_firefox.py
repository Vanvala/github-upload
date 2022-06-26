from selenium import webdriver
import time
from multiprocessing import Pool


options = webdriver.FirefoxOptions()

# disable webdriver mode
options.set_preference('dom.webdriver.enabled', False)

# headless mode
# options.headless = True

# change useragent
options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')

def get_data(url):
    try:
        driver = webdriver.Firefox(
            executable_path=r'C:\projects\Selenium\firefoxdriver\geckodriver', options=options
        )
        driver.get(url=url)
        driver.implicitly_wait(10)
        driver.find_element_by_class_name('lazyload-wrapper').find_element_by_class_name('item-video-container').click()
        time.sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    proces_count = int(input('Enter the number of process: '))
    url = input('Enter the URL: ')
    urls_list = [url] * proces_count
    print(urls_list)
    p = Pool(processes=proces_count)
    p.map(get_data, urls_list)