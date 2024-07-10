#Imports modules such as time, os, sys, and random into the program
import sys
import os
import time
import random

gameStart = 0

#Creates the class for the player. Includes the name, current health, max health, current stamina, max stamina, and attack damage of the player.

#Class of entities(including player), objects are three monsters and the player
class Entities():
    def __init__(self, name, currentHealth, maxHealth, currentStamina,
                 maxStamina, attackDamage):
        self.name = name

        self.maxHealth = maxHealth
        self.currentHealth = currentHealth

        self.maxStamina = maxStamina
        self.currentStamina = currentStamina

        self.attackDamage = attackDamage


Player = Entities('You', 90, 90, 100, 100, 7)

Tree = Entities('Evil Tree', 50, 50, 50, 50, 5)

Megalopython = Entities('Megalopython', 110, 110, 60, 60, 4)

EvilSelf = Entities('Evil Self', 90, 90, 100, 100, 7)


#When run, shows the ending of the storyline and sources for the project
def end():

    print(
        "In this forest, you've seen the unexplainable... and yet you've made it alive to tell the tale..."
    )
    time.sleep(3.5)
    print("Congratulations, diligent mercenary.")
    time.sleep(2)
    print('The End.')

    print('Presented to you by Justin Lim')

    print("Sources: https://www.geeksforgeeks.org/python-classes-and-objects/")
    print()
    print('https://www.scaler.com/topics/how-to-clear-screen-in-python/')
    print()
    print('https://www.programiz.com/python-programming/time/sleep')
    print()
    print('https://www.w3schools.com/python/module_random.asp')

    print()
    print()
    print()

    print('Error and Bugs Help:')
    print(
        'https://careerkarma.com/blog/python-local-variable-referenced-before-assignment/#:~:text=The%20UnboundLocalError%3A%20local%20variable%20referenced,you%20assign%20it%20a%20value.'
    )
    print()
    print(
        'https://discuss.codecademy.com/t/cant-clear-terminal-with-os-system-cls/434230'
    )
    print()
    print(
        'https://stackoverflow.com/questions/9264763/why-does-this-unboundlocalerror-occur-closure'
    )

    print(
        'https://vbsreddy1.medium.com/unboundlocalerror-when-the-variable-has-a-value-in-python-e34e097547d6'
    )

    print()
    print()
    print()

    print('For ASCII Text Art: ')
    print("https://patorjk.com/software/taag/#p=display&f=Graffiti&t=.")

    time.sleep(5)
    sys.exit()
  
#Shows player stats, called when the 'stats' option is entered
def showStats():

    while 1 == 1:

        print('----------------------------------------------------------------')
        print('                             Stats                              ')
        print('----------------------------------------------------------------')
        print('-                                                              -')
        print(f'-  Name: {Player.name}                                        -')
        print('-                                                              -')
        print(f'-  Health: {Player.currentHealth}/{Player.maxHealth}          -')
        print('-                                                              -')
        print(f'-  Stamina: {Player.currentStamina}/{Player.maxStamina}       -')
        print('-                                                              -')
        print(f'-  Attack: 7                                                  -')
        print('-                                                              -')
        print('-                                                              -')
        print("-   [E] Type 'E' to exit                                       -")
        print('-                                                              -')
        print('----------------------------------------------------------------')

        choice = input("[E] Type 'E' to exit")

        if choice == 'e':
            break

        if choice == 'E':
            break

        else:
            print("Please type 'E' to exit")
            continue


#The 'Attack' option/sub-menu inside the main combat menu
def combat_attack(monstername):
    os.system('clear')

    while 1 == 1:
        try:

            print('----------------------------------------------------------------')
            print('                             Attack                             ')
            print('----------------------------------------------------------------')
            print('-                                                              -')
            print('-                                                              -')
            print('-    [1] Slice & Dice                     [2] Slash            -')
            print('-                                                              -')
            print('-  -Rolls a dice numbered               -25% Chance of         -')
            print('-   from 1-12, that number                doing 0 damage       -')
            print('-    will be the damage                                        -')
            print('-   inflicted on the enemy              -75% Chance of         -')
            print('-                                        doing 7 damage        -')
            print('-                                                              -')
            print('-  -  Drains 5 Stamina                 - Drains 2 Stamina      -')
            print('-                                                              -')
            print('-                                                              -')
            print('-                                                              -')
            print('-    [3] Return to combat                                      -')
            print('-             menu                                             -')
            print('-                                                              -')
            print('-                                                              -')
            print('-                                                              -')
            print('-                                                              -')
            print('----------------------------------------------------------------')
            print(f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -')
            print(f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -')
            print('----------------------------------------------------------------')

            choice = int(input('Enter choice: '))

            #If the player chooses 1, the monster's current health will be subtracted by a random number from range 1-12, player stamina will decrease by 5, returns to main combat menu

            if choice == 1:
                slice_dice = random.randint(1, 12)
                monstername.currentHealth = monstername.currentHealth - slice_dice
                Player.currentStamina = Player.currentStamina - 5
                print(
                    f'You did {slice_dice} damage! {monstername.name} is now at {monstername.currentHealth} health!'
                )
                time.sleep(2)
                slice_dice = 0
                global player_turn
                player_turn = 0
                break

            if choice == 2:
                slash = random.randint(1, 4)
                player_turn = 0

                if slash == 1:
                    monstername.currentHealth = monstername.currentHealth - 7
                    print(
                        f'You did 7 damage! {monstername.name} is now at {monstername.currentHealth} health!'
                    )
                    time.sleep(0.7)
                    break

                if slash == 2:
                    monstername.currentHealth = monstername.currentHealth - 7
                    print(
                        f'You did 7 damage! {monstername.name} is now at {monstername.currentHealth} health!'
                    )
                    time.sleep(0.7)
                    break

                if slash == 3:
                    monstername.currentHealth = monstername.currentHealth - 7
                    print(
                        f'You did 7 damage! {monstername.name} is now at {monstername.currentHealth} health!'
                    )
                    time.sleep(0.7)
                    break

                if slash == 4:
                    print(
                        f'You missed that attack! {monstername.name} is now at {monstername.currentHealth} health!'
                    )
                    time.sleep(0.7)
                    break

            if choice == 3:
                break

            else:
                print('Enter one of the options!')
                continue

        except ValueError:
            print('Please enter a number!')
            continue


#Main combat menu for Tree
def combatMenu_tree():

    while 1 == 1:

        try:

            os.system('clear')
            print(
                '----------------------------------------------------------------'
            )
            print(
                '- ------                                                -----  -'
            )
            print(
                f'-   {Tree.name}  {Tree.currentHealth}/{Tree.maxHealth}                -'
            )
            print(
                '-     ----        --------------------------        ----       -'
            )
            print(
                '-     -------------      ---------     -------------           -'
            )
            print(
                '-                        ---------                             -'
            )
            print(
                '-                      ----V---V----                           -'
            )
            print(
                '-                     ------vvv------                          -'
            )
            print(
                '-                     ------www------                          -'
            )
            print(
                '-                     --- -------  ---                         -'
            )
            print(
                '-                    ---  -------  ---                         -'
            )
            print(
                '-                     --- ------- ---                          -'
            )
            print(
                '-                     --- ------- ---                          -'
            )
            print(
                '-                --------  ---  - -----------                  -'
            )
            print(
                '-                 ------ ------ -- -- ------------             -'
            )
            print(
                '-                   -------    ----- - ---                     -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                           ----                               -'
            )
            print(
                '-                         --------                             -'
            )
            print(
                '-                         - ---- -                             -'
            )
            print(
                '-                           -  -                               -'
            )
            print(
                '-                                                              -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
            )
            print(
                '-                  -                   -                       -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
            )
            print(
                f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
            )
            print(
                '----------------------------------------------------------------'
            )

            choice = int(input('Enter choice: '))

            if choice == 1:
                combat_attack(Tree)

            #Conditional when the player decides to try to flee the fight. Ends in a "you died" screen and kills the program
            if choice == 2:
                os.system('clear')
                print('Interesting... This time, you were able to escape.')
                time.sleep(3)

                storyline4()

            #Stats option, calls showStats function
            if choice == 3:
                showStats()
                continue

            #If the Tree runs out of health
            if Tree.currentHealth <= 0:
                os.system('clear')
                print('The mysterious tree suddenly stops attacking...')
                time.sleep(3)
                print('An interesting tree.')
                time.sleep(1)

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '- ------                                                -----  -'
                )
                print(
                    '-  -----                                              ------   -'
                )
                print(
                    '-     ----        --------------------------        ----       -'
                )
                print(
                    '-         ---------     -----------   ----------Z--            -'
                )
                print(
                    '-                       -----------        Z                   -'
                )
                print(
                    '-                      ---__---__---   Z                       -'
                )
                print(
                    '-                     --------------Z                          -'
                )
                print(
                    '-                     -------O--------                         -'
                )
                print(
                    '-                     --- -------  ---                         -'
                )
                print(
                    '-                    ---  -------  ---                         -'
                )
                print(
                    '-                     --- ------- ---                          -'
                )
                print(
                    '-                     --- ------- ---                          -'
                )
                print(
                    '-                --------  ---  - -----------                  -'
                )
                print(
                    '-                 ------ ------ -- -- ------------             -'
                )
                print(
                    '-                   -------    ----- - ---                     -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ----                               -'
                )
                print(
                    '-                         --------                             -'
                )
                print(
                    '-                         - ---- -                             -'
                )
                print(
                    '-                           -  -                               -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )

                print(' __      _______ _____ _______ ____  _______     ___ ')
                print(' \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |')
                print('  \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |')
                print('   \ \/ /   | || |       | | | |  | |  _  / \   / | |')
                print('    \  /   _| || |____   | | | |__| | | \ \  | |  |_|')
                print('     \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)')

                time.sleep(3)

                storyline4()

            #If the player runs out of health
            if Player.currentHealth <= 0:
                os.system('clear')

                print('You had a good run...')
                time.sleep(3)
                print(
                    'But you could not defeat something so deadly as a tree...'
                )

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #If the player runs out of stamina
            if Player.currentStamina <= 0:
                os.system('clear')
                print('You feel too tired to continue the fight.')
                time.sleep(2.5)
                print('No longer able to defend yourself...')

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #Checks if monster_turn == 1, if it is equal to 1, the monster will attack. variable is set to 0 and player goes.
            global player_turn
            if player_turn <= 0:
              
                time.sleep(1)
                os.system('clear')

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '- ------                                                -----  -'
                )
                print(
                    f'-   {Tree.name}  {Tree.currentHealth}/{Tree.maxHealth}                -'
                )
                print(
                    '-     ----        --------------------------        ----       -'
                )
                print(
                    '-     -------------      ---------     -------------           -'
                )
                print(
                    '-                        ---------                             -'
                )
                print(
                    '-                      ----V---V----                           -'
                )
                print(
                    '-                     ------vvv------                          -'
                )
                print(
                    '-                     ------www------                          -'
                )
                print(
                    '-                     --- -------  ---                         -'
                )
                print(
                    '-                    ---  -------  ---                         -'
                )
                print(
                    '-                     --- ------- ---                          -'
                )
                print(
                    '-                     --- ------- ---                          -'
                )
                print(
                    '-                    ----  ---  - -----                        -'
                )
                print(
                    '-                   ----- ------ -- -- ---                     -'
                )
                print(
                    f'-                   --------       ----- -----   -{Tree.attackDamage} '
                )
                print(
                    '-                    ------              ------                -'
                )
                print(
                    '-               ---------                 --------             -'
                )
                print(
                    '-             -------------              -------               -'
                )
                print(
                    '-               ------                     --------            -'
                )
                print(
                    '-                - --  --__     ----   __--------              -'
                )
                print(
                    '-                |  |  |      --------    |  |  |              -'
                )
                print(
                    '-                 \  \  \     - ---- -    /  /  /              -'
                )
                print(
                    '-                  -- -- --     -  -   -- -- --                -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                )
                print(
                    '-                  -                   -                       -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                )
                print(
                    f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                )
                print(
                    '----------------------------------------------------------------'
                )

                print(
                    f"The tree swings both arms around at you. You took {Tree.attackDamage} damage."
                )

                time.sleep(1)

                player_turn = 1

        except ValueError:
            print('Please enter a valid option.')


#Main combat menu for Evil Self
def combatMenu_EvilSelf():

    while 1 == 1:

        try:

            os.system('clear')

            print(
                '----------------------------------------------------------------'
            )
            print(
                '-                                                              -'
            )
            print(
                f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                           ------             -'
            )
            print(
                '-    ---------              ----                               -'
            )
            print(
                '-                         --------            --      --       -'
            )
            print(
                '-                         - ---- -                             -'
            )
            print(
                '-                           -  -                   ------      -'
            )
            print(
                '-        ----                                                  -'
            )
            print(
                '-                       ----                   -         -     -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                           ----                               -'
            )
            print(
                '-                         --------                             -'
            )
            print(
                '-                         - ---- -                             -'
            )
            print(
                '-                           -  -                               -'
            )
            print(
                '-                                                              -'
            )
            print(
                f'-                  {Player.name}                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '-                                                              -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
            )
            print(
                '-                  -                   -                       -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
            )
            print(
                f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
            )
            print(
                '----------------------------------------------------------------'
            )

            print(
                "The figure looks just like you... just only much more sinister..."
            )

            choice = int(input('Enter choice: '))

            if choice == 1:
                combat_attack(EvilSelf)

            #Conditional when the player decides to try to flee the fight. Ends in a "you died" screen and kills the program
            if choice == 2:
                os.system('clear')
                print(
                    'What are you doing? Did you forget who you were facing?')
                time.sleep(4)
                print(
                    'Your evil twin chases you for a good ten minutes, until you reach the end of a cliff...'
                )
                time.sleep(4)

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #Stats option
            if choice == 3:
                showStats()
                continue

            #If the EvilSelf runs out of health
            if EvilSelf.currentHealth <= 0:
                os.system('clear')
                print('You deal the final blow to your evil doppelganger.')
                time.sleep(5)
                print(
                    'Your enemy shatters in pieces, revealing its true form... glass.'
                )
                time.sleep(5)
                print('as if it was only walking fragments of a mirror...')
                time.sleep(5)

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ---*-----     ---*--               -'
                )
                print(
                    '-    ----*---    -      ----  --                               -'
                )
                print(
                    '               --      --*-----  --*--      --      --         -'
                )
                print(
                    '-                         - -----   ----                       -'
                )
                print(
                    '-                   ---    ---  *--     --*--                  -'
                )
                print(
                    '-        ----                   -   ------                     -'
                )
                print(
                    '-                       ---*     --*--         -         -     -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ----                               -'
                )
                print(
                    '-                         --------                             -'
                )
                print(
                    '-                         - ---- -                             -'
                )
                print(
                    '-                           -  -                               -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )

                time.sleep(2)

                print(' __      _______ _____ _______ ____  _______     ___ ')
                print(' \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |')
                print('  \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |')
                print('   \ \/ /   | || |       | | | |  | |  _  / \   / | |')
                print('    \  /   _| || |____   | | | |__| | | \ \  | |  |_|')
                print('     \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)')

                time.sleep(5.5)

                end()

            #If the player runs out of health
            if Player.currentHealth <= 0:
                os.system('clear')

                print('You had a good run...')
                time.sleep(3)
                print(
                    "You tried your best... Don't beat yourself up over it. Hehe. Ba dum tss."
                )
                time.sleep(3)

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #If the player runs out of stamina
            if Player.currentStamina <= 0:
                os.system('clear')
                print('You feel too tired to continue the fight.')
                time.sleep(3)
                print('No longer able to defend yourself...')

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #Checks if monster_turn == 1, if it is equal to 1, the monster will attack. variable is set to 0 and player goes.
            global player_turn
            if player_turn <= 0:
                os.system('clear')

                time.sleep(0.7)

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-                                                              -'
                )
                print(
                    f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                           ------             -'
                )
                print(
                    '-    ---------                                                 -'
                )
                print(
                    '-                                             --      --       -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                  ------      -'
                )
                print(
                    '-        ----                                                  -'
                )
                print(
                    '-                       ----                   -         -     -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ----    |   ----                   -'
                )
                print(
                    '-                         --------  +---------                 -'
                )
                print(
                    '-                         - ---- -      ---- -                 -'
                )
                print(
                    '-                           -  -        -  -                   -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    f'-                  {Player.name}                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                )
                print(
                    '-                  -                   -                       -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                )
                print(
                    f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                )
                print(
                    '----------------------------------------------------------------'
                )

                print("'Your evil twin uses 'Slash' on you.")
                os.system('clear')

                attack_hit = random.randint(1,4)
                if attack_hit == 1:
                    
  
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                           ------             -'
                  )
                  print(
                      '-    ---------                                                 -'
                  )
                  print(
                      '-                                             --      --       -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                  ------      -'
                  )
                  print(
                      '-        ----                                                  -'
                  )
                  print(
                      '-                       ----                   -         -     -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                  -7       ----    |   ----                   -'
                  )
                  print(
                      '-                         --------  +---------                 -'
                  )
                  print(
                      '-                         - ---- -      ---- -                 -'
                  )
                  print(
                      '-                           -  -        -  -                   -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-                  {Player.name}                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                  )
                  print(
                      '-                  -                   -                       -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                  )
                  print(
                      f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
  
                  time.sleep(1)
                  os.system('clear')
  
                  Player.currentHealth = Player.currentHealth - EvilSelf.attackDamage
  
                  player_turn = 1

                if attack_hit == 2:
                    
  
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                           ------             -'
                  )
                  print(
                      '-    ---------                                                 -'
                  )
                  print(
                      '-                                             --      --       -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                  ------      -'
                  )
                  print(
                      '-        ----                                                  -'
                  )
                  print(
                      '-                       ----                   -         -     -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                  -7       ----    |   ----                   -'
                  )
                  print(
                      '-                         --------  +---------                 -'
                  )
                  print(
                      '-                         - ---- -      ---- -                 -'
                  )
                  print(
                      '-                           -  -        -  -                   -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-                  {Player.name}                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                  )
                  print(
                      '-                  -                   -                       -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                  )
                  print(
                      f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
  
                  time.sleep(1)
                  os.system('clear')
  
                  Player.currentHealth = Player.currentHealth - EvilSelf.attackDamage
  
                  player_turn = 1


                if attack_hit == 3:
                    
  
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                           ------             -'
                  )
                  print(
                      '-    ---------                                                 -'
                  )
                  print(
                      '-                                             --      --       -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                  ------      -'
                  )
                  print(
                      '-        ----                                                  -'
                  )
                  print(
                      '-                       ----                   -         -     -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                  -7       ----    |   ----                   -'
                  )
                  print(
                      '-                         --------  +---------                 -'
                  )
                  print(
                      '-                         - ---- -      ---- -                 -'
                  )
                  print(
                      '-                           -  -        -  -                   -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-                  {Player.name}                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                  )
                  print(
                      '-                  -                   -                       -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                  )
                  print(
                      f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
  
                  time.sleep(1)
                  os.system('clear')
  
                  Player.currentHealth = Player.currentHealth - EvilSelf.attackDamage
  
                  player_turn = 1
                  
                if attack_hit == 4:
                  
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-   {EvilSelf.name}  {EvilSelf.currentHealth}/{EvilSelf.maxHealth}-'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                           ------             -'
                  )
                  print(
                      '-    ---------                                                 -'
                  )
                  print(
                      '-                                             --      --       -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                  ------      -'
                  )
                  print(
                      '-        ----                                                  -'
                  )
                  print(
                      '-                       ----                   -         -     -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                  Miss     ----    |   ----                   -'
                  )
                  print(
                      '-                         --------  +---------                 -'
                  )
                  print(
                      '-                         - ---- -      ---- -                 -'
                  )
                  print(
                      '-                           -  -        -  -                   -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      f'-                  {Player.name}                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '-                                                              -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      '-  [1] Attack      -  [2] Run          -   [3] Stats           -'
                  )
                  print(
                      '-                  -                   -                       -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  print(
                      f'-  Health: {Player.currentHealth}/ {Player.maxHealth}         -'
                  )
                  print(
                      f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}      -'
                  )
                  print(
                      '----------------------------------------------------------------'
                  )
                  
                  time.sleep(1)
                  os.system('clear')
  
                  player_turn = 1
                  
        except ValueError:
            print('Please enter a valid option.')


#Main combat menu for Megalopython
def combatMenu_megalopython():

    while 1 == 1:

        try:

            os.system('clear')
            print(
                '-----------------------------------------------------------------'
            )
            print(
                '-                                                               -'
            )
            print(
                f'-   {Megalopython.name} {Megalopython.currentHealth}/{Megalopython.maxHealth}'
            )
            print(
                '-                                                               -'
            )
            print(
                '-                             -O------0                         -'
            )
            print(
                '-                        --------------                         -'
            )
            print(
                '-                        ----------V V                          -'
            )
            print(
                '-                      -------------                            -'
            )
            print(
                '-                           -------------                       -'
            )
            print(
                '-                     ---------------                           -'
            )
            print(
                '-                    ------------                               -'
            )
            print(
                '-                     --------------     --                     -'
            )
            print(
                '-                   ------------       ---                      -'
            )
            print(
                '-                      --------     -------                     -'
            )
            print(
                '-                        -----------------                      -'
            )
            print(
                '-                            --------                           -'
            )
            print(
                '-                                                               -'
            )
            print(
                '-                                                               -'
            )
            print(
                '-                           ----                                -'
            )
            print(
                '-                         --------                              -'
            )
            print(
                '-                         - ---- -                              -'
            )
            print(
                '-                           -  -                                -'
            )
            print(
                '-                                                               -'
            )
            print(
                f'-                  {Player.name}                               -'
            )
            print(
                '-                                                               -'
            )
            print(
                '-                                                               -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                '-  [1] Attack      -  [2] Run          -   [3] Stats            -'
            )
            print(
                '-                  -                   -                        -'
            )
            print(
                '----------------------------------------------------------------'
            )
            print(
                f'-  Health: {Player.currentHealth}/ {Player.maxHealth}          -'
            )
            print(
                f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}       -'
            )
            print(
                '---------------------------------------------------------------- '
            )

            choice = int(input('Enter choice: '))

            if choice == 1:
                combat_attack(Megalopython)

            #Conditional when the player decides to try to flee the fight. Ends in a "you died" screen and kills the program
            if choice == 2:
                os.system('clear')
                print('You try to run the opposite direction of the monster.')
                time.sleep(3)
                print('It starts to slither on the ground really fast.')
                time.sleep(2)
                os.system('clear')
                print('Megalopython: SSSSSSSSSSSSSSSSSSSSSSSSSSS!')
                time.sleep(2)

                print('It manages to get a good few circles around you.')
                time.sleep(4)
                print(
                    'And then the circles start to get smaller and smaller, and tighter and tighter... Until...'
                )

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #Stats option
            if choice == 3:
                showStats()
                continue

            #If the Megalopython runs out of health
            if Megalopython.currentHealth <= 0:
                os.system('clear')
                print(
                    'Megalopython: SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS!'
                )
                print('The Megalopython suddenly falls to the ground.')
                time.sleep(3)
                time.sleep(1)

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                             -_------_                        -'
                )
                print(
                    '-                        --------------                        -'
                )
                print(
                    '-                        ----------V V                         -'
                )
                print(
                    '-                      -------------                           -'
                )
                print(
                    '-                           -------------                      -'
                )
                print(
                    '-                     ---------------                          -'
                )
                print(
                    '-                    ------------                              -'
                )
                print(
                    '-                     --------------     --                    -'
                )
                print(
                    '-                   ------------       ---                     -'
                )
                print(
                    '-                      --------     -------                    -'
                )
                print(
                    '-                        -----------------                     -'
                )
                print(
                    '-                            --------                          -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ----                               -'
                )
                print(
                    '-                         --------                             -'
                )
                print(
                    '-                         - ---- -                             -'
                )
                print(
                    '-                           -  -                               -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(' __      _______ _____ _______ ____  _______     ___ ')
                print(' \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |')
                print('  \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |')
                print('   \ \/ /   | || |       | | | |  | |  _  / \   / | |')
                print('    \  /   _| || |____   | | | |__| | | \ \  | |  |_|')
                print('     \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)')

                time.sleep(5.5)

                storyline3()

            #If the player runs out of health
            if Player.currentHealth <= 0:
                os.system('clear')
                print('You had a good run...')
                time.sleep(3)
                print('But unfortunately, you endured one hit too many...')

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

            #Checks if monster_turn == 1, if it is equal to 1, the monster will attack. variable is set to 0 and player goes.
            global player_turn
            if player_turn <= 0:

                os.system('clear')

                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                             -O------0                        -'
                )
                print(
                    '-                        --------------                        -'
                )
                print(
                    '-                        ----------V V                         -'
                )
                print(
                    '-                      -------------                           -'
                )
                print(
                    '-                           -------------                      -'
                )
                print(
                    '-                     ---------------                          -'
                )
                print(
                    '-                    ------------                              -'
                )
                print(
                    '-                     --------------     --                    -'
                )
                print(
                    '-                   ------------       ---                     -'
                )
                print(
                    '-                      --------     -------                    -'
                )
                print(
                    '-                        -----------------                     -'
                )
                print(
                    '-                            --------                          -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                           ----                               -'
                )
                print(
                    '-                         --------                             -'
                )
                print(
                    '-                         - ---- -                             -'
                )
                print(
                    '-                           -  -                               -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '-                                                              -'
                )
                print(
                    '----------------------------------------------------------------'
                )

                time.sleep(0.4)
              
                os.system('clear')
              
                print(
                    '-----------------------------------------------------------------'
                )
                print(
                    '-                                                               -'
                )
                print(
                    f'-   {Megalopython.name} {Megalopython.currentHealth}/{Megalopython.maxHealth}'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '-                             -O------0                         -'
                )
                print(
                    '-                        --------------                         -'
                )
                print(
                    '-                        ----------V V                          -'
                )
                print(
                    '-                      -------------                            -'
                )
                print(
                    '-                           -------------                       -'
                )
                print(
                    '-                     ---------------                           -'
                )
                print(
                    '-                    ------------                               -'
                )
                print(
                    '-                     --------------                            -'
                )
                print(
                    '-                   ------------                                -'
                )
                print(
                    '-                      --------                                 -'
                )
                print(
                    '-                        --------                               -'
                )
                print(
                    '-                            --------                           -'
                )
                print(
                    '-                                 --------                      -'
                )
                print(
                    '-                                   -------                     -'
                )
                print(
                    f'-                           ----    -------                     '
                )
                print(
                    '-                        --------   -----                       -'
                )
                print(
                    '-                         - ---- -  ---                         -'
                )
                print(
                    '-                           -  -                                -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    f'-                  {Player.name}                               -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-  [1] Attack      -  [2] Run          -   [3] Stats            -'
                )
                print(
                    '-                  -                   -                        -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    f'-  Health: {Player.currentHealth}/ {Player.maxHealth}          -'
                )
                print(
                    f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}       -'
                )
                print(
                    '---------------------------------------------------------------- '
                )
              
                print('The megalopython whips its tail at you. It stings.')

                time.sleep(0.4)
                os.system('clear')

                print(
                    '-----------------------------------------------------------------'
                )
                print(
                    '-                                                               -'
                )
                print(
                    f'-   {Megalopython.name} {Megalopython.currentHealth}/{Megalopython.maxHealth}'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '-                             -O------0                         -'
                )
                print(
                    '-                        --------------                         -'
                )
                print(
                    '-                        ----------V V                          -'
                )
                print(
                    '-                      -------------                            -'
                )
                print(
                    '-                           -------------                       -'
                )
                print(
                    '-                     ---------------                           -'
                )
                print(
                    '-                    ------------                               -'
                )
                print(
                    '-                     --------------                            -'
                )
                print(
                    '-                   ------------                                -'
                )
                print(
                    '-                      --------                                 -'
                )
                print(
                    '-                        --------                               -'
                )
                print(
                    '-                            --------                           -'
                )
                print(
                    '-                                 --------                      -'
                )
                print(
                    '-                                   -------                     -'
                )
                print(
                    f'-                           ----    -------    -{Megalopython.attackDamage}'
                )
                print(
                    '-                        --------   -----                       -'
                )
                print(
                    '-                         - ---- -  ---                         -'
                )
                print(
                    '-                           -  -                                -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    f'-                  {Player.name}                               -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '-                                                               -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    '-  [1] Attack      -  [2] Run          -   [3] Stats            -'
                )
                print(
                    '-                  -                   -                        -'
                )
                print(
                    '----------------------------------------------------------------'
                )
                print(
                    f'-  Health: {Player.currentHealth}/ {Player.maxHealth}          -'
                )
                print(
                    f'-  Stamina: {Player.currentStamina}/ {Player.maxStamina}       -'
                )
                print(
                    '---------------------------------------------------------------- '
                )

                time.sleep(0.7)

                Player.currentHealth = Player.currentHealth - Megalopython.attackDamage
                print(f'You took {Megalopython.attackDamage} damage!')

                player_turn = 1

            #If the player runs out of stamina
            if Player.currentStamina <= 0:
                os.system('clear')
                print('You feel too tired to continue the fight.')
                time.sleep(2.5)
                print('No longer able to defend yourself...')

                print()
                print()
                print()
                print()
                print()

                print(' __     __           _____  _          _ _ ')
                print(' \ \   / /          |  __ \(_)        | | |')
                print('  \ \_/ /__  _   _  | |  | |_  ___  __| | |')
                print('   \   / _ \| | | | | |  | | |/ _ \/ _` | |')
                print('    | | (_) | |_| | | |__| | |  __/ (_| |_|')
                print('    |_|\___/ \__,_| |_____/|_|\___|\__,_(_)')

                sys.exit()

        except ValueError:
            print('Please enter a valid option.')


#Storyline part 4
def storyline4():

    print('----------------------------------------------------------------')
    print('                          You vs You                           -')
    print('----------------------------------------------------------------')

    os.system('clear')
    print(
        'You reach into your bag of items and grab a Pheonix Down. You use it.'
    )
    time.sleep(3)

    print('Healing character...')

    Player.currentStamina = Player.maxStamina
    Player.currentHealth = Player.maxHealth

    print("You feel replenished.")
    time.sleep(5)

    os.system('clear')
    print('...')
    time.sleep(3)
    print('There seems to be something in the distance. A shadowy figure.')
    time.sleep(1)
    print('...')
    time.sleep(4)
    print("It's a human.")
    time.sleep(1)
    print("The closer it gets to you, the more familiar the figure looks.")
    time.sleep(3)
    print('The figure looks exactly like you.')
    time.sleep(2.5)
    print("Only, of course, it can't actually be you, because you're you...")
    time.sleep(4)
    print("It looks just like you, but it is a far more sinister thing.")
    time.sleep(4)

    print('----------------------------------------------------------------')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                           ---*--             -')
    print('-    --*------              ----                               -')
    print('                          --------            --      --       -')
    print('-                         - ---- -                             -')
    print('-                           -  -                   ----*-      -')
    print('-        --*-                                                  -')
    print('-                       --*-                   -         -     -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                           ----                               -')
    print('                          --------                             -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    time.sleep(3.5)
    combatMenu_EvilSelf()


#Storyline part 3
def storyline3():
    os.system('clear')

    print('You try to catch your breath.')
    print('You lay down, leaning again a tree log...')
    time.sleep(4)
    print('Despite how lumpy the tree is, and how chilly the forest is...')
    print('Before you could stop yourself, you start to fall asleep...')

    print()
    print()
    print()

    print('Healing character...')

    Player.currentStamina = Player.maxStamina
    Player.currentHealth = Player.maxHealth

    os.system('clear')
    time.sleep(2)

    print('----------------------------------------------------------------')
    print('                      The Sentient Tree                        -')
    print('----------------------------------------------------------------')

    print(
        "It's now morning. You feel well rested. It's quiet... it almost feels peaceful."
    )
    time.sleep(3)
    print(
        "Despite that, you are still in this unpredictable nightmare of a forest. There is no time to have your guard down."
    )
    time.sleep(5)
    os.system('clear')
    print(
        'After about half an hour of wandering through the forest... you notice a tree.'
    )
    time.sleep(3)

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------                             -')
    print('-                      -------------                           -')
    print('-                     ---------------                          -')
    print('-                     ---------------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----                               -')
    print('                          --------                             -')
    print('-                         - ---- -                             -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    print("You: Funny looking tree. Heh.")
    print("You: It almost looks like it has arms...")
    time.sleep(3)
    print('It does. It does indeed.')
    time.sleep(2)
    os.system('clear')

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------                             -')
    print('-                      ----V---V----                           -')
    print('-                     ------vvv------                          -')
    print('-                     ------www------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----                               -')
    print('                          --------                             -')
    print('-                         - ---- -                             -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    time.sleep(1)
    os.system('clear')

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------      /---------------\      -')
    print('-                      ----V---V----    |  WHO ARE YOU? |      -')
    print('-                     ------vvv------  <----------------/      -')
    print('-                     ------www------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----                               -')
    print('                          --------                             -')
    print('-                         - ---- -                             -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    time.sleep(2.5)
    os.system('clear')

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------      /---------------\      -')
    print('-                      ----V---V----    |  WHO ARE YOU? |      -')
    print('-                     ------vvv------  <----------------/      -')
    print('-                     ------www------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----     /-----\                   -')
    print('-                         --------  <| ... |                   -')
    print('-                         - ---- -   \-----/                   -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    time.sleep(1.5)
    os.system('clear')

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------                             -')
    print('-                      ----V---V----                           -')
    print('-                     ------vvv------                          -')
    print('-                     ------www------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----       /----------------\      -')
    print('-                         --------    |  Huh? You can...|      -')
    print('-                         - ---- -    <----------------/       -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')

    time.sleep(1)
    os.system('clear')

    print('----------------------------------------------------------------')
    print('- ------                                                -----  -')
    print('-    --------------                          ------------      -')
    print('-     ----        --------------------------        ----       -')
    print('-     -------------      ---------     -------------           -')
    print('-                        ---------                             -')
    print('-                      ----V---V----                           -')
    print('-                     ------vvv------                          -')
    print('-                     ------www------                          -')
    print('-                     --- -------  ---                         -')
    print('-                    ---  -------  ---                         -')
    print('-                     --- ------- ---                          -')
    print('-                     --- ------- ---                          -')
    print('-                --------  ---  - -----------                  -')
    print('-                 ------ ------ -- -- ------------             -')
    print('-                   -------    ----- - ---                     -')
    print('-                                                              -')
    print('-                           ----     /-----------------------\ -')
    print("-                         --------   | I don't understand... | -")
    print('-                         - ---- -  <------------------------/ -')
    print('-                           -  -                               -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('-                                                              -')
    print('----------------------------------------------------------------')
    time.sleep(1)

    print('Before you can process the information, the tree attacks you.')
    time.sleep(2.5)
    combatMenu_tree()


#Storyline part 2
def storyline2():

    os.system('clear')
    print('You enter the forest...')
    time.sleep(4)
    print("It's very dark...")
    time.sleep(5)
    print('You light your torch.')

    os.system('clear')
    print('...')
    time.sleep(3)
    print('?: Hssssssssssssss...')
    time.sleep(2)
    os.system('clear')
    print('          __  __ ____  _    _  _____ _    _ _')
    print('    /\   |  \/  |  _ \| |  | |/ ____| |  | | |')
    print('   /  \  | \  / | |_) | |  | | (___ | |__| | |')
    print('  / /\ \ | |\/| |  _ <| |  | |\___ \|  __  | |')
    print(' / ____ \| |  | | |_) | |__| |____) | |  | |_|')
    print('/_/    \_\_|  |_|____/ \____/|_____/|_|  |_(_')

    time.sleep(2.5)
    combatMenu_megalopython()


#Storyline part 1
def storyline1():
    try:
        os.system('clear')
        print(
            '----------------------------------------------------------------')
        print(
            '                      Entering the Woods                       -')
        print(
            '----------------------------------------------------------------')
        time.sleep(3)
        print(
            'You are a gifted and highly-skilled mercenary. You arrived after a journey from the Northeast.'
        )
        time.sleep(4.5)
        print(
            'Now, here you are, standing before the deadly woods of the South West Lands.'
        )
        time.sleep(3)

        print(
            "Whenever an option comes up, you can type 's' to show your stats, health, and stamina."
        )

        while 1 == 1:
            print('[1] Walk in     [s] Stats')
            choice = input('Enter choice: ')

            if choice == '1':
                storyline2()
                break

            if choice == 's':
                showStats()
                continue

            if choice == 'S':
                showStats()
                continue

            else:
                print("Enter option '1' or 's'")
                continue

    except ValueError:
        print("Enter option '1' or 's'")


#Intro to game
def start():

    os.system('clear')

    print('In a world far, far away…')
    time.sleep(2)
    print(
        'A kingdom is run by an evil tyrant called Emperor Malice…'
    )
    time.sleep(3.5)
    print(
        'No outsiders dare to go near the forest surrounding the kingdom, the forest of Doom...'
    )
    time.sleep(3)
    print('Except for a lone wanderer...')
    time.sleep(3)
    print('Their name was…')

    userName = input('(Enter your name): ')
    Player.name = userName
    time.sleep(0.5)
    print(f'... {userName}!')
    print()

    gameStart = 1

    if gameStart == 1:
        storyline1()


#Allows the player to choose a point of the game to load
def checkpointload():
    while 1 == 1:
        try:

            print('----------------------------------------------------------')
            print('-                                                        -')
            print('-                  Load a Checkpoint                     -')
            print('-                                                        -')
            print('----------------------------------------------------------')
            print('-                -                    -                  -')
            print('- [1] Entering   -  [2] The Sentient  -  [3] You vs You  -')
            print('-   the Woods    -        Tree        -                  -')
            print('-                -                    -                  -')
            print('----------------------------------------------------------')
            print('-                                                        -')
            print('-                       Battles          [7] Back ->     -')
            print('-                                                        -')
            print('----------------------------------------------------------')
            print('-                -                    -                  -')
            print('[4] Megalopython -  [5] Tree          -  [6] Clone       -')
            print('-                -                    -                  -')
            print('----------------------------------------------------------')

            choice = int(input('Enter choice: '))

            if choice == 1:
                storyline1()

            if choice == 2:
                storyline3()

            if choice == 3:
                storyline4()

            if choice == 4:
                combatMenu_megalopython()

            if choice == 5:
                combatMenu_tree()

            if choice == 6:
                combatMenu_EvilSelf()

            if choice == 7:
                mainGameMenu()

            else:
                print('Please enter an option.')
                continue

        except ValueError:
            print('Please enter a number!')
            continue


#Main startup menu of the game
def mainGameMenu():

    print('------------------------------------------------------------')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-   _______  _______  _______  _______  _______ _________  -')
    print('-   (  ____ \(  ___  )(  ____ )(  ____ \(  ____ \\__   __/ -')
    print('-   | (    \/| (   ) || (    )|| (    \/| (    \/   ) (    -')
    print('-   | (__    | |   | || (____)|| (__    | (_____    | |    -')
    print('-   |  __)   | |   | ||     __)|  __)   (_____  )   | |    -')
    print('-   | (      | |   | || (\ (   | (            ) |   | |    -')
    print('-   | )      | (___) || ) \ \__| (____/\/\____) |   | |    -')
    print('-   |/       (_______)|/   \__/(_______/\_______)   )_(    -')
    print('-                                                          -')
    print('-                                                          -')
    print('- _________ _______ _________ _______  _        _______    -')
    print('- \__   __/(  ____ )\__   __/(  ___  )( \      (  ____ \   -)')
    print('-    ) (   | (    )|   ) (   | (   ) || (      | (    \/   -')
    print('-    | |   | (____)|   | |   | (___) || |      | (_____    -')
    print('-    | |   |     __)   | |   |  ___  || |      (_____  )   -')1
    print('-    | |   | (\ (      | |   | (   ) || |            ) |   -')
    print('-    | |   | ) \ \_____) (___| )   ( || (____/\/\____) |   -')
    print('-    )_(   |/   \__/\_______/|/     \|(_______/\_______)   -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-                                                          -')
    print('-        [1]    Start Game       [2]    Exit               -')
    print('-                                                          -')
    print('-           [3] Start from a chosen point                  -')
    print('-                                                          -')
    print('------------------------------------------------------------')

    try:

        gameStartup = int(input("Type '1' or '2' or '3' to continue: "))

        if gameStartup == 1:
            start()

        if gameStartup == 2:
            sys.exit()

        if gameStartup == 3:
            checkpointload()

        else:
            print('Please choose of the options above!')
            mainGameMenu()

    except ValueError:
        print('Please choose of the options above!')
        mainGameMenu()


mainGameMenu()


