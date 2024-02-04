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

from AlumnusApp.DataBaseInterface.QueryExecutor import QueryExecutor

class ActionProcessor:
    def __init__(self):
        self.query_executor = QueryExecutor()
        
    def login(self, email, password):
        query = "SELECT * FROM ConectUser WHERE email = %s AND password = %s"
        parameters = (email, password)
        results = self.query_executor.execute_query(query, parameters)
        if len(results) == 1:
            return results[0]
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
        