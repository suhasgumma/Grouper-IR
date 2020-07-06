'''
Input: string array and the number of clusters
Output: clustered array

'''

from sklearn.cluster import KMeans
import numpy as np
import lsa

def clusterthedocs(stringArray, clusterNo):
    #Lsi Corpus
    lsad = lsa.createLsiCorpus(stringArray)

    numpied = np.array(lsad)

    #Generate Kmeans model.....
    kmeans_model = KMeans(n_clusters = clusterNo, precompute_distances='auto', random_state = 0).fit(numpied)

    # generate labels.....
    labels=kmeans_model.labels_.tolist()

    cluster_list = []

    for i in range(clusterNo):
        cluster_list.append([])

    for i in range(len(labels)):
        cluster_list[labels[i]].append(i)

    return cluster_list


# stringArray = stringArray = ['this is designed for evaluating tfidf gibberish','run for tdidf','stuff is old', 'old stuff is great', 'tfidf sucks suckss sss yeydh']
# clusterthedocs(stringArray, 3)





