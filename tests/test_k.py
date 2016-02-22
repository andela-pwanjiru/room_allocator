import random
import unittest
from main.main import Amity
from models.rooms import Office
from models.rooms import LivingSpace
from models.person import Fellow
from models.person import Staff


class AmityTest(unittest.TestCase):
    """Tests class amity"""
    def setUp(self):
        self.amity = Amity()
        self.amity.populate()
        self.amity.read_file('main/input.txt')

    def test_amity_offices(self):
        # test that amity has an Oculus office
        list_of_office_names = [x.name for x in self.amity.offices]
        self.assertIn('Oculus', list_of_office_names)
        self.assertEquals(10, len(self.amity.offices))
        # test that amity.offices only contains office objects
        for i in self.amity.offices:
            self.assertIsInstance(i, Office)

    def test_amity_livingspaces(self):
        list_of_livingspace_names = [x.name for x in self.amity.living_spaces]
        self.assertIn('Ruby', list_of_livingspace_names)
        self.assertEquals(10, len(self.amity.living_spaces))
        for i in self.amity.living_spaces:
            self.assertIsInstance(i, LivingSpace)

    def test_amity_allocating(self):
        # the rooms are less than the people, hence some will be unallocated.
        self.amity.allocate_rooms()
        # get a random office
        office_index = random.randint(0, 9)
        an_office = self.amity.offices[office_index]
        self.assertFalse(an_office.has_space())
        self.assertEquals(6, len(an_office.people))
        living_index = random.randint(0, 9)
        living_space = self.amity.living_spaces[living_index]
        self.assertFalse(living_space.has_space())
        self.assertEquals(4, len(living_space.people))
        # test the unallocated fellows list
        for i in self.amity.unallocated_fellows:
            self.assertIsInstance(i, Fellow)
        self.assertIsInstance(self.amity.unallocated, list)


class ModelsTest(unittest.TestCase):

    """Tests models created"""

    def test_office_creation(self):
        """Test correct office instantiation"""
        new_office = Office('Mordor')
        self.assertIsInstance(new_office, Office)
        self.assertEquals(new_office.name, 'Mordor')

    def test_office_methods(self):
        new_office = Office('Mordor')
        self.assertTrue(new_office.has_space())
        # test that people are added.
        temp_person = Staff('Some Guy')
        new_office.add_person(temp_person)
        self.assertIn(temp_person, new_office.people)

    def test_livingspace_methods(self):
        new_livingspace = LivingSpace('lounge')
        self.assertTrue(new_livingspace.has_space())
        # test that people are added.
        temp_person = Fellow('Some chic', True)
        new_livingspace.add_person(temp_person)
        self.assertIn(temp_person, new_livingspace.people)

    def test_fellow_class(self):
        afellow = Fellow('Different Guy', True)
        self.assertIsInstance(afellow, Fellow)
        self.assertEquals(afellow.name, 'Different Guy')
        self.assertTrue(afellow.choice)
        self.assertEqual(afellow.job_title, 'fellow')

    def test_staff_class(self):
        astaff = Staff('Some Diff Staff')
        self.assertIsInstance(astaff, Staff)
        self.assertEquals('Some Diff Staff', astaff.name)
        self.assertEquals(astaff.job_title, 'staff')


if __name__ == '__main__':
    unittest.main()
