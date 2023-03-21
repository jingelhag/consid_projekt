# Library database viewer

Project for consid traniee. 

## Project description and features

This is library database viewer that holds functionality to handle times in a library.
It also can manage employees. For more detailed information on what features the application has, problem description can be found in this zip-file. Here one can read on what one can or can't do. 

### Installation

To be able to run this one needs to have:
- mysql server
- mysql workbench (Not sure if neccesary)
- python packages: tkinter and mysql-connector & of course python.  

The last on the list is easily installed with the command:

```bash
pip install tk
pip install mysql-connector
```

================

Follow the installation instructions for mysql server & workbench. Make sure to remember user & password.  

### Initialization

In databaseConnection.py one must configure user and passwd.


```python
def connectToDb(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root", # change if neccesary
            passwd="Juing02a", # change if neccesary
            auth_plugin='mysql_native_password',
            database="Library"
        )
        return db

def initialize(self):
        db = mysql.connector.connect(
                host="localhost",
                user="root", # change if neccesary
                passwd="Juing02a", # change if neccesary 
                auth_plugin='mysql_native_password'
            )
        dbCursor = db.cursor()
        dbCursor.execute("CREATE DATABASE Library")
        dbCursor.close()
        db.close()
```

===============

If using this application for the first time, uncomment theses two commands in main.py

```python
# Use these commands to remove database and setup everything from start :)

# databaseObject.removeDatabase()
databaseObject.initialize()
databaseObject.setupTables()
```

This will setup the database and the tables. Uncomment these afterwards since they will not be needed anymore.

If you want to start over and remove database, uncomment:


```python
# Use these commands to remove database and setup everything from start :)

databaseObject.removeDatabase()
databaseObject.initialize()
databaseObject.setupTables()
```

### Usage

First the user is greeted with an menu. 

One can choose to:
- Add category
- Add library item
- Add employee

These will add, if possible, a new item to the database. 

If the user wants to view what's inside each table, edit, delete, check in or check out items, one can click on:
- View categories
- View library items
- View employees


#### Add 
Fill in each inputs and the press submit to add to database.

#### Edit
- Select item to edit.
- Select which attribute to edit.
- Input new value and submit.

#### Delete
- Select item to delete.
- Press yes on pop-up to delete. No if not.

#### Check In
- Select item to check in.
- Press check in

#### Check out
- Select item to check out
- Write the name of the person who is lending the item 

### Future work
I've tried to test the software and find as much bugs as possible but there is a possibility that there can be a few left ;)

Stuff I know is a bit "janky":
- the sort button sometimes needs to be clicked two this before applying the right order on the table. 
- Haven't had time to check what happends to the attribute called "isBorrowable" if one where to change a reference book to something else.
- Inputs are checked somewhat but a user can input numbers as "first name". Sure it's a quickfix but I don' wanna mess with the application for now.  
- Some actions done in the software will not a pop-up window appear. Check terminal for information.
- Some pop-ups donesn't give exactly whats wrong more than that the opoeration is invalid.
- Some windows are not the right size, works well on some machine and some not so well.

There is probably more stuff that I haven't mentioned here.
