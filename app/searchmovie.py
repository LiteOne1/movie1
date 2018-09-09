from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





search_input = "captain america"
def escape_input(search_input):
    remove_sq = search_input.replace("'", "")#replace ' with nothing
    return quote(remove_sq)

options = Options()#options for selenium not to open a new webpage. It is a very slow solution.
options.add_argument("--headless")
driver = webdriver.Chrome('./app/static/chrome/chromedriver.exe')
url_rotten = "https://www.rottentomatoes.com/search/?search="+ escape_input(search_input)
driver.get(url_rotten)
url_imdb = 'https://www.imdb.com/title/tt5463162'

#html_get = requests.get(url_rotten)
html_get = driver.page_source
#html_get.encoding = 'UTF-8'
html_get_imdb = requests.get(url_imdb)
html_get_imdb.encoding = 'UTF-8'

soup_search = BeautifulSoup(html_get, 'html.parser')
soup1_search = BeautifulSoup(html_get_imdb.text, 'html.parser')

def movie_url(url_rotten):
    div_url = soup_search.find('div', class_ = 'poster')
    get_url = div_url.find('a')
    return get_url['href']


movie_search = movie_url(html_get)


