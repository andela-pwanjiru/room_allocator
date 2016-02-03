class Person(object):

    def __init__(self, name):
        self.name = name


class Fellow(Person):
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        self.job_title = 'fellow'


class Staff(Person):

    def __init__(self, name):
        self.name = name
        self.job_title = 'staff'
