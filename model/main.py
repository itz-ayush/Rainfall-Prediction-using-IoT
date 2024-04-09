import test as t 
# import model as m
import joblib

model = joblib.load('model_joblib')

print(f"Temperature :{t.temp}")
print(f"Humidity:{t.humidity}")
rain = model.predict([[t.temp, t.humidity]])[0]

print(f"The predicted rain in mm is {rain}")
