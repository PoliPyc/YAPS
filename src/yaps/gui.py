from tkinter import scrolledtext as tkst
from tkinter import filedialog
from tkinter import *

class Gui:
    def __init__(self, master):
        self.src = ''
        self.target = ''

        destinationButtons = Frame(master)
        destinationButtons.pack()
        
        self.srcButton = Button(
            destinationButtons, text="Podaj katalog źródłowy", command=self.selectSrc
        )
        self.targetButton = Button(
            destinationButtons, text="Podaj katalog docelowy", command=self.selectTarget
        )

        fileMethods = Frame(master)
        fileMethods.pack()

        self.copyButton = Button(
            fileMethods, text="Kopiuj", command=self.copyFiles
        )
        self.moveButton = Button(
            fileMethods, text="Przenieś", command=self.moveFiles
        )

        self.srcButton.pack(side=LEFT)
        self.targetButton.pack(side=LEFT)

        self.copyButton.pack(side=LEFT)
        self.moveButton.pack(side=LEFT)

        self.consoleFrame = Frame(master, height=100)
        self.consoleFrame.pack()

        self.consoleText = tkst.ScrolledText(self.consoleFrame)
        self.consoleText.pack(side=TOP)

    def selectSrc(self):
        self.src = filedialog.askdirectory()
        self.updateConsoleText('Ustawiono katalog źródłowy: ' + self.src + '\n')

    def selectTarget(self):
        self.target = filedialog.askdirectory()
        self.updateConsoleText('Ustawiono katalog docelowy: ' + self.src + '\n')

    def updateConsoleText(self, text):
        self.consoleText.insert(INSERT, text)

    def copyFiles(self):
        pass

    def moveFiles(self):
        pass