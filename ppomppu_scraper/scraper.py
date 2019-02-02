import time
from .utils import get_soup
from .parser import parse_page

base = 'http://www.ppomppu.co.kr/zboard/zboard.php?id={}&divpage={}&page={}'

def yield_parsed_page(id_, divpage, max_page=3, sleep=1.0, debug=False):
    for page in range(1, max_page + 1):
        url = base.format(id_, divpage, page)
        soup = get_soup(url)
        links = soup.select('tr[class=list0] a[href^="view.php?"]')
        urls = ['http://www.ppomppu.co.kr/zboard/%s' % a.attrs.get('href', '').replace('&amp;', '') for a in links]
        urls = list(set(urls))
        if debug:
            urls = urls[:5]
        for url in urls:
            information = parse_page(url)
            yield information
            time.sleep(sleep)
        print('scrap {} from {} / {} pages'.format(id_, page, max_page))