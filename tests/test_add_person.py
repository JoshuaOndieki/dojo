import unittest
from models.dojo import Dojo

class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.dojo=Dojo()
        initial_people = len(self.dojo.all_people)

    def test_create_people_successfully(self):
        fellow = self.dojo.add_person('Joshua','Ondieki' 'Fellow')
        staff = self.dojo.add_person('Annette','Kamau' 'Staff')
        self.assertTrue(fellow and staff)
        new_people = len(self.dojo.all_people)
        self.assertEqual(new_people - initial_people, 2)
