from colors import Use_colors
import random
import magic

class Player:

    def __init__(self, name, life_points, mana_points, attack, defence, magic, items):
        self.name = name
        self.life_points = life_points
        self.mana_points = mana_points
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.items = items
        self.full_life_points = life_points
        self.full_mana_points = mana_points

        self.actions = ["Attack", "Magic", "Items"]
        self.magic = ["fire", "thunder", "life"]
        self.items = ["life_potion", "mana_potion", "greek fire"]





    # show life points of our character
    def show_life(self):
        return self.life_points

    # I try to make a graphical representation of our character atributes
    def print_stats(self):
        print("\n\n")
        print("Name                           HP                       MP")
        print("                   ___________________________          __________ ")
        print(Use_colors.BOLD + Use_colors.RED + self.name + "   " +
              str(self.life_points) + "/" + str(self.full_life_points) + Use_colors.ENDC + "  |" + Use_colors.GREEN + "███████████████████████████" + Use_colors.ENDC + "|" +
             " " + Use_colors.BLUE + str(self.mana_points) + "/" + str(self.full_mana_points) + "  |" + Use_colors.BLUE + "██████████" + Use_colors.ENDC + "|"
              )

    def generate_damage(self):
        attack_low = self.attack - 10
        attack_high = self.attack + 10

        return random.randrange(attack_low, attack_high)




    def take_damage(self, damage):
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0
        return self.life_points

    def get_hitpoints(self):
        return self.life_points

    def get_more_mana(self,damage):
        print("Mana potion give 30 mana points")
        self.mana_points += damage
        if self.mana_points > self.full_mana_points:
            self.mana_points = self.full_mana_points


    def heal(self, damage):
        print("Life potion heals for 75")
        self.life_points += damage
        if self.life_points > self.full_life_points:
            self.life_points = self.full_life_points


    def get_max_hitpoints(self):
        return self.full_life_points

    def get_mana(self):
        return self.mana_points

    def get_max_mana(self):
        return self.full_mana_points

    def reduce_mana(self, cost):
        self.mana_points -= cost

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for action in self.actions:
            print("        " + str(i) + '.', action)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
        for spell in self.magic:

            print("        " + str(i) + "." + spell)
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        print("""
        1. Life potion : Heals 75 life points  x
        2. Mana potion : Give  30 mana points  x
        3. Greek fire  : Give 120 damage       x""")




class Warrior(Player):

    def __init__(self, name):
        super().__init__(name, 180, 50, 30, 10, "", "")
        self.spells = ["Warrior cry", "Our is the furry"]
        self.items_list = ["Small life potion", "large life potion", "javelin",
                               "small mana potion", "large mana potion"]




class Ranger(Player):

    def __init__(self, name):
        super().__init__(name, 160, 55, 20, 8, "", "")
        self.spells = ["Head Shot", "triple arrow"]
        self.items_list = ["Small life potion", "large life potion",
                               "small mana potion", "large mana potion", ]




class Wizard(Player):

    def __init__(self, name):
        super().__init__(name, 150, 55, 20, 8, "", "")
        self.spells = ["Fire ball", "Tornado"]
        self.items_list = ["Small life potion", "large life potion",
                               "small mana potion", "large mana potion", ]





