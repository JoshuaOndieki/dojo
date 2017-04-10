import unittest
from models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo=Dojo()
        initial_rooms = len(self.dojo.all_rooms)

    def test_create_rooms_successfully(self):
        amity_livingspace = self.dojo.create_room('Amity', 'livingspace')
        spire_office = self.dojo.create_room('Spire','office')
        self.assertTrue(spire_office and amity_livingspace)
        new_rooms = len(self.dojo.all_rooms)
        self.assertEqual(new_rooms - initial_rooms, 2)
