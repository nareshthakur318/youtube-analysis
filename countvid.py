import pandas as pd
#import matplotlib.pyplot as plt 

a = pd.read_csv('finalyoutube.csv')
#print(a)


b= a.groupby(["vid_cat"]).count()
#print(b)  

d=b[["vid_id"]]

print(d)
