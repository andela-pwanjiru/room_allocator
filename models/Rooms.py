class Room(object):
    def __init__(self, name):
        self.name = name
        self.people = []

    def has_space(self):
        if len(self.people) < self.__class__.max_people:
            return True
        else:
            return False


class Office(Room):
    max_people = 6

    def add_person(self, person):
        self.people.append(person)


class LivingSpace(Room):
    max_people = 4

    # return true if person is added, false otherwise
    def add_person(self, person):
        if person.job_title == 'fellow':
            self.people.append(person)
            return True
        else:
            return False
