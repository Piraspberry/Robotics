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

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import csv




#masker=np.array(Image.open("ual.jpg"))
text=""
with open('Negative Keyword.csv', 'rU') as infile:
  
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

miles= data['KEYWORDS']
orig=data['ORIGIN']
desti=data['DESTINATION']

def ocounter(stri):
    return(orig.count(stri))
def dcounter(stri):
    return(desti.count(stri))
    
    


stringer=" " 
mile = [x + stringer for x in miles]
text = text.join(mile);
#print(text)
#text=str(text)
#print(type(text))

#stri=input("Enter")
#print(ocounter(stri))
uniqo=list(set(orig))
uniqd=list(set(desti))
uniqoctr=[]
uniqdctr=[]
for i in uniqo:
    uniqoctr.append(ocounter(i))
for i in uniqd:
    uniqdctr.append(dcounter(i))
    #print("{} is {} times".format(i, ocounter(i)))
#print(uniqoctr)
##pv = pd.pivot_table(df, index=, columns=["ORIGIN"], values=[''], aggfunc=sum, fill_value=0)
##
##
##trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
##trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
##trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
##trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

#########

sl=["EWR","BOM","AMS"]
sln=["10","8","50"]
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Feedback Analysis'),
    html.Div([
	html.Label(html.H5("  United Airlines Flight Feedback Analysis Trends   ")),
        dcc.Graph(
            id='example-graph4',
            figure={
                #for i in range(0, len(uniqo)):
                'data': [
                    {'x':sl,'y': sln, 'type': 'bar'},
##		    {'x':uniqo[1],'y': uniqoctr[1], 'type': 'bar'},
##                    {'x':uniqo[2],'y': uniqoctr[2], 'type': 'bar'},
##                    {'x':uniqo[3],'y': uniqoctr[3], 'type': 'bar'},
##                    {'x':uniqo[4],'y': uniqoctr[4], 'type': 'bar'},
                    ],

                'layout': {
                    #'title':"Miles vs Cost",
                    'height':400,
                    #'paper_bgcolor': colors['bg5'],
                    #'plot_bgcolor':colors['bg5'],
                    'barmode':'stack',
                    #'font': {
                    #    'color': colors['txtblack']
                    #    }
                    }
                },
            ),
        ],
        style={'width': '80%','display': 'inline'},
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)
