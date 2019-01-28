from .utils import get_soup
from bs4 import BeautifulSoup
import re


date_pattern = re.compile('등록일: [\d]{4}-[\d]{2}-[\d]{2}')


def parse_page(url):
    soup = get_soup(url)
    informations = {
        'title': parse_title(soup),
        'contents': parse_contents(soup),
        'date': parse_date(soup)
    }
    return informations

def parse_contents(soup):
    td = soup.select('td[class=board-contents]')
    if not td:
        return ''
    td = BeautifulSoup(str(td).replace('<br/>', '\n'), 'lxml')
    text = [s.strip() for s in td.text.split('\n')]
    text = [s for s in text if s]
    text = '\n'.join(text)
    if text[:2] == '[\n':
        text = text[2:].strip()
    if text[-2:] == '\n]':
        text = text[-2:].strip()
    return text

def parse_title(soup):
    font = soup.select('font[class=view_title2]')
    if not font:
        return ''
    title = font[0].text.strip()
    return title

def parse_date(soup):
    match = date_pattern.findall(str(soup.select('td[class=han]')))
    if match:
        match = match[0][5:]
    else:
        match = ''
    return match