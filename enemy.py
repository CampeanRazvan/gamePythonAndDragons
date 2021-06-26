
import winsound
import random
from colors import Use_colors




class Enemy:

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
        self.attack_min = attack - 10
        self.attack_max = attack - 10
        self.actions = ["Attack", "Magic", "Items"]

        # show life points of our character

    def show_life(self):
        return self.life_points

        # I try to make a graphical representation of our character atributes

    def print_stats(self):
        print("\n\n")
        print("Name                                 HP                    MP")
        print("                                ___________________________          __________ ")
        print(Use_colors.BOLD + Use_colors.RED + str(self.name) + "      " +
              str(self.life_points) + "/" + str(
            self.full_life_points) + Use_colors.ENDC + "  |" + Use_colors.GREEN + "███████████████████████████" + Use_colors.ENDC + "|" +
              " " + Use_colors.BLUE + str(self.mana_points) + "/" + str(
            self.full_mana_points) + "  |" + Use_colors.BLUE + "██████████" + Use_colors.ENDC + "|"
              )

    def get_stats(self,):
        print("                          ___________________________        __________ ")
        print(Use_colors.BOLD + str(self.name) +
              str(self.life_points) + "/" + str(self.full_life_points) + " |" + Use_colors.GREEN + "██████████████          " + Use_colors.ENDC + "|" +
              str(self.mana_points) + "/" + str(self.full_mana_points) + Use_colors.BLUE + " |" + "██████████" + Use_colors.ENDC + "|")

    def generate_damage(self):
        attack_low = self.attack - 10
        attack_high = self.attack + 10
        return random.randrange(attack_low, attack_high)

    def take_damage(self, damage):
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0
        return self.life_points

    def get_life_points(self):
        return self.life_points

    def heal(self, damage):
        self.life_points += damage
        if self.life_points > self.full_life_points:
            self.life_points = self.full_life_points

    def get_full_life_points(self):
        return self.full_life_points

    def get_mana_point(self):
        return self.mana_points

    def get_full_mana_points(self):
        return self.full_mana_points

    def reduce_mana(self, cost):
        self.mana_points -= cost

    def choose_action(self):
        i = 1
        print("\n" + "           " + Use_colors.BOLD + self.name + Use_colors.ENDC)
        print(Use_colors.BLUE + Use_colors.BOLD + "    ACTIONS" + Use_colors.ENDC)
        for item in self.actions:
            print("        " + str(i) + '.', item)
            i += 1

    # def choose_magic(self):
    #     i = 1
    #
    #     print("\n" + "       " + Use_colors.BLUE + Use_colors.BOLD + "     MAGIC" + Use_colors.ENDC)
    #     for spell in self.magic:
    #         print("        " + str(i) + ".", spell.name, '(cost:', str(spell.cost) + ')')
    #         i += 1

    def choose_item(self):
        i = 1
        print("\n" + Use_colors.GREEN + Use_colors.BOLD + "     ITEMS" + Use_colors.ENDC)
        for item in self.items:
            print("            " + str(i) + ".", item["item"].name, ":", item["item"].description,
                  " x" + str(item["quantity"]))
            i += 1

    @staticmethod
    def random_enemy():
        sound = 'BattleFinal.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        random_number = random.randint(0, 2)
        if random_number == 0:
            goblin = Goblin()
            return goblin

        elif random_number == 1:
            orc = Orc()
            return orc

        elif random_number == 2:
            wrath = Wrath()
            return wrath


class Goblin(Enemy):
    def __init__(self):
        super().__init__(Goblin , 190, 30, 29, 11,  "", "")
        # print("""\nI'm a vengeful goblin.
# My poisonous arrows will pierce you!""")



class Orc(Enemy):
    def __init__(self):
        super().__init__(Orc , 200, 50, 31, 9, "", "")
        # print("""\nI'm the Dark Lord orc captain.
# Your head will be my trophy!""")




class Wrath(Enemy):
    def __init__(self):
        super().__init__( Wrath, 220, 50, 32, 10 ,"", "")
        # print("""\nI'm one of the nine dead kings."
# You are no match to my powers!""")

