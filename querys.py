from datetime import date
import databaseConnection as dc
import extra_functions as ef
# General functions for quering the database
def checkInDatabase(dbObject, tableName, listOfColumns, listOfValues):
    dbObject.startConnection()
    query = "SELECT * FROM {} WHERE ".format(tableName)
    for i in range(len(listOfColumns)):
        if i > 0:
            query += " AND "
        query += "{} = %s".format(listOfColumns[i])
    dbObject.cursor.execute(query, listOfValues)
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return int(0 if answer is None else 1)

def getCategoryId(dbObject, categoryName):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT Id FROM Category WHERE CategoryName = %s", (categoryName,))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return int(0 if answer is None else answer[0])

def getCategoryName(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT Type FROM LibraryItem WHERE Id = %s", (Id,))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else answer[0]
    
def getColumns(dbObject, table):
    dbObject.startConnection()
    query = "SHOW COLUMNS FROM {}".format(table)
    dbObject.cursor.execute(query)

    # Get the column names from the cursor fetchall method
    column_names = [col[0] for col in dbObject.cursor.fetchall()]
    return column_names   

def getManagerId(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT Id FROM Employees WHERE Id = %s AND isManager = 1", (Id,))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else answer[0]

# checks if there is an CEO already in the database
def isCEO(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT * FROM Employees WHERE isCEO = 1 AND Id = %s", (Id, ))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else 1

def isManager(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT * FROM Employees WHERE isManager = 1 AND Id = %s", (Id, ))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else 1

def checkForCEO(dbObject):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT * FROM Employees WHERE isCEO = 1")
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else 1

# checking if a manager is managing over someone

def checkDeleteEmployee(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT * FROM Employees WHERE ManagerId = %s", (Id, ))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return 0 if answer is None else 1

# Checks if one can borrow the item
def isBorrowable(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT IsBorrowable FROM LibraryItem WHERE Id = %s", (Id,))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    # assuming that this field is never "None" since I set its value everytime. Might wanna change this.
    print(answer[0]) 
    return int(answer[0])

# 
def checkConditionsForCeo(dbObject):
    return not checkForCEO(dbObject)

def checkConditionsForManager(dbObject, managerId):
    if len(managerId) == 0:
        return True
    return isCEO(dbObject, managerId) or isManager(dbObject, managerId)

def checkConditionsForEmployee(dbObject, managerId):
    return not isCEO(dbObject, managerId) and isManager(dbObject, managerId)

def isReferenceBook(dbObject, Id):
    if getCategoryName(dbObject, Id) == "Reference Book":
        print("yes, ref")
        return 1
    else:
        print("no ref")
        return 0

# Functions for Category items
def addCategory(dbObject, name):
    if not checkInDatabase(dbObject, "Category", ["CategoryName"], [name]):
        dbObject.startConnection()
        dbObject.cursor.execute("INSERT INTO Category (CategoryName) VALUES (%s)", (name, ))
        dbObject.database.commit()
        print("Category was added!")
        dbObject.closeConnection()
    else:
        print("Cannot add this category since it already exists in database")

def editCategory(dbObject, Id, newName):
    if checkInDatabase(dbObject, "Category", ["Id"], [Id]):
        dbObject.startConnection()
        dbObject.cursor.execute("UPDATE Category CategoryName = %s WHERE Id = %s", (newName, Id))
        dbObject.database.commit()
        print("Category was edited!")
        dbObject.closeConnection()
    else:
        print("Cannot edit, category doesn't exist in database!")

def deleteCategory(dbObject, Id):
    if checkInDatabase(dbObject, "Category", ["Id"], [Id]) and \
          not checkInDatabase(dbObject, "Libraryitem", ["CategoryId"], [Id]):
        dbObject.startConnection()
        dbObject.cursor.execute("DELETE FROM Category WHERE Id = %s", (Id,))
        dbObject.database.commit()
        print("Category was deleted!")
        dbObject.closeConnection()
    else:
        print("Cannot delete category. It's connected to an library item.")

# Functions for Library items
def addLibraryItem(dbObject, values):
    # checking so that not both the name and type already exists
    if not checkInDatabase(dbObject, "Libraryitem", ["Title", "Type"], [values[1], values[-1]]): # made an assumption that titles cannot be exactly the same, not sure if this reasonable
        dbObject.startConnection()
        query = "INSERT INTO libraryitem (CategoryId, Title, Author, Pages, RunTimeMinutes, \
              IsBorrowable, Borrower, BorrowDate, Type) VALUES ({})".format(", ".join(["%s"] * len(values)))
        dbObject.cursor.execute(query, values)
        dbObject.database.commit()
        print("Item was added to database!")
        dbObject.closeConnection()
    else:
        print("Cannot add this item since it already exists in database")

def editItem(dbObject, Id, attribute, newValue):
    if checkInDatabase(dbObject, "LibraryItem", ["Id"] , [Id]):
        # not a nice implementation but works for now
        if attribute == "type":
            if not checkInDatabase(dbObject, "Category", ["Id"], [getCategoryId(dbObject, newValue)]):
                print("Not in database")
                addCategory(dbObject, newValue)
            categoryId = getCategoryId(dbObject, newValue)
            dbObject.startConnection()
            dbObject.cursor.execute("UPDATE LibraryItem SET CategoryId = %s WHERE Id = %s", (categoryId, Id))
            dbObject.cursor.execute("UPDATE LibraryItem SET " + attribute + " = %s WHERE Id = %s", (newValue, Id))  
            dbObject.database.commit()
            print("Item was edited!")
            dbObject.closeConnection()

        else:
            dbObject.startConnection()
            dbObject.cursor.execute("UPDATE LibraryItem SET " + attribute + " = %s WHERE Id = %s", (newValue, Id))  
            dbObject.database.commit()
            print("Item was edited!")
            dbObject.closeConnection()
    else:
        print("Cannot edit, item doesn't exist in database!")

def deleteItem(dbObject, Id):
    if checkInDatabase(dbObject, "LibraryItem", ["Id"], [Id]):
        dbObject.startConnection()
        dbObject.cursor.execute("DELETE FROM LibraryItem WHERE Id = %s", (Id,))
        dbObject.database.commit()
        print("Category was deleted!")
        dbObject.closeConnection()
    else:
        print("Cannot delete item. It's not in the database.") 


# Functions for employees
def addEmployee(dbObject, values):
    # No specification that employees must be uniqe, therefore no check in database
    dbObject.startConnection()
    query = "INSERT INTO Employees (FirstName, LastName, Salary, IsCEO, IsManager, \
            ManagerID) VALUES ({})".format(", ".join(["%s"] * len(values)))
    dbObject.cursor.execute(query, values)
    dbObject.database.commit()
    print("Employee was added to database!")
    dbObject.closeConnection()

def editEmployee(dbObject, Id, attribute, newValue):
    canEdit = 1
    if attribute == "isCEO":
        canEdit = not checkForCEO(dbObject)
    if checkInDatabase(dbObject, "Employees", ["Id"], [Id]) and canEdit:
        dbObject.startConnection()
        dbObject.cursor.execute("UPDATE Employees SET " + attribute + " = %s WHERE Id = %s", (newValue, Id))
        if attribute == "isCEO" and canEdit:
            dbObject.cursor.execute("UPDATE Employees SET ManagerId = %s WHERE Id = %s", (None, Id))
        dbObject.database.commit()
        dbObject.closeConnection()
    else:
        print("Cannot edit employee!")   

def deleteEmployee(dbObject, Id):
    if checkInDatabase(dbObject, "Employees", ["Id"], [Id]):
            dbObject.startConnection()
            dbObject.cursor.execute("DELETE FROM Employees WHERE Id = %s", (Id,))
            dbObject.database.commit()
            print("Category was deleted!")
            dbObject.closeConnection()
    else:
        print("Cannot delete item. It's not in the database.") 
    
# Functions for check in & check out
def checkIn(dbObject, Id):
    if checkInDatabase(dbObject, "LibraryItem", ["Id"], [Id]):
        dbObject.startConnection()
        dbObject.cursor.execute("UPDATE LibraryItem SET isBorrowable = %s WHERE Id = %s", (1, Id))
        dbObject.cursor.execute("UPDATE LibraryItem SET borrower = %s WHERE Id = %s", (None, Id))
        dbObject.cursor.execute("UPDATE LibraryItem SET borrowDate = %s WHERE Id = %s", (None, Id))
        dbObject.database.commit()
        print("Item was checked in!")
        dbObject.closeConnection()
    else:
        print("Cannot check in this item since it doesn't exists in database")

def checkOut(dbObject, Id, borrower):
    if checkInDatabase(dbObject, "LibraryItem", ["Id"], [Id]):
        currentDate = date.today()
        currentDate = currentDate.strftime("%Y-%m-%d")
        dbObject.startConnection()
        dbObject.cursor.execute("UPDATE LibraryItem SET isBorrowable = %s WHERE Id = %s", (0, Id))
        dbObject.cursor.execute("UPDATE LibraryItem SET borrower = %s WHERE Id = %s", (borrower, Id))
        dbObject.cursor.execute("UPDATE LibraryItem SET borrowDate = %s WHERE Id = %s", (currentDate, Id))
        dbObject.database.commit()
        print("Item was checked out!")
        dbObject.closeConnection()
    else:
        print("Cannot check in this item since it doesn't exists in database")

def getDataFromTable(dbObject, table, orderBy):
    dbObject.startConnection()
    query = "SELECT * FROM {} ORDER BY {}".format(table, orderBy)
    dbObject.cursor.execute(query)
    newValues = dbObject.cursor.fetchall()
    dbObject.closeConnection()
    return newValues