import requests
import unicodedata
import json
import simplejson
import ast
import re
title=""
#link = "http://www.javascriptkit.com/dhtmltutors/javascriptkit.json"
link = "https://mykraftapi.azurewebsites.net/TestQuestion"
#link= "http://maps.googleapis.com/maps/api/geocode/json?address=google"
f = requests.get(link)

#print f.text
title = f.text
#print(type(f.text))
#print("_________")
#print(title)
title=unicodedata.normalize('NFKD', title).encode('ascii','ignore')
#string_to_modify =title
#remove_these = '[ ]'
#''.join(x for x in string_to_modify if x not in remove_these)
#print(string_to_modify)
rm="[]"
title=filter(lambda x: not (x in rm),title)


#title = re.sub('[', '', title)
#title = re.sub(']', '', title)
#print(title)
title=title[1:-1]


l = ['"data":']

title=re.sub('|'.join(re.escape(r) for r in l), '', title)
print(title)

#dic=dict(title)
#print(type(title))
print("_________")
tit="["
tit=tit+title
tit=tit+"]"
#d = json.loads(title)
#print(d)
#print(type(d))
#print d[0]['expected_reponse']
###

##
#print d[0][1]

asss=ast.literal_eval(tit)
print(asss)
print(type(asss))
print(asss[0]['expected_reponse'])
