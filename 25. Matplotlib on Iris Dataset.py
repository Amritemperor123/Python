from matplotlib import pyplot as p
import pandas as pd
a=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Dataset/Corolla.CSV")
x=a.iloc[:,1]
# scatter plot
d=p.subplot(3,1,1);d=p.scatter(a.iloc[:,1],a.iloc[:,2])
# histogram
d=p.subplot(3,1,2);d=p.hist(a.iloc[:,1])
# bar chart
d=p.subplot(3,1,3);d=p.bar(a.iloc[:,1],a.iloc[:,2])
p.show()