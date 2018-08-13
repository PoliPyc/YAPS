import sys
import os
import magic
import exifread
import datetime
from shutil import copyfile
from tkinter import scrolledtext as tkst
from tkinter import filedialog
from tkinter import *


class Yaps:
    def __init__(self):
        self.UNKNOWN_DIR = 'unknown_date'
        self.directory = False
        self.outputDirectory = False

    def setDirectory(self, directory):
        if(os.path.isdir(directory)):
            self.directory = directory
        else:
            raise FileNotFoundError('Directory not found')

    def setOutputDirectory(self, directory):
        if(os.path.isdir(directory)):
            if not self.os.access(directory, os.W_OK):
                raise Exception('Directory not writable')

            self.outputDirectory = directory
        else:
            raise FileNotFoundError('Output directory not found')

    def iterateFiles(self):
        for filename in os.listdir(self.directory):
            print('Znaleziono plik: ', filename)
            fullFilePath = self.directory + '/' + filename
            if(os.path.isdir(fullFilePath)):
                continue
            if(self.checkIfImage(fullFilePath)):
                imageDate = self.readExifData(fullFilePath)

                if imageDate:
                    dirName = self.getDirNameByDate(imageDate)
                else:
                    dirName = self.UNKNOWN_DIR

                self.createDirIfNotExist(dirName)

                if(self.outputDirectory):
                    target = self.outputDirectory + '/' + dirName + '/' + filename
                else:
                    target = './' + dirName + '/' + filename
                self.copyFileIfNotExist(fullFilePath, target)

    def checkIfImage(self, filename):
        BMP_MIME = 'image/bmp'
        JPEG_MIME = 'image/jpeg'
        GIF_MIME = 'image/gif'

        mime = magic.Magic(mime=True)
        file_mime = mime.from_file(filename)
        if(file_mime == BMP_MIME or file_mime == JPEG_MIME or file_mime == GIF_MIME):
            return True
        else:
            return False

    def readExifData(self, filename):
        f = open(filename, 'rb')
        tags = exifread.process_file(f, details=False)
        f.close()

        if 'Image DateTime' in tags:
            print("Zdjęcie zrobiono dnia: ",tags['Image DateTime'])
            return tags['Image DateTime'].values
        else:
            return False

    def getDirNameByDate(self, date):
        try:
            return datetime.datetime.strptime(date, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')
        except ValueError:
            return self.UNKNOWN_DIR

    def createDirIfNotExist(self, name):
        if(self.outputDirectory):
            directory = self.outputDirectory + '/' + name
        else:
            directory = './' + name

        if(os.path.isdir(directory)):
            return
        os.mkdir(directory)

    def copyFileIfNotExist(self, src, target):
        return copyfile(src, target)

class Gui:
    def __init__(self, master):
        self.src = ''
        self.target = ''

        w = Label(master, text="YAPS (Yet Another Picture Sorter")
        w.pack()

        frame = Frame(master)
        frame.pack()
        
        self.srcButton = Button(
            frame, text="Podaj katalog źródłowy", command=self.selectSrc
        )
        self.targetButton = Button(
            frame, text="Podaj katalog docelowy", command=self.selectTarget
        )
        self.srcButton.pack(side=TOP)
        self.targetButton.pack(side=TOP)

        self.consoleFrame = Frame(master, height=200)
        self.consoleFrame.pack()

        self.consoleText = tkst.ScrolledText(self.consoleFrame)
        self.consoleText.pack(side=TOP)



    def selectSrc(self):
        self.src = filedialog.askdirectory()
        self.updateConsoleText('Source directory set as: ' + self.src + '\n')

    def selectTarget(self):
        self.target = filedialog.askdirectory()
        self.updateConsoleText('Target directory set as: ' + self.src + '\n')

    def updateConsoleText(self, text):
        self.consoleText.insert(INSERT, text)

# app = Yaps()

# if(len(sys.argv) > 1):
#     app.setDirectory(sys.argv[1])
# else:
#     raise Exception('Not enough parameters')

# if(len(sys.argv) > 2):
#     app.setOutputDirectory(sys.argv[2])

# app.iterateFiles()

root = Tk()
gui = Gui(root)
root.mainloop()
root.destroy()
