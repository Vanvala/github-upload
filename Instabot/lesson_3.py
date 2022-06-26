from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from time import sleep
from random import randrange
from selenium.common.exceptions import NoSuchElementException


class InstagramBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(executable_path=r'C:\projects\Selenium\Instabot\chromedriver\chromedriver.exe')

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
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

    def like_photo_by_hashtag(self, hashtag):
        browser = self.browser
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(5)

        for i in range(1,4):
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(randrange(3, 5))

        hrefs = browser.find_elements_by_tag_name('a')
        posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]
        sleep(5)

        for url in posts_urls:
            try:
                browser.get(url)
                sleep(3)
                like_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                sleep(randrange(80, 100))
            except Exception as ex:
                print(ex)
                self.close_browser()

    # проверяем по xpath существует ли элемент
    def xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist
    # ставим лайк на пост по прямой ссылке
    def put_exactly_like(self, userpost):

        browser = self.browser
        browser.get(userpost)
        sleep(5)

        wrong_userpage = '/html/body/div[1]/section/main/div/h2'
        if self.xpath_exists(wrong_userpage):
            print('Такого поста не существует, проверьте URL')
            self.close_browser()
        else:
            print("Пост успешно найден, ставим лайк!")
            sleep(2)

        like_button = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button'
        browser.find_element_by_xpath(like_button).click()
        sleep(2)

        print(f'Лайк на пост: {userpost} поставлен!')
        self.close_browser()

    # ставим лайк по ссылке на аккаутн пользователя
    def put_many_likes(self, userpage):

        browser = self.browser
        browser.get(userpage)
        sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/h2'
        if self.xpath_exists(wrong_userpage):
            print('Такого пользователя не существует, проверьте URL')
            self.close_browser()
        else:
            print("Пользователь успешно найден, ставим лайк!")
            sleep(2)

            posts_count = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text
            posts_count = int(posts_count.replace(" ", ""))
            loops_count = int(posts_count // 12)
            print(loops_count)

            posts_urls = []
            for i in range(1, loops_count):
                hrefs = browser.find_elements_by_tag_name('a')
                hrefs = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

                for href in hrefs:
                    posts_urls.append(href)

                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(randrange(2, 4))
                print(f'Итерация #{i}')

            file_name = userpage.split('/')[-2]

            with open(f'{file_name}.txt', 'a') as file:
                for posts_url in posts_urls:
                    file.write(posts_url + '\n')

            set_posts_urls = set(posts_urls)
            set_posts_urls = list(set_posts_urls)
            with open(f'{file_name}_set.txt', 'a') as file:
                for post_url in set_posts_urls:
                    file.write(post_url + '\n')

            with open(f'{file_name}_set.txt') as file:
                urls_list = file.readlines()

                for post_url in urls_list:
                    try:
                        browser.get(post_url)
                        sleep(2)

                        like_button = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button'
                        browser.find_element_by_xpath(like_button).click()
                        sleep(randrange(80, 100))

                        print(f'Лайк на пост: {post_url} поставлен!')
                    except Exception as ex:
                        print(ex)
                        self.close_browser()

            self.close_browser()




my_bot = InstagramBot(username, password)
my_bot.login()
my_bot.put_many_likes("https://www.instagram.com/gotham_89/")
# my_bot.put_many_likes("https://www.instagram.com/bekker_by/")
