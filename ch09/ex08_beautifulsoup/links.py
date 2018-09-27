# p314

"""example usage
$ python links.py http://boingboing.net"""


def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup

    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get("href") for element in doc.find_all("a")]
    return links


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("2 arguments are required.")
    else:
        for url in sys.argv[1:]:
            print("Links in", url)
            for num, link in enumerate(get_links(url), start=1):
                print(num, link)
            print()
