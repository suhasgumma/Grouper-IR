import webparse
import clustering


def getClusters(queryList):

    count = 0

    no_of_clusters = int(input('enter the no of clusters: '))
    stringList = []
    for query in queryList:
        # queryList.append(query)
        string = webparse.giveQueryandgetString(query)
        stringList.append(string)

    cluster_list = clustering.clusterthedocs(stringList,no_of_clusters)

    returnList = []
    for i in cluster_list:
        rLL = []
        for j in i:
            rLL.append(queryList[j])
        returnList.append(rLL)

    return returnList


def printList(clusterList):
    for i in range(len(clusterList)):
        string = ''
        for j in clusterList[i]:
            string+= j+ ' '+','
        print('Cluster '+ str(i+1)+ ': '+ string)


queryList = []
i = 1
while  i != '0':
    i = input('Enter the query, if you are done enter 0: ')
    if i != '0':
        queryList.append(i)

cl = getClusters(queryList)

printList(cl)










    

    
