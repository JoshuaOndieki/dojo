import unittest
from models.dojo import Dojo
from pathlib import Path
import os
from modules.ui import *

class TestPrint(unittest.TestCase):
    def setUp(self):
        """ SetUp Dojo instance and populate test data"""
        self.instance=Dojo()
        self.instance.offices = {'Blue':['Joshua Ondieki','Loice Andia','James Ndiga','Annette Kamau'],'Brown':['Morris Kimani','Elizabeth Mabishi'],'Band':['Joy Warugu','Evans Musomi','Jackson Saya']}
        self.instance.livingspaces={'Black':['Loice Andia'],'Bold':[],'Blueberry':['Elizabeth Mabishi','Joy Warugu']}
        self.instance.fellows =['Joshua Ondieki','Loice Andia','Morris Kimani','Elizabeth Mabishi','Joy Warugu']
        self.instance.staff = ['James Ndiga','Annette Kamau','Evans Musomi','Jackson Saya']
        self.instance.fellows.append('Lost Guy')
        self.instance.all_people.append('Lost Guy')  #add a person without getting allocations :: LOST GUY FELLOW Y
        self.instance.all_rooms = {'Blue':['office',['Joshua Ondieki','Loice Andia','James Ndiga','Annette Kamau']],'Brown':['office',['Morris Kimani','Elizabeth Mabishi']],'Band':['office',['Joy Warugu','Evans Musomi','Jackson Saya']],'Black':['livingspace',['Loice Andia']],'Bold':['livingspace',[]],'Blueberry':['office',['Elizabeth Mabishi','Joy Warugu']]}

    def test_print_names_of_people_in_specific_room(self):

        people_in_Blue = {'Blue':['Joshua Ondieki','Loice Andia','James Ndiga','Annette Kamau']}
        query_with_room_name=self.instance.print_room('Blue')
        self.assertEqual(query_with_room_name,people_in_Blue)

    def test_print_allocations_with_file(self):
        self.instance.print_allocations('test.txt')
        test_file = Path("test.txt")
        self.assertTrue(test_file.is_file())

    def test_print_unallocations_with_file(self):
        self.instance.print_unallocations('test1.txt')
        test_file = Path("test1.txt")
        self.assertTrue(test_file.is_file())
