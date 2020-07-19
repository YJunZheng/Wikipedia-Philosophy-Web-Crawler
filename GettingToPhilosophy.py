from bs4 import BeautifulSoup
import requests

def getHtmlCode(url):       # Returns all the html code from the URL
    r = requests.get(url)

    return r.text

def isInParentheses(htmlCode, index):
    for i in range(index, -1, -1):
        if htmlCode[i] == '(':
            return True
        elif htmlCode[i] == ')':
            return False

    return False

def getFirstLink(htmlCode): # Returns the first link in the main content
    # The below code uses indices instead of bs4's find function
    # as bs4's find(startID) returns EVERYTHING which is unnecessary
    mainCode = htmlCode[htmlCode.index(startID): htmlCode.index(endID)]
    soup = BeautifulSoup(mainCode, features='html.parser')

    try:
        soup.i.decompose()  # Removes all italics as part of the rules
    except:
        pass

    try:
        soup.find('span', id='coordinates').decompose() # Removes coordinates in locations
    except:
        pass

    for paragraph in soup.findAll('p'):    # Only use text: no side panels
        for link in BeautifulSoup(str(paragraph), features='html.parser').findAll('a'):
            if 'href=\"/wiki/' in str(link) and not link.attrs['href']\
                    == urlSuffix and not 'href=\"/wiki/File' in str(link)\
                    and not 'href=\"/wiki/Help:' in str(link):
                # The above if statement stops the bot from clicking a link
                # to itself, wiki/File: and wiki/Help:
                indexOfLink = mainCode.index(link['href'])

                if not isInParentheses(mainCode, indexOfLink):
                    return link.attrs

    return None

startID = 'mw-content-text'     # Id of the start of the main content
endID = 'mw-data-after-content' # Id of the end of the main content
urlPrefix = 'https://en.wikipedia.org'
urlSuffix = '/wiki/Special:random'
linksVisited = set()

redirectedUrl = requests.get(urlPrefix + urlSuffix).url
urlSuffix = redirectedUrl[redirectedUrl.index('/wiki/'):]
print("Start: " + urlSuffix)

while True:
    if urlSuffix == '/wiki/Philosophy': # If we have reached the end
        print('\nWe have reached philosophy!')
        break

    if urlSuffix in linksVisited:       # If we have entered a loop
        print('\nWe are stuck in a loop!')
        break

    linksVisited.add(urlSuffix)
    link = getFirstLink(getHtmlCode(urlPrefix + urlSuffix))

    if link == None:    # If no links are returned (blank or referral pages)
        print('\nWe have reached a dead end!')
        break
    else:
        print(link['title'])
        urlSuffix = link['href']
