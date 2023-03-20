from tkinter import *
import querys as qs
from tkinter import ttk

# to keep track on current sort option
currentSort = "Title"

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

# Submit functionality
def submitBook(selectCategoryWindow, submitBookWindow, title, author, pages):

    if qs.ef.checkInputBookOrReferenceBook(title, author, pages):
        dbObject = qs.dc.databaseConnection()
        titleWithAcronym = title + qs.ef.getAcronym(title)
        if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Book"]):
            values = (qs.getCategoryId(dbObject, "Book"), titleWithAcronym, author, pages, None, 1, None, None, "Book")
            qs.addLibraryItem(dbObject, values)
        else:
            qs.addCategory(dbObject, "Book")
            values = (qs.getCategoryId(dbObject, "Book"), titleWithAcronym, author, pages, None, 1, None, None, "Book")
            qs.addLibraryItem(dbObject, values)
        close_window(submitBookWindow)
        close_window(selectCategoryWindow)
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("300x50")
        centerWindow(wrongInputWindow, 300, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)

def submitDvd(selectCategoryWindow, submitBookWindow, title, runTimeInMinutes):
    if qs.ef.checkInputAudioBookorDvd(title, runTimeInMinutes):
        dbObject = qs.dc.databaseConnection()
        titleWithAcronym = title + qs.ef.getAcronym(title)
        if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Dvd"]):
            values = (qs.getCategoryId(dbObject, "Dvd"), titleWithAcronym, None, None, runTimeInMinutes, 1, None, None, "Dvd")
            qs.addLibraryItem(dbObject, values)
        else:
            qs.addCategory(dbObject, "Dvd")
            values = (qs.getCategoryId(dbObject, "Dvd"), titleWithAcronym, None, None, runTimeInMinutes, 1, None, None, "Dvd")
            qs.addLibraryItem(dbObject, values)
        close_window(submitBookWindow)
        close_window(selectCategoryWindow)
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("300x50")
        centerWindow(wrongInputWindow, 300, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)

def submitAudioBook(selectCategoryWindow, submitBookWindow, title, runTimeInMinutes):
    if qs.ef.checkInputAudioBookorDvd(title, runTimeInMinutes):
        dbObject = qs.dc.databaseConnection()
        titleWithAcronym = title + qs.ef.getAcronym(title)
        if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Audio Book"]):
            values = (qs.getCategoryId(dbObject, "Audio Book"), titleWithAcronym, None, None, runTimeInMinutes, 1, None, None, "Audio Book")
            qs.addLibraryItem(dbObject, values)
        else:
            qs.addCategory(dbObject, "Audio Book")
            values = (qs.getCategoryId(dbObject, "Audio Book"), titleWithAcronym, None, None, runTimeInMinutes, 1, None, None, "Audio Book")
            qs.addLibraryItem(dbObject, values)
        close_window(submitBookWindow)
        close_window(selectCategoryWindow)
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("300x50")
        centerWindow(wrongInputWindow, 300, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)

def submitReferenceBook(selectCategoryWindow, submitBookWindow, title, author, pages):
    if qs.ef.checkInputBookOrReferenceBook(title, author, pages):
        dbObject = qs.dc.databaseConnection()
        titleWithAcronym = title + qs.ef.getAcronym(title)
        if qs.checkInDatabase(dbObject, "Category", ["CategoryName"], ["Reference Book"]):
            values = (qs.getCategoryId(dbObject, "Reference Book"), titleWithAcronym, author, pages, None, 1, None, None, "Reference Book")
            qs.addLibraryItem(dbObject, values)
        else:
            qs.addCategory(dbObject, "Reference Book")
            # putting zero on isBorrowable
            values = (qs.getCategoryId(dbObject, "Reference Book"), title, author, pages, None, 0, None, None, "Reference Book")
            qs.addLibraryItem(dbObject, values)
        close_window(submitBookWindow)
        close_window(selectCategoryWindow)
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("300x50")
        centerWindow(wrongInputWindow, 300, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)

def submitCategory(name):
    if isinstance(name, str):
        dbConnection = qs.dc.databaseConnection()
        qs.addCategory(dbConnection, str(name))
        name.delete(0, END)
        del dbConnection
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("300x50")
        centerWindow(wrongInputWindow, 300, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)

def submitEmployee(submitEmployeeWindow, firstName, lastName, role, rank, managerId):
    if qs.ef.checkInputEmployee(firstName, lastName):
        dbObject = qs.dc.databaseConnection()
        if role == "Employee" and qs.checkConditionsForEmployee(dbObject, managerId):
            salary = 1.125*float(rank)
            values = (firstName, lastName,salary, 0, 0, managerId)
            qs.addEmployee(dbObject, values)
            close_window(submitEmployeeWindow)
        elif role == "Manager" and qs.checkConditionsForManager(dbObject, managerId):
            salary = 1.725*float(rank)
            if len(managerId) > 0:
                values = (firstName, lastName,salary, 0, 1, managerId)
                qs.addEmployee(dbObject, values)
            else:
                values = (firstName, lastName,salary, 0, 1, None)
                qs.addEmployee(dbObject, values)
            close_window(submitEmployeeWindow)
        elif role == "CEO" and qs.checkConditionsForCeo(dbObject):
            salary = 2.725*float(rank)
            values = (firstName, lastName,salary, 1, 0, None)
            qs.addEmployee(dbObject, values)
            close_window(submitEmployeeWindow)
        else:
            wrongInputWindow = Toplevel()
            wrongInputWindow.geometry("350x50")
            centerWindow(wrongInputWindow, 350, 50) 
            question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
            question.grid(row=0, column=0)
            placeWindowOnTop(wrongInputWindow)
    else:
        wrongInputWindow = Toplevel()
        wrongInputWindow.geometry("350x50")
        centerWindow(wrongInputWindow, 350, 50) 
        question = Label(wrongInputWindow, text="Wrong input! Make sure to match each input to its correct type")
        question.grid(row=0, column=0)
        placeWindowOnTop(wrongInputWindow)    

# add functionality
def addCategory():
    addCategoryWindow = Toplevel()
    addCategoryWindow.title("Category") 
    addCategoryWindow.geometry("350x100") 
    centerWindow(addCategoryWindow, 350, 100)

    category_name = Entry(addCategoryWindow, width=10)
    category_name.grid(row=0, column=1, padx=10)

    category_name_label  = Label(addCategoryWindow, text="Name of category (String)")
    category_name_label.grid(row=0, column=0)

    submit_button = Button(addCategoryWindow, text="Add category to database", command=lambda:submitCategory(category_name.get()))
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

    title_label  = Label(addBookWindow, text="Title (String)")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(addBookWindow, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(addBookWindow, text="Author (String)")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(addBookWindow, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(addBookWindow, text="Pages (Integer)")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(addBookWindow, text="Add book to database", command=lambda:submitBook(selectCategoryWindow, addBookWindow, title.get(), author.get(), pages.get()))
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

    title_label  = Label(addDvdWindow, text="Title (String)")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(addDvdWindow, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(addDvdWindow, text="Runtime in minutes (Integer)")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(addDvdWindow, text="Add DVD to database", command=lambda:submitDvd(selectCategoryWindow, addDvdWindow, title.get(), runTimesMinutes.get()))
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

    title_label  = Label(addAudioBookWindow, text="Title (String)")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(addAudioBookWindow, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(addAudioBookWindow, text="Runtime in minutes (Integer)")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(addAudioBookWindow, text="Add Audio book to database", command=lambda:submitAudioBook(selectCategoryWindow, addAudioBookWindow, title.get(), runTimesMinutes.get()))
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

    title_label  = Label(addReferenceBookWindow, text="Title (String)")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(addReferenceBookWindow, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(addReferenceBookWindow, text="Author (String)")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(addReferenceBookWindow, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(addReferenceBookWindow, text="Pages (Integer)")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(addReferenceBookWindow, text="Add book to database", command=lambda:submitReferenceBook(selectCategoryWindow, addReferenceBookWindow, title.get(), author.get(), pages.get()))
    submit_button.grid(row=3, column=0)
    placeWindowOnTop(addReferenceBookWindow)

def addEmployee():
    addEmployeeWindow = Toplevel()
    addEmployeeWindow.title("Libraryitems")
    addEmployeeWindow.geometry("300x160")  
    centerWindow(addEmployeeWindow, 300, 160)

    # First name input and label
    firstName = Entry(addEmployeeWindow, width=10)
    firstName.grid(row=0, column=1, padx=10)

    firstName_label  = Label(addEmployeeWindow, text="First name (String)")
    firstName_label.grid(row=0, column=0)
    
    # Last name input and label
    lastName = Entry(addEmployeeWindow, width=10)
    lastName.grid(row=1, column=1, padx=10)

    lastName_label  = Label(addEmployeeWindow, text="lastName (String)")
    lastName_label.grid(row=1, column=0)
    
    # Role input and label
    roles = ["CEO", "Manager", "Employee"]
    role = StringVar(addEmployeeWindow)
    role.set(roles[2])
    role.trace("w", lambda *args: showHideManagerId(role.get()))

    option_menu = OptionMenu(addEmployeeWindow, role, *roles)
    option_menu.grid(row=2, column=1, padx=10)

    role_label  = Label(addEmployeeWindow, text="Role")
    role_label.grid(row=2, column=0)


    def showHideManagerId(selected_option):
        if selected_option == "CEO":
            managerId.grid_remove()
        else:
            managerId.grid(row=3, column=1, padx=10)


    # Manager ID input and label
    managerId = Entry(addEmployeeWindow, width=10)
    managerId.grid(row=3, column=1, padx=10)

    managerId_label  = Label(addEmployeeWindow, text="Manager ID (Integer)")
    managerId_label.grid(row=3, column=0)

    ranks = list(range(1,10))
    rank = StringVar(addEmployeeWindow)
    rank.set(ranks[0])

    rank_menu = OptionMenu(addEmployeeWindow, rank, *ranks)
    rank_menu.grid(row=4, column=1, padx=10)

    rank_label  = Label(addEmployeeWindow, text="Rank")
    rank_label.grid(row=4, column=0)

    submit_button = Button(addEmployeeWindow, \
                            text="Add Employee to database", \
                            command=lambda:submitEmployee(addEmployeeWindow, firstName.get(), lastName.get(), role.get(), rank.get(), managerId.get()))
    submit_button.grid(row=5, column=0) 
    
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
    global currentSort
    selectedItem = tree.focus()
    Id = tree.item(selectedItem)["values"][0]
    editCategoryWindow = Toplevel()
    editCategoryWindow.geometry("250x100")
    centerWindow(editCategoryWindow, 250, 100) 
    question = Label(editCategoryWindow, text="Input the new value").pack()
    answer = Entry(editCategoryWindow, width=10)
    answer.pack()
    dbObject = qs.dc.databaseConnection()
    yesButton = Button(editCategoryWindow, text="Submit", command=lambda: (qs.editItem(dbObject, Id, attribute, answer.get()), close_window(editCategoryWindow), updateView(dbObject, tree, "LibraryItems", currentSort))).pack()

def editEmployee(tree, attribute):
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
    yesButton = Button(editCategoryWindow, text="Submit", command=lambda: (qs.editEmployee(dbObject, Id, attribute, answer.get()), close_window(editCategoryWindow), updateView(dbObject, tree, "Employees", "Id"))).pack()   

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
        deleteCategoryWindow.geometry("270x100")
        centerWindow(deleteCategoryWindow, 270, 100) 
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

def deleteEmployee(tree, dbObject):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        if not qs.checkDeleteEmployee(dbObject, Id):
            deleteEmployeeWindow = Toplevel()
            deleteEmployeeWindow.geometry("270x100")
            centerWindow(deleteEmployeeWindow, 270, 100) 
            question = Label(deleteEmployeeWindow, text="Are you sure you wanna delete this employee?").pack()
            dbObject = qs.dc.databaseConnection()
            yesButton = Button(deleteEmployeeWindow, text="Yes", command=lambda: (qs.deleteEmployee(dbObject, Id), updateView(dbObject, tree, "Employees", "Id"), close_window(deleteEmployeeWindow))).pack()
            noButton = Button(deleteEmployeeWindow, text="No", command=lambda:close_window(deleteEmployeeWindow)).pack()
        else:
            deleteEmployeeWindow = Toplevel()
            deleteEmployeeWindow.geometry("250x50")
            centerWindow(deleteEmployeeWindow, 250, 50) 
            question = Label(deleteEmployeeWindow, text="Operation can't be done!")
            question.grid(row=0, column=0)
    else:
        deleteEmployeeWindow = Toplevel()
        deleteEmployeeWindow.geometry("250x50")
        centerWindow(deleteEmployeeWindow, 250, 50) 
        question = Label(deleteEmployeeWindow, text="Operation can't be done!")
        question.grid(row=0, column=0)

# view functionality
def viewCategories():
    viewCategoriesWindow = Toplevel()
    tree = ttk.Treeview(viewCategoriesWindow)
    viewCategoriesWindow.geometry("300x300")
    centerWindow(viewCategoriesWindow, 300, 300) 
    # Set up the columns in the Treeview widget
    dbObject = qs.dc.databaseConnection()
    columns = qs.getColumns(dbObject, "Category")
    tree = ttk.Treeview(viewCategoriesWindow, columns=columns, show="headings")
    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=50)

    updateView(dbObject, tree, "Category", "Id")
    scrollbar =  Scrollbar(viewCategoriesWindow, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    tree.grid(row=0, column=0, sticky="nsew")
    tree.configure(yscrollcommand=scrollbar.set)

    # Create buttons
    editButton = Button(viewCategoriesWindow, text="Edit Category", command=lambda:editCategory(tree))
    deleteButton = Button(viewCategoriesWindow, text="Delete Category", command=lambda:deleteCategory(tree))
    # Place buttons in the grid
    editButton.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    deleteButton.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    

    viewCategoriesWindow.grid_columnconfigure(0, weight=1)
    viewCategoriesWindow.grid_rowconfigure(0, weight=1)

def viewLibraryItems():
    global currentSort
    viewLibraryItemsWindow = Toplevel()
    viewLibraryItemsWindow.geometry("720x400")
    centerWindow(viewLibraryItemsWindow, 720, 400) 
    # Set up the columns in the Treeview widget
    dbObject = qs.dc.databaseConnection()
    columns = qs.getColumns(dbObject, "LibraryItem")
    tree = ttk.Treeview(viewLibraryItemsWindow, columns=columns, show="headings")
    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=40)

    updateView(dbObject, tree, "LibraryItem", "Type")

    # Add the Treeview widget to a scrollable frame

    scrollbar =  Scrollbar(viewLibraryItemsWindow, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    tree.grid(row=0, column=0, sticky="nsew")
    tree.configure(yscroll=scrollbar.set)

    # Create buttons
    editButton = Button(viewLibraryItemsWindow, text="Edit Item", command=lambda: (selectItemAttribute(tree)))
    deleteButton = Button(viewLibraryItemsWindow, text="Delete Item", command=lambda: (deleteItem(tree)))
    checkInButton = Button(viewLibraryItemsWindow, text="Check In Item", command=lambda: (checkIn(tree)))
    checkOutButton = Button(viewLibraryItemsWindow, text="Check Out Item", command=lambda: (checkOut(tree)))
    sortButton = Button(viewLibraryItemsWindow, text="Sort by " + currentSort, command=lambda: (updateView(dbObject, tree, "LibraryItem", currentSort), updateButtonText(sortButton)))
    refreshButton =  Button(viewLibraryItemsWindow, text="Update table", command=lambda: (updateView(dbObject, tree, "LibraryItem", currentSort)))
    
    # Place buttons in the grid
    editButton.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    deleteButton.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    checkInButton.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    checkOutButton.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    sortButton.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    refreshButton.grid(row=6, column=0, padx=5, pady=5, sticky="e")

    # Bind the TreeviewSelect event to the on_select function
    viewLibraryItemsWindow.grid_columnconfigure(0, weight=1)
    viewLibraryItemsWindow.grid_rowconfigure(0, weight=1)

def viewEmployees():
    viewEmployeesWindow = Toplevel()
    tree = ttk.Treeview(viewEmployeesWindow)
    viewEmployeesWindow.geometry("350x300")
    centerWindow(viewEmployeesWindow, 350, 300) 
    # Set up the columns in the Treeview widget
    dbObject = qs.dc.databaseConnection()
    columns = qs.getColumns(dbObject, "Employees")
    tree = ttk.Treeview(viewEmployeesWindow, columns=columns, show="headings")
    tree["columns"] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=50)

    updateView(dbObject, tree, "Employees", "Id")
    scrollbar =  Scrollbar(viewEmployeesWindow, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    tree.grid(row=0, column=0, sticky="nsew")
    tree.configure(yscrollcommand=scrollbar.set)

    # Create buttons
    editButton = Button(viewEmployeesWindow, text="Edit Employee", command=lambda:selectEmployeeAttribute(tree))
    deleteButton = Button(viewEmployeesWindow, text="Delete Employee", command=lambda:deleteEmployee(tree, dbObject))
    # Place buttons in the grid
    editButton.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    deleteButton.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    

    viewEmployeesWindow.grid_columnconfigure(0, weight=1)
    viewEmployeesWindow.grid_rowconfigure(0, weight=1)

# Check In & Check Out
def checkIn(tree):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    dbObject = qs.dc.databaseConnection()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        if not qs.isBorrowable(dbObject, Id) and not qs.isReferenceBook(dbObject, Id):
            checkInWindow = Toplevel()
            checkInWindow.geometry("250x100")
            centerWindow(checkInWindow, 250, 100) 
            question = Label(checkInWindow, text="Are you sure you wanna check in this item?")
            question.grid(row=0, column=0)
            yesButton = Button(checkInWindow, text="Yes", command=lambda: (qs.checkIn(dbObject, Id), close_window(checkInWindow), updateView(dbObject, tree, "LibraryItem", currentSort)))
            yesButton.grid(row=1, column=0)
            noButton = Button(checkInWindow, text="No", command=lambda:close_window(checkInWindow))
            noButton.grid(row=1, column=1)
        else:
            checkInWindow = Toplevel()
            checkInWindow.geometry("300x50")
            centerWindow(checkInWindow, 300, 50) 
            question = Label(checkInWindow, text="Can't check in item since it's either a reference book or it is already check in!")
            question.grid(row=0, column=0)
    else:
        editCategoryWindow = Toplevel()
        editCategoryWindow.geometry("250x50")
        centerWindow(editCategoryWindow, 250, 50) 
        question = Label(editCategoryWindow, text="Select an item in the list you want to check in!")
        question.grid(row=0, column=0)

def checkOut(tree):
    # tree.focus holds the highlighted id number[0]
    selectedItem = tree.focus()
    dbObject = qs.dc.databaseConnection()
    if selectedItem:
        Id = tree.item(selectedItem)["values"][0]
        if qs.isBorrowable(dbObject, Id):
            checkInWindow = Toplevel()
            checkInWindow.geometry("250x100")
            centerWindow(checkInWindow, 250, 100) 
            question = Label(checkInWindow, text="Name of borrower:")
            question.grid(row=0, column=0)
            yesButton = Button(checkInWindow, text="Check out", command=lambda: (qs.checkOut(dbObject, Id, answer.get()), close_window(checkInWindow), updateView(dbObject, tree, "LibraryItem", currentSort)))
            yesButton.grid(row=1, column=0)
            answer = Entry(checkInWindow, width=10)
            answer.grid(row=0, column=1)
        else:
            checkInWindow = Toplevel()
            checkInWindow.geometry("250x50")
            centerWindow(checkInWindow, 250, 50) 
            question = Label(checkInWindow, text="Can't check out item since it already is checked out!")
            question.grid(row=0, column=0)
    else:
        editCategoryWindow = Toplevel()
        editCategoryWindow.geometry("250x50")
        centerWindow(editCategoryWindow, 250, 50) 
        question = Label(editCategoryWindow, text="Select an item in the list you want to check out!")
        question.grid(row=0, column=0)

def selectItemAttribute(tree):

    selectedItem = tree.focus()
    if selectedItem:
        selectCategoryWindow = Toplevel()
        selectCategoryWindow.geometry("220x260")

        centerWindow(selectCategoryWindow, 220, 260)

        question = Label(selectCategoryWindow, text="Select the attribute you want to edit").pack()

        title = Button(selectCategoryWindow, text="Title", command=lambda: editItem(tree, "Title")).pack()

        author = Button(selectCategoryWindow, text="Author", command=lambda: editItem(tree, "Author")).pack()

        pages = Button(selectCategoryWindow, text="Pages", command=lambda: editItem(tree, "Pages")).pack()

        runTimeMinutes = Button(selectCategoryWindow, text="Runtime in minutes", command=lambda: editItem(tree, "runTimeMinutes")).pack()

        borrower = Button(selectCategoryWindow, text="Borrower", command=lambda: editItem(tree, "borrower")).pack()

        borrowDate = Button(selectCategoryWindow, text="Borrow Date", command=lambda: editItem(tree, "borrowDate")).pack()

        itemType = Button(selectCategoryWindow, text="Type of item", command=lambda: editItem(tree, "type")).pack()
    else:
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x50")
        centerWindow(deleteCategoryWindow, 250, 50) 
        question = Label(deleteCategoryWindow, text="Select an item in the list you want to edit!")
        question.grid(row=0, column=0)

def selectEmployeeAttribute(tree):
    selectedItem = tree.focus()
    if selectedItem:
        selectCategoryWindow = Toplevel()
        selectCategoryWindow.geometry("220x230")

        centerWindow(selectCategoryWindow, 220, 230)

        question = Label(selectCategoryWindow, text="Select the attribute you want to edit").pack()

        firstName = Button(selectCategoryWindow, text="First Name", command=lambda: (editEmployee(tree, "firstName"), close_window(selectCategoryWindow))).pack()

        lastName = Button(selectCategoryWindow, text="Last Name", command=lambda: (editEmployee(tree, "lastName"), close_window(selectCategoryWindow))).pack()

        role = Button(selectCategoryWindow, text="Role", command=lambda: (selectRole(tree), close_window(selectCategoryWindow))).pack()
    else:
        deleteCategoryWindow = Toplevel()
        deleteCategoryWindow.geometry("250x50")
        centerWindow(deleteCategoryWindow, 250, 50) 
        question = Label(deleteCategoryWindow, text="Select an employee in the list you want to edit!")
        question.grid(row=0, column=0)

def selectRole(tree):
    selectedItem = tree.focus()
    Id = tree.item(selectedItem)["values"][0]
    selectCategoryWindow = Toplevel()
    selectCategoryWindow.geometry("220x230")

    centerWindow(selectCategoryWindow, 220, 230)

    question = Label(selectCategoryWindow, text="Select the new roll").pack()
    dbObject = qs.dc.databaseConnection()
    firstName = Button(selectCategoryWindow, text="CEO", command=lambda: (qs.editEmployee(dbObject, Id, "isCEO", 1), close_window(selectCategoryWindow))).pack()

    lastName = Button(selectCategoryWindow, text="Manager", command=lambda: (qs.editEmployee(dbObject, Id, "isManager", 1), close_window(selectCategoryWindow))).pack()

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

def updateView(dbObject, tree, table, orderBy):
    tree.delete(*tree.get_children())
    newValues = qs.getDataFromTable(dbObject, table, orderBy)
    for row in newValues:
        tree.insert("", END, values=row)
    print("Updating table")

def updateButtonText(button):
    global currentSort
    if currentSort == "Title":
        currentSort = "Type"
        button.config(text="Sort by Type")
    else:
        currentSort = "Title"
        button.config(text="Sort by Title")