from models.Rooms import Office
from models.Rooms import LivingSpace


def populate():
    offices = []
    office_names = ['Valhalla', 'Oculus', 'Krypton', 'Shire',
                    'Hogwarts', 'Mordor', 'Orange', 'Turquoise',
                    'Peach', 'Cyan']

    for i in range(0, len(office_names)):
        offices.append(Office(office_names[i]))

    living_names = ['Pearl', 'Ruby', 'Gem', 'Emerald', 'Sapphire',
                    'Diamond', 'Graphite', 'Gold', 'Lithium', 'Chlorine']
    living_spaces = [LivingSpace(x) for x in living_names]

    return {'offices': offices,
            'living_spaces': living_spaces
            }
