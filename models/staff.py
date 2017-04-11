from models.person import Person

class Staff(Person):
    def __init__(self,firstname,surname):
        # super().__init__(self,firstname,surname)
        self.firstname=firstname
        self.surname=surname
