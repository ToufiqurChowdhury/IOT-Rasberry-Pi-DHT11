import pyrebase

config = {
  "apiKey": "AIzaSyC9FfHYcKLNvDK9DBherDzSu1V3QsqknC0",
  "authDomain": "rbpi-dht11-iot.firebaseapp.com",
  "databaseURL": "https://rbpi-dht11-iot.firebaseio.com",
  "storageBucket": "rbpi-dht11-iot.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

    
def data_upload(humidity, temp_c, temp_f):
    
    data = {
             "Humidity": humidity,
             "Temperature-C": temp_c,
             "Temperature-F": temp_f        
             }

    db.child('Home').update(data); 

def print_data():
    humidity = db.child('Home/Humidity').get()
    temp_c = db.child('Home/Temperature-C').get()
    temp_f = db.child('Home/Temperature-F').get()

    print(humidity.key() + ": " + humidity.val())
    print(temp_c.key() + ": " + temp_c.val())
    print(temp_f.key() + ": " + temp_f.val())
    
    
#db.update({"Humidity","5%"})
#db.child('Humidity').remove()
#db.child('Temperature-C').remove()
#db.child('Temperature-F').remove()

#humidity_old = db.child('Home/Humidity').get()

#data = {
#         "Humidity": "10%",
#         "Temperature-C": "15",
#         "Temperature-F": "20"         
#         }

#db.child('Home').update(data); 

#humidity_new = db.child('Home/Humidity').get()
#print(humidity_old.key() + ": " + humidity_old.val())
#print(humidity_new.key() + ": " + humidity_new.val())





