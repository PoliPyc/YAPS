import os
import magic
import exifread
import datetime
from shutil import copyfile


########## NOTES
# Checking for duplicates
# 1. List file paths with their sizes
# 2. From previous list create another one with files of same size and their md5 sums
# 3. Check for duplicate md5 sums
#
########## TO-DO List
# Check for duplicates
# Tests!
# More interactive
# Refactor setOutputDirectory and iterateFiles
# GUI
# Other exif filters
# Yaps readme, help messages
#


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
            if not os.access(directory, os.W_OK):
                raise Exception('Directory not writable')

            self.outputDirectory = directory
        else:
            raise FileNotFoundError('Output directory not found')

    def iterateFiles(self):
        for filename in os.listdir(self.directory):
            print('File found: ', filename)
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
            print("Picture was shot on: ",tags['Image DateTime'])
            return tags['Image DateTime'].values
        else:
            return False

    def getDirNameByDate(self, date):
        try:
            return datetime.datetime.strptime(date, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')
        except (ValueError, TypeError):
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
