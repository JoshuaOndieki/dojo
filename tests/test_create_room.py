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

if __name__ == '__main__':
    unittest.main()
