import pytest

from src.yaps.logger import Logger

from pprint import pprint

def testLogger():
    logger = Logger()

    assert logger.getLog() == ''

    logger.putLog('first message')

    assert logger.getLog() == 'first message\n'

    logger.putLog('second message')

    assert logger.getLog() == 'first message\nsecond message\n'

    logger.clearLog()

    assert logger.getLog() == ''
