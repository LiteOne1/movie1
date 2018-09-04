from bs4 import BeautifulSoup
import requests


url = 'https://www.rottentomatoes.com/m/deadpool_2'
url_imdb = 'https://www.imdb.com/title/tt5463162'

html_get = requests.get(url)
html_get.encoding = 'UTF-8'
html_get_imdb = requests.get(url_imdb)
html_get_imdb.encoding = 'UTF-8'

soup = BeautifulSoup(html_get.text, 'html.parser')
soup1 = BeautifulSoup(html_get_imdb.text, 'html.parser')

def get_posters(url_adress):
    posters = soup.find('div', class_ = 'slick-list') #get only first poster. To be change after redesign
    print(posters)
    #for poster in posters:
        #return poster['src']

get_posters(html_get)