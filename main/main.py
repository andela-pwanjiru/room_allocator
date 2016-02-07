"""Import Statements"""
from models.Rooms import Office
from models.Rooms import LivingSpace
from models.person import Fellow
from models.person import Staff
import random


class amity(object):
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

        for i in range(0, len(office_names)):
            self.offices.append(Office(office_names[i]))

        living_names = ['Pearl', 'Ruby', 'Gem', 'Emerald', 'Sapphire',
                        'Diamond', 'Graphite', 'Gold', 'Lithium', 'Chlorine']

        for i in range(0, len(living_names)):
            self.living_spaces.append(LivingSpace(living_names[i]))

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
                choice = False
                if words[3] == 'Y':
                    choice = True
                fel = Fellow(person_name, choice)
                self.people.append(fel)
            elif words[2] == 'STAFF':
                self.people.append(Staff(person_name))
            else:
                raise Exception('Invalid input format')

        return self.people

    def allocate_rooms(self):
        """Allocates rooms"""
        random.shuffle(self.people)
        people_count = 0
        people_len = len(self.people)

        # allocate the offices
        for office in self.offices:
            while office.has_space():
                if(people_count >= people_len):
                    break
                office.add_person(self.people[people_count])
                people_count += 1

        self.unallocated = self.people[people_count:]
        # allocate the living_spaces
        people_count = 0
        for living_space in self.living_spaces:
            while living_space.has_space():
                if(people_count >= people_len):
                    break
                living_space.add_person(self.people[people_count])
                people_count += 1

        for i in range(people_count, len(self.people)):
            if self.people[i].job_title == 'fellow' and \
                    self.people[i].choice is True:
                self.unallocated_fellows.append(self.people[i])
