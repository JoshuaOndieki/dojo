from models.fellow import Fellow
from models.staff import Staff
from models.livingspace import LivingSpace
from models.office import Office
import random
from modules.ui import error,success

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
            return(error('Only offices and livingspaces allowed!'))
        if not isinstance(name,str):
            return(error('Room names can only be strings!'))
        if name in self.all_rooms:
            return(error('Room %s exists!'%(name)))
        else:
            if room_type.lower()=='office'.lower():
                #create an office
                self.room=Office(name)
                self.offices[name]=self.room.members
                self.all_rooms[name]=[room_type,self.room.members]
                return(success('An office called %s has been created successfully!'%(name)))
            elif room_type.lower()=='livingspace'.lower():
                #create a livingspace
                self.room=LivingSpace(name)
                self.livingspaces[name]=self.room.members
                self.all_rooms[name]=[room_type,self.room.members]
                return(success('A Livingspace called %s has been created successfully!'%(name)))

    def add_person(self, firstname,surname,person_type,wants_accomodation='N'):
        if person_type.lower() not in ['fellow','staff']:
            return(error('Only fellow and staff allowed!'))
        if not isinstance(firstname,str) or not isinstance(surname,str):
            return(error('People names can only be strings!'))
        if firstname+' '+surname in self.all_people:
            return(error('%s %s exists!'%(firstname,surname)))
        else:
            if person_type.lower()=='fellow':
                #create a fellow
                fellow=Fellow(firstname,surname)
                self.fellows.append(firstname +' '+ surname)
                self.all_people.append(firstname +' '+ surname)
                if self.offices:
                    all_offices = list(self.offices.keys())
                    checked_offices = []
                    while True:
                        office=random.choice(list(self.offices))
                        if len(self.offices[office]) < 6:
                            self.offices[office].append(firstname +' '+ surname)
                            print(success('Fellow %s %s has been assigned office %s!'%(firstname,surname,office)))
                            break
                        if office not in checked_offices: checked_offices.append(office)
                        if checked_offices == all_offices:
                            print(error('All offices are full at the moment!'))
                            break
                else:
                    print(error('No office to assign!'))
                if wants_accomodation=='Y' and self.livingspaces:
                    all_livingspaces = list(self.livingspaces.keys())
                    checked_livingspaces = []
                    while True:
                        room=random.choice(list(self.livingspaces))
                        if len(self.livingspaces[room]) < 4:
                            self.livingspaces[room].append(firstname +' '+ surname)
                            print(success('Fellow %s %s has been assigned livingspace %s!'%(firstname,surname,room)))
                            break
                        if room not in checked_livingspaces: checked_livingspaces.append(room)
                        if checked_livingspaces == all_livingspaces:
                            print(error('All livingspaces are full at the moment!'))
                            break
                return(success('Fellow %s %s has been added successfully!'%(firstname,surname)))
            elif person_type.lower()=='staff':
                #create a staff member
                if wants_accomodation == 'Y':
                    print(error('Staff can not be allocated livingspace!'))
                staff=Staff(firstname,surname)
                self.staff.append(firstname +' '+ surname)
                self.all_people.append(firstname +' '+ surname)
                if self.offices:
                    office=random.choice(list(self.offices))
                    self.offices[office].append(firstname +' '+ surname)
                    print(success('Staff %s %s has been assigned office %s!'%(firstname,surname,office)))
                else:
                    print(error('No office to assign!'))
                return(success('Staff %s %s has been added successfully!'%(firstname,surname)))
    def print_room(self,name):
        if name in self.all_rooms:
            room_members = {k:v[1] for k,v in self.all_rooms.items() if k==name}
            return room_members
        return (error("Room %s does not exist!"%(name)))

    def print_allocations(self,filename=None):
        allocations={k: v[1] for k, v in self.all_rooms.items() if v[1]}
        # return allocations
        for room in allocations:
            print(room)
            print('```````````````````````````````````````````')
            members = ''
            room_members = allocations[room]
            for member in room_members:
                members = members + ' '+ member
            print(members)
            print('')
        if filename is not None:
            #save to file
            return 0


    def print_unallocations(self,filename=None):
        allocated = []
        for room in self.all_rooms:
            members = self.all_rooms[room]
            for member in members:
                allocated.append(member)
        unallocated_people = []
        for person in self.all_people:
            if person not in allocated:
                unallocated_people.append(person+ '\n')
        if filename is None:
            for person in unallocated_people:
                print(person)
            # return unallocated_people
        else:
            with open(filename, 'w') as file:
                file.writelines(unallocated_people)
