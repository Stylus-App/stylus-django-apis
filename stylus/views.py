import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCnjqu1Jy5v-_w61VvQxWwXZjOpU3tCkQw",
    "authDomain": "stylus-76d03.firebaseapp.com",
    "projectId": "stylus-76d03",
    "storageBucket": "stylus-76d03.appspot.com",
    "messagingSenderId": "453969796350",
    "appId": "1:453969796350:web:99a6bf30edf89d2035d9af",
    "measurementId": "G-M23F2V4BRC"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# authentication
auth = firebase.auth()