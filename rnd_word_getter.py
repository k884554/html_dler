from selenium import webdriver

class Random_word_getter:
    def __init__(self):
        self.url = 'https://fakena.me/random-english-words/one/'
        self.driver = None
    
    def rndm_word(self):
        self.driver = webdriver.PhantomJS()
 
        self.driver.get(self.url)
        w = self.driver.find_element_by_tag_name("h3")
 
        return w.text
