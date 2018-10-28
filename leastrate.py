import pandas as pd
#import matplotlib.pyplot as plt 

a = pd.read_csv('finalyoutube.csv')
#print(a)

e=a.sort_values(["ratings","vid_id"], ascending = True)
#print(e)
#g=e.to_csv('leastrated.csv')
#m=pd.read_csv('leastrated.csv')
n=e[["vid_id","vid_cat","ratings",]]
f=n.iloc[0:2]
print(f)

