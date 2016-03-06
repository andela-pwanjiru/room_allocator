import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from model.rooms import Office
from model.rooms import LivingSpace
from model.person import Fellow
from model.person import Staff
import random


class Amity(object):
    def __init__(self):
        self.people = []
        self.offices = []
        self.living_spaces = []
        self.unallocated = []
        self.unallocated_fellows = []

    def populate(self):
        """prepopulates amity with 10 offices and 10 livingspaces"""
        office_names = ['Valhalla', 'Oculus', 'Krypton', 'Shire',
                        'Hogwarts', 'Mordor', 'Orange', 'Turquoise',
                        'Peach', 'Cyan']

        for office in range(0, len(office_names)):
            self.offices.append(Office(office_names[office]))

        living_names = ['Pearl', 'Ruby', 'Gem', 'Emerald', 'Sapphire',
                        'Diamond', 'Graphite', 'Gold', 'Lithium', 'Chlorine']

        for living in range(0, len(living_names)):
            live = LivingSpace(living_names[living])
            self.living_spaces.append(live)

    def read_file(self, filename):
        """Returns the people from the input file passed."""
        input_file = open(filename)
        for line in input_file:
            # line is a line in the file filename
            # slice the last character in line, as it is \n
            line = line[:-1]
            words = line.split(' ')
            person_name = words[0] + ' ' + words[1]
            if words[2] == 'FELLOW':
                temp_choice = False
                if words[3] == 'Y':
                    temp_choice = True
                fel = Fellow(person_name, temp_choice)
                self.people.append(fel)
            elif words[2] == 'STAFF':
                self.people.append(Staff(person_name))
            else:
                raise Exception('Invalid input format')

    def allocate_rooms(self):
        """Allocates rooms"""
        random.shuffle(self.people)
        people_count = 0
        people_len = len(self.people)
        for office in self.offices:
            while office.has_space():
                if people_count >= people_len:
                    break
                office.add_person(self.people[people_count])
                people_count += 1
            if people_count >= people_len:
                break
        self.unallocated = self.people[people_count:]
        people_count = 0

        for living_space in self.living_spaces:
            while living_space.has_space():
                if(people_count >= people_len):
                    break
                living_space.add_person(self.people[people_count])
                people_count += 1
            if people_count >= people_len:
                break
        for person in range((people_count)-1, len(self.people)):
            if self.people[person].job_title == 'fellow' and \
                    self.people[person].choice is True:
                self.unallocated_fellows.append(self.people[person])
