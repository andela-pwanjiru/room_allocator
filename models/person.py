class Person(object):

    def __init__(self, name):
        self.name = name


class Fellow(Person):
    def __init__(self, name, choice):
        Person.__init__(name)
        self.choice = choice
        self.job_title = 'fellow'


class Staff(Person):

    def __init___(self, name):
        Person.__init__(name)
        self.job_title = 'Staff'
