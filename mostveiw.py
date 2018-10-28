import pandas as pd
#import matplotlib.pyplot as plt 

a = pd.read_csv('finalyoutube.csv')
#print(a)


e=a.sort_values(["viewcount","vid_id"], ascending = False) # true means ascending order if ascending false means descending order
#print(e)
#g=e.to_csv('veiwcount2.csv')
#m=pd.read_csv('veiwcount2.csv')
n=e[["vid_id","vid_cat","viewcount"]]
f=n.iloc[0:5]
print(f)