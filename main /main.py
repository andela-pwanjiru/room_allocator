from ..models.Rooms import Office
from ..models.Rooms import LivingSpace


offices = []
offices.append(Office('Valhalla'))
offices.append(Office('Oculus'))
offices.append(Office('Krypton'))
offices.append(Office('Shire'))
offices.append(Office('Hogwarts'))
offices.append(Office('Mordor'))
offices.append(Office('Orange'))
offices.append(Office('Turquoise'))
offices.append(Office('Peach'))
offices.append(Office('Cyan'))

living_spaces = []
living_spaces.append(LivingSpace('Pearl'))
living_spaces.append(LivingSpace('Ruby'))
living_spaces.append(LivingSpace('Gem'))
living_spaces.append(LivingSpace('Emerald'))
living_spaces.append(LivingSpace('Sapphire'))
living_spaces.append(LivingSpace('Diamond'))
living_spaces.append(LivingSpace('Graphite'))
living_spaces.append(LivingSpace('Gold'))
living_spaces.append(LivingSpace('Lithium'))
living_spaces.append(LivingSpace('Chlorine'))

# The offices:
for i in offices:
    print i.name

# The living spaces:
for i in living_spaces:
    print i.name
