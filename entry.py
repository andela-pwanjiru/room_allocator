from main.populate import populate
from main.main import amity

models = populate()

print [x.name for x in models['offices']]
print [x.name for x in models['living_spaces']]

x = amity()
people = x.read_file('main/input.txt')
print people
