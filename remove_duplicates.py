directory = 'output'

from glob import glob

#paths = glob('{}/*'.format(directory))
paths = ['output/mini', 'output/phone3']

for path in paths:
    exists = set()
    with open(path, encoding='utf-8') as f:
        docs = [doc.strip() for doc in f]
    with open(path, 'w', encoding='utf-8') as f:
        for doc in docs:
            if doc in exists:
                continue
            f.write('{}\n'.format(doc))
            exists.add(doc)
    print('done with {}'.format(path))