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
        self.queryExecutor = QueryExecutor()
        
    def login(self, conectUserId, password):
        """ if len(results) == 1:
            # Print out the column names returned by the query
            print("Column names:", [desc[0] for desc in self.queryExecutor.cursor.description])
            # Find the index of the column name "conectuserid" dynamically
            column_names = [desc[0] for desc in self.queryExecutor.cursor.description]
            column_index = None
            for index, name in enumerate(column_names):
                if name.lower() == 'conectuserid':
                    column_index = index
                    break
            if column_index is not None:
                print("Index of the column name 'conectuserid':", column_index)
                print("Value of the column name 'conectuserid':", results[0][column_index])
                return results[0] """
                
        query = "SELECT * FROM ConectUser WHERE conectuserid = %s AND conectuserpassword = %s"
        parameters = (conectUserId, password)
        results = self.queryExecutor.execute_query(query, parameters)
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
            return user
        return None        
            
        return None

           
    
    def logout(self, user):
        # TODO: Implement logout logic
        pass
    
    def addStudent(self, student_id, student_name):
        # TODO: Implement addStudent logic
        pass
    
    def removeStudent(self, student_id):
        # TODO: Implement removeStudent logic
        pass
    
    def addTeacher(self, teacher_id, teacher_name):
        # TODO: Implement addTeacher logic
        pass
    
    def removeTeacher(self, teacher_id):
        # TODO: Implement removeTeacher logic
        pass
    
    def addRoom(self, room_id, room_name):
        # TODO: Implement addRoom logic
        pass
    
    def removeRoom(self, room_id):
        # TODO: Implement removeRoom logic
        pass
    
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
        