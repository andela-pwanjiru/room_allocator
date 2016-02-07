from models.Rooms import Office
from models.Rooms import LivingSpace
from models.person import Fellow
from models.person import Staff
import random


# returns the people from the input file passed.
class amity(object):
    def __init__(self):
        self.people = []
        self.offices = []
        self.living_spaces = []
        self.unallocated = []
        self.unallocated_fellows = []

    def populate(self):
        office_names = ['Valhalla', 'Oculus', 'Krypton', 'Shire',
                        'Hogwarts', 'Mordor', 'Orange', 'Turquoise',
                        'Peach', 'Cyan']

        for i in range(0, len(office_names)):
            self.offices.append(Office(office_names[i]))

        living_names = ['Pearl', 'Ruby', 'Gem', 'Emerald', 'Sapphire',
                        'Diamond', 'Graphite', 'Gold', 'Lithium', 'Chlorine']
        """living_spaces = [LivingSpace(x) for x in living_names]"""

        for i in range(0, len(living_names)):
            self.living_spaces.append(LivingSpace(living_names[i]))

    def get_living_space(self):
        pass

    def read_file(self, filename):
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
        people_count = 0
        # allocate the living_spaces
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
