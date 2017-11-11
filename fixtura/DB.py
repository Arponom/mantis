import mysql.connector
import re
from model.project import Project
#
class DbFixture:
    def __init__(self, host = 'localhost', name= 'bugtracker', user= 'root', password= ''):
        self.host = 'localhost'
        self.name = 'bugtracker'
        self.user = 'root'
        self.password = ''
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_project_id(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from mantis_project_table")
            for row in cursor:
                (id) = row
                list.append(Project(id=id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()