import joblib
import numpy as np
import firebase_admin
from firebase_admin import db, credentials
import json
__model = None
__cred = credentials.Certificate("./artifacts/credentials.json")


def get_sensor_data():
    # authenticate to firebase

    # creating reference to root node
    ref = db.reference("/")

    # retrieving data from root node
    data = ref.get()
    humidity = data['DHT']['humidity']
    temp = data['DHT']['temperature']
    print(f"Humidity : {humidity}")
    print(f"Temperature: {temp}")
    result = np.array([temp, humidity])
    result_list = result.tolist()
    json_result = json.dumps(result_list)
    return json_result


def get_estimated_rainfall(temp, hum):
    return np.round(__model.predict([[temp, hum]])[0], 2)


def load_saved_artifacts():
    print("Loading saved artifacts....Start")
    global __model
    global __cred

    firebase_admin.initialize_app(__cred, {
        "databaseURL": ""}) #enter the url to access the firebase here

    __model = joblib.load("./artifacts/model_joblib")
    print("Loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    res = get_sensor_data()
    print(res)

