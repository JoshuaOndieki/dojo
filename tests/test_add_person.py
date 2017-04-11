import unittest
from models.dojo import Dojo

class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.dojo=Dojo()
        self.initial_people = len(self.dojo.all_people)

    def test_create_people_successfully(self):
        self.fellow = self.dojo.add_person('Joshua','Ondieki', 'Fellow')
        self.staff = self.dojo.add_person('Annette','Kamau', 'Staff')
        # self.assertTrue(self.fellow and self.staff)
        new_people = len(self.dojo.all_people)
        self.assertEqual(new_people - self.initial_people, 2)

if __name__ == '__main__':
    unittest.main()
