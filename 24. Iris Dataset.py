import pandas as pd
# first columns index is 0
a=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Dataset/Iris.CSV",index_col=0)
# missing value will be assigned to na_values for filtering
a=pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Dataset/Iris.CSV",na_values=0)
print(a.index) #no. of indexes
print(a.columns) #no. of columns
print(a.size) #size of the dataset
print(a.shape) #no. of rows and columns
print(a.memory_usage) #memory usage of each column
print(a.ndim) #dimention
print(a.head()) #top 5 rows
print(a.tail()) #last 5 rows
#indexing in dataframe, 1st parameter row index, 2nd parameter column name
print(a.at[0,'species'])
#indexing in dataframe, 1st parameter row index, 2nd parameter column index
print(a.iat[0,4])
#location in dataframe, 1st parameter rows, 2nd parameter columns
print(a.loc[:,'species'])
print(a.dtypes) #datatype of columns
print(a.select_dtypes(float)) #output is a given datatype
print(a.info()) #summary of the dataset