import unittest
from models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo=Dojo()
        self.initial_rooms = len(self.dojo.all_rooms)

    def test_create_rooms_successfully(self):
        amity_livingspace = self.dojo.create_room('Amity', 'livingspace')
        spire_office = self.dojo.create_room('Spire','office')
        self.new_rooms = len(self.dojo.all_rooms)
        self.assertEqual(self.new_rooms - self.initial_rooms, 2)
        self.assertEqual('An office called Spire has been created successfully!',spire_office)
        self.assertEqual('A Livingspace called Amity has been created successfully!',amity_livingspace)

    def test_it_fails_with_existing_room(self):
        exist_room = self.dojo.create_room('Amhere','office')
        try_overwrite_o = self.dojo.create_room('Amhere','office')
        exist_room = self.dojo.create_room('Amhere','livingspace')
        try_overwrite_l = self.dojo.create_room('Amhere','livingspace')
        self.assertTrue(try_overwrite_o == 'Room Amhere exists!' and try_overwrite_l == 'Room Amhere exists!')

    def test_it_fails_with_invalid_room_type(self):
        invalid_type = self.dojo.create_room('Amhere','Kitchen')
        self.assertEqual('Only offices and livingspaces allowed!',invalid_type)

    def test_fails_with_room_name_not_string(self):
        invalid_room = self.dojo.create_room(['Amhere'],'office')
        invalid_room1 = self.dojo.create_room({'Amhere':'room'},'office')
        invalid_room2 = self.dojo.create_room(['Amhere'],'livingspace')
        invalid_room3 = self.dojo.create_room({'Amhere':'room'},'livingspace')
        self.assertEqual(invalid_room,'Room names can only be strings!')
        self.assertEqual(invalid_room1,'Room names can only be strings!')
        self.assertEqual(invalid_room2,'Room names can only be strings!')
        self.assertEqual(invalid_room3,'Room names can only be strings!')

if __name__ == '__main__':
    unittest.main()
