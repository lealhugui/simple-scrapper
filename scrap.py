# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def extract_links(html):
    if html is None:
        return []
    html = BeautifulSoup(html, 'html.parser')
    ref_list = []
    a_list = html.find_all('a')
    for a in a_list:
        try:
            link = a['href']
            if 'http' in link or 'https' in link:
                ref_list.append(link)
        except:
            pass

    return ref_list


def work(URL, items=[]):

    if len(items) >= 50:
            return items

    ref_list = []

    try:
        response = requests.get(URL)
    except:
        return
    if response.status_code != 200:
        return
    html = response.text

    if html is None:
        return

    ref_list = extract_links(html)

    for item in [href for href in ref_list if href not in items]:
        items.append(item)
        print("len(items)=%d" % len(items))
        work(item, items)

        if len(items) >= 50:
            return items

    return items


if __name__ == '__main__':
    print('peon: work work...')
    with open('link_list.txt', 'w+') as f:
        l = work('http://www.google.com')
        f.write(str(l))
    print('peon...work is done!')
