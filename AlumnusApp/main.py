# Class main
from flask import Flask, render_template, request
from ActionProcessor.ActionProcessor import ActionProcessor
from User.User import User

app = Flask(__name__)
actionProcessor = ActionProcessor()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form['userid'])
        print(request.form['password'])
        user = actionProcessor.login(request.form['userid'], request.form['password'])
        if (user != None):
            print("Login:" , user.name, user.email, user.role)
            if user.role == "admin":
                return render_template('admin.html', user=user)
            elif user.role == "student":
                return render_template('student.html', user=user)
            elif user.role == "teacher":
                return render_template('teacher.html', user=user)
            return render_template('home.html')
        else:
            print("Login failed")
            return render_template('home.html', message="Login failed")
    return render_template('home.html')

@app.route("/adduser", methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        userProperties = {
            "conectuserid": request.form['userid'],
            "conectusername": request.form['username'],
            "email": request.form['email'],
            "role": request.form['role'].lower(),
            "conectuserpassword": request.form['password']
        }
        userFlag = actionProcessor.addUser(userProperties)
        if userFlag:
            return render_template('adduser.html', message="User added successfully")
    return render_template('adduser.html', message="User not added")

@app.route("/manageroom", methods=['GET', 'POST'])
def addRoom():
    if request.method == 'POST':
        roomProperties = {
            "roomid": request.form['roomid'],
            "roomdesc": request.form['roomdesc']
        }
        if actionProcessor.addRoom(roomProperties):
            return render_template('manageroom.html', message="Room added successfully", roomList=actionProcessor.getRooms())
        return render_template('manageroom.html', message="Room add fail", roomList=actionProcessor.getRooms())
    return render_template('manageroom.html', message="Room not added", roomList=actionProcessor.getRooms())

@app.route("/deleteroom", methods=['POST'])
def deleteRoom():
    roomid = request.form['roomid']
    print(roomid)
    actionProcessor.deleteRoom(roomid)
    return render_template('manageroom.html', message="Room deleted successfully: " + roomid, roomList=actionProcessor.getRooms())



