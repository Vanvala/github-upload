from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from time import sleep
from random import randrange

def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome(executable_path=r'C:\projects\Selenium\Instabot\chromedriver\chromedriver.exe')

    try:
        browser.get('https://www.instagram.com')
        browser.implicitly_wait(5)

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)
        browser.implicitly_wait(5)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(5)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            sleep(5)

            for i in range(1,4):
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(randrange(3, 5))

            hrefs = browser.find_elements_by_tag_name('a')
            posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]
            sleep(5)
            print(posts_urls)


            # for item in hrefs:
            #     href = item.get_attribute('href')
            #
            #     if '/p/' in href:
            #         posts_urls.append(href)
            #
            #         print(href)

            for url in posts_urls:
                try:
                    browser.get(url)
                    sleep(3)
                    like_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    sleep(randrange(80, 100))
                except Exception as ex:
                    print(ex)

            browser.close()
            browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()


    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()



hashtag_search(username, password, 'беловежскаяпуща')
