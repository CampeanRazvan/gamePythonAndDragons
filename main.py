import Items
import utils
import character
import enemy
from magic import Spell
from Items import Item
from colors import Use_colors
import magic


def battle_1():

    running = True

    list_of_spells = ["thunder", "fire","life"]
    list_of_items = []



    count_life_potion = 0
    count_mana_potion = 0
    count_greekfire_potion = 0
    while running:

        player.choose_action()

        print(" You are under attack , this are your option ")

        choice = input("    Choose action: ->")

        if choice == "1":
            damage = player.generate_damage()
            enemy_1.take_damage(damage)
            print("You attacked for", damage, "points of damage . Enemy HP:", enemy_1.show_life())

        elif choice == "2":

            player.choose_magic()
            magic_choice = int(input("Choose magic:"))

            if magic_choice == 1:
                magic.Thunder.attack_spell_thunder("fire",player,enemy_1)

            elif magic_choice == 2:
                magic.Fire.attack_spell_fire("fire", player, enemy_1)

            elif magic_choice == 3:
                magic.Life.life_spell("life",player ,enemy_1)


        elif choice == "3":
            player.choose_item()
            item_choice = int(input("Chose item ->"))

            if item_choice == 1:
                item_life_potion = Items.Life_Potion()

                number_items = item_life_potion.number
                if number_items <= count_life_potion:
                    print(Use_colors.RED + "\n" + "None left..." + Use_colors.ENDC)
                    break
                print(number_items)
                count_life_potion += 1
                player.heal(item_life_potion.action)



            elif item_choice == 2:
                item_mana_potion = Items.Mana_Potion()
                if item_mana_potion.number <= count_mana_potion:
                    print(Use_colors.RED + "\n" + "None left..." + Use_colors.ENDC)
                    continue
                count_mana_potion += 1
                player.get_more_mana(item_mana_potion.action)

            elif item_choice == 3:
                item_greek_fire_potion = Items.Greek_Fire()
                if item_greek_fire_potion.number <= count_greekfire_potion:
                    print(Use_colors.RED + "\n" + "None left..." + Use_colors.ENDC)
                    continue
                count_greekfire_potion += 1
                enemy_1.take_damage(item_greek_fire_potion.action)
                print(Use_colors.BLUE + "\n" + item_greek_fire_potion.name + " deals", str(item_greek_fire_potion.action),
                      "points of damage" + Use_colors.ENDC)

        enemy_choice = 1

        enemy_damage = enemy_1.generate_damage()
        player.take_damage(enemy_damage)
        print("Enemy attacks for", enemy_damage, "Player HP:", enemy_1.get_life_points())

        print("___________________________________")
        print("Enemy HP:", Use_colors.RED + str(enemy_1.get_life_points()) + "/" + str(
            enemy_1.get_full_life_points()) + Use_colors.ENDC + "\n")
        print("Your HP:", Use_colors.GREEN + str(player.get_hitpoints()) + "/" + str(
            player.get_max_hitpoints()) + Use_colors.ENDC)

        print("Your mana: ", Use_colors.BLUE + str(player.get_mana()) + "/" + str(
            player.get_max_mana()) + Use_colors.ENDC + "\n")
        if enemy_1.show_life() <= 0:
            print(Use_colors.GREEN + "You WIN!" + Use_colors.ENDC)
            running = False
        elif player.show_life() <= 0:
            print(Use_colors.RED + "You are ded! " + Use_colors.ENDC)
            running = False


print(utils.Utils.game_intro())
utils.Utils.game_start()

player_choice = int(input("Chose your hero class (1,2,3) ->"))
if player_choice == 1:
    print("You choose to be a mighty warrior")
    player_name = input("Chose a name for your hero ->")
    player = character.Warrior(player_name)
    player.print_stats()
    utils.Utils.world_intro()
    player.choose_magic()

    enemy_1 = enemy.Enemy.random_enemy()
    print(enemy_1.print_stats())
    battle_1()
elif player_choice == 2:
    print("You choose to be a powerful wizard")
    player_name = input("Chose a name for your hero ->")
    player = character.Wizard(player_name)
    player.print_stats()
    utils.Utils.world_intro()

    enemy_1 = enemy.Enemy.random_enemy()
    print(enemy_1.get_stats())
    battle_1()
elif player_choice == 3:
    print("You choose to be a agile ranger")
    player_name = input("Chose a name for your hero ->")
    player = character.Ranger(player_name)
    player.print_stats()
    utils.Utils.world_intro()

    enemy_1 = enemy.Enemy.random_enemy()
    print(enemy_1.get_stats())
    battle_1()