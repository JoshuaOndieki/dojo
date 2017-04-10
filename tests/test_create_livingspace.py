import unittest
from models.livingspace import LivingSpace

class TestLivingSpace(unittest.TestCase):
    def test_creates_livingspace_instance(self):
        self.livingspace=LivingSpace('Amity')
        self.assertTrue(self.livingspace)
        self.assertEqual(self.livingspace.capacity,4)
        self.assertEqual(self.livingspace.members,[])
