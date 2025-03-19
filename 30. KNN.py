# K's nearest neighbour is the most basic classification algorithm.
# classification algorithms determines which class a smaple data belongs to, given a dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv(r"<you can use the Iris.csv dataset for this program>",index_col=0)

x = data.iloc[:, :-1]
y= data.iloc[:, -1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
predict = knn.predict(x_test)

print(accuracy_score(y_test, predict))
