from colors import Use_colors

class Item:
    def __init__(self, name, type, description, action, number):
        self.name = name
        self.type = type
        self.description = description
        self.action = action
        self.number = number

    def show_Item_name(self):
        return self.name

    def item_action(self):
        return self.action

    def item_count(self):
        if self.number == 0:
            print("Inventar is empty")
        else:
            self.number -= 1








# potion = Item("Potion", "potion", "Heals 50 HP", 50)
# hipotion = Item("HI_Potion", "potion", "Heals 100 HP", 100)
# superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
# elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
# hielixer = Item("megaElixer", "elixer", "Fully restore all party's HP/MP ", 9999)
#
#  player_items = [{"item": potion, "quantity": 15},
#                         {"item": hipotion, "quantity": 5},
#                         {"item": superpotion, "quantity": 5},
#                         {"item": elixer, "quantity": 2},
#                         {"item": hipotion, "quantity": 5},
#                         {"item": grenade, "quantity": 5}]

class Life_Potion(Item):

    def __init__(self):
        super().__init__("life potion" ,"potion", "Heals 75 life points", 75, 3  )

    def number_of_items(self):
        return self.number


class Mana_Potion(Item):

    def __init__(self):
        super().__init__("mana potion", "elixer", "Give 25 mana points", 25, 2 )

class Greek_Fire(Item):

    def __init__(self):
        super().__init__("greek fire", "attack item", "Give 120 attack damage", 120 , 1)


