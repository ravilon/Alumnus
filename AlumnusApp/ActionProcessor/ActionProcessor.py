# Class to use the QueryExecutor class to get the users from the database
""" _ActionOperator_
--
userid: String
actionForRole: Map[String, String]
--
+ login(String, String)
+ logout(User)

+ addStudent(String, String)
+ removeStudent(String)

+ addTeacher(String, String)
+ removeTeacher(String)

+ addRoom(Integer, String)
+ removeRoom(Integer)

+ addClass(String, String, Date, Date)
+ removeClass(String)

+ classCheckin(String, String, Date)
+ classCheckout(String, String, Date) """

from DataBaseInterface.QueryExecutor import QueryExecutor
from User.User import User

class ActionProcessor:
    def __init__(self):
        __ActionProcessor__ = "ActionProcessor"
        
    def login(self, conectUserId, password):
        queryExecutor = QueryExecutor()       
        query = "SELECT * FROM ConectUser WHERE conectuserid = %s AND conectuserpassword = %s"
        parameters = (conectUserId, password)
        results = queryExecutor.execute_query(query, parameters)
        if len(results) == 1:
            # Create a map for each index to column value
            print(results[0])
            userProperties = {
                "conectuserid": results[0][0],
                "conectusername": results[0][1],
                "conectuserpassword": results[0][2],
                "role": results[0][3],
                "email": results[0][4],
            }
            user = User(userProperties)
            queryExecutor.close()
            return user
        queryExecutor.close()
        return None        
           
    def logout(self, user):
        # TODO: Implement logout logic
        pass
    
    def addUser(self, newUserProperties):
        try:
            queryExecutor = QueryExecutor()
            query = """
            INSERT INTO ConectUser (conectuserid, conectusername, email, conectuserpassword, role)
            VALUES (%s, %s, %s, %s, %s)
            """
            parameters = (newUserProperties['conectuserid'], 
                        newUserProperties['conectusername'], 
                        newUserProperties['email'], 
                        newUserProperties['conectuserpassword'], 
                        newUserProperties['role'])
            queryExecutor.execute_query(query, parameters)
            if queryExecutor.cursor.rowcount == 1:
                queryExecutor.close()
                return True
        except Exception as e:
            queryExecutor.close()
            return False
    
    def getUsers(self):
        queryExecutor = QueryExecutor()
        query = "SELECT * FROM conectuser"
        results = queryExecutor.execute_query(query)
        userList = []
        for result in results:
            userProperties = {
                "conectuserid": result[0],
                "conectusername": result[1],
                "conectuserpassword": result[2],
                "role": result[3],
                "email": result[4]
            }
            userList.append(User(userProperties))
        queryExecutor.close()
        return userList
    
    def removeUser(self, student_id):
        # TODO: Implement removeStudent logic
        pass
    
    def addRoom(self, roomProperties):
        try: 
            queryExecutor = QueryExecutor()
            query = "INSERT INTO room (roomid, roomdesc) VALUES (%s, %s)"
            parameters = (roomProperties['roomid'], roomProperties['roomdesc'])
            queryExecutor.execute_query(query, parameters)
            if queryExecutor.cursor.rowcount == 1:
                queryExecutor.close()
                return True
        except Exception as e:
            queryExecutor.close()
            return False
    
    def getRooms(self):
        queryExecutor = QueryExecutor()
        query = "SELECT * FROM room"
        results = queryExecutor.execute_query(query)
        queryExecutor.close()
        return results
    
    def deleteRoom(self, room_id):
        queryExecutor = QueryExecutor()
        query = "DELETE FROM room WHERE roomid = %s"
        parameters = (room_id,)
        queryExecutor.execute_query(query, parameters)
        if queryExecutor.cursor.rowcount == 1:
            queryExecutor.close()
            return True
        else:
            queryExecutor.close()
            return False
        
    
    def addClass(self, class_id, class_name, start_date, end_date):
        # TODO: Implement addClass logic
        pass
    
    def removeClass(self, class_id):
        # TODO: Implement removeClass logic
        pass
    
    def classCheckin(self, student_id, class_id, checkin_date):
        # TODO: Implement classCheckin logic
        pass
    
    def classCheckout(self, student_id, class_id, checkout_date):
        # TODO: Implement classCheckout logic
        pass
        