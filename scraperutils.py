import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://nwmissouri.smartcatalogiq.com'


def makeSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html5lib')


def getAllClasses(url):
    soup = makeSoup(url)
    classlist = soup.find('ul', {'class': 'sc-child-item-links'})
    return {x.text.split()[1]: {'name': ' '.join(x.text.split()[2:]), 'url': BASE_URL + x['href']} for x in
            classlist.findAll('a')}


def getPrereqs(url):
    soup = makeSoup(url)
    return [x.text.split()[1] for x in soup.findAll('a', {'class': 'sc-courselink'})]
