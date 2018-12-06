import sys
from tkinter import Tk

from yaps import Yaps
from gui import Gui

def runGui(app):
    root = Tk()
    gui = Gui(root, app)
    root.mainloop()
    root.destroy()

def runCli(app):
    app.setDirectory(sys.argv[1])
    if(len(sys.argv) > 2):
        app.setOutputDirectory(sys.argv[2])
    app.iterateFiles()


app = Yaps()

if(len(sys.argv) > 1):
    if sys.argv[1] == '--gui' or sys.argv[1] == '-g':
        runGui(app)
    else:
        runCli(app)
else:
    raise Exception('Not enough parameters')




