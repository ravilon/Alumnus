# Test for ActionProcessor
from ActionProcessor.ActionProcessor import ActionProcessor
from User.User import User

actionProcessor = ActionProcessor()
addflag = actionProcessor.addUser({
    "conectuserid": "rasadmin",
    "conectusername": "admin",
    "email": "",
    "role": "admin",
    "conectuserpassword": "admin"
})

if addflag:
    print("User added successfully")
else:
    print("User not added")
