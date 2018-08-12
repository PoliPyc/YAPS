import sys
import os
import magic

class Yaps:
    def setDirectory(self, directory):
        if(os.path.isdir(directory)):
            self.directory = directory
        else:
            raise FileNotFoundError('Directory not found')

    def iterateFiles(self):
        for filename in os.listdir(self.directory):
            print('Znaleziono plik: ', filename)
            self.checkIfImage(filename)

    def checkIfImage(self, file):
        mime = magic.Magic(mime=true)
        print(mime.from_file(self.directory,'/',file))

app = Yaps()

if(len(sys.argv) > 1):
    app.setDirectory(sys.argv[1])
    app.iterateFiles()
else:
    raise Exception('Not enough parameters')
