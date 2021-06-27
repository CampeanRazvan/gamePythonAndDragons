magic = ["fire", "thunder", "blizzard", "meteor", "cure", "cura"]

i = 1
for item in magic:
    print(str(i) + "." + item)
     i +=1

# create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 40, "black")

# create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("HI_Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("megaElixer", "elixer", "Fully restore all party's HP/MP ", 9999)

grenade = Item("Grenade", "attack", " Deals 500 damage", 500)

player_magic = ["fire", "thunder", "blizzard", "meteor", "cure", "cura"]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 2},
                {"item": hipotion, "quantity": 5},
                {"item": grenade, "quantity": 5}]



""" ~         ~~          __
        T      .,,.    ~--~ ^^
 ^^    / \                    ~
      [ O ]    ^^    _II__
      |___|         /     /\
__ _ /     \ ______/     /  \_,__
    II ____ \,-- :/____ /____\,
;  /  \      |    |[]   |  O |
:' |  | []  -|    |.,.,.| [] |
   |[]|,.,.,.\,    -,.    |
  ..    ..-     ;        .     """