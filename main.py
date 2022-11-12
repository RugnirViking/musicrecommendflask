
import requests
from bs4 import BeautifulSoup

def scrape():
    # scrape list of artists and links from https://everynoise.com/engenremap-afghanpop.html

    # create a list of artists and links
    artists = []
    links = []

    # open the webpage
    url = 'https://everynoise.com/engenremap-afghanpop.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    divs = soup.find_all('div', class_='genre scanme')

    for div in divs:
        artistname = div.text
        artistname = artistname.strip().replace('»', '').replace('»', '')

        artists.append(artistname)
        links.append(div.a['href'])

    print(artists)
    print(links)
    for artist in artists:
        print(artist)


if __name__ == '__main__':
    scrape()