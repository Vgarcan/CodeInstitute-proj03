from flask import Flask, render_template, flash, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

app = Flask(__name__)

### Extra Functionalities ###
def obtainCollection(selected_collection, comm_query, id=None):
    """
    This function connects to a MongoDB database, performs a specified query, and returns the result.

    Parameters:
    selected_collection (str): The name of the MongoDB collection to connect to.
    comm_query (str): The type of query to perform. It can be 'find' or 'find_one'.
    id (str, optional): The ID of the document to find when using 'find_one' query. Defaults to None.

    Returns:
    collection: The result of the query. If an error occurs during the connection or query, it returns None.

    Raises:
    Exception: If an error occurs during the connection or query.
    """
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")

    try:
        # Connect to the DB
        client = MongoClient(mongo_uri)
        dbname = client[os.getenv("DB_NAME")]
        # Performs specific query
        if comm_query == 'find':
            collection = dbname[selected_collection].find()
        elif comm_query == 'find_one' and id is not None:
            collection = dbname[selected_collection].find_one({"_id": ObjectId(id)})
        else:
            collection = None

    except Exception as e:
        print("Error connecting to MONGO_DB:\n", e)
        collection = None

    return collection

### ROUTES ###
@app.route('/')
def index():
    return render_template('index.html', jobs=obtainCollection('jobs', 'find'))


@app.route('/job-description/<string:job_id>')
def job_description(job_id):
    job = obtainCollection('jobs', 'find_one', job_id)
    return render_template('job-description.html', job=job)


@app.route('/users-list')
def user_list():
    # return "Hello users"
    return render_template('users.html', users=obtainCollection('users', 'find'))


@app.route('/user-description/<string:user_id>')
def user_description(user_id):
    user = obtainCollection('users', 'find_one', user_id)
    return render_template('user-description.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)