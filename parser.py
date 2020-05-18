import requests
import lxml.html
import csv


def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    print(text_original[0])
    print(text_translate[0])
    name = get_name(url)
    return text_original, text_translate, name


def write_txt(url):
    text_original, text_translate, name = parse(url)
    with open("%s.txt" % name, "w", newline='', encoding='utf-8') as txt_file:
        leng = len(text_original)
        for i in range(leng):
            txt_file.write(text_original[i])
            txt_file.write(text_translate[i])


def write_csv(url):
    text_original, text_translate, name = parse(url)
    with open("%s.csv" % name, "w", newline='', encoding='utf-8') as csv_file:
        leng = len(text_original)
        write = csv.writer(csv_file)
        tmp = []
        for i in range(leng):
            tmp.append(text_original[i])
            tmp.append(text_translate[i])
        write.writerow(tmp)


def get_name(url):
    return url.split("/")[-1].split(".")[0]


def main():
    url = "https://www.amalgama-lab.com/songs/i/i_am_giant/death_of_you.html"
    write_txt(url)
    write_csv(url)

if __name__ == "__main__":
    main()
