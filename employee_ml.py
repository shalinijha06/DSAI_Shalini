import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
df=pd.read_csv("Employee.csv.xls")
print(df)
df.head()
df.tail()

