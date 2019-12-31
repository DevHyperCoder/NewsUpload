import re

import html5lib
import lxml
import requests
import urllib3
from bs4 import BeautifulSoup

DEBUG = False


def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    if url.__contains__("https://gadgets.ndtv"):
        print("gadegets")

        url = url.replace("\n", '')
        r = requests.get(
            url,
            headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        # print('\n'.join([i.text for i in soup.select('.description p')]))
        return '\n'.join([i.text for i in soup.select('.description p')])

    # TODO complete the parsing for verge and bgr
    if url.__contains__("https://www.theverge.com/"):
        text = ""
        headers = {'User-Agent': 'Mozilla/5.0'}
        print("the verge.com")
        if url.__contains__("\n"):
            url = url.replace("\n", "")

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        div_for_text = soup.find_all("p")
        text = ""
        for tag in div_for_text:
            text += tag.text
            text += "\n"

        if DEBUG:
            print(text)

        return text

    if url.__contains__('https://www.bgr.in/'):
        print("bgr.com")
        if url.__contains__("\n"):
            url = url.replace("\n", "")

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        tags = soup.find_all("div", {'class': 'article-content'})
        text = '\n'.join([i.text for i in soup.select('.article-content p')])
        return text

    if url.__contains__('https://indianexpress.com/'):
        print("bgr.com")
        if url.__contains__("\n"):
            url = url.replace("\n", "")

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        text = '\n'.join([i.text for i in soup.select('.l-container p')])
        print(text)
        return text


def parse_title(url):
    if url.__contains__("https://gadgets.ndtv"):
        print("gadegets")
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = url.replace("\n", '')
        r = requests.get(
            url,
            headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        h1 = soup.find("h1", {"itemprop": "headline"})

        print(h1.text)
        return h1.text

    if url.__contains__("https://www.theverge.com/"):
        print("verge")
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = url.replace("\n", '')
        r = requests.get(
            url,
            headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        h1 = soup.find("h1")

        print(h1.text)
        return h1.text
    if url.__contains__('https://www.bgr.in/'):
        print("bgr")
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = url.replace("\n", '')
        r = requests.get(
            url,
            headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

        title = soup.find("h1", {"class": "title_name"})
        print(title.text)
        return title.text

    if url.__contains__('https://indianexpress.com'):
        print("indian express")
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = url.replace("\n", '')
        r = requests.get(
            url,
            headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

        title = soup.find("h1", {"class": "m-story-header__title"})

        print(title.text.replace("\n", "").replace("\t", ""))

        return title.text.replace("\n", "").replace("\t", "")
