"""Importations"""
from main.main import Amity
import sys

x = Amity()


# Set up amity
def initialise_amity():
    x.read_file('main/input.txt')
    x.populate()
    x.allocate_rooms()


# Prints office allocations
def get_offices():
    for office in x.offices:
        print 'These are the people in: %s' % (office.name)
        for person in office.people:
            print person.name


# Prints livingspace allocations
def get_livingspaces():
    for livingspace in x.living_spaces:
        print 'These are the people in: %s' % (livingspace.name)
        for person in livingspace.people:
            print person.name


# prints individual office with its occupants
def individual_office(name):

    for office in x.offices:
        if office.name == name:
            for person in office.people:
                print person.name


# prints individual living space occupants
def individual_living(name):

    for livingspace in x.living_spaces:
        if livingspace.name == name:
            for person in livingspace.people:
                print person.name


# Gets unallocated employees
def get_unallocated():
    """Return a list of unallocated employees"""
    print [m.name for m in x.unallocated]


# prints unallocated fellows
def get_unallocated_fellows():
    print [r.name for r in x.unallocated_fellows]

"""intializes"""
initialise_amity()

"""List of command line arguments"""
if sys.argv[1] == "get_offices":
    get_offices()

elif sys.argv[1] == "get_livingspaces":
    get_livingspaces()

elif sys.argv[1] == "print" and sys.argv[2] == \
        "members" and sys.argv[3] == "in":
    individual_office(sys.argv[4])

elif sys.argv[1] == "print" and sys.argv[2] == \
        "residents" and sys.argv[3] == "in":
    individual_living(sys.argv[4])

# show people (both fellows and staff) who were not allocated offices.
elif sys.argv[1] == "print" and sys.argv[2] == "unallocated" and \
        sys.argv[3] == "employees":
    get_unallocated_fellows()

# print fellows who wanted a living space but were unallocated.
elif sys.argv[1] == "print" and sys.argv[2] == "unallocated" and \
        sys.argv[3] == "fellows":
    get_unallocated_fellows()

else:
    print "Invalid program arguments"
    raise Exception("Invalid arguments")
