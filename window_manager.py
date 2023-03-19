from tkinter import *
import querys as qs
from tkinter import ttk

def centerWindow(root, width, height):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position of window
    x = (screen_width // 2) - (200 // 2)  # Change 'width' to your window's width
    y = (screen_height // 2) - (100 // 2)  # Change 'height' to your window's height

    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def placeWindowOnTop(window):
    window.attributes("-topmost", True)

def submitBook(selectCategoryWindow, submitBookWindow, title, author, pages):
    dbObject = qs.dc.databaseConnection()
    if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Book"]):
        values = (qs.getCategoryId(dbObject, "Book"), title.get(), author.get(), pages.get(), None, 1, None, None, "Book")
        qs.addLibraryItem(dbObject, values)
    else:
        qs.addCategory(dbObject, "Book")
        values = (qs.getCategoryId(dbObject, "Book"), title.get(), author.get(), pages.get(), None, 1, None, None, "Book")
        qs.addLibraryItem(dbObject, values)
    title.delete(0, END)
    author.delete(0, END)
    pages.delete(0, END)
    close_window(submitBookWindow)
    close_window(selectCategoryWindow)

def submitDvd(selectCategoryWindow, submitBookWindow, title, runTimeInMinutes):
    dbObject = qs.dc.databaseConnection()
    if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Dvd"]):
        values = (qs.getCategoryId(dbObject, "Dvd"), title.get(), None, None, runTimeInMinutes.get(), 1, None, None, "Dvd")
        qs.addLibraryItem(dbObject, values)
    else:
        qs.addCategory(dbObject, "Dvd")
        values = (qs.getCategoryId(dbObject, "Dvd"), title.get(), None, None, runTimeInMinutes.get(), 1, None, None, "Dvd")
        qs.addLibraryItem(dbObject, values)
    title.delete(0, END)
    runTimeInMinutes.delete(0, END)
    close_window(submitBookWindow)
    close_window(selectCategoryWindow)

def submitAudioBook(selectCategoryWindow, submitBookWindow, title, runTimeInMinutes):
    dbObject = qs.dc.databaseConnection()
    if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Audio Book"]):
        values = (qs.getCategoryId(dbObject, "Audio Book"), title.get(), None, None, runTimeInMinutes.get(), 1, None, None, "Audio Book")
        qs.addLibraryItem(dbObject, values)
    else:
        qs.addCategory(dbObject, "Audio Book")
        values = (qs.getCategoryId(dbObject, "Audio Book"), title.get(), None, None, runTimeInMinutes.get(), 1, None, None, "Audio Book")
        qs.addLibraryItem(dbObject, values)
    title.delete(0, END)
    runTimeInMinutes.delete(0, END)
    close_window(submitBookWindow)
    close_window(selectCategoryWindow)

def submitReferenceBook(selectCategoryWindow, submitBookWindow, title, author, pages):
    dbObject = qs.dc.databaseConnection()
    if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Reference Book"]):
        values = (qs.getCategoryId(dbObject, "Reference Book"), title.get(), author.get(), pages.get(), None, 1, None, None, "Reference Book")
        qs.addLibraryItem(dbObject, values)
    else:
        qs.addCategory(dbObject, "Reference Book")
        # putting zero on isBorrowable
        values = (qs.getCategoryId(dbObject, "Reference Book"), title.get(), author.get(), pages.get(), None, 0, None, None, "Reference Book")
        qs.addLibraryItem(dbObject, values)
    title.delete(0, END)
    author.delete(0, END)
    pages.delete(0, END)
    close_window(submitBookWindow)
    close_window(selectCategoryWindow)

def submitCategory(name):
    dbConnection = qs.dc.databaseConnection()
    qs.addCategory(dbConnection, str(name.get()))
    name.delete(0, END)
    del dbConnection

# add functionality
def addCategory():
    addCategoryWindow = Toplevel()
    addCategoryWindow.title("Category") 
    addCategoryWindow.geometry("350x100") 
    centerWindow(addCategoryWindow, 350, 100)

    category_name = Entry(addCategoryWindow, width=10)
    category_name.grid(row=0, column=1, padx=10)

    category_name_label  = Label(addCategoryWindow, text="Name of category")
    category_name_label.grid(row=0, column=0)

    submit_button = Button(addCategoryWindow, text="Add category to database", command=lambda:submitCategory(category_name))
    submit_button.grid(row=1, column=0)
    placeWindowOnTop(addCategoryWindow)

def addBook(selectCategoryWindow):
    addBookWindow = Toplevel()
    addBookWindow.title("Libraryitems")
    addBookWindow.geometry("300x130")  
    centerWindow(addBookWindow, 300, 130)

    # Title input and label
    title = Entry(addBookWindow, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(addBookWindow, text="Title")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(addBookWindow, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(addBookWindow, text="Author")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(addBookWindow, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(addBookWindow, text="Pages")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(addBookWindow, text="Add book to database", command=lambda:submitBook(selectCategoryWindow, addBookWindow, title, author, pages))
    submit_button.grid(row=3, column=0) 
    
    placeWindowOnTop(addBookWindow)

def addDvd(selectCategoryWindow):
    addDvdWindow = Toplevel()
    addDvdWindow.title("Libraryitems")
    addDvdWindow.geometry("300x110")  
    centerWindow(addDvdWindow, 300, 110)
    # Title input and label
    title = Entry(addDvdWindow, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(addDvdWindow, text="Title")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(addDvdWindow, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(addDvdWindow, text="Runtime in minutes")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(addDvdWindow, text="Add DVD to database", command=lambda:submitDvd(selectCategoryWindow, addDvdWindow, title, runTimesMinutes))
    submit_button.grid(row=2, column=0) 
    
    placeWindowOnTop(addDvdWindow)

def addAudioBook(selectCategoryWindow):
    addAudioBookWindow = Toplevel()
    addAudioBookWindow.title("Add audio book")
    addAudioBookWindow.geometry("340x100")  
    centerWindow(addAudioBookWindow, 340, 100)
    # Title input and label
    title = Entry(addAudioBookWindow, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(addAudioBookWindow, text="Title")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(addAudioBookWindow, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(addAudioBookWindow, text="Runtime in minutes")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(addAudioBookWindow, text="Add Audio book to database", command=lambda:submitAudioBook(selectCategoryWindow, addAudioBookWindow, title, runTimesMinutes))
    submit_button.grid(row=2, column=0) 
    placeWindowOnTop(addAudioBookWindow)

def addReferenceBook(selectCategoryWindow):
    addReferenceBookWindow = Toplevel()
    addReferenceBookWindow.title("Add reference book")
    addReferenceBookWindow.geometry("300x130")  
    centerWindow(addReferenceBookWindow, 300, 130)
    # Title input and label
    title = Entry(addReferenceBookWindow, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(addReferenceBookWindow, text="Title")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(addReferenceBookWindow, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(addReferenceBookWindow, text="Author")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(addReferenceBookWindow, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(addReferenceBookWindow, text="Pages")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(addReferenceBookWindow, text="Add book to database", command=lambda:submitReferenceBook(selectCategoryWindow, addReferenceBookWindow, title, author, pages))
    submit_button.grid(row=3, column=0)
    placeWindowOnTop(addReferenceBookWindow)

def addEmployee():
    addEmployeeWindow = Toplevel()
    addEmployeeWindow.title("Employees") 
    addEmployeeWindow.geometry("220x120")
    centerWindow(addEmployeeWindow, 220, 120)
    placeWindowOnTop(addEmployeeWindow)

def addItem():
    addItemWindow = Toplevel()
    addItemWindow.geometry("220x120")

    centerWindow(addItemWindow, 220, 120)

    book = Button(addItemWindow, text="Book", command=lambda: addBook(addItemWindow)).pack()

    dvd = Button(addItemWindow, text="DVD", command=lambda: addDvd(addItemWindow)).pack()

    audioBook = Button(addItemWindow, text="Audio Book", command=lambda: addAudioBook(addItemWindow)).pack()

    refrenceBook = Button(addItemWindow, text="Reference Book", command=lambda: addReferenceBook(addItemWindow)).pack()

    placeWindowOnTop(addItemWindow)

# edit functionality
def editCategory(tree):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        editCategoryWindow = Toplevel()
        editCategoryWindow.geometry("250x100")
        centerWindow(editCategoryWindow, 850, 100) 
        question = Label(editCategoryWindow, text="Write the new name").pack()
        answer = Entry(editCategoryWindow, width=10)
        answer.pack()
        dbObject = qs.dc.databaseConnection()
        yesButton = Button(editCategoryWindow, text="Submit", command=lambda: (qs.editCategory(dbObject, Id, str(answer.get())), close_window(editCategoryWindow))).pack()
    else:
        editCategoryWindow = Toplevel()
        editCategoryWindow.geometry("250x50")
        centerWindow(editCategoryWindow, 250, 50) 
        question = Label(editCategoryWindow, text="Select a category in the list you want to edit!")
        question.grid(row=0, column=0)

def editItem(tree, attribute):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    Id = tree.item(selectedItem)["values"][0]
    editCategoryWindow = Toplevel()
    editCategoryWindow.geometry("250x100")
    centerWindow(editCategoryWindow, 250, 100) 
    question = Label(editCategoryWindow, text="Input the new value").pack()
    answer = Entry(editCategoryWindow, width=10)
    answer.pack()
    dbObject = qs.dc.databaseConnection()
    yesButton = Button(editCategoryWindow, text="Submit", command=lambda: (qs.editCategory(dbObject, Id, attribute, answer.get()), close_window(editCategoryWindow))).pack()

# delete functionality
def deleteCategory(tree):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x100")
        centerWindow(deleteCategoryWindow, 850, 100) 
        question = Label(deleteCategoryWindow, text="Are you sure you wanna delete this item?")
        question.grid(row=0, column=0)
        dbObject = qs.dc.databaseConnection()
        yesButton = Button(deleteCategoryWindow, text="Yes", command=lambda: (qs.deleteCategory(dbObject, Id), close_window(deleteCategoryWindow)))
        yesButton.grid(row=1, column=0)

        noButton = Button(deleteCategoryWindow, text="No", command=lambda:close_window(deleteCategoryWindow))
        noButton.grid(row=1, column=1)
    else:
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x50")
        centerWindow(deleteCategoryWindow, 250, 50) 
        question = Label(deleteCategoryWindow, text="Select an item in the list you want to delete!")
        question.grid(row=0, column=0)

def deleteItem(tree):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x100")
        centerWindow(deleteCategoryWindow, 850, 100) 
        question = Label(deleteCategoryWindow, text="Are you sure you wanna delete this item?")
        question.grid(row=0, column=0)
        dbObject = qs.dc.databaseConnection()
        yesButton = Button(deleteCategoryWindow, text="Yes", command=lambda: (qs.deleteItem(dbObject, Id), close_window(deleteCategoryWindow)))
        yesButton.grid(row=1, column=0)

        noButton = Button(deleteCategoryWindow, text="No", command=lambda:close_window(deleteCategoryWindow))
        noButton.grid(row=1, column=1)
    else:
        editCategoryWindow = Toplevel()
        editCategoryWindow.geometry("250x50")
        centerWindow(editCategoryWindow, 250, 50) 
        question = Label(editCategoryWindow, text="Select an item in the list you want to delete!")
        question.grid(row=0, column=0)

# view functionality
def viewCategories():
    viewCategoriesWindow = Toplevel()
    tree = ttk.Treeview(viewCategoriesWindow)
    viewCategoriesWindow.geometry("400x400")
    centerWindow(viewCategoriesWindow, 400, 400) 
    # Set up the columns in the Treeview widget
    dbObject = qs.dc.databaseConnection()
    columns = qs.getColumns(dbObject, "Category")
    tree["columns"] = columns
    for col in columns:
        tree.column(col, width=100)
        tree.heading(col, text=col)

    # Starts connection and fetches from table
    dbObject.startConnection()

    query = "SELECT * FROM {}".format("Category")
    dbObject.cursor.execute(query)

    for row in dbObject.cursor.fetchall():
        tree.insert("", END, values=row)

    dbObject.closeConnection()

    # Add the Treeview widget to a scrollable frame

    scrollbar =  Scrollbar(viewCategoriesWindow, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    tree.grid(row=0, column=0, sticky="nsew")
    tree.configure(yscrollcommand=scrollbar.set)

    # Create buttons
    editButton = Button(viewCategoriesWindow, text="Edit Category", command=lambda:editCategory(tree))
    deleteButton = Button(viewCategoriesWindow, text="Delete Category", command=lambda:deleteCategory(tree))

    # Place buttons in the grid
    editButton.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    deleteButton.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    # Bind the TreeviewSelect event to the on_select function
    viewCategoriesWindow.grid_columnconfigure(0, weight=1)
    viewCategoriesWindow.grid_rowconfigure(0, weight=1)

def viewLibraryItems():
    viewLibraryItemsWindow = Toplevel()
    tree = ttk.Treeview(viewLibraryItemsWindow)
    viewLibraryItemsWindow.geometry("400x400")
    centerWindow(viewLibraryItemsWindow, 400, 400) 
    # Set up the columns in the Treeview widget
    dbObject = qs.dc.databaseConnection()
    columns = qs.getColumns(dbObject, "LibraryItem")
    tree["columns"] = columns
    for col in columns:
        tree.column(col, width=100)
        tree.heading(col, text=col)

    # Starts connection and fetches from table
    dbObject.startConnection()

    query = "SELECT * FROM {}".format("LibraryItem")
    dbObject.cursor.execute(query)

    for row in dbObject.cursor.fetchall():
        tree.insert("", END, values=row)

    dbObject.closeConnection()

    # Add the Treeview widget to a scrollable frame

    scrollbar =  Scrollbar(viewLibraryItemsWindow, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    tree.grid(row=0, column=0, sticky="w")
    tree.configure(yscrollcommand=scrollbar.set)

    # Create buttons
    editButton = Button(viewLibraryItemsWindow, text="Edit Item", command=lambda:selectItemAttribute(tree))
    deleteButton = Button(viewLibraryItemsWindow, text="Delete Item", command=lambda:deleteItem(tree))

    # Place buttons in the grid
    editButton.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    deleteButton.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    # Bind the TreeviewSelect event to the on_select function
    viewLibraryItemsWindow.grid_columnconfigure(0, weight=1)
    viewLibraryItemsWindow.grid_rowconfigure(0, weight=1)

def viewEmployees():
    print()

def selectItemAttribute(tree):

    selectedItem = tree.focus()
    if selectedItem:
        selectCategoryWindow = Toplevel()
        selectCategoryWindow.geometry("220x200")

        centerWindow(selectCategoryWindow, 220, 170)

        question = Label(selectCategoryWindow, text="Select the attribute you want to edit").pack()

        title = Button(selectCategoryWindow, text="Title", command=lambda: editItem(tree, "title")).pack()

        author = Button(selectCategoryWindow, text="Author", command=lambda: editItem(tree, "author")).pack()

        pages = Button(selectCategoryWindow, text="Pages", command=lambda: editItem(tree, "pages")).pack()

        runTimeMinutes = Button(selectCategoryWindow, text="Runtime in minutes", command=lambda: editItem(tree, "runTimeMinutes")).pack()

        borrower = Button(selectCategoryWindow, text="Borrower", command=lambda: editItem(tree, "borrower")).pack()

        borrowDate = Button(selectCategoryWindow, text="Borrow Date", command=lambda: editItem(tree, "borrowDate")).pack()

        itemType = Button(selectCategoryWindow, text="Runtime in minutes", command=lambda: editItem(tree, "type")).pack()

        placeWindowOnTop(selectCategoryWindow)
    else:
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x50")
        centerWindow(deleteCategoryWindow, 250, 50) 
        question = Label(deleteCategoryWindow, text="Select an item in the list you want to edit!")
        question.grid(row=0, column=0)

def setupMainMenu(root):
    categoryButton = Button(root, text="Add Category", command=addCategory)
    categoryButton.grid(row=0, column=0)

    libraryItemButton = Button(root, text="Add Libraryitem", command=addItem)
    libraryItemButton.grid(row=1, column=0)

    employeesButton = Button(root, text="Add Employee", command=addEmployee)
    employeesButton.grid(row=2, column=0)

    categoryViewButton = Button(root, text="View Categories", command=viewCategories)
    categoryViewButton.grid(row=0, column=1)


    libraryItemViewButton = Button(root, text="View Libraryitem", command=viewLibraryItems)
    libraryItemViewButton.grid(row=1, column=1)

    employeesViewButton = Button(root, text="View Employees", command=viewEmployees)
    employeesViewButton.grid(row=2, column=1)

def close_window(window):
    window.destroy()

def checkBookInput(values):
    print()

def getAcronym(stringVariable):
   
    # add first letter
    output = stringVariable[0]
     
    # iterate over string
    for i in range(1, len(stringVariable)):
        if stringVariable[i-1] == ' ':
           
            # add letter next to space
            output += stringVariable[i]
             
    # uppercase oupt
    output = output.upper()
    return output