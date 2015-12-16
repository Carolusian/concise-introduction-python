# menu.py

import urllib.request

URL = "http://www.central.edu/go/gcsmenu"

def getpage(url):
    with urllib.request.urlopen(url) as f:
        return str(f.read())

def gettag(page, tag, start=0):
    opentag = "<" + tag + ">"
    closetag = "</" + tag + ">"
    i = page.find(opentag, start)
    if i == -1:
        return None, i
    j = page.find(closetag, i)
    return page[i + len(opentag):j], j

def process(page):
    heading, i = gettag(page, "h2")
    result = "\n" + heading.center(60) + "\n\n"
    day, i = gettag(page, "h3", i)
    while day is not None:
        result += day + "\n"
        meal, i = gettag(page, "p", i)
        result += "  " + meal.strip("<>p") + "\n"
        day, i = gettag(page, "h3", i)
    return result
    
def main():
    page = getpage(URL)
    print(process(page))
    
main()
