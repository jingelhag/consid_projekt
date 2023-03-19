from tkinter import *

def centerWindow(root, width, height):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position of window
    x = (screen_width // 2) - (200 // 2)  # Change 'width' to your window's width
    y = (screen_height // 2) - (100 // 2)  # Change 'height' to your window's height

    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def placeWindowOnTop(top):
    top.attributes("-topmost", True)

def submitBook(title, author, pages):
    print(title.get())
    print(author.get())
    print(pages.get())
    title.delete(0, END)
    author.delete(0, END)
    pages.delete(0, END)

def submitDvd(title, runTimeInMinutes):
    print(title.get())
    print(runTimeInMinutes.get())
    title.delete(0, END)
    runTimeInMinutes.delete(0, END)

def submitAudioBook(title, runTimeInMinutes):
    print(title.get())
    print(runTimeInMinutes.get())
    title.delete(0, END)
    runTimeInMinutes.delete(0, END)

def submitReferenceBook(title, author, pages):
    print(title.get())
    print(author.get())
    print(pages.get())
    title.delete(0, END)
    author.delete(0, END)
    pages.delete(0, END)

def addCategory():
    top = Toplevel()
    top.title("Category") 
    top.geometry("350x100")  
    centerWindow(top, 350, 100)

    category_name = Entry(top, width=10)
    category_name.grid(row=0, column=1, padx=10)

    category_name_label  = Label(top, text="Name of category")
    category_name_label.grid(row=0, column=0)

    submit_button = Button(top, text="Add category to database", command=lambda:submitCategory(category_name))
    submit_button.grid(row=1, column=0)
    placeWindowOnTop(top)

def addBook():
    top = Toplevel()
    top.title("Libraryitems")
    top.geometry("300x130")  
    centerWindow(top, 300, 130)

    # Title input and label
    title = Entry(top, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(top, text="Title")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(top, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(top, text="Author")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(top, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(top, text="Pages")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(top, text="Add book to database", command=lambda:submitBook(title, author, pages))
    submit_button.grid(row=3, column=0) 
    
    placeWindowOnTop(top)

def addDvd():
    top = Toplevel()
    top.title("Libraryitems")
    top.geometry("300x110")  
    centerWindow(top, 300, 110)
    # Title input and label
    title = Entry(top, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(top, text="Title")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(top, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(top, text="Runtime in minutes")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(top, text="Add DVD to database", command=lambda:submitDvd(title, runTimesMinutes))
    submit_button.grid(row=2, column=0) 
    
    placeWindowOnTop(top)

def addAudioBook():
    top = Toplevel()
    top.title("Add audio book")
    top.geometry("340x100")  
    centerWindow(top, 340, 100)
    # Title input and label
    title = Entry(top, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(top, text="Title")
    title_label.grid(row=0, column=0)

    # runTimeMinutes input and label
    runTimesMinutes = Entry(top, width=10)
    runTimesMinutes.grid(row=1, column=1, padx=10)

    runTimesMinutes_label  = Label(top, text="Runtime in minutes")
    runTimesMinutes_label.grid(row=1, column=0)
    
    submit_button = Button(top, text="Add Audio book to database", command=lambda:submitAudioBook(author))
    submit_button.grid(row=2, column=0) 
    placeWindowOnTop(top)

def addReferenceBook():
    
    top = Toplevel()
    top.title("Add reference book")
    top.geometry("300x130")  
    centerWindow(top, 300, 130)
    # Title input and label
    title = Entry(top, width=10)
    title.grid(row=0, column=1, padx=10)

    title_label  = Label(top, text="Title")
    title_label.grid(row=0, column=0)
    
    # Author input and label
    author = Entry(top, width=10)
    author.grid(row=1, column=1, padx=10)

    author_label  = Label(top, text="Author")
    author_label.grid(row=1, column=0)
    
    # Pages input and label
    pages = Entry(top, width=10)
    pages.grid(row=2, column=1, padx=10)

    pages_label  = Label(top, text="Pages")
    pages_label.grid(row=2, column=0)
    
    submit_button = Button(top, text="Add book to database", command=lambda:submitBook(author))
    submit_button.grid(row=3, column=0)
    placeWindowOnTop(top)

def addEmployee():
    top = Toplevel()
    top.title("Employees") 
    top.geometry("220x120")
    centerWindow(top, 220, 120)
    placeWindowOnTop(top)

def selectCategory():

    top = Toplevel()
    top.geometry("220x120")

    centerWindow(top, 220, 120)

    book = Button(top, text="Book", command=addBook).pack()

    dvd = Button(top, text="DVD", command=addDvd).pack()

    audioBook = Button(top, text="Audio Book", command=addAudioBook).pack()

    refrenceBook = Button(top, text="Reference Book", command=addReferenceBook).pack()

    placeWindowOnTop(top)

def setupMainMenu(root):
    categoryButton = Button(root, text="Add Category", command=addCategory)
    categoryButton.grid(row=0, column=0)

    libraryItemButton = Button(root, text="Add Libraryitem", command=selectCategory)
    libraryItemButton.grid(row=1, column=0)

    employeesButton = Button(root, text="Add Employee", command=addEmployee)
    employeesButton.grid(row=2, column=0)

    categoryViewButton = Button(root, text="View Categories", command=addCategory)
    categoryViewButton.grid(row=0, column=1)


    libraryItemViewButton = Button(root, text="View Libraryitem", command=selectCategory)
    libraryItemViewButton.grid(row=1, column=1)

    employeesViewButton = Button(root, text="View Employees", command=addEmployee)
    employeesViewButton.grid(row=2, column=1)