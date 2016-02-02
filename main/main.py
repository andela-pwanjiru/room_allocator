from models.person import Fellow
from models.person import Staff


# returns the people from the input file passed.
class amity(object):
    def __init__(self):
        self.people = []

    def read_file(self, filename):
        f = open(filename)
        for i in f:
            # i is a line in the file filename
            # slice the last character in i, as it is \n
            i = i[:-1]
            words = i.split(' ')
            person_name = words[0] + ' ' + words[1]
            if (words[2] == 'FELLOW'):
                choice = False
                if (words[3] == 'Y'):
                    choice = True
                fel = Fellow(person_name, choice)
                self.people.append(fel)
            elif (words[2] == 'STAFF'):
                self.people.append(Staff(person_name))
            else:
                raise Exception('Invalid input format')

        return self.people


"""def allocate_rooms(a):
    # a should be a list of ppl
    pas

ppl = read_file('afile.txt')
allocate_rooms(ppl)"""
