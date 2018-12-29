class Logger:
    def __init__(self):
        self.logMessage = ''

    def putLog(self, message):
        self.logMessage += message + '\n'

    def getLog(self):
        return self.logMessage

    def clearLog(self):
        self.logMessage = ''