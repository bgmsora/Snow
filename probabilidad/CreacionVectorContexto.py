# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 01:39:26 2020

@author: Brandon
"""
import nltk
import numpy as np
#obtener vocabulario
f=open('vocabulario.txt')
vocabulary=f.read()
f.close()
vocabulary=nltk.word_tokenize(vocabulary)

#print(vocabulary[:50])

#Obtener el vector contexto
from pickle import load,dump
f=open('contexto.pkl','rb')
contexts=load(f)
f.close

vectors={}
counter=0
for word in vocabulary:
    context=contexts[word]
    vector=[]
    for voc in vocabulary:
        vector.append(context.count(voc))
    vectors[word]=vector
    counter+=1
    del(vector)

counter=0
for valor in vectors:
    vector=[]
    valor=np.array(valor)
    for voc in vocabulary:
        vector.append(context.count(voc))
    vectors[word]=vector
    counter+=1
    del(vector)

#print(vectors['grand'])
#creacion del vector probabilidad
for word in vocabulary:
    vector=[]
    vector2=[]
    vector=vectors[word]
    vec=np.array(vector)
    div=np.sum(vec)
    for valor in vector:
        vector2.append(valor/div)
    vectors[word]=vector2
    del(vector)
    del(vector2)

print("vector proba")
#print(vectors['grand'])
#guardando
output=open('vector.pkl','wb')
dump(vectors,output,-1)
output.close()