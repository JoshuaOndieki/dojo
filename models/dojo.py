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
        if room_type.lower() not in ['office','livingspace']:
            return('Only offices and livingspaces allowed!')
        if not isinstance(name,str):
            return('Room names can only be strings!')
        if name in self.all_rooms:
            return('Room %s exists!'%(name))
        else:
            if room_type.lower()=='office'.lower():
                room=Office(name)
                self.offices[name]=room.members
                self.all_rooms[name]=[room_type,room.members]
                return('An office called %s has been created successfully!'%(name))
            elif room_type.lower()=='livingspace'.lower():
                room=LivingSpace(name)
                self.livingspaces[name]=room.members
                self.all_rooms[name]=[room_type,room.members]
                return('A Livingspace called %s has been created successfully!'%(name))

    def add_person(self, firstname,surname,person_type,wants_accomodation='N'):
        if person_type.lower() not in ['fellow','staff']:
            return('Only fellow and staff allowed!')
        if not isinstance(firstname,str) or not isinstance(surname,str):
            return('People names can only be strings!')
        if firstname+' '+surname in self.all_people:
            return('%s %s exists!'%(firstname,surname))
        else:
            if person_type.lower()=='fellow':
                fellow=Fellow(firstname,surname)
                self.fellows.append(firstname +' '+ surname)
                self.all_people.append(firstname +' '+ surname)
                return('Fellow %s %s has been added successfully!'%(firstname,surname))
            elif person_type.lower()=='staff':
                staff=Staff(firstname,surname)
                self.staff.append(firstname +' '+ surname)
                self.all_people.append(firstname +' '+ surname)
                return('Staff %s %s has been added successfully!'%(firstname,surname))
