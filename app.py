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
    """
    This function is a route for the home page. It retrieves all job documents from the 'jobs' collection 
    and passes them to the 'index.html' template for rendering.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template with the 'jobs' data passed to it.

    Raises:
    None
    """
    return render_template('index.html', jobs=obtainCollection('jobs', 'find'))


@app.route('/job-description/<string:job_id>')
def job_description(job_id):
    """
    This function is a route for the job description page. It retrieves a specific job document from the 'jobs' collection 
    based on the provided job_id and passes it to the 'job-description.html' template for rendering.

    Parameters:
    job_id (str): The unique identifier of the job document to retrieve.

    Returns:
    render_template: A rendered HTML template with the 'job' data passed to it.

    Raises:
    None
    """
    job = obtainCollection('jobs', 'find_one', job_id)
    return render_template('job-description.html', job=job)


@app.route('/users-list')
def user_list():
    """
    This function is a route for the users list page. It retrieves all user documents from the 'users' collection 
    and passes them to the 'users.html' template for rendering.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template with the 'users' data passed to it.

    Raises:
    None
    """
    # return "Hello users"
    return render_template('users.html', users=obtainCollection('users', 'find'))

 
@app.route('/user-description/<string:user_id>')
def user_description(user_id):
    """
    This function is a route for the user description page. It retrieves a specific user document from the 'users' collection 
    based on the provided user_id and passes it to the 'user-description.html' template for rendering.

    Parameters:
    user_id (str): The unique identifier of the user document to retrieve.

    Returns:
    render_template: A rendered HTML template with the 'user' data passed to it.

    Raises:
    None
    """
    user = obtainCollection('users', 'find_one', user_id)
    return render_template('user-description.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)