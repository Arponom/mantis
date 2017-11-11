from sys import maxsize
#
class Project:

    def __init__(self,name=None, description=None, id=None ):
        self.name = name
        self.description = description
        self.id=id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize