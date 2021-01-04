# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 02:21:09 2020

@author: Brandon
"""
import nltk
#obtener vocabulario
f=open('vocabulario.txt')
vocabulary=f.read()
f.close()
vocabulary=nltk.word_tokenize(vocabulary)

#obtener vector contexto
from pickle import load
f=open('vector.pkl','rb')
vectors=load(f)
f.close

#-------------------------Palabra a buscar-------------------------
word='grand'

import numpy as np
vec=vectors[word]
vec=np.array(vec)

cosines={}
for voc in vocabulary:
    vector=vectors[voc]
    vector=np.array(vector)
    cosine=np.dot(vec,vector)/((np.sqrt(np.sum(vec ** 2)))*(np.sqrt(np.sum(vector ** 2))))
    cosines[voc]=cosine

#ordenando por el valor del coseno
import operator
cosines=sorted(cosines.items(),
               key=operator.itemgetter(1),
               reverse=True)

#guarda lo obtenido
f=open('palabras similiares de ' + word + '.txt','w')
for item in cosines:
    word=item[0]
    cosine=item[1]
    string=str(word)+' '+str(cosine)+'\n'
    f.write(string)
f.close()