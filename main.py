import window_manager as wm
import databaseConnection
databaseObject = databaseConnection.databaseConnection()

# Use these commands to remove database and setup everything from start :)

# databaseObject.removeDatabase()
# databaseObject.initialize()
# databaseObject.setupTables()

root = wm.Tk()
root.geometry("200x100")
root.title("Library")

wm.centerWindow(root, 280, 100)
wm.setupMainMenu(root)

root.mainloop()
