from models.room import Room

class Office(Room):
    def __init__(self,name):
        # super().__init__(self,name)
        self.name=name
        self.capacity=6
        self.members=[]
