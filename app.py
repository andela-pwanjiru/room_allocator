from main.mains import Amity
# import sys
import argparse

x = Amity()


# Set up amity
def initialise_amity():
    x.read_file('main/input.txt')
    x.offices
    x.populate()
    # allocate persons to rooms
    x.allocate_rooms()


# Prints office allocations
def get_offices():

    for office in x.offices:
        print 'These are the people in: %s' % (office.name)
        for person in office.people:
            print person.name
        print "\n"


# Prints livingspace allocations
def get_livingspaces():

    for livingspace in x.living_spaces:
        print 'These are the people in: %s' % (livingspace.name)
        for person in livingspace.people:
            print person.name
        print "\n"


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

initialise_amity()

"""List of command line arguments"""
parser = argparse.ArgumentParser(
    prog='rm_allocator', description='Process allocation of rooms')

parser.add_argument("-o", "--office", action='store_true',
                    help="Print the offices with the allocated people.")

parser.add_argument("-l", "--living", action='store_true',
                    help="Print the living spaces with the allocated people.")

parser.add_argument('-g', "--get", nargs=2, help="print individual members")

parser.add_argument('-s', "--show", nargs=1, help="print unallocated members")


args = parser.parse_args()

if (args.office):
    get_offices()

if (args.living):
    get_livingspaces()


if (args.get):
    if (args.get[0] == 'office'):
        individual_office(args.get[1])
    elif (args.get[0] == 'living'):
        individual_living(args.get[1])
    else:
        raise Exception('Argument can either be living or office')

if (args.show):
    if (args.show[0] == 'employees'):
        get_unallocated()
    elif (args.show[0] == 'fellows'):
        get_unallocated_fellows()
    else:
        raise Exception('Argument can either be living or office')
