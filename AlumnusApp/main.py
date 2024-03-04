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

@app.route("/manageuser", methods=['GET', 'POST'])
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
            return render_template('manageuser.html', message="User added successfully", userList=actionProcessor.getUsers())
    return render_template('manageuser.html', message="User not added", userList=actionProcessor.getUsers())

@app.route("/deleteuser", methods=['POST'])
def deleteUser():
    userid = request.form['userid']
    if actionProcessor.deleteUser(userid):
        return render_template('manageuser.html', message="User deleted successfully: " + userid, userList=actionProcessor.getUsers())
    return render_template('manageuser.html', message="User not deleted", userList=actionProcessor.getUsers())


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
    actionProcessor.deleteRoom(roomid)
    return render_template('manageroom.html', message="Room deleted successfully: " + roomid, roomList=actionProcessor.getRooms())

@app.route("/managelesson", methods=['GET', 'POST'])
def addLesson():
    if request.method == 'POST':
        lessonProperties = {
            "lessonid": request.form['lessonid'],
            "room": request.form['room'],
            "teacher": request.form['teacher'],
            "discipline": request.form['discipline'],
            "starttime": request.form['starttime'],
            "endtime": request.form['endtime'],
            "energyconsumed": request.form['energyconsumed']
        }
        if actionProcessor.addLesson(lessonProperties):
            return render_template('managelesson.html', message="Lesson added successfully", 
                                   lessonList=actionProcessor.getLessons(request.form['teacher']),
                                   roomList=actionProcessor.getRooms(),
                                    userid=request.form['teacher'])
                                   
        return render_template('managelesson.html', message="Lesson add fail", 
                               lessonList=actionProcessor.getLessons(request.form['teacher']),
                               roomList=actionProcessor.getRooms(),
                               userid=request.form['teacher'])
    userid = request.args.get('userid')
    return render_template('managelesson.html', message="Lesson not added", 
                           lessonList=actionProcessor.getLessons(userid), 
                           roomList=actionProcessor.getRooms(),
                           userid=userid)



