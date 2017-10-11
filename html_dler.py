import requests
from get_urls import get_urls
import sys

argvs = sys.argv
argc = len(argvs)
n = int(argvs[1])

if (argc != 2):
    print('Usage: # python %s [num_of_html_docs]' % argvs[0])
    quit()
    
url_list = get_urls(n)

for i in range(n):
    try:
        print(i)
        file = open('./docs/doc%05.f.html' % i,'w')
        file.write(requests.get(url_list[i]).text)
    except:
        pass