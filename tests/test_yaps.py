import pytest
import os

from src.yaps.yaps import Yaps

from pprint import pprint

def testSetDirectory():
    yaps = Yaps()

    assert yaps.directory == False

    yaps.setDirectory('.')
    assert yaps.directory == '.'

    with pytest.raises(FileNotFoundError):
        yaps.setDirectory('./notExistingDir')

def testSetOutputDirectory(tmpdir):
    d = tmpdir.mkdir('unwriteableDir', '0666')
    path = str(d)
    yaps = Yaps()
    yaps.setOutputDirectory(path)

    pprint(str(d))
    assert 0


