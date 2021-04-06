class PictureList(list):
    def __str__(self):
        string = ''
        for item in self:
            string += str(item)+"\n"
        return string

class Picture():
    def __init__(self, filename, mime):
        self.filename = filename
        self.mime = mime