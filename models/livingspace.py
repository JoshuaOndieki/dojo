from room import Room

class LivingSpace(Room):
    def __init__(self,name):
        super().__init__(self,name)
        self.name=name
        self.capacity=4
        self.members=[]
