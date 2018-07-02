##import dash
##import dash_core_components as dcc
##import dash_html_components as html
##from dash.dependencies import Input, Output
##import base64
##import plotly.plotly as py
##from plotly.graph_objs import *
##import pandas_datareader.data as web
##import datetime
##import dash
##import dash_core_components as dcc
##import dash_html_components as html
##from dash.dependencies import Input, Output
##import csv
##import dash_html_components as html
##from itertools import chain
##from wordcloud import WordCloud
##import matplotlib.pyplot as plt
##import numpy as np
##from PIL import Image
import csv
import time
import base64
import os
import collections
            
##
#=====
 
    
with open('nk.csv', 'rU') as infile:
  
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
desti=[]
desti=data["DESTINATION"]


des=[]
uniqo=list(set(orig))
#uniqd=list(set(desti))
###d = collections.defaultdict(list)
##d={}
##e={}
##for i in uniqo:
##  flag=0
##  for j in range(0,len(orig)):
##    
##    if(i==orig[j]):
##      des.append(desti[j])
####  print(i)
####  des=list(set(des))
####  print(des)
####  print("\n")
##  des=list(set(des))
##  for k in des:
##    
##    
##    d.setdefault(i, []).append(k)
##
##        
##        #d.setdefault(orig[j], []).append(desti[j])
####s = set( val for dic in d for val in dic.values())
####print(s)
####
####unique_values = set(chain.from_iterable(d.values() for d in dictionaries_list))
####for value in unique_values:
####    print(value)
####
####print(len(unique_values))
####for value in set(chain.from_iterable(d.values() for d in dictionaries_list)):
des=[]
new=[]
new=list(zip(orig, desti))
print(new)
for j in uniqo:
  
  for i in range(0,len(orig)):
    if((new[i][0])==(j)):
      des.append(new[i][1])
  print(j)
  print(des)
  print("====")
