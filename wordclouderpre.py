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

text=""
sc=input("Source")
de=input("Destination")
#req: orig, desti, keyw

#=====
with open('negative Keywords.csv', 'rU') as infile:
  
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
wordlist=[]
for i in range(0,len(orig)):
    if((sc==orig[i]) and (de==desti[i])):
    #collect keyword corresponding to i
        wordlist.append(keyw[i])
print(len(wordlist))
stringer=" " 
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

plt.savefig("worderer.jpg") 
