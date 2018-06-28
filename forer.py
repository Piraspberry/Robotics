import dash

import dash_core_components as dcc

import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd
import csv

##

text=""
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

miles= data['KEYWORDS']
orig=data['ORIGIN']
desti=data['DESTINATION']

def ocounter(stri):
    return(orig.count(stri))
def dcounter(stri):
    return(desti.count(stri))
    
    


#
stringer=" " 
mile = [x + stringer for x in miles]
text = text.join(mile);
#=======
#print(text)
#text=str(text)
#print(type(text))

#stri=input("Enter")
#print(ocounter(stri))
#================
uniqo=list(set(orig))
uniqd=list(set(desti))
uniqoctr=[]
uniqdctr=[]

for i in uniqo:
    uniqoctr.append(ocounter(i))
    
for i in uniqd:
    uniqdctr.append(dcounter(i))

stater=uniqo+uniqd
quater=uniqoctr+uniqdctr
namer=[]
maner=[]
for i in range(0,len(stater)):
    namer.append("United Airlines")
    
for i in range(0,len(uniqo)):
    maner.append("Origin")

for i in range(len(uniqo),(len(stater)+1)):
    maner.append("Destination")
    
rower = zip(["Name"],["Manager"],["Quantity"],["Status"])
with open("Outer1.csv", "w") as fi:
    writer = csv.writer(fi)
    for row in rower:
        writer.writerow(row)

rows = zip(namer,maner,quater,stater)
with open("Outer1.csv", "a") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

##

with open('Outer1.csv', 'rU') as infile:
  
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

uniqo= data['Status']
uniqoctr=data['Quantity']



df = pd.read_csv("/home/pi/worder/Outer1.csv")

mgr_options = df["Manager"].unique()



#uniqorig=["EWR","ORD","BOM","SFO","OMR","TCS"]
app = dash.Dash()



colors = {

'background': 
'white',

'text': '#020000'

}



app.layout = html.Div([

html.H2("Sales Funnel Report"),

html.Div(
    [
        dcc.Dropdown(
            id="Manager",
            options=[{
                'label': i,
                'value': i
                }
                     for i in mgr_options],
            value='All Managers'),
        ]),
dcc.Graph(id='funnel-graph',
          style={'width':'50%',
                 'float':'left'
                 }
          ),
##dcc.Graph(id='example-graph',
##          figure={
##              'data': [
##                  {'x': [1,2, 3], 'y': [4, 1,2], 'type':'line', 'name':'SF'},
##                  {'x': [1,2, 3],'y': [2, 4,5], 'type':'line', 'name':u'Montréal'},
##                  ],
##              'layout': {
##                  'plot_bgcolor': colors['background'],
##                  'paper_bgcolor': colors['background'],
##                  'font': {
##                      'color': colors['text']
##                      }
##                  }
##              },
##          style={'width':'50%','float':'right'}
##          )
])





@app.callback(

dash.dependencies.Output('funnel-graph','figure'), [dash.dependencies.Input('Manager','value')])

def update_graph(Manager):
    if Manager == "All Managers":

        df_plot = df.copy()

    else:

        df_plot = df[df['Manager'] == Manager]



    pv = pd.pivot_table(df_plot, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)
    rl=[]
    for i in range(0,len(uniqo)):
        fn="trace"+str(i)
        fn = go.Bar(x=pv.index, y=pv[('Quantity', str(uniqo[i]))], name=str(uniqo[i]))
        rl.append(fn)
    



    return {
        'data': rl,
        'layout': go.Layout(
            title='United Airlines Source-Destination Comments Log for {}'.format(Manager),
            height=3000,
            barmode='stack'
            )
        }





if __name__ =='__main__':

    app.run_server(debug=True)
