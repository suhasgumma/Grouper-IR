import tfidf1
from gensim import corpora
from gensim.models import LsiModel


# find term dictionary....every unique term wil be in key.......
def form_term_dictionaty(strings):
    length = len(strings)

    list_of_wordlists = []
    for string in strings:
        s = string.split()
        list_of_wordlists.append(s)
    

    # forming dictionary
    dictionary = corpora.Dictionary(list_of_wordlists)
    doc_term_matrix = [dictionary.doc2bow(doc.split()) for doc in strings]

    return dictionary,doc_term_matrix


def createLsiModel(tdidfMatrix,termDict):
    lsaModel = LsiModel(tdidfMatrix, id2word=termDict)
    return lsaModel

def createLsiCorpus(stringArray):
    wordDict, doctermMatrix = form_term_dictionaty(stringArray)
    model = createLsiModel(doctermMatrix,wordDict)

    lsacorpus = model[doctermMatrix]

    lsacorpusf = []

    for x in lsacorpus:
        m = []
        for n in x:
            m.append(n[1])
        lsacorpusf.append(m)

    return lsacorpusf



# stringArray = ['this is designed for evaluating tfidf gibberish and all the stuff you are going to type','run for tdidf','stuff is old', 'old stuff is great', 'tfidf sucks suckss sss yeydh xdhjxhw xhjwxkbwjc hewjkhw xywbwnm']


# P = createLsiCorpus(stringArray)