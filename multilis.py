import plotly.plotly as py
from plotly.graph_objs import *
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv
import dash_html_components as html
#from itertools import izip
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import csv
import time
import base64

text=""

#req: orig, desti, keyw

#=====
with open('negative Keywords.csv', 'rU') as infile: #negative Keywords
  
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

keyw= data['KEYWORDS']
orig=data['ORIGIN']
desti=data['DESTINATION']
sc=[]
de=[]
sc=orig
de=desti
wordlist=[]

comlis=[]
comlis=list(set(list(zip(orig,desti))))
print(len(comlis))

for j in range(158, len(comlis)):
    for i in range(0,len(orig)):
        if((comlis[j][0]==orig[i]) and (comlis[j][1]==desti[i])):
    #collect keyword corresponding to i
            wordlist.append(keyw[i])
    print(len(wordlist))
    stringer=" "
    text=""
    mile = [x + stringer for x in wordlist]
    text = text.join(mile);
#print(text)
    text=str(text)
#print(type(text))


    wordcloud=WordCloud().generate(text)
    plt.figure(figsize=(10,10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig(str(comlis[j][0]+comlis[j][1]+".png"))
    time.sleep(0.2)


#comlis= list(set(list(map(lambda x,y:[x,y],orig,desti))))
#for i in range(0,len(comlis)):

#print(comlis)
##print(comlis[0][0])
##print(comlis[0][1])
##print(comlis[1][0])
##print(comlis[1][1])
##print(comlis[2][0])
##print(comlis[2][1])

