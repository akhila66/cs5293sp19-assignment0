import json
import random
import urllib.request
import urllib
# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"


def download():
    """ This function downloads the json data from the url."""
    # TODO add code here
    urldata = urllib.request.urlopen(url) # request utl to open 
    data = json.loads(urldata.read().decode()) # loading json
    print(data)
    return data


def extract_requests(text:str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    # TODO add code here
    # print(text['promises'])
    return text['promises']


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    # TODO add code here
    TList = []
    for i in promises:
        print(i['title'])
        TList.append(i['title'])
    return TList

