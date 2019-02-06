import json
import random
import urllib.request
import urllib
import ast
# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"


def download():
    """ This function downloads the json data from the url."""
    # TODO add code here
    urldata = urllib.request.urlopen(url) # request utl to open 
    data = json.loads(urldata.read().decode()) 
    data = json.dumps(data,separators=(',',':'))# loading json
    return data


def extract_requests(text:str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    # TODO add code here
    text1 = ast.literal_eval(text)
    return text1['promises']


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    # TODO add code here
    TList = []
    for i in promises:
        TList.append(i['title'])
    return TList


def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    # TODO add code here
    secure_random = random.SystemRandom()
    ranT =secure_random.choice(titles)
    return ranT

#text = download()
#promises = extract_requests(text)
#titles = extract_titles(promises)
#randomtitle = random_title(titles)
#print(f"A promise: {randomtitle}")


