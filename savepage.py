import ssl
import os
from termcolor import colored
from urllib import request
from urllib.request import Request, urlopen
from html.parser import HTMLParser

# proxy_support = request.ProxyHandler(
#     {'http' : 'http://LipatkinAE:GRANCH.LOCAL:Pro100tema@10.87.1.18:8080', 
#     'https': 'http://LipatkinAE:GRANCH.LOCAL:Pro100tema@10.87.1.18:8080'})
# opener = request.build_opener(proxy_support)
# request.install_opener(opener)

mainDir = "./bookmarks"
currDir = mainDir
currTag = ""
href = ""
context = ssl._create_unverified_context()

def downloadPage(url, path, name):
    print(url)
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        pageName = path + "/" + name + ".html"

        if os.path.exists(pageName):
            return

        with urlopen(req, context=context, timeout=3) as response:
            page_content = response.read()
            with open(pageName, 'wb') as fid:
                fid.write(page_content)
    except Exception as e:
        print(e)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global currTag
        global href

        tag = tag.strip().lower()
        currTag = tag
        print(f"Start tag : {tag}")
        if tag == 'a':
            for x in attrs:
                if x[0] == 'href':
                    href = x[1]

    def handle_endtag(self, tag: str):
        global currDir
        global currTag

        tag = tag.strip().lower()
        currTag = tag
        if tag == 'dl':
            currDir = currDir[:currDir.rindex('/')]
            print(currDir)

        if tag == 'dl':
            tag = colored(tag, color='red')
        print(f"End tag   : \\{tag}\n")

    def handle_data(self, data):
        global currTag
        global currDir
        global href

        data = data.strip()
        if len(data) <= 0:
            return
        print(f"Some data : {data}")

        if (currTag == 'h3'):
            data = data.replace('/', '-')
            currDir = currDir + "/" + data
            if not os.path.exists(currDir):
                os.mkdir(currDir)
            print(currDir)
            # input('press enter')
        elif currTag == 'a':
            dirName = data if len(data) <= 100 else data[:100]
            dirName = dirName.replace('/', '-')
            pagePath = currDir + "/" + dirName
            if not os.path.exists(pagePath):
                os.mkdir(pagePath)
            downloadPage(href, pagePath, dirName)

if __name__ == "__main__":


    parser = MyHTMLParser()
    with open('bookmarks.html', 'r') as htmlFile:
        parser.feed(htmlFile.read())