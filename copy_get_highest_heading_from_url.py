from  urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd


def h1(i):
    try:
        print(i)
        print("Inside Finc")
        reqs = requests.get(i, timeout=10)
        soup = BeautifulSoup(reqs.text, 'lxml')
        print("Parsing")
        for heading in soup.find_all("h1"):
            heading_tag = heading.name
            if "h1" in heading_tag:
                x=heading.text.strip()
        print(x)
        return x
    except:
        pass

def h2(i):
    try:
        print(i)
        print("Inside Finc")
        reqs = requests.get(i, timeout=10)
        soup = BeautifulSoup(reqs.text, 'lxml')
        print("Parsing")
        for heading in soup.find_all("h2"):
            heading_tag = heading.name
            if "h2" in heading_tag:
                x=heading.text.strip()
        print(x)
        return x
    except:
        pass





