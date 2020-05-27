import requests
import os

urls = ['https://images.pexels.com/photos/853199/pexels-photo-853199.jpeg',
        'https://images.pexels.com/photos/1402787/pexels-photo-1402787.jpeg',
        'https://images.pexels.com/photos/1213447/pexels-photo-1213447.jpeg'
]


def get_file(url):
    r = requests.get(url, stream=True)
    return r


def get_name(url):
    name = url.split('/')[-1]
    folder = url.split('/')[3]
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.abspath(folder)
    return os.path.join(path, name)


def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chung in file_object.iter_content(8192):
            f.write(chung)


def main():
    for url in urls:
        save_image(get_name(url), get_file(url ))


if __name__ == '__main__':
    main()