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
import pandas as pd
##
#=====
mostNegativeDF = pd.read_csv(
    "/home/pi/worder/main/mostNegativeDF.csv"
)
glx=""
gly=""
#=pd.read_csv()
def negativecomments(text):
    origin=glx
    destination=gly

    airportDF = mostNegativeDF[mostNegativeDF['ORIGIN_AIRPORT'] == origin]
    airportDF = airportDF[airportDF['DEST_AIRPORT'] == destination]
#######
    negativeCommentsResults = airportDF[airportDF['VERBATIM_EN'].str.contains(text)]
    negativeCommentsResults = negativeCommentsResults.reset_index()

    negativeCommentsResults = negativeCommentsResults.drop(['SentimentValue','MILEAGEPLUS','ORIGIN_COUNTRY_CODE','ORIGIN_ST_CODE','DEST_COUNTRY_CODE','DEST_ST_CODE','ACTUAL_ARRIVAL_DATETIME','ACTUAL_DEPARTURE_DATETIME','SCHEDULE_ARRIVAL_DATETIME','SCHEDULE_DEPARTURE_DATETIME','ARRIVAL_DELAY_MIN','DEPARTURE_DELAY_MINS','DELAY_CODE','DELAY_TYPE','DELAY_CD_DSCR','DEPARTURE_GATE','CABIN_CLASS','CARRIER','EQUIP_CODE','EQUIP_TYPE','FLEET_GROUP','FLEET_TYPE_DESC','FLEET_USAGE','RECORD_LOCATOR','SCHEDULE_MILES','SCH_BLK_MIN','SEATNBR','TAIL_NBR','GH_GATE','GH_LOBBY','GH_RAMP','MEDIA_EQUIP','SURVEYED_LEG_ID','TOTAL_FLIGHT_LEG','CHKD_BAG_IND','CABIN_TYPE','Q_LANGUAGE','SSR','TOTAL_DURATION','SURVEY_TYPE_DESC','LANG','ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|E_PO_AVAIL_SAT','ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|E_DIRECTV_EN_SAT','ONBOARD|PRIMARY|WI-FI|E_WIFI_SAT', 'ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|E_PDE_EN_SAT','ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|E_MAIN_SCR_EN_SAT', 'AIRPORT|PRIMARY|BAGGAGE|EXP_BAGGAGE','AIRPORT|PRIMARY|GATE|EXP_GATE','AIRCRAFT|PRIMARY|CABIN COMFORT|CCE_SEAT_AREA', 'EXCLUDE FROM AIRPORT|PRIMARY|CONNECTION|AIRPORT_EXP_DISTANCE_SAT','EXCLUDE FROM AIRPORT|PRIMARY|CONNECTION|AIRPORT_EXP_TIME_SAT', 'EXCLUDE FROM AIRPORT|PRIMARY|CONNECTION|AIRPORT_EXP_SIGN_SAT','IRROPS-IRROPS_DH_EXP_SAT', 'AIRCRAFT|PRIMARY|CABIN CLEANLINESS|CCE_SMTHG_DIRTY', 'ONBOARD|PRIMARY|FOOD & BEVERAGE|OBE_FOOD_BEVER','AIRPORT|PRIMARY|SECURITY|EXP_TSA', 'AIRCRAFT|PRIMARY|CABIN APPEARANCE|CCE_SMTHG_POOR_CONDITION', 'AIRPORT|PRIMARY|CHECK-IN|EXP_CHECK_IN','ONBOARD|PRIMARY|INFLIGHT SERVICE|OBE_FA', 'AIRPORT|PRIMARY|CLUB|EXP_LOUNGE', 'NOT FOR REPORTING|PRIMARY|NET PROMOTER SCORE|RECOMMEND','AIRCRAFT|PRIMARY|WORKABILITY|ONBORD_WORKING_YN', 'ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|SEATBACK_SCREEN_SAT','ONBOARD|PRIMARY|INFLIGHT ENTERTAINMENT|SEATBACK_SCREEN_LOOP_SAT','|PRIMARY|FLIGHT ATTENDANT|FA_RECOGNIZE','GENDER','DOCUMENT_ID','TITLE','FIRST_NAME','LAST_NAME','index','Sentiment','Unnamed: 0','OVERALL SATISFACTION|PRIMARY|OVERALL SATISFACTION|SAT_SCORE' ,'|PRIMARY|NET PROMOTER SCORE NEW (1-10)|RECOMMEND1_10','DEST_AIRPORT','ORIGIN_AIRPORT','FLIGHTNUMBER','MMILER','RESP_GRP','MPLEVEL'], axis = 1)
    return negativeCommentsResults
#print(negativeCommentsResults)

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
skw=list(set(keyw))
def genwordcloud(sc,de):
    text=""

#req: orig, desti, keyw

    wordlist=[]

    try:
        for i in range(0,len(orig)):
            if((sc==orig[i]) and (de==desti[i])):
    #collect keyword corresponding to i
                wordlist.append(keyw[i])
    except:
        print("before")
        #print(len(wordlist))
    try:
        stringer=" " 
        mile = [x + stringer for x in wordlist]
        text = text.join(mile);
#print(text)
        text=str(text)
#print(type(text))
    except:
        print("exce")
    try:
        wordcloud=WordCloud().generate(text)
        plt.figure(figsize=(10,10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        #plt.margins(x=0, y=0)

        plt.savefig(str(sc+de+".png"))
        time.sleep(0.1)
        
    except:
        print("Source and Destination not matching")
    return None
        







##
app = dash.Dash()

app.layout = html.Div([
    html.Div([
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
    
    html.Img(id= 'image'),
##        'layout': {
##            #'title':"Miles vs Cost",
##            'height':400,
##            'paper_bgcolor': colors['bg4'],
##            'plot_bgcolor':colors['bg4'],
##            'font': {
##                'color': colors['txtblack']
##             }
##            },
##    style={'width': '10%'}
            
           ]),#src='data:image/png;base64,{}'.format(encoded_image.decode())
    #html.Div(negativeCommentsResults)
    ##
    html.Div([
   	html.Label(html.H2("Comments: ")),
        dcc.Input(id='input1', value='flight', type='text'),
        

        
        html.Div(id='output1'),
        ],
        style={'width': '80%','float':'center'}
        ),


#            'layout': {
#                'plot_bgcolor': colors['background'],
#                'paper_bgcolor': colors['background'],
#                'font': {
#                    'color': colors['text']
#                }
    ##
    ])


@app.callback(
    Output('image', 'src'),
    [Input('input-x', 'value'),
     Input('input-y', 'value')]
)

def update_result(x, y):
    try:
        global glx
        global gly
        glx=x
        gly=y
        nam=str(x+y)
        if(os.path.isfile("/home/pi/worder/main/"+nam+".png")):
            return 'data:image/png;base64,{}'.format((base64.b64encode(open(str(x+y+".png"), 'rb').read())).decode())
       
        elif((len(x)>2) and (len(y)>2)):
            genwordcloud(x,y)
            return 'data:image/png;base64,{}'.format((base64.b64encode(open(str(x+y+".png"), 'rb').read())).decode())
    except:
        print("Err in update result")
        
        
@app.callback(
    Output(component_id='output1', component_property='children'),
    [Input(component_id='input1', component_property='value')],
)
def update_value(input_data):
    nc=negativecomments(input_data)
    texter=" "
    for index, row in nc.iterrows():
        
        texter=texter+str("\n")+r"~"
        texter= texter + row
        print(texter)
    tex=""
    #for i in texter:
        
##    out=nc.tolist()
##    out=" ".join(out)
    #in list separate
    return texter


if __name__ == '__main__':
        app.run_server(host='0.0.0.0', debug=True, port=50800)