import random
from colors import Use_colors
class Spell:


    def __init__(self,name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type


    def show_magic_name(self):
        return self.name

    def show_magic_cost(self):
        return self.cost



    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low,high)

    # fire = Spell("Fire", 10, 100, "black")
    # thunder = Spell("Thunder", 10, 100, "black")
    # blizzard = Spell("Blizzard", 10, 100, "black")
    # meteor = Spell("Meteor", 20, 200, "black")
    # quake = Spell("Quake", 14, 40, "black")
    #
    # # create White Magic
    # cure = Spell("Cure", 12, 120, "white")
    # cura = Spell("Cura", 18, 200, "white")




class Thunder(Spell):
    def __init__(self, name):
        super().__init__(name, 15, 50, "offensive spell")

    def attack_spell_thunder(self,player, enemy_1):

        spell = Fire("fire")

        magic_damage = spell.generate_damage()
        print(magic_damage)

        curent_mana = player.get_mana()
        if spell.cost > curent_mana:
            print(Use_colors.RED + "\n Not enough mana" + Use_colors.ENDC)

        player.reduce_mana(spell.cost)

        if spell.type == "defensive":
            player.heal(magic_damage)
            print(Use_colors.BLUE + "\n" + spell.name + " heals for", str(magic_damage),
                  "HP." + Use_colors.ENDC)

        elif spell.type == "offensive spell":

            enemy_1.take_damage(magic_damage)
            print(Use_colors.BLUE + "\n" + spell.name + " deals", str(magic_damage),
                  "points of damage" + Use_colors.ENDC)

class Fire(Spell):
    def __init__(self,name):
        super().__init__(name, 19, 55, "offensive spell")

    def attack_spell_fire(self,player, enemy_1):

        spell = Fire("fire")

        magic_damage = spell.generate_damage()
        print(magic_damage)

        curent_mana = player.get_mana()
        if spell.cost > curent_mana:
            print(Use_colors.RED + "\n Not enough mana" + Use_colors.ENDC)

        player.reduce_mana(spell.cost)

        if spell.type == "defensive":
            player.heal(magic_damage)
            print(Use_colors.BLUE + "\n" + spell.name + " heals for", str(magic_damage),
                  "HP." + Use_colors.ENDC)

        elif spell.type == "offensive spell":

            enemy_1.take_damage(magic_damage)
            print(Use_colors.BLUE + "\n" + spell.name + " deals", str(magic_damage),
                  "points of damage" + Use_colors.ENDC)

class Life(Spell):
    def __init__(self,name):
        super().__init__(name, 25, 75, "defensive spell")

    def life_spell(self, player, enemy_1):

        spell = Fire("life")

        magic_damage = spell.generate_damage()
        print(magic_damage)

        curent_mana = player.get_mana()
        if spell.cost > curent_mana:
            print(Use_colors.RED + "\n Not enough mana" + Use_colors.ENDC)

        player.reduce_mana(spell.cost)


        player.heal(magic_damage)
        print(Use_colors.BLUE + "\n" + spell.name + " heals for", str(magic_damage),
                  "HP." + Use_colors.ENDC)






