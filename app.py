from flask import Flask, render_template, flash, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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


@app.route('/companies-list')
def companies_list():
    """
    This function is a route for the companies list page. It retrieves all company documents from the 'companies' collection 
    and passes them to the 'companies.html' template for rendering.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template with the 'companies' data passed to it.

    Raises:
    None
    """
    # return "Hello users"
    companies = obtainCollection('companies', 'find')
    # return print(companies)
    return render_template('companies.html', companies=companies)

 
@app.route('/company-profile/<string:comp_id>')
def com_prof(comp_id):
    """
    This function is a route for the company profile page. It retrieves a specific company document from the 'companies' collection 
    based on the provided comp_id and passes it to the 'company-description.html' template for rendering.

    Parameters:
    comp_id (str): The unique identifier of the company document to retrieve.

    Returns:
    render_template: A rendered HTML template with the 'company' data passed to it.

    Raises:
    None
    """
    sel_company = obtainCollection('companies', 'find_one', id=comp_id)
    return render_template('company-description.html', company=sel_company)

@app.route('/application-list')
def application_list():
    """
    This function is a route for the applications list page. It retrieves all application documents from the 'applications' collection 
    and passes them to the 'applications.html' template for rendering.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template with the 'applications' data passed to it.

    Raises:
    None
    """
    # return "Hello users"
    applications = obtainCollection('applications', 'find')
    # return print(companies)
    return render_template('applications.html', applications=applications)

 
@app.route('/application-desc/<string:appl_id>')
def appl_desc(appl_id):
    """
    This function is a route for the application description page. It retrieves a specific application document from the 'applications' collection 
    based on the provided appl_id and passes it to the 'application-description.html' template for rendering.

    Parameters:
    appl_id (str): The unique identifier of the application document to retrieve.

    Returns:
    render_template: A rendered HTML template with the 'application' data passed to it.

    Raises:
    None
    """
    applications = obtainCollection('applications', 'find_one', id=appl_id)
    return render_template('application-description.html', application=applications)



if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)