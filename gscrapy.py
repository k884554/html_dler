from collections import namedtuple
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from rnd_word_getter import Random_word_getter
 
class GoogleScrapy:
 
    def __init__(self, default_wait=5):
        self.url = 'https://www.google.com/webhp?gl=us&hl=en&gws_rd=cr&pws=0'
        self.end = None
        self.default_wait = default_wait
        self.driver = None
        self.searches = []

    def enter_keyword(self, keyword):
        """キーワードを入力し、エンターを押す"""
        self.keyword = keyword
        self.driver.get(self.url)
        self.driver.find_element_by_id('lst-ib').clear()
        self.driver.find_element_by_id('lst-ib').send_keys(self.keyword)
        self.driver.find_element_by_id('lst-ib').send_keys(Keys.RETURN)

    def get_search(self):
        """通常の検索結果を取得する"""
        all_search = self.driver.find_elements_by_class_name('rc')
        for data in all_search:
            url = data.find_element_by_css_selector('h3 > a').get_attribute('href')
            self.searches.append(url)
 
    def start(self, end):
        """　ブラウザを立ち上げ、各種データの取得を開始する"""
        self.end = end
        
        try:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(self.default_wait)
            br = Random_word_getter()
            
            while True:
                self.enter_keyword(br.rndm_word())
                self.get_search()
                if len(self.searches) >= self.end:
                    break
        finally:
            br.driver.quit()
            self.driver.quit()
