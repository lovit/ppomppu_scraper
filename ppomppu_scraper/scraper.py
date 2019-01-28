import time


def yield_page(id_, divpage, base, max_page=3, sleep=1.0):
    for page in range(1, max_page + 1):
        url = base.format(id_, divpage, page)
        soup = get_soup(url)
        links = soup.select('tr[class=list0] a[href^=view.php?]')
        urls = ['http://www.ppomppu.co.kr/zboard/%s' % a.attrs.get('href', '').replace('&amp;', '') for a in links]
        for url in urls:
            page = parse_page(url)
            yield page
            time.sleep(sleep)
        print('scrap from {} / {} pages'.format(page, max_page))