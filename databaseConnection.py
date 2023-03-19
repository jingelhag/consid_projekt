import mysql.connector

class databaseConnection:
    def __init__(self, database=None, cursor=None):
        self.datbase = database
        self.cursor = cursor

    # connects to the database
    def connectToDb(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Juing02a",
            auth_plugin='mysql_native_password',
            database="Library"
        )
        return db

    def startConnection(self):
        self.database = self.connectToDb()
        self.cursor = self.database.cursor()

    def closeConnection(self):
        self.cursor.close()
        self.database.close()

    def removeDatabase(self):
        self.startConnection()
        self.cursor.execute("DROP DATABASE Library")
        self.closeConnection()

    def setupTables(self):
        self.startConnection()
        self.cursor.execute("CREATE TABLE Category (Id int UNSIGNED PRIMARY KEY AUTO_INCREMENT, CategoryName VARCHAR(50) NOT NULL)")
        self.cursor.execute("CREATE TABLE LibraryItem (\
                        Id int PRIMARY KEY AUTO_INCREMENT, \
                        CategoryId int UNSIGNED, \
                        FOREIGN KEY(CategoryId) REFERENCES Category(Id), \
                        Title VARCHAR(100) NOT NULL, \
                        Author VARCHAR(100), \
                        Pages int UNSIGNED, \
                        RunTimeMinutes int UNSIGNED, \
                        IsBorrowable BOOLEAN, \
                        Borrower VARCHAR(50), \
                        BorrowDate DATE, \
                        Type VARCHAR(50) NOT NULL)")
        self.cursor.execute("CREATE TABLE Employees (\
                        Id int PRIMARY KEY AUTO_INCREMENT,\
                        FirstName VARCHAR(50) NOT NULL, \
                        LastName VARCHAR(50) NOT NULL, \
                        Salary DECIMAL(10,2), \
                        CHECK (Salary >= 0), \
                        IsCEO BOOLEAN NOT NULL, \
                        IsManager BOOLEAN NOT NULL, \
                        ManagerId int)")
        self.closeConnection()


    # connects to MySQL and adds the database called "Library"
    def initialize(self):
        db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Juing02a",
                auth_plugin='mysql_native_password'
            )
        dbCursor = db.cursor()
        dbCursor.execute("CREATE DATABASE Library")
        dbCursor.close()
        db.close()
