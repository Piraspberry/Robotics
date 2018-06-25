
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv

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
app=dash.Dash()


app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': mile, 'y': cost, 'type': 'line'}
                ],
                'layout': {
                    'title': 'Miles vs Cost',
                    'height':600
		    
                    }
                }
            ),
        ],
        style={'width': '100%'}
        ),

    html.Div([
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'Miles vs Cost', 'value': 'NYC'},
                {'label': 'Duration vs PPM', 'value': 'MTL'},
                {'label': 'Random variable vs units', 'value': 'SF'}
                ],
            value=['MTL', 'SF','NYC'],
            multi=True
        ),

        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'x': hrs, 'y': ppm, 'type': 'line'}
                ],
                'layout': {
                    'title': 'Duration of flight vs Price per mile',
                    'height':600
                    }
                }
            )
        ],
        style={'width': '33%', 'display':'inline' }
        ),

    html.Div([
        dcc.Graph(
            id='example-graph4',
            figure={
                'data': [
                    {'x': [1, 2, 3,4,5], 'y': [3,6,1,3,7], 'type': 'bar'},
		    {'x':[1,2,3,4,5], 'y':[7,2,4,7,1], 'type':'bar'}
                ],
                'layout': {
                    'title': 'Data Visualization of Random values',
                    'height':600
                    }
                }
            )
        ],
        style={'width': '40%', 'display': 'inline-block', 'float':'right',},
        ),
    html.Div([
        dcc.Graph(
            id='example-graph5',
            figure={
                'data': [
                    {
                        "values": [16, 15, 12, 6, 5, 4, 42],
                        "labels": [
                            "US",
                            "China",
                            "European Union",
                            "Russian Federation",
                            "Brazil",
                            "India",
                            "Rest of World"
                            ],
                        "domain": {"x": [0, .48]},
                        "name": "GHG Emissions",
                        "hoverinfo":"label+percent+name",
                        "hole": .5,
                        "type": "pie"
                        },
		    {
			"values":[32,21,57],
			"labels":["POsitive","Negative","Neutral"],
			"hole": .9,
			"type":"pie"
			}
                    ],
                'layout': {
                    'title': 'Pie Visuals',
                    "annotations":
                    [
                        {
                            "font": {
                                "size": 20
                                },
                            "showarrow": False,
                            "text": "GHG",
                            "x": 0.20,
                            "y": 0.5
                            },
			{
			    "font":{
				"size":20
				},
			    "showarrow":True,
			    "text":"GHG",
 		            "x":0.20,
			    "y":0.5
			    }
                        ],
                    'height':750
                    
                    }
                }
            )
        ],
        style={'width': '60%', 'display': 'inline-block' },
        ),
#    html.Div([
#        dcc.Input(id='input', value='Enter something here!', type='text'),
#        html.Div(id='output')
#    ]
#    )
    #
    html.Div(children=[
        html.Div(children='''\
            Symbol to graph:
        '''),
        dcc.Input(id='input', value= "UAL", type='text'),
        html.Div(id='output-graph')
    ]
    )

#
    ]
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
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server()
