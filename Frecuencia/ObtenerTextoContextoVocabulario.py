import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

#quito la parte del html, solo me quedo con el texto
stopwords = set(stopwords.words('spanish'))
f=open('e961024.htm',encoding='utf-8')
text=f.read()
f.close()

soup=BeautifulSoup(text,'lxml')
text=soup.get_text()

tokens=re.findall(r'(?!\\+|_|`|.\\)[A-zÁ-úÄ-ü]+',str(text).lower())
tokens=[w for w in tokens if not w in stopwords]
textoRaro=tokens;

#guardo el texto tokenizado
f=open('textoTokenizado.txt','w')
for palabra in textoRaro:
    f.write(palabra+'\n')
f.close()

newText=[]
from nltk.stem import SnowballStemmer 
spanish = SnowballStemmer("spanish")
for word in textoRaro:
    newText.append(spanish.stem(word))

f=open('textoStem.txt','w')
for palabra in newText:
    f.write(palabra+'\n')
f.close()

#guardar el vocabulario
tokens=set(tokens)
tokens=sorted(tokens)
print("Tokens sin stem: ",len(tokens))
tokens=set(newText)
tokens=sorted(tokens)
f=open('vocabulario.txt','w')
for palabra in tokens:
    f.write(palabra+'\n')
f.close()
print("Token son stem: ",len(tokens))


windowSize=8
contexto=[]
contextoChido={}
for w in tokens:
    contexto=[]
    for i in range(len(newText)):
        if newText[i]==w:
            for j in range(i-int(windowSize/2),i):
                if j >=0:
                    contexto.append(newText[j])
            try:
                for j in range(i+1, i+(int(windowSize/2)+1)):
                    contexto.append(newText[j])
            except IndexError:
                pass
    contextoChido[w]=contexto
    del(contexto)


#guarda los contextos[palabra]
from pickle import dump
output=open('contexto.pkl','wb')
dump(contextoChido,output,-1)
output.close()