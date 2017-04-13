import unittest
from models.office import Office

class TestOffice(unittest.TestCase):
    def test_creates_office_instance(self):
        self.office=Office('Spire')
        self.assertEqual(self.office.capacity,6)
        self.assertEqual(self.office.members,[])

if __name__ == '__main__':
    unittest.main()
