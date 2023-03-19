import window_manager as wm

root = wm.Tk()
root.geometry("200x100")
root.title("Library")

wm.centerWindow(root, 280, 100)
wm.setupMainMenu(root)

root.mainloop()