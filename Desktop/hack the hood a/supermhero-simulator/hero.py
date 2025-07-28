# Lab 6 - Sebastian Elenes

import random
from ability import Ability
from armor import Armor
class Hero:
    def __init__(self, name, starting_health=100)
    self.name = name
    self.starting_health = starting_health
    self.current.health = starting_health
    self.abilities = []
    self.armors = []


def battle(self, opponent):
    ''' Print a random winner'''
    winner = print(random.choice(self.name, opponent.name))
    print(f"{winner} has won the battle!")

def add_ablity(self, ability):
'''Adds an ability to the existing abilities list'''
self.abilites.append(ability)
print(f"{ability.name} has been added to {self.name}'s  ability list")

    def sum_of_attacks(self):
        '''Loops through abilities list and sums up all '''
    total_damage = 0
    for ability in self.abilities:
        total_damage += ability.attack()
        return total_damage

        def add_armor(self, armor)
        '''Adds an armor to the armors list.'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name} 's ability list")

        def defend(Self); 
        '''Loops through armors list and sums up all block '''
    total_block = 0
    for armor in self.armors:
        total_block += armor.block()
    return 


    if __name__ == "__main__"
my_hero = Hero("Grace Hopper", 200)
my_hero2 = Hero("Superman", 500)
print(my_hero.name)            # Grace Hopper
print(my_hero.curret_health)   #200
my_hero.batttle(my_hero2)
fireball = Ability("fireball, 50")
lighting = Ability("lighting, 55")
telekenisis = Ability("telekenisis, 60")
my_hero.add_ability(fireball)
my_hero.add_ability(lighting)
my_hero.add_ability(telekenisis)
print(my_hero.sum_of_attacks())
Shield = Armor("Shield", 30)
Helmet = Armor("Helmet", 25)
boots = Armor("boots", 10)
my_hero.add_armor(Shield)
my_hero.add_armor(Helmet)
my_hero.add_armor(boots)
print(my_hero.defend())
 
