from bs4 import BeautifulSoup
import requests
from urllib.parse import quote_plus, quote


search_input = "WON'T YOU BE MY NEIGHBOR?"
def escape_input(search_input):
    remove_sq = search_input.replace("'", "")#replace ' with nothing
    return quote(remove_sq)

url_rotten = "https://www.rottentomatoes.com/search/?search="+ escape_input(search_input)

url_imdb = 'https://www.imdb.com/title/tt5463162'

html_get = requests.get(url_rotten)
html_get.encoding = 'UTF-8'
html_get_imdb = requests.get(url_imdb)
html_get_imdb.encoding = 'UTF-8'

soup_search = BeautifulSoup(html_get.text, 'html.parser')
soup1_search = BeautifulSoup(html_get_imdb.text, 'html.parser')

def movie_url(url_rotten):
    div_url = soup_search.find('div')
    return div_url
    #get_url = div_url.find('a')
    ##return get_url['href']


print(movie_url(html_get))


