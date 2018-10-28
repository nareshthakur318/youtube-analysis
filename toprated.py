import pandas as pd
#import matplotlib.pyplot as plt 

a = pd.read_csv('finalyoutube.csv')
#print(a)


e=a.sort_values(["ratings","vid_id"], ascending = False)
print(e)
#g=e.to_csv('topratedvideos2.csv')
#m=pd.read_csv('topratedvideos2.csv')
n=e[["vid_id","vid_cat","ratings"]]
f=n.iloc[0:5]
print(f)

