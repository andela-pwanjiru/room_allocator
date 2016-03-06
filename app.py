"""
Room Allocator

Usage:
    app.py print (offices|living)
    app.py print members <name> (--office|--living)
    app.py print unallocated (fellows|employees)

Options:
    -h --help     Show this screen.
    --version     Show version.

"""


from main.mains import Amity
from docopt import docopt

main_class = Amity()


# Set up amity
def initialise_amity():
    main_class.read_file('main/input.txt')
    main_class.populate()
    main_class.allocate_rooms()

# Prints office allocations
def get_offices():

    for office in main_class.offices:
        print 'These are the people in: %s' % (office.name)
        for person in office.people:
            print person.name
        print "\n"


# Prints livingspace allocations
def get_livingspaces():

    for livingspace in main_class.living_spaces:
        print 'These are the people in: %s' % (livingspace.name)
        for person in livingspace.people:
            print person.name
        print "\n"


# prints individual office with its occupants
def individual_office(name):

    for office in main_class.offices:
        if office.name == name:
            for person in office.people:
                print person.name


# prints individual living space occupants
def individual_living(name):

    for livingspace in main_class.living_spaces:
        if livingspace.name == name:
            for person in livingspace.people:
                print person.name


# Gets unallocated employees
def get_unallocated():
    """Return a list of unallocated employees"""
    unallocated = [employee.name for employee in main_class.unallocated]
    print unallocated
    print len(unallocated)


# prints unallocated fellows
def get_unallocated_fellows():
    unallocated_fellows = [fel.name for fel in main_class.unallocated_fellows]
    print unallocated_fellows
    print len(unallocated_fellows)

initialise_amity()

if __name__ == '__main__':
    args = docopt(__doc__, version='Room Allocator 1.0')

    if args['offices']:
        get_offices()

    if args['living']:
        get_livingspaces()

    if args['--office']:
        individual_office(args['<name>'])

    if args['--living']:
        individual_living(args['<name>'])

    if args['fellows']:
        get_unallocated_fellows()

    if args['employees']:
        get_unallocated()
