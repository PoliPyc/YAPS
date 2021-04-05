class PictureList(list):
    def __str__(self):
        pass

class Picture():
    def __init__(self, filename, mime):
        self.filename = filename
        self.mime = mime