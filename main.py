import sys
import os
import magic
import exifread

class Yaps:
    def setDirectory(self, directory):
        if(os.path.isdir(directory)):
            self.directory = directory
        else:
            raise FileNotFoundError('Directory not found')

    def iterateFiles(self):
        for filename in os.listdir(self.directory):
            print('Znaleziono plik: ', filename)
            fullFilePath = self.directory + '/' + filename
            if(os.path.isdir(fullFilePath)):
                continue  
            if(self.checkIfImage(fullFilePath)):
                self.readExifData(fullFilePath)

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
        if 'Image DateTime' in tags:
            print("Zdjęcie zrobiono dnia: ",tags['Image DateTime'])
        f.close()

app = Yaps()

if(len(sys.argv) > 1):
    app.setDirectory(sys.argv[1])
    app.iterateFiles()
else:
    raise Exception('Not enough parameters')
