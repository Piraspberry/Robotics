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
  
##
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
nutw=[] 
ptwee=[]
ntwee=[]
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = '9n0vsgfDZtQ7sZAj4K9qNMQU5'
        consumer_secret = 'dzZlZTnPldmMLi0iJKuExchr2QTYE8cl7Rodwo4oYii7arBbzi'
        access_token = '806124059352240128-W9utBKUsMmvy2vw2WQSv5DxGXETvMU6'
        access_token_secret = 'bNWkAeIT0y56J55cQySgkeQE9tO64xqotsg0yuZqjBkWB'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 500):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
 
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = ('United Airlines' or 'united airlines' or 'UnitedAirlines'), count = 1000)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    nutweets=[tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) -len(ntweets) - len(ptweets))/len(tweets)))
    
    # printing first 5 positive tweets
    ptwee=[]
    ntwee=[]
    nutwee=[]
    try:
        print("\n\nPositive tweets:")
        for tweet in ptweets[:3]:
            ptwee=tweet['text']
        print(ptwee)
    except:
        pass
    try:

    # printing first 5 negative tweets
        print("\n\nNegative tweets:")
        for tweet in ntweets[:3]:

            ntwee=tweet['text']

            print(ntwee)
    except:
        pass
    try:

        for tweet in nutweets[:6]:
            nutwee=tweet['text']
    except:
        pass

        
    
    #if(len(ptwee)<3):
    #    for tweet in ptweets[3:]:
    #        ptwee=tweet['text']
           
    #if(len(ntwee)<3):
    #    for tweet in ntweets[3:]:
    #        ntwee=tweet['text']
    #if(len(ptwee)<2):
    #    ptwee=nutwee

    #if(len(ntwee)<2):
    #    ntwee=nutwee

           



    return ptwee,ntwee,nutwee, len(ptweets) ,len(ntweets), (len(tweets) -len(ntweets) - len(ptweets))
#if __name__ == "__main__":
    # calling main function

ptwee,ntwee,nutwee,np,nn,nnu= main()

         
##
with open('sudodataUA1.csv', 'rU') as infile:
  
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

mile= data['Miles']
cost = data['Price']
hrs = data['Duration1']
ppm = data['Price1']
mile=list(map(float,mile))
cost=list(map(float,cost))
hrs=list(map(float,hrs))
ppm=list(map(float,ppm))
print(mile)
print(cost)
print(hrs)
print(ppm)

#Define Dash App
app=dash.Dash("UAL Dash")

       


app.css.append_css({
    "external_url":"https://codepen.io/anon/pen/bKxpXB.css" #"https://codepen.io/chriddyp/pen/bWLwgP.css"
})

 
#Layout(
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)'
#)
colors = {
    'bg1': '#d5c6ae',
    'txtblue':'#7FDBFF',
    'txtblack':' #000000',
    'txtdarblu':'#06015d',
    'bg2': '#fce9f0',
    'bg3':'#c6e2ff',
    'bg4':'#D1D0CE',
    'bg5':'#A0CFEC',
}

#fig = Figure(data=data, layout=layout)

#plot_url = py.plot(fig, filename='transparent-background')


app.layout = html.Div([


    html.H1(
        children='United Airlines Data Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['txtdarblu']
        }
    ),

    html.Div(children='Fly the Friendly Skies, with the United Airlines', style={
        'textAlign': 'center',
        'color': colors['txtblack']
    }),


   
    #html.Div(children= html.H1('United Airlines Data Dashboard'), style={
    #    'textAlign': 'center',
    #    'color': colors['text']
    #}),
    #html.Div([
    #    html.H1('_________'+'United Airlines '+'Data Dashboard_______'),
    #	html.Div("Fly the Friendly Skies, with United Airlines")
    #    ],
    #         style={'width': '80%', 'display':'inline' },
        #html.H4("Fly the Friendly Skies")
    #   ),
    

    html.Div([
   	html.Label(html.H5("Miles vs Cost (INR) Trends in UAL flights: ")),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': mile, 'y': cost, 'type': 'line'}
                ],
                'layout': {
                    #'title':"Miles vs Cost",
                    'height':400,
		    'paper_bgcolor': colors['bg4'],
                    'plot_bgcolor':colors['bg4'],
                    'font': {
                        'color': colors['txtblack']
                     }

                    
                    }
                }
            ),
        ],
        style={'width': '100%'}
        ),


#            'layout': {
#                'plot_bgcolor': colors['background'],
#                'paper_bgcolor': colors['background'],
#                'font': {
#                    'color': colors['text']
#                }

    html.Div([
        html.Label(html.H5('Duration of flight vs Price per mile Trends: ')),
        #dcc.Dropdown(
        #    options=[
        #        {'label': 'Miles vs Cost', 'value': 'NYC'},
        #        {'label': 'Duration vs PPM', 'value': 'MTL'},
        #        {'label': 'Random variable vs units', 'value': 'SF'}
        #        ],
        #    value=['MTL', 'SF','NYC'],
        #    multi=True
        #),
	

        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'x': hrs, 'y': ppm, 'type': 'line'}
                ],
                
                'layout': {
                    #'title':"Miles vs Cost",
                    'height':400,
                    'paper_bgcolor': colors['bg2'],
                    'plot_bgcolor':colors['bg2'],
                    'font': {
                        'color': colors['txtblack']
                     }
                 




                    }
                }   
            )
        ],
        style={'width': '60%','display':'inline','float':'left' }
        ),

    html.Div([
	html.Label(html.H5("  Random  Visualization   ")),
        dcc.Graph(
            id='example-graph4',
            figure={
                
                'data': [
                    {'x': [1, 2, 3,4,5], 'y': [3,6,1,3,7], 'type': 'bar'},
		    {'x':[1,2,3,4,5], 'y':[7,2,4,7,1], 'type':'bar'}
                    ],

                'layout': {
                    #'title':"Miles vs Cost",
                    'height':400,
                    'paper_bgcolor': colors['bg5'],
                    'plot_bgcolor':colors['bg5'],
                    'font': {
                        'color': colors['txtblack']
                        }
                    }
                },
            ),
        ],
        style={'width': '40%','display': 'inline','float':'right'},
        ),
    html.Div([
	html.Label(html.H5(" Pie Visualizations: ")),
        dcc.Graph(
            id='example-graph5',
            figure={
                'data': [
                    #{
                        #"values": [16, 15, 12, 6, 5, 4, 42],
                        #"labels": [
                        #    "US",
                        #    "China",
                        #    "European Union",
                        #    "Russian Federation",
                        #    "Brazil",
                        #    "India",
                        #    "Rest of World"
                        #    ],
                        #"domain": {"x": [0, .48]},
                        #"name": "GHG Emissions",
                        #"hoverinfo":"label+percent+name",
                        #"hole": .6,
                        #"type": "pie"
                        #},
		    {
			"values":[int(np),int(nn),int(nnu)],
			"labels":["Positive","Negative","Neutral"],
			"hole": .6,
			"type":"pie"
			}
                    ],
                'layout': {
                    #'title': 'Pie Visuals',
                    "annotations":
                    [
                        #{
                           # "font": {
                           #     "size": 20
                           #     },
                           # "showarrow": False,
                           # "text": "",
                           # "x": 0.20,
                           # "y": 0.5
                           # },
			{
			    "font":{
				"size":20
				},
			    "showarrow":False,
			    "text":"Tweets",
 		            "x":0.5,
			    "y":0.5			    }
                        ],
                    'height':400
                    
                    }
                }
            )
        ],
        style={'width': '50%', 'display': 'inline','float':'left' },#inline-block
        ),
    html.Div([
        
        html.Label(html.H5("Live from Twitter: " )),
        html.Div("."),

        html.Div("Positive/Sarcastic Tweets: "),
        html.Div(str(ptwee)),
        #nutw=nutwee[3:]
        html.Div(str(nutwee[3:])),                
        html.Div("."),
        html.Div("UAL"),
        html.Div("."),
        html.Div("Negative Tweets:"),
        #html.Div(str(ntwee)),
        #if(len(ntwee)<2):
        #nutw=nutwee[:3]
        html.Div(str(ntwee)),
        html.Div(str(nutwee[:3])),
        
        ],
        style={'width': '50%','display':'inline','float':'right' },
        
        ),
    #
    html.Div(children=[
        html.Div(children='''\
            Symbol to graph:
        '''),
        html.Div("\n\n"+"""\
        
         
        
        """),

        dcc.Input(id='input', value= "UAL", type='text'),
        html.Div(id='output-graph')
        ],
        style={'width':'100%','display':'inline','float':'right'},
    
        ),
    #'layout': {
        #'title':"Miles vs Cost",
        
    #    'bgcolor': colors['bg3'],
        
        #'font': {
                #    'color': colors['txtblack']
    #     }


#
    ],

    
)

#@app.callback(
#    Output(component_id='output', component_property='children'),
#    [Input(component_id='input', component_property='value')]
#)
#def update_value(input_data):
#    return 'Input: "{}"'.format(input_data)


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'morningstar', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)

    return dcc.Graph(
        id='example-grapher',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
#            'layout': {
#                'title': input_data
#            }
            'layout': {
                #'title':"Miles vs Cost",
                'height':400,
          
                'font': {
                    'color': colors['txtblack']
                    }
                }

        }
    )

ptwee,ntwee,nutwee,np,nn,nnu= main()

if __name__ == '__main__':
    app.run_server()
    main()
