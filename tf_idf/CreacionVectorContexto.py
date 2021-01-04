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

#este es el idf
cuantasVecesEsta={}
for palabra in vocabulary:
    esta=0
    for word in vocabulary:
        context=contexts[word]
        if palabra in context:
            esta=esta+1
    cuantasVecesEsta[palabra]=esta

print("grande aparece en ",cuantasVecesEsta["grand"]," contextos")
#print(len(cuantasVecesEsta))
#print("ya saque numero de repeticiones de contexto")

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

print("ya obtuve el vector probabilidad")
k=1.2
v_tf={}
for word in vocabulary:
    vector=[]
    vector2=[]
    vector=vectors[word]
    vec=np.array(vector)
    div=np.sum(vec)
    for valor in vector:
        vector2.append(((k+1)*valor)/(valor+k))
    v_tf[word]=vector2
    del(vector)
    del(vector2)
print("vtf vale")
print(len(v_tf))
print(len(cuantasVecesEsta))

this=[]
#de esta manera puedo obtener que tiene de valor cada palabra
for key in cuantasVecesEsta:
    #print(key,":",cuantasVecesEsta[key])
    this.append(cuantasVecesEsta[key])

print("abad: ",this[0])
#print(v_tf["grand"])
new={}
for word in vocabulary:
    vector=[]
    vector2=[]
    vector=v_tf[word]
    i=0
    for valor in vector:
        vector2.append(valor*this[0])
        i+=1
    new[word]=vector2
    del(vector)
    del(vector2)


print("Empiezo a guardar")
#print(new["grand"])

#guardando
output=open('vector.pkl','wb')
dump(new,output,-1)
output.close()