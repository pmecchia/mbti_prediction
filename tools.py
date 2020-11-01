import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = stopwords.words("english")
porter = PorterStemmer()

def cleanData(posts):
    # Lowercase
    clean_text = posts.lower()
    #remove all hyperlinks
    clean_text = re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})','',clean_text)
    word_list = word_tokenize(clean_text)
    clean_posts = []
    for word in word_list:
        if word.isalpha() and word not in stop_words:
            word = porter.stem(word)
            clean_posts.append(word)
    return " ".join(clean_posts)

def type_prediction(data,pred_EI,pred_NS,pred_TF,pred_PJ):
    result_IE = pred_EI.predict(data)
    result_NS = pred_NS.predict(data)
    result_TF = pred_TF.predict(data)
    result_PJ = pred_PJ.predict(data)
    return f'{result_IE[0]}{result_NS[0]}{result_TF[0]}{result_PJ[0]}'
