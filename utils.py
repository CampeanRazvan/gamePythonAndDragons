import winsound
import os
from colors import Use_colors

from magic import Spell
from Items import Item
import enemy




class Utils:

    @staticmethod
    def game_intro():
        sound = 'Main_Menu.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        intro_message = Use_colors.BOLD + Use_colors.BLUE + """
            ***************************************************************************************
                                              Welcome stranger,
              On the lands of Nahara, you'll face many enemies,you will conquer strong fortresses,
              omnipotent wizards and also you will run and hide from the dragons ... and who knows... 
                       if you survive long enough maybe you will kill some dragons to
                     In a country where magic rules, anything is possible if you wish so.
                                     It all depends on you, brave hero!
            ***************************************************************************************
            
             """ + Use_colors.ENDC
        return intro_message

    @staticmethod
    def world_intro():
        sound = 'Exploring.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        os.system('cls')
        print(Use_colors.BLUE +
              """      
              ***************************************************************************************
            The lands of Nahara are in grave danger and only you can stand a chance against the enemy armies
               ***************************************************************************************
               
                         """ + Use_colors.ENDC)
        crossroad_options = (f""" {Use_colors.RED}
                            1.Village {Use_colors.ENDC}
            {Use_colors.GREEN}                2.Forest {Use_colors.ENDC}
            {Use_colors.YELLOW}                3.Desert{Use_colors.ENDC}
    """)
        print("You are at a crossroads :")
        print(crossroad_options)
        index = 1

        chosen_path = int(input("Choose your path carefully -> "))
        if chosen_path == 1:
            Utils.village()
        elif chosen_path == 2:
            Utils.forest()
        elif chosen_path == 3:
            Utils.desert()
        else:
            print("Incorrect choice")

    @staticmethod
    def game_start():
        start_option = input("Ready to begin your adventure?" + Use_colors.GREEN + "Yes" + Use_colors.ENDC +
                             "/" + Use_colors.RED + "No" + Use_colors.ENDC + " -> ")
        print(())

        if start_option.strip() in ['Y', "Yes", "yes", "y", "YES"]:
            os.system('cls')
            print("Choose your hero class :")
            print(Use_colors.RED + Use_colors.BOLD + "1.Warrior" + Use_colors.ENDC)
            print(Use_colors.BLUE + Use_colors.BOLD + "2.Wizard" + Use_colors.ENDC)
            print(Use_colors.GREEN + Use_colors.BOLD + "3.Ranger" + Use_colors.ENDC)

        elif start_option.strip() in ["N", "n", "no", "NO", "No"]:
            print("Goodbye")
        else:
            print(
                Use_colors.BOLD + Use_colors.RED + "Incorrect choice , please choose a valid option" + Use_colors.ENDC)
        return

    @staticmethod
    def village():
        os.system('cls')
        village_intro_message = "\t\t\tYour adventure starts in the village of Rosemill\n"
        print(village_intro_message)

        return

    @staticmethod
    def forest():
        os.system('cls')
        forest_intro_message = "\t\t\tYour adventure starts in the Wolfpath forest\n"
        print(forest_intro_message)

        return

    @staticmethod
    def desert():
        os.system('cls')
        desert_intro_message = "\t\t\tYour adventure starts in the Dead Wasteland\n"
        print(desert_intro_message)

        return

