from main.populate import populate
from main.main import amity

models = populate()

#print [x.name for x in models['offices']]
#print [x.name for x in models['living_spaces']]

x = amity()
x.read_file('main/input.txt')
x.populate()
x.allocate_rooms()

for office in x.offices:
    print 'These are the people in: %s' % (office.name)
    for person in office.people:
        print person.name
