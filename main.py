import sys
from tkinter import Tk

from yaps import Yaps
from gui import Gui

def runGui():
    root = Tk()
    gui = Gui(root)
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
        runGui()
    else:
        runCli()
else:
    raise Exception('Not enough parameters')




