import pytest
import os

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
    notExistingPath = strtmpdir + '/notExistingDir')

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



