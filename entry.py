from main.main import amity
import sys

# models = populate()
# print [x.name for x in models['offices']]
# print [x.name for x in models['living_spaces']]

x = amity()


def initialise_amity():
    x.read_file('main/input.txt')
    x.populate()
    x.allocate_rooms()


def get_offices():
    for office in x.offices:
        print 'These are the people in: %s' % (office.name)
        for person in office.people:
            print person.name


def get_livingspaces():
    for livingspace in x.living_spaces:
        print 'These are the people in: %s' % (livingspace.name)
        for person in livingspace.people:
            print person.name


def individual_office(name):

    for office in x.offices:
        if office.name == name:
            for person in office.people:
                print person.name


def get_unallocated():
    """Return a list of unallocated employees"""
    print [m.name for m in x.unallocated]


def get_unallocated_fellows():
    print [r.name for r in x.unallocated_fellows]


initialise_amity()


if sys.argv[1] == "get_offices":
    get_offices()

elif sys.argv[1] == "get_livingspaces":
    get_livingspaces()

elif sys.argv[1] == "print" and sys.argv[2] == \
        "members" and sys.argv[3] == "in":
    individual_office(sys.argv[4])

# show people (both fellows and staff) who were not allocated offices.
elif sys.argv[1] == "get_unallocated":
    get_unallocated()

    """# call allocate rooms
    if len(sys.argv) == 3 and sys.argv[1] == ""
    and sys.argv[2][-3:] == "txt":
        building.allocate(sys.argv[2])"""

# print fellows who wanted a living space but were unallocated.
elif sys.argv[1] == "print" and sys.argv[2] == "unallocated" and \
        sys.argv[3] == "fellows":
    get_unallocated_fellows()

else:
    print "Invalid program arguments"
    raise Exception("Invalid arguments")
