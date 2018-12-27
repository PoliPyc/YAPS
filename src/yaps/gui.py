from tkinter import scrolledtext as tkst
from tkinter import filedialog
from tkinter import *

class Gui:
    def __init__(self, master, yaps):
        LIGHT_TEXT = "#EDEFE6"
        CONTRAST_TEXT = "#670167"
        MAIN_BACKGROUND = "#9291A1"
        BUTTON_BACKGROUND = "#E95F6A"
        CONTENT_BACKGROUND = "#6A8DC5"

        BUTTON_WIDTH = 30

        self.yaps = yaps
        self.src = ''
        self.target = ''

        destinationButtons = Frame(master, bg=MAIN_BACKGROUND, pady=5)
        destinationButtons.pack()
        
        self.srcButton = Button(
            destinationButtons, text="Podaj katalog źródłowy", bg=BUTTON_BACKGROUND, width=BUTTON_WIDTH, fg=LIGHT_TEXT, bd=0, command=self.selectSrc
        )
        self.targetButton = Button(
            destinationButtons, text="Podaj katalog docelowy", bg=BUTTON_BACKGROUND, width=BUTTON_WIDTH, fg=LIGHT_TEXT, bd=0, command=self.selectTarget
        )

        fileMethods = Frame(master, bg=MAIN_BACKGROUND, pady=5)
        fileMethods.pack()

        self.copyButton = Button(
            fileMethods, text="Kopiuj", bg=BUTTON_BACKGROUND, width=BUTTON_WIDTH, fg=LIGHT_TEXT, bd=0, command=self.copyFiles
        )
        self.moveButton = Button(
            fileMethods, text="Przenieś", bg=BUTTON_BACKGROUND, width=BUTTON_WIDTH, fg=LIGHT_TEXT, bd=0, command=self.moveFiles
        )

        self.srcButton.pack(side=LEFT, padx=2)
        self.targetButton.pack(side=LEFT, padx=2)

        self.copyButton.pack(side=LEFT, padx=2)
        self.moveButton.pack(side=LEFT, padx=2)

        self.consoleFrame = Frame(master, height=100)
        self.consoleFrame.pack()

        self.consoleText = tkst.ScrolledText(self.consoleFrame, bg=CONTENT_BACKGROUND, fg=CONTRAST_TEXT, padx=5, pady=5)
        self.consoleText.pack(side=TOP)

    def selectSrc(self):
        self.src = filedialog.askdirectory()
        self.yaps.setDirectory(self.src)
        self.updateConsoleText('Ustawiono katalog źródłowy: ' + self.src + '\n')

    def selectTarget(self):
        self.target = filedialog.askdirectory()
        self.yaps.setOutputDirectory(self.target)
        self.updateConsoleText('Ustawiono katalog docelowy: ' + self.target + '\n')

    def updateConsoleText(self, text):
        self.consoleText.insert(INSERT, text)

    def copyFiles(self):
        try:
            self.updateConsoleText('Transfer zdjęć...\n')
            self.yaps.iterateFiles()
            self.updateConsoleText('Zakończono\n')
        except Exception as e:
            self.updateConsoleText('Błąd: ' + e.value + '\n')



    def moveFiles(self):
        self.updateConsoleText('Funkcja jeszcze nieaktywna\n')