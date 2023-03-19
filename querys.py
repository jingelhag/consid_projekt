import databaseConnection as dc
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
    return answer[0]

def getCategoryName(dbObject, Id):
    dbObject.startConnection()
    dbObject.cursor.execute("SELECT Type FROM LibraryItem WHERE Id = %s", (Id,))
    answer = dbObject.cursor.fetchone()
    dbObject.closeConnection()
    return answer[0]
    

def getColumns(dbObject, table):
    dbObject.startConnection()
    query = "SHOW COLUMNS FROM {}".format(table)
    dbObject.cursor.execute(query)

    # Get the column names from the cursor fetchall method
    column_names = [col[0] for col in dbObject.cursor.fetchall()]
    return column_names   

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
    if checkInDatabase(dbObject, "Category", Id):
        dbObject.startConnection()
        dbObject.cursor.execute("UPDATE Category SET CategoryName = %s WHERE Id = %s", (newName, Id))
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
        dbObject.startConnection()
        # not a nice implementation but works for now
        if attribute == "Type":
            if not checkInDatabase(dbObject, "Category", ["Id"], [getCategoryId(dbObject, newValue)]):
                addCategory(dbObject, newValue)
                dbObject.cursor.execute("UPDATE Category SET CategoryName = %s WHERE Id = %s", (newValue, Id))
        
        dbObject.cursor.execute("UPDATE LibraryItem SET %s = %s WHERE Id = %s", (attribute, newValue, Id))  
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
