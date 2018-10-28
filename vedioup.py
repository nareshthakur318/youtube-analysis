import pandas as pd
#import matplotlib.pyplot as plt 

#a = pd.read_csv('finalyoutube.csv')
#print(a)


#b= a.groupby(["vid_cat"]).count()
#print(b)  

#t=pd.to_csv('vedioup.csv')

#bb=pd.read_csv('vedioup.csv')

#n=bb.sort_values(["vid_id"], ascending = False) 
#g=n.to_csv('vedioup2.csv')
m=pd.read_csv('vedioup2.csv')
b=m[["vid_cat","vid_id"]]
f=b.iloc[0:5]
print(f)