class User:
    # Class to create a user
    # This class should have the attributes of the user
    # The attributes are: id, name, email, password, role
    # The class should have a method to create a user
    def __init__(self , userProperties):
        self.id = userProperties['conectuserid']
        self.name = userProperties['conectusername']
        self.email = userProperties['email']
        self.password = userProperties['conectuserpassword']
        self.role = userProperties['role']
        self.loginFlag = True
        