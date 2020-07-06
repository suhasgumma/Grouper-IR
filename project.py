

from googlesearch import search
from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# nltk.download('stopwords')


# gives a list
def flist(link):
    tk = RegexpTokenizer(r'\w+')
    url = link
    sw=stopwords.words('english')
    ps = PorterStemmer()
    info = requests.get(url)

    soup = BeautifulSoup(info.text, "html5lib")

    textlist = tk.tokenize(soup.get_text())
    wordlist=[]
    for x in textlist:
        if x not in sw:
            wordlist.append(x)

    for x in range(len(wordlist)):
        wordlist[x]=ps.stem(wordlist[x])


    return wordlist




# query = input()
query = "ysr stadium"
searched_links=search(query, tld="co.in", num=10, stop=10, pause=2)
file = open("ppppp.txt", "w", encoding="utf-8")

for i in searched_links:
    p=i
    links_wordlist=flist(p)
    for x in links_wordlist:
        x+=' '
        file.write(x)

