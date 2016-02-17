class Room(object):
    """This class represents a room."""
    def __init__(self, name):
        self.name = name
        self.people = []

    def has_space(self):
        """Check to see whether a room has a space."""
        if len(self.people) < self.__class__.max_people:
            return True
        else:
            return False

    def add_person(self, person):
        """Add a person to a room."""
        self.people.append(person)


class Office(Room):
    """This class represents an office."""
    max_people = 6


class LivingSpace(Room):
    """This class represents a livingspace."""
    max_people = 4

    def add_person(self, person):
        """Add a person to a living space."""
        if person.job_title == 'fellow':
            self.add_person(person)
            return True
        return False
