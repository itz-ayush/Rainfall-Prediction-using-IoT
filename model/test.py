# import required modules
import firebase_admin
from firebase_admin import db, credentials

# authenticate to firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": ""}) #enter the url to access firebase here

# creating reference to root node
ref = db.reference("/")

# retrieving data from root node
dict=ref.get()
humidity = dict['DHT']['humidity']
temp=dict['DHT']['temperature']
# print(f"Humidity : {humidity}")
# print(f"Temperature: {temp}")
