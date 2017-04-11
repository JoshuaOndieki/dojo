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
    def test_it_fails_with_existing_person(self):
        exist_person = self.dojo.add_person('Joshua','Ondieki', 'Fellow')
        try_overwrite_f = self.dojo.add_person('Joshua','Ondieki', 'Fellow')
        exist_person = self.dojo.add_person('Evans','Musomi', 'Staff')
        try_overwrite_s = self.dojo.add_person('Evans','Musomi', 'Staff')
        self.assertTrue(try_overwrite_f == 'Joshua Ondieki exists!' and try_overwrite_s == 'Evans Musomi exists!')

    def test_it_fails_with_invalid_person_type(self):
        invalid_type = self.dojo.add_person('Loice','Andia','BFA')
        self.assertEqual('Only fellow and staff allowed!',invalid_type)

    def test_fails_with_person_name_not_string(self):
        invalid_person = self.dojo.add_person(['Oj'],'Josh','Fellow')
        invalid_person1 = self.dojo.add_person({'Oj':'Josh'},{},'Fellow')
        invalid_person2 = self.dojo.add_person(['Oj'],['Josh'],'Staff')
        invalid_person3 = self.dojo.add_person({'Oj':'Josh'},{},'Staff')
        self.assertEqual(invalid_person,'People names can only be strings!')
        self.assertEqual(invalid_person1,'People names can only be strings!')
        self.assertEqual(invalid_person2,'People names can only be strings!')
        self.assertEqual(invalid_person3,'People names can only be strings!')



if __name__ == '__main__':
    unittest.main()
