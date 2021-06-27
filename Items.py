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


