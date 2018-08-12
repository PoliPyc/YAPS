import sys
import os

class Yaps:
    def setDirectory(self, directory):
        if(os.path.isdir(directory)):
            self.directory = directory
        else:
            raise FileNotFoundError('Directory not found')

app = Yaps()

if(len(sys.argv) > 1):
    app.setDirectory(sys.argv[1])
else:
    raise Exception('Not enough parameters')
