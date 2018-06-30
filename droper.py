import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64
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
import os
##
#=====
with open('Negative Keyword.csv', 'rU') as infile:
  
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
    
def genwordcloud(sc,de):
    text=""

#req: orig, desti, keyw

    wordlist=[]
    if((len(sc)<3) or (len(de)<3)):
        return None
    try:
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
    except:
        print("Err in text gen")
    try:
        
        wordcloud=WordCloud().generate(text)
    except:
        print("texter")
   # try:
        #plt.figure(figsize=(10,10))
   # except:
   #     print("Err in FIG")
    try:

        plt.imshow(wordcloud, interpolation="bilinear")
    except:
        print("Err in imshow")
    try:
        plt.axis("off")
        plt.margins(x=0, y=0)
    except:
        print("Err in clouder")
    try:
        plt.savefig(str(sc+de+".png"))
        time.sleep(0.1)
        return None
    except:
        print("Err in saving ", sys.exc_info()[0])
        return None







##
app = dash.Dash()

app.layout = html.Div([
    html.H1("Word-Cloud"),
    dcc.Input(
        id='input-x',
        placeholder='Source',
        type='text',
        value='EWR',
    ),
    dcc.Input(
        id='input-y',
        placeholder='Destination',
        type='text',
        value='ORD',
    ),
    #html.Br(),
    
    html.Img(id= 'image') #src='data:image/png;base64,{}'.format(encoded_image.decode())

    ])


@app.callback(
    Output('image', 'src'),
    [Input('input-x', 'value'),
     Input('input-y', 'value')]
)
def update_result(x, y):
    try:
        nam=str(x+y)
        if(os.path.isfile("/home/pi/worder/main/"+nam+".png")):
            return 'data:image/png;base64,{}'.format((base64.b64encode(open(str(x+y+".png"), 'rb').read())).decode())
       
        elif((len(x)==3) and (len(y)==3)):
            genwordcloud(x,y)
            return 'data:image/png;base64,{}'.format((base64.b64encode(open(str(x+y+".png"), 'rb').read())).decode())
    except:
        print("Err in update result")

if __name__ == '__main__':
        app.run_server()
