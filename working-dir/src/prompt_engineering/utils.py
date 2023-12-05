import requests
import json

from bs4 import BeautifulSoup


def get_page_content(url):
    # Real response

    # r = requests.get(url)
    # content = r.text

    # Mocking the response
    with open("mock.html", "r") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    for script in soup.find_all("script"):
        script.decompose()
    for svg in soup.find_all("svg"):
        svg.decompose()
    for foot in soup.find_all("footer"):
        foot.decompose()
    return soup.find("body").text
