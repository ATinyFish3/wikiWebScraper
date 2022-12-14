# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

import sys


def scraper():  # main scraping function
    NUM_RESULTS = 3  # number of results that the searching should return
    BASE_WIKI_ADDRESS = 'https://en.wikipedia.org'  # wiki URL to prepend to URLs

    SEARCH = 'ai'  # the 'user' search to be replaced with input

    # Get results from user search
    wikiLinks = []  # store links to search result pages
    searchResults = userSearch(SEARCH, NUM_RESULTS)
    if not searchResults:
        sys.exit("No results found")
    for i in searchResults:
        wikiLinks.append(i.find('a')['href'])
    # print(wikiLinks)

    # need to get user to choose which result they want to use, for now just use top result

    URL = BASE_WIKI_ADDRESS + wikiLinks[0]
    print('Page URL: ', URL)

    # Get summary
    if True:  # Replace with user input
        summary(URL)

    # Get all text
    if True:
        print('allText here')
        # allText(URL)

    # Get headers from contents table || get from user input later
    # contentsHeaders = soup.find(id="toc")# id of contents

    # print(contentsHeaders.text)


def getHTML(pageURL):
    try:
        page = requests.get(pageURL)
    except:
        sys.exit('Bad URL')
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


def userSearch(searchTerm, numResults):
    searchReq = "https://en.wikipedia.org/w/index.php?search=" + searchTerm + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    soup = getHTML(searchReq)

    allResults = soup.find_all('div', class_='mw-search-result-heading')

    # Need to add validation

    if allResults:
        return allResults[:numResults]
    else:
        return False


def summary(pageURL):
    soup = getHTML(pageURL)
    try:
        paras = soup.select('p')
    except:
        sys.exit('Error in extracting summary info')  # keep to handle exceptionos
    numParas = len(paras)  # don't access paras[5] if only 2 elements
    # print(numParas)
    if numParas >= 2 and len(paras[0]) <= 1:
        print(paras[1].text)
    elif numParas != 0:
        print(paras[0].text)
    else:
        print('Summary unavailable')

# Better if get rid of things in []
def allText(pageURL):  # Return all text from wiki page
    soup = getHTML(pageURL)
    try:
        paras = soup.select('p')
    except:
        sys.exit('Error in extracting summary info')  # keep to handle exceptionos
    for i in paras:
        print(i.text)


if __name__ == '__main__':
    scraper()
