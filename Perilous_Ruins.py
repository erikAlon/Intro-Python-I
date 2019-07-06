"""
You are the asynchronous hero in search of the holy well guarded by monsters along the path, but whose really guarding it?
"""

import asyncio
import random
import sys


def mon_gen():
    return random.randint(0, 3)


def cool_gen():
    return random.randint(1, 2)


class GameObject:
    class_name = None
    desc = None
    cooldown = None
    health = None
    dead = False
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.name + ": " + self.desc

    def get_cool(self):
        return self.cooldown

    def get_hp(self):
        return self.health

    def is_dead(self):
        return self.dead

    def kill_switch(self):
        self.dead = not self.dead

    def del_npc(self, npc):
        if npc in self.objects:
            del self.objects[npc]

    def __str__(self):
        return f'{self.name}'


class Hero(GameObject):
    death_flavor = [
        "Your limbs get ripped apart while monsters feast on your bones",
        "You have taken your final breadths and feel very weak",
        "You're gravely wounded and bleed profusely",
        "You're' severely wounded",
        "You're deeply wounded",
        "You're wounded",
        "Your armor is now useless",
        "Your armor is damaged",
        "Your armor is dented",
        "Your armor took a hit",
        "You have polished armor equipped"
    ]

    def __init__(self, name):
        self.class_name = "hero"
        self.health = 10
        self.cooldown = 1
        self._desc = self.death_flavor[self.health]
        super().__init__(name)

    @property
    def desc(self):
        return self._desc

    def take_damage(self):
        if self.health > 0:
            self.health -= 1
            self._desc = self.death_flavor[self.health]


class Monster(GameObject):
    death_flavor = [
        "Lays lifeless on the ground with its severed head",
        "On the verge of death",
        "Has life",
        "Full of life"
    ]

    def __init__(self, c_name, health, cooldown, name):
        self.class_name = c_name
        self.health = health
        self.cooldown = cooldown
        self._desc = self.death_flavor[self.health]
        super().__init__(name)

    @property
    def desc(self):
        return self._desc

    def take_damage(self):
        if self.health > 0:
            self.health -= 1
            self._desc = self.death_flavor[self.health]


class Orc(Monster):
    max_health = 3
    name = "Orc"

    def __init__(self, c_name):
        super().__init__(c_name, self.max_health, cool_gen(), self.name)


class Troll(Monster):
    max_health = 2
    cooldown = cool_gen()
    name = "Troll"

    def __init__(self, c_name):
        super().__init__(c_name, self.max_health, self.cooldown, self.name)


class Imp(Monster):
    max_health = 1
    cooldown = cool_gen()
    name = "Imp"

    def __init__(self, c_name):
        super().__init__(c_name, self.max_health, self.cooldown, self.name)


class Dungeon(object):

    def generate_threats(self, threats):
        counter = 0
        monster_availability = [Hero("False_Hero"), Orc(
            "Orc1"), Orc("Orc2"), Orc("Orc3"), Troll("Troll1"), Troll("Troll2"), Troll("Troll3"), Imp("Imp1"), Imp("imp2"), Imp("imp3")]
        monster_list = []
        if threats > 0:
            while counter < threats:
                chosen_monster = random.randint(
                    1, len(monster_availability) - 1)
                monster_list.append(monster_availability[chosen_monster])
                del monster_availability[chosen_monster]
                counter += 1
        return monster_list

    def get_threats(self):
        if len(self.threats) > 0:
            return self.threats
        else:
            return "There is an eery calmness about"

    def __init__(self, area, threats):
        self.area = area
        self.threats = self.generate_threats(threats)
        if threats > 0:
            self.has_threats_bool = True
        else:
            self.has_threats_bool = False

    def __str__(self):
        return f'{self.area}\n'

    def has_threats(self):
        return self.has_threats_bool


def combat(hero, monsters):
    for monster in monsters:
        print(f'Nasty {monster} appeared!')
        print("\n")

    async def fight0():
        threats = len(monsters)
        while threats > 0:
            for monster in monsters:
                if not monster.is_dead():
                    await asyncio.sleep(hero.get_cool())
                    print(f"{hero} attacks {monster}!")
                    monster.take_damage()
                    print(monster.get_desc())
                    if monster.get_hp() <= 0:
                        monster.kill_switch()
                        threats -= 1
                    print("\n")
        print(f"{hero} survived the onslaught!")

    async def fight1():
        while not monsters[0].is_dead():
            await asyncio.sleep(monsters[0].get_cool())
            if not monsters[0].is_dead():
                print(f"{monsters[0]} attacks {hero}!")
                hero.take_damage()
                print(hero.get_desc())
                print("\n")
                if hero.get_hp() <= 0:
                    print("You've been KILLED")
                    sys.exit()

    async def fight2():
        while not monsters[1].is_dead():
            await asyncio.sleep(monsters[1].get_cool())
            if not monsters[1].is_dead():
                print(f"{monsters[1]} attacks {hero}!")
                hero.take_damage()
                print(hero.get_desc())
                print("\n")
                if hero.get_hp() <= 0:
                    print("You've been KILLED")
                    sys.exit()

    async def fight3():
        while not monsters[2].is_dead():
            await asyncio.sleep(monsters[2].get_cool())
            if not monsters[2].is_dead():
                print(f"{monsters[2]} attacks {hero}!")
                hero.take_damage()
                print(hero.get_desc())
                print("\n")
                if hero.get_hp() <= 0:
                    print("You've been KILLED")
                    sys.exit()

    loop = asyncio.get_event_loop()
    if len(monsters) == 3:
        loop.run_until_complete(asyncio.gather(
            fight0(), fight1(), fight2(), fight3()))
    elif len(monsters) == 2:
        loop.run_until_complete(asyncio.gather(
            fight0(), fight1(), fight2()))
    elif len(monsters) == 1:
        loop.run_until_complete(asyncio.gather(
            fight0(), fight1()))
    else:
        print(hero.get_desc())


def main():

    # get name
    player_name = input("What is your name traveler? ")
    hero = Hero(player_name)

    # initialize areas
    start = Dungeon(
        f"{hero.name} unmounts from his horse and embarks on a journey in search of the coveted holy well", 0)
    trail = Dungeon(f"A cleared path surrounded by nature", mon_gen())
    shore = Dungeon(
        f"{hero.name} can see the world reflect and sparkle from the shoreline", mon_gen())
    cave = Dungeon(
        f"{hero.name} has entered a dark cave and lights up a torch", mon_gen())
    flood = Dungeon(
        f"There cave is deep but the water looks deeper", mon_gen())
    woods = Dungeon(
        f"Light dances between the leaves and the trunks in this green space", mon_gen())
    well = Dungeon(
        f"The sight of a pristine water hole, {hero.name} found the holy well!", 0)

    # get first direction
    print(start)
    print(f'{hero.name} sees two paths.. a cave or a trail')
    direction = input("What path will you take? ")

    if direction == "trail":
        print(trail)
        # check if monsters
        if trail.has_threats():
            combat(hero, trail.get_threats())
        else:
            print(trail.get_threats())

        print(f'{hero.name} sees two paths.. the woods or the shore')
        direction = input(f"What path will {hero.name} take? ")

        if direction == "shore":
            print(shore)
            # check if monsters
            if shore.has_threats():
                combat(hero, shore.get_threats())
            else:
                print(trail.get_threats())

            print(f'{hero.name} sees two paths.. the grove or the ford')
            direction = input(f"What path will {hero.name} take? ")

            if direction == "grove":
                # final fight

                print(well)
                sys.exit()
            elif direction == 'ford':
                print(
                    "The hero did not find the well but instead a very large and hungry Leviathan")
            else:
                print("wrong input")
        elif direction == 'woods':
            print(woods)
            # check if monsters
            if woods.has_threats():
                combat(hero, woods.get_threats())
            else:
                print(woods.get_threats())

            print(f'{hero.name} sees two paths.. a house or the grove')
            direction = input(f"What path will {hero.name} take? ")

            if direction == "grove":
                # final fight

                print(well)
                sys.exit()
            elif direction == 'house':
                print(
                    "The hero did not find the well but instead a party of trolls too many to count")
                sys.exit()
            else:
                print("wrong input")
        else:
            print('wrong input')
    elif direction == 'cave':
        print(cave)
        # check if monsters
        if cave.has_threats():
            combat(hero, cave.get_threats())
        else:
            print(cave.get_threats())

        print(f'{hero.name} sees two paths.. a flood or the woods')
        direction = input(f'What path will {hero.name} take? ')

        if direction == 'flood':
            print('flood')
            if flood.has_threats():
                combat(hero, flood.get_threats())
            else:
                print(flood.get_threats())

            print(f'{hero.name} sees two paths.. a nest or a pit')
            direction = input(f"What path will {hero.name} take? ")

            if direction == "nest":
                print(
                    "The hero did not find the well only a new abomination last heard of in fairy tales")
                sys.exit()
            elif direction == 'pit':
                print(
                    "The hero did not find the well but instead fell into a dark bottomless hole")
                sys.exit()
            else:
                print("wrong input")

        elif direction == 'woods':
            print(woods)
            # check if monsters
            if woods.has_threats():
                combat(hero, woods.get_threats())
            else:
                print(woods.get_threats())

            print(f'{hero.name} sees two paths.. a house or the grove')
            direction = input(f"What path will {hero.name} take? ")

            if direction == "grove":
                # final fight

                print(well)
                sys.exit()
            elif direction == 'house':
                print(
                    "The hero did not find the well but instead a party of trolls too many to count")
                sys.exit()
            else:
                print("wrong input")
        else:
            print('wrong input')

    else:
        print("wrong input")


main()
