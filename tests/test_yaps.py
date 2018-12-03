import pytest
# from yaps import Yaps
class TestYaps:

    def testSetDirectory(self):
        yaps = Yaps()
        yaps.setDirectory('.')