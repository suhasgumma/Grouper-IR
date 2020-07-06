# Takes string and returns term frequency of each word in a dictionary...
def form_tf_dict(str):
    word_list = str.split()
    tf_matrix = {}

    for word in word_list:
        if word in tf_matrix:
            tf_matrix[word] += 1
        else:
            tf_matrix[word] = 1
    
    
    length = len(word_list)
    for word in tf_matrix:
        tf_matrix[word] /= length
    
    return tf_matrix

# Takes variable number of strings and returns doc frequency of each word in a dictionary
# doc frequency is the occurence of a word in the corpus of docs
def form_df_dict(strings):
    length = len(strings)

    # forming a dictionary of tf_dicts
    tfs_dict = {}

    for i in range(length):
        tfs_dict[strings[i]] = form_tf_dict(strings[i])
    
    

    # forming a list of words in all the documents(strings)....
    all_word_string = ''
    for string in strings:
        all_word_string += ' ' + string
    
    all_word_list = all_word_string.split()

    # forming df_dict......
    df_dict = {}

    for word in all_word_list:
        if word not in df_dict:
            count = 0
            for tfdict in tfs_dict.values():
                if word in tfdict:
                    count+=1
            df_dict[word] = count/length

    return df_dict



#Finally... Forming tf_idf MatriCES of all the docs.....
# TF-IDF matrix is a 2-d matrix.......
def form_tfidf_matrix(strings):
    length = len(strings)

    # forming a list of words in all the documents(strings)....
    all_word_string = ''
    for string in strings:
        all_word_string += ' ' + string
    
    all_word_list = all_word_string.split()

    tf_idf_matrix = []

    # Forming the tf-idf matrix of each string(doc).....
    for string in strings:

        tf_dict = form_tf_dict(string)
        df_dict = form_df_dict(strings)

        # Finding TF_IDF of each word.....
        visited = {}
        tf_idf_of_word = []
        for word in all_word_list:
            if word not in visited:
                visited[word] = True

                if word in tf_dict:
                    ans = tf_dict[word]/df_dict[word]
                else:
                    ans = 0
                
                tf_idf_of_word.append(ans)
        
        tf_idf_matrix.append(tf_idf_of_word)


    return tf_idf_matrix


# tfidfmatrices = form_tfidf_matrix(['this is designed for evaluating tfidf'])

# for matrix in tfidfmatrices:
#     print(matrix)
#     print('*****')







