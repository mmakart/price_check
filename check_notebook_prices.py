#!/usr/bin/env python3
import requests as req
import re
import time

urls = [url[:-1] for url in open('goods.txt', 'r').readlines()]

f = open('prices.log', 'a')

for url in urls:
    page = req.get(url)
    if url.find('citilink.ru') != -1:
        name_pattern_str = '"name": "(.+)"'
        price_pattern_str = '"price": "(\d+)"'
    elif url.find('nix.ru') != -1:
        name_pattern_str = '<title>([^<]+)</title>'
        price_pattern_str = 'meta itemprop="price" content="(\d+)"'
    else:
        name_pattern_str = ''
        price_pattern_str = ''

    # getting name of the notebook
    name_pattern = re.compile(name_pattern_str)
    name_arr = name_pattern.findall(page.text)
    if name_arr:
        name = name_arr[0]
    else:
        name = 'NONE'
    # finding out price
    price_pattern = re.compile(price_pattern_str)
    price_arr = price_pattern.findall(page.text)
    if price_arr:
        price = price_arr[0]
    else:
        price = 'NONE'
    
    datestr = time.asctime()
    print(datestr, name, price, url, sep='\t', file=f)

print(file=f)
f.close()
