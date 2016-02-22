# person superclass
class Person(object):
    """This class represents a person."""

    def __init__(self, name):
        self.name = name


# fellow class extended from person
class Fellow(Person):
    """This class represents a fellow person."""

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        self.job_title = 'fellow'


# staff class extended from person
class Staff(Person):
    """This class represents a staff person."""

    def __init__(self, name):
        self.name = name
        self.job_title = 'staff'
