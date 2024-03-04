import json
import os
import psycopg2

# Class to create a interface to the database postgress
# This class is used to execute queries in the database
# Database is postgress and the information to conect is on dbconnect.json
# This class should have a method to execute a query and return the result

class QueryExecutor:
    def __init__(self):
        self.dbconnect = self.get_dbconnect()
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    # Method to get the information to connect to the database
    # The information is stored in a json file
    def get_dbconnect(self):
        current_directory = os.getcwd()
        json_file_path = os.path.join(current_directory, 'dbconnect.json')
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            return data

    # Method to connect to the database
    def connect(self):
        return psycopg2.connect(
            dbname=self.dbconnect['dbname'],
            user=self.dbconnect['user'],
            password=self.dbconnect['password'],
            host=self.dbconnect['host'],
            port=self.dbconnect['port']
        )

    # Method to execute a query
    # This method should receive the query and the parameters
    # The method should return the result of the query
    def execute_query(self, query, parameters):
        self.cursor.execute(query, parameters)
        if "SELECT" in query:
            return self.cursor.fetchall()
        else:
            self.connection.commit()
            return None

    # Method to close the connection to the database
    def close(self):
        self.cursor.close()
        self.connection.close()





