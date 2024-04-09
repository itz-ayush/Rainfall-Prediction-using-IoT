import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
df = pd.read_csv('weather1.csv')
# print(df.head())

X = df.drop(['rain (mm)'],axis = 'columns').values
y = df['rain (mm)'].values

model = RandomForestRegressor(n_estimators=60)

model.fit(X,y)

joblib.dump(model,'model_joblib')
