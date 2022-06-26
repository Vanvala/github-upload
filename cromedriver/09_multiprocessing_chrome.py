from selenium import webdriver
from multiprocessing import Pool

# options
options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument('--disable-blink-features=AutomationControlled')

# headless mode
# options.headless = True

options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')


urls_list = ['https://stackoverflow.com', 'https://instagram.com', 'https://vk.com']

def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path=r'C:\projects\Selenium\cromedriver\chromedriver',
            options=options
        )
        driver.get(url=url)
        driver.implicitly_wait(5)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
        

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    p = Pool(processes=3)
    p.map(get_data, urls_list)

