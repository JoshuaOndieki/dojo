import unittest
from models.fellow import Fellow


class TestFellow(unittest.TestCase):
    def test_creates_fellow_instance(self):
        self.fellow = Fellow('Joshua', 'Ondieki')
        self.assertTrue('Joshua' == self.fellow.firstname and 'Ondieki' == self.fellow.surname)

if __name__ == '__main__':
    unittest.main()
