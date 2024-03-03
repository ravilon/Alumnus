# Class main
from flask import Flask
from ActionProcessor.ActionProcessor import ActionProcessor
from User.User import User

import os

print("Current working directory:", os.getcwd())


app = Flask(__name__)
@app.route("/")
def hello_world():
    actionProcessor = ActionProcessor()
    # Create a query to get all the Users
    user = actionProcessor.login("admin", "Inter@1234")
    if (user != None):
        print("Login:" , user.name, user.email, user.role)
    else:
        print("Login failed")
    return "<p>Hello, World!</p>"
# Create a instance of the class ActionProcessor





