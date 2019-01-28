import argparse
import json
import os
import time
from ppomppu_scraper import yield_parsed_page


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, default='./output/', help='Output directory')
    parser.add_argument('--sleep', type=float, default=1.5, help='Sleep time for each submission (post)')
    parser.add_argument('--parameters', type=str, default='phone3 12 3 mini 9 3 camera 14 3', help='id divpage max_page')
    #parser.add_argument('--parameters', type=str, default='phone3 12 1800 mini 9 1300 camera 14 2000', help='id divpage max_page')
    parser.add_argument('--debug', dest='debug', action='store_true')

    args = parser.parse_args()
    directory = args.directory
    sleep = args.sleep
    parameters = args.parameters
    debug = args.debug

    parameters = parameters.split()
    n = len(parameters)
    if n % 3 != 0:
        raise ValueError('Check boards argument')
    m = int(n/3)
    idxs = [parameters[3*i] for i in range(m)]
    divpages = [parameters[3*i+1] for i in range(m)]
    max_pages = [int(parameters[3*i+2]) for i in range(m)]

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    def write(path, buffer):
        with open(path, 'a', encoding='utf-8') as f:
            for page in buffer:
                page_str = json.dumps(page, ensure_ascii=False)
                f.write('{}\n'.format(page_str))

    for idx, divpage, max_page in zip(idxs, divpages, max_pages):
        buffer = []
        path = '{}/{}'.format(directory, idx)
        for i, page in enumerate(yield_parsed_page(idx, divpage, max_page, sleep, debug)):
            buffer.append(page)
            if i % 20 == 0 and i > 0:
                write(path, buffer)
                buffer = []
        if buffer:
            write(path, buffer)
        print('done with {}\n\n'.format(idx))

if __name__ == '__main__':
    main()