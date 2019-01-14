import pytest
import os
import shutil

from src.yaps.yaps import Yaps
from src.yaps.logger import Logger

from pprint import pprint

def testSetDirectory():
    logger = Logger()
    yaps = Yaps(logger)

    assert yaps.directory == ''

    yaps.setDirectory('.')
    assert yaps.directory == '.'

    with pytest.raises(FileNotFoundError):
        yaps.setDirectory('./notExistingDir')

def testSetOutputDirectory(tmpdir):
    unwritableDirPath = str(tmpdir + '/unwriteableDir')
    writableDirPath = str(tmpdir + '/writeableDir')
    notExistingPath = str(tmpdir + '/notExistingDir')

    os.mkdir(unwritableDirPath, 0o555)
    os.mkdir(writableDirPath, 0o777)
    logger = Logger()
    yaps = Yaps(logger)
    
    with pytest.raises(Exception):
        yaps.setOutputDirectory(unwritableDirPath)

    yaps.setOutputDirectory(writableDirPath)

    assert yaps.outputDirectory == writableDirPath

    with pytest.raises(FileNotFoundError):
        yaps.setOutputDirectory(notExistingPath)

def testGetDirNameByDate():
    logger = Logger()
    yaps = Yaps(logger)

    date = '2018:09:01 04:40:23'
    assert yaps.getDirNameByDate(date) == '2018-09-01'

    date = '2018:09:01'
    assert yaps.getDirNameByDate(date) == yaps.UNKNOWN_DIR

    date = 'fdasfasdg'
    assert yaps.getDirNameByDate(date) == yaps.UNKNOWN_DIR

    assert yaps.getDirNameByDate(None) == yaps.UNKNOWN_DIR


def testCheckIfImage():
    logger = Logger()
    yaps = Yaps(logger)

    scriptPath = os.path.dirname(os.path.abspath(__file__))
    testImagePath = str(scriptPath + '/resources/IMG_0001.jpg')
    assert yaps.checkIfImage(testImagePath) == True
    
    testImagePath = str(scriptPath + '/resources/textFile.txt')
    assert yaps.checkIfImage(testImagePath) == False

def testReadExifData():
    logger = Logger()
    yaps = Yaps(logger)

    scriptPath = os.path.dirname(os.path.abspath(__file__))
    testImagePath = str(scriptPath + '/resources/IMG_0001.jpg')
    assert yaps.readExifData(testImagePath) == '2018:05:26 08:53:55'

    testImagePath = str(scriptPath + '/resources/textFile.txt')
    assert yaps.readExifData(testImagePath) == False

    assert yaps.logger.getLog() == 'Picture was shot on: 2018:05:26 08:53:55\n'

def testIterateFiles():
    logger = Logger()
    yaps = Yaps(logger)

    scriptPath = os.path.dirname(os.path.abspath(__file__))
    sourcePath = str(scriptPath + '/resources')
    destinationPath = str(scriptPath + '/destination')
    os.mkdir(destinationPath)
    yaps.setDirectory(sourcePath)
    yaps.setOutputDirectory(destinationPath)

    yaps.iterateFiles()

    assert os.path.isdir(destinationPath+ '/2018-05-26') == True
    assert os.path.isfile(destinationPath+ '/2018-05-26/IMG_0001.jpg') == True
    assert os.path.isfile(destinationPath+ '/2018-05-26/IMG_0002.jpg') == False
    assert os.path.isdir(destinationPath+ '/2018-11-04') == True
    assert os.path.isfile(destinationPath+ '/2018-11-04/IMG_0002.jpg') == True
    assert os.path.isfile(destinationPath+ '/2018-11-04/IMG_0001.jpg') == False

    shutil.rmtree(destinationPath)