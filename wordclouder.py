from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import csv




#masker=np.array(Image.open("ual.jpg"))
text=""
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
#for i in uniqo:
#    print("{} is {} times".format(i, ocounter(i)))
#wordcloud=WordCloud().generate(text)
#plt.figure(figsize=(10,10))
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.margins(x=0, y=0)
#plt.show()
#plt.savefile("worder.jpg") 
#print(len(orig))


