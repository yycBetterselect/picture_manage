import requests
from lxml import etree


def get_picture_url():
    url = "https://www.nvshens.net/gallery/dachidu/"
    res = requests.get(url=url)
    result = res.content.decode()
    tree = etree.HTML(result)
    li_list = tree.xpath('//*[@id="listdiv"]/ul/li')
    print(li_list)
    href_list = []
    for li in li_list:
        href = li.xpath('div[1]/a/@href')[0]
        href = "https://www.nvshens.net" + href
        print(href)
        href_list.append(href)
    # print(result)
    print(href_list)


if __name__ == '__main__':
    get_picture_url()

































