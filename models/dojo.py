from models.fellow import Fellow
from models.staff import Staff
from models.livingspace import LivingSpace
from models.office import Office
class Dojo():
    def __init__(self):
        self.offices={}
        self.livingspaces={}
        self.fellows=[]
        self.staff=[]
        self.all_rooms={}
        self.all_people=[]

    def create_room(self, name,room_type):
        if room_type=='office':
            room=Office(name)
            self.offices[name]=room.members
            self.all_rooms[name]=[room_type,room.members]
        elif room_type=='livingspace':
            room=LivingSpace(name)
            self.livingspaces[name]=room.members
            self.all_rooms[name]=[room_type,room.members]

    def add_person(self, firstname,surname,person_type,wants_accomodation='N'):
        if person_type=='Fellow':
            fellow=Fellow(firstname,surname)
            self.fellows.append([fellow.firstname,fellow.surname])
            self.all_people.append([fellow.firstname,fellow.surname])
        elif person_type=='Staff':
            staff=Staff(firstname,surname)
            self.staff.append([firstname,surname])
            self.all_people.append([firstname,surname])
