from models.fellow import Fellow
from models.staff import Staff
from models.livingspace import LivingSpace
from models.office import Office
import random

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
                self.room=Office(name)
                self.offices[name]=self.room.members
                self.all_rooms[name]=[room_type,self.room.members]
                return('An office called %s has been created successfully!'%(name))
            elif room_type.lower()=='livingspace'.lower():
                self.room=LivingSpace(name)
                self.livingspaces[name]=self.room.members
                self.all_rooms[name]=[room_type,self.room.members]
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
                if self.offices:
                    office=random.choice(list(self.offices))
                    self.offices[office].append(firstname +' '+ surname)
                    print('Fellow %s %s has been assigned office %s!'%(firstname,surname,office))
                else:
                    print('No office to assign!')
                if wants_accomodation=='Y' and self.livingspaces:
                    room=random.choice(list(self.livingspaces))
                    self.livingspaces[room].append(firstname +' '+ surname)
                    print('Fellow %s %s has been assigned livingspace %s!'%(firstname,surname,room))
                return('Fellow %s %s has been added successfully!'%(firstname,surname))
            elif person_type.lower()=='staff':
                staff=Staff(firstname,surname)
                self.staff.append(firstname +' '+ surname)
                self.all_people.append(firstname +' '+ surname)
                if self.offices:
                    office=random.choice(list(self.offices))
                    self.offices[office].append(firstname +' '+ surname)
                    print('Staff %s %s has been assigned office %s!'%(firstname,surname,office))
                else:
                    print('No office to assign!')
                return('Staff %s %s has been added successfully!'%(firstname,surname))
    def print_room(self,name):
        room_members = {k:v[1] for k,v in self.all_rooms.items() if k==name}
        return room_members

    def print_allocations(self,filename=None):
        return 0

    def print_unallocations(self,filename=None):
        return 0
