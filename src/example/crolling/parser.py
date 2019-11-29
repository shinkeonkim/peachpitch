import requests
from bs4 import BeautifulSoup

def crawling(title, artist, parsingTag):
    link = 'https://www.youtube.com/results?search_query='
    link = link + title+ "+" + artist
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    resultLink = soup.select(
        parsingTag
    )[0]['href']
    print("https://www.youtube.com/"+resultLink)

if __name__ == "__main__":
    crawling('mcmong','fame', 'h3 > a')
    #print(max([len(i) for i in englishWordList]))
    #print(min([len(i) for i in englishWordList]))
    