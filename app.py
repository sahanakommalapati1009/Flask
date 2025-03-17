from flask import Flask

'''
It creates an instance of flask class.
which will act as a WSGI(web server gateway interface) 
which will further interact with the web server itselfapplication
'''
app=Flask(__name__)


@app.route('/') # This is a decorator which will tell the flask that this is the route of the application
def welcome():
    return "Welcome to this flask application"
@app.route('/index') # This is a decorator which will tell the flask that this is the route of the application
def index():
    return "Hi sana, welcome to the index page"
if __name__=='__main__': # This is the entry point of any .py file, if we run this file 1st it will go and check this line and the execution begins from here.
    app.run(debug=True) # This will run the flask application
    # debug=True will help us to see the changes in the code without restarting the server again and again.
    # This will run the server on the default port 5000
    # To run the server on the different port we can use app.run(port=8080)