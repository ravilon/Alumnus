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
        queryExecutor.close()
        return results
    
    def deleteUser(self, studentId):
        queryExecutor = QueryExecutor()
        query = "DELETE FROM conectuser WHERE conectuserid = %s"
        parameters = (studentId,)
        queryExecutor.execute_query(query, parameters)
        if queryExecutor.cursor.rowcount == 1:
            queryExecutor.close()
            return True
        else:
            queryExecutor.close()
            return False
    
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
    
    def deleteRoom(self, roomId):
        queryExecutor = QueryExecutor()
        query = "DELETE FROM room WHERE roomid = %s"
        parameters = (roomId,)
        queryExecutor.execute_query(query, parameters)
        if queryExecutor.cursor.rowcount == 1:
            queryExecutor.close()
            return True
        else:
            queryExecutor.close()
            return False
        
    
    def addLesson(self, lessonProperties):
        #INSERT INTO LESSON (LESSONID, ROOM, TEACHER, DISCIPLINE, STARTTIME, ENDTIME, ENERGYCONSUMED)
        #VALUES ('lesson1', 354, 'teacher1', '354', '2024-03-01 09:00:00', '2024-03-01 11:00:00', 50.5);
        try:
            queryExecutor = QueryExecutor()
            query = """
            INSERT INTO lesson (lessonid, room, teacher, discipline, starttime, endtime, energyconsumed)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            parameters = (lessonProperties['lessonid'], 
                        lessonProperties['room'], 
                        lessonProperties['teacher'], 
                        lessonProperties['discipline'], 
                        lessonProperties['starttime'], 
                        lessonProperties['endtime'], 
                        lessonProperties['energyconsumed'])
            queryExecutor.execute_query(query, parameters)
            if queryExecutor.cursor.rowcount == 1:
                queryExecutor.close()
                return True
        except Exception as e:
            queryExecutor.close()
            return False
    
    def getLessons(self, teacherId):
        # SELECT * FROM lesson WHERE teacher = 'teacher1'
        queryExecutor = QueryExecutor()
        query = "SELECT * FROM lesson WHERE teacher = %s"
        parameters = (teacherId,)
        results = queryExecutor.execute_query(query, parameters)
        queryExecutor.close()
        return results
    
    def lessonCheckin(self, student_id, class_id, checkin_date):
        # TODO: Implement classCheckin logic
        pass
    
    def lessonCheckout(self, student_id, class_id, checkout_date):
        # TODO: Implement classCheckout logic
        pass
        