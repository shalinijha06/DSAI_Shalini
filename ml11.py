import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
df=pd.read_csv("experience_salary_40_records.csv")
df
data = {
    "area" : [1000,1200,1500,1800,2000],
    "price" : [25,30,40,50,55]

}

df = pd.DataFrame(data)

x= df[["area"]]
y=df[["price"]]

model = LinearRegression()

model.fit(x,y)

new_data = pd.DataFrame({"area": [2100]})
predictPrice = model.predict(new_data)

print("Price of house=",predictPrice[0])
#pickle.dump(model, open("house_model.pkl","wb")
print("Model saved successfully")