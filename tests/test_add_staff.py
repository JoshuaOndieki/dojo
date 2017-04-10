import unittest
from models.staff import Staff

class TestStaff(unittest.TestCase):
    def test_creates_staff_instance(self):
        self.staff=Staff('James','Ndiga')
        self.assertTrue(self.staff)
        self.assertTrue('James'==self.staff.firstname and 'Ndiga'==self.staff.surname)
