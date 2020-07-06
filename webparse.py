from googlesearch import search
from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer



# gives a list
def flist(link):
    tk = RegexpTokenizer(r'\w+')
    url = link
    sw=stopwords.words('english')
    ps = PorterStemmer()
    info = requests.get(url)

    textlist = ''

    
    soup = BeautifulSoup(info.text, "html5lib")
    for script in soup(["script", "style"]):
        script.extract()

    textlist = tk.tokenize(soup.get_text())


    wordlist=[]
    for x in textlist:
        if x not in sw:
            wordlist.append(x)

    for x in range(len(wordlist)):
        wordlist[x]=ps.stem(wordlist[x])


    return wordlist




# query = input()

def giveQueryandgetString(query):
    searched_links=search(query, tld="co.in", num=5,stop = 4,pause=2)

    resultString = ''

    for i in searched_links:
        # print(i)
        links_wordlist=flist(i)
        for x in links_wordlist:
            x+=' '
            resultString+= x
    return resultString


# print(giveQueryandgetString('suhas gumma'))

