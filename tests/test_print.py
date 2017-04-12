import unittest
from models.dojo import Dojo
from pathlib import Path
import os

class TestPrint(unittest.TestCase):
    def setUp(self):
        """ SetUp Dojo instance and populate test data"""
        self.instance=Dojo()
        offices=['Blue','Brown','Band']
        livingspaces=['Black','Bold','Blueberry']
        for livingspace in livingspaces:
            self.instance.create_room(livingspace,'livingspace')
        for office in offices:
            self.instance.create_room(office,'office')
        people = [['Joshua','Ondieki','fellow'],['Loice','Andia','fellow','Y'],['Morris','Kimani','fellow'],['Elizabeth','Mabishi','fellow','Y'],['Joy','Warugu','fellow','Y'],['Evans','Musomi','staff'],['Jackson','Saya','staff'],['James','Ndiga','staff'],['Annette','Kamau','staff']]

        for person in people:
            if len(person)==4:
                self.instance.add_person(person[0],person[1],person[2],person[3])
            else:
                self.instance.add_person(person[0],person[1],person[2])
        self.instance.print_allocations('test.txt')
        self.instance.print_unallocations('test1.txt')

    def tearDown(self):
        """Delete all files used during testing"""
        os.remove('test.txt')
        os.remove('test1.txt')

    def test_print_names_of_people_in_specific_room(self):
        people_in_Blue=self.instance.all_rooms['Blue'][1]
        query_with_room_name=self.instance.print_room('Blue')
        self.assertEqual(query_with_room_name,people_in_Blue)

    def test_print_allocations_without_file(self):
        get_allocations={k: v[1] for k, v in self.instance.all_rooms.items() if v[1]}
        print_allocations = self.instance.print_allocations()
        self.assertEqual(print_allocations,get_allocations)

    def test_print_allocations_with_file(self):
        test_file = Path("test.txt")
        self.assertTrue(if test_file.is_file())

    def test_print_unallocations_without_file(self):
        allocated_people = []
        for key, value in self.instance.all_rooms.items():
            for person in value[1]:
                allocated_people.append(person)
        unallocated_people = [p for p in self.instance.all_people if p is not in allocated_people]
        print_unallocations = self.instance.print_unallocations()
        self.assertEqual(print_unallocations,unallocated_people)

    def test_print_unallocations_with_file(self):
        test_file = Path("test1.txt")
        self.assertTrue(if test_file.is_file())
