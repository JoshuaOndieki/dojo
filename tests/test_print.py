import unittest
from models.dojo import Dojo

class TestPrint(unittest.TestCase):
    def setUp(self):
        self.instance=Dojo()
        offices=['Blue','Brown','Band']
        livingspaces=['Black','Bold','Blueberry']
        for livingspace in livingspaces:
            self.instance.create_room(livingspace,'livingspace')
        for office in offices:
            self.instance.create_room(office,'office')
        people = [['Joshua','Ondieki','fellow'],['Loice','Andia','fellow','Y'],['Morris','Kimani','fellow'],['Elizabeth','Mabishi','fellow','Y'],['Joy','Warugu','fellow','Y'],['Evans','Musomi','staff'],['Jackson','Saya','staff'],['James','Ndiga','staff'],['Annette','Kamau','staff']]

        for person in people:
            if len(person)==4:
                self.instance.add_person(person[0],person[1],person[2],person[3])
            else:
                self.instance.add_person(person[0],person[1],person[2])
