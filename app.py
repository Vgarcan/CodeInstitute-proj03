from flask import Flask, render_template, flash, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient


import os
from dotenv import load_dotenv


app = Flask(__name__)


@app.route('/')
def hello_world():
    
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la URI de conexión desde las variables de entorno
    mongo_uri = os.getenv("MONGO_URI")

    try:
        # Create an instance of the "MongoClient"
        client = MongoClient(mongo_uri)

        # Access tu DB named "jsearchweb"
        dbname = client[os.getenv("DB_NAME")]

        # If the connection is succesful
        print("CONNECTED\n")
        
        collection= dbname['jobs'].find()
        

        print("Listando colecciones:")
        print(dbname.list_collection_names())

    except Exception as e:
        print("Error connecting to MONGO_DB:\n", e)
        


    return render_template('index.html', jobs=collection)

if __name__ == '__main__':
    app.run(debug=True)