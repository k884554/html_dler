from gscrapy import GoogleScrapy
from rnd_word_get import rndm_word

def get_urls(i):
    url_list = []
    
    while True:
        google = GoogleScrapy()
        google.start(end=i)
 
        for row in google.searches:
                url_list.append(row)
        
        if len(url_list) >= i:
                    break
                    
    return url_list
