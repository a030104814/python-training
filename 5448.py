# a = ""
# l =""
# l = [i for i in range(100)]
# l2 = str(l)


# for i in range (1,10,2):
#     print(i)


# def Apple (a):
#
#     k = 100 + a
#
#     print(k)
#
# Apple(1)

# score = int(input(''))
#
#
# if score > 100 :
#     print("Apple")
# elif score > 50 :
#
#     print("Dog")
# else :
#     print("Cat")



# for i in range(100):
    # a+=str(i)+","

# print(type(a))
# ss = str(l)
# print (ss)

# '1,2,3'
#
# listToStr = ' '.join(map(str, l))
#
#
#
# print(listToStr)
#
# l2 = ['1','2']
#
# listToStr2 = ' '.join(map(str, l2))
#
#
# print(listToStr2)
# n = int(input('輸入一個正整數:'))
#
# for c in range(2,n):
#     if n % c == 0:
#         print('不是質數')
#         break
#     elif c == n-1:
#         print('是質數')
# if n == 2:
#      print('是質數')

# import lightgbm
# import catboost as cb
# from sklearn import metrics
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import GridSearchCV
# import xgboost as xgb
# from sklearn import metrics
# import tensorflow as tf
# import numpy as np

# class MyClass:
#     def sum(self,a,b):
#         # 返回2個參數的和."
#         total = a+b
#         # print("函數內 : ", total)
#         return total
#
# r = MyClass().sum(1,2)
#  調用sum函數
#  total = sum(1,2)
# print("函數外 : ", r)

# def echo_word(word1,echo):
#     h = word1*echo
#     return h


# echo_word = (lambda word1, echo: word1 * echo)


# result = echo_word('hey', 5)


# print(result)


# L=[('b',2),('a',1),('c',3),('d',4)]

# L=sorted(L, key=lambda z:z[1])               # 利用key

# print(L)


# import pandas as pd
#
# calories = {"day1": 420, "day2": 380, "day3": 390}
#
# myvar = pd.Series(calories, index = ["day1", "day2"])
#
# print(type(myvar))

# stop_words = {'their', 'then', 'not', 'ma', 'here', 'other', 'won', 'up', 'weren', 'being', 'we', 'those', 'an', 'them', 'which', 'him', 'so', 'yourselves', 'what', 'own', 'has', 'should', 'above', 'in', 'myself', 'against', 'that', 'before', 't', 'just', 'into', 'about', 'most', 'd', 'where', 'our', 'or', 'such', 'ours', 'of', 'doesn', 'further', 'needn', 'now', 'some', 'too', 'hasn', 'more', 'the', 'yours', 'her', 'below', 'same', 'how', 'very', 'is', 'did', 'you', 'his', 'when', 'few', 'does', 'down', 'yourself', 'i', 'do', 'both', 'shan', 'have', 'itself', 'shouldn', 'through', 'themselves', 'o', 'didn', 've', 'm', 'off', 'out', 'but', 'and', 'doing', 'any', 'nor', 'over', 'had', 'because', 'himself', 'theirs', 'me', 'by', 'she', 'whom', 'hers', 're', 'hadn', 'who', 'he', 'my', 'if', 'will', 'are', 'why', 'from', 'am', 'with', 'been', 'its', 'ourselves', 'ain', 'couldn', 'a', 'aren', 'under', 'll', 'on', 'y', 'can', 'they', 'than', 'after', 'wouldn', 'each', 'once', 'mightn', 'for', 'this', 'these', 's', 'only', 'haven', 'having', 'all', 'don', 'it', 'there', 'until', 'again', 'to', 'while', 'be', 'no', 'during', 'herself', 'as', 'mustn', 'between', 'was', 'at', 'your', 'were', 'isn', 'wasn'}
# tokenized_sent = ['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'The', 'weather', 'is', 'great', ',', 'and', 'city', 'is', 'awesome', '.', 'The', 'sky', 'is', 'pinkish-blue', '.', 'You', 'should', "n't", 'eat', 'cardboard']
#
#
# filtered_sent=[]
# for w in tokenized_sent:
#     if w not in stop_words:
#         filtered_sent.append(w)
# print("Tokenized Sentence:",tokenized_sent)
# print("Filterd Sentence:",filtered_sent)



