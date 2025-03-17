from flask import Flask, render_template
# render_template is used to redirect the html file
'''
It creates an instance of flask class.
which will act as a WSGI(web server gateway interface) 
which will further interact with the web server itselfapplication
'''
app=Flask(__name__)


@app.route('/') # This is a decorator which will tell the flask that this is the route of the application
def welcome():
    return "<html><H1>Welcome to this flask application</H1></html>"

@app.route('/index') # This is a decorator which will tell the flask that this is the route of the application
def index():
    return render_template('index.html')

@app.route('/about') # This is a decorator which will tell the flask that this is the route of the application
def about():
    return render_template('about.html')
if __name__=='__main__': # This is the entry point of any .py file, if we run this file 1st it will go and check this line and the execution begins from here.
    app.run(debug=True)