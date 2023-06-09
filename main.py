import random
import sys
from os.path import exists

save_warn = False

def save_slot_check(saveno=4):
    global save_warn, save1, save2, save3
    if saveno == 1:
        if save1.read() != "":
            save_warn = True
    elif saveno == 2:
        if save2.read() != "":
            save_warn = True
    elif saveno == 3:
        if save3.read() != "":
            save_warn = True
    else:
        save_warn = False

materials = [0, 0, 0, 0, 0]

difficulty = ''

exists_save1 = exists("save1")
exists_save2 = exists("save2")
exists_save3 = exists("save3")

if exists_save1 is True and exists_save1 is True and exists_save1 is True:
    save1 = open("./save1.txt", "w+")
    save2 = open("./save2.txt", "w+")
    save3 = open("./save3.txt", "w+")
else:
    save1 = open("./save1.txt", "a+")
    save2 = open("./save2.txt", "a+")
    save3 = open("./save3.txt", "a+")

save1.seek(0)
save2.seek(0)
save3.seek(0)
# use save1.truncate(0) to clear save files
def save(save_slot):
    global materials, save_warn, save1, save2, save3
    if str(save_slot) == '1':
        save_slot_check(1)
        if save_warn == True:
            question = input("you will be overwriting a save with a game on it are you shure what you are doing is intendid? 'yes or 'no'")
            if question != "yes":
                interface_loop()
        if exists_save2 is True:
            save3 = open("./save3.txt", "w+")
        else:
            save3 = open("./save3.txt", "a+")
        save1.seek(0)
        savestring = [(str(str(materials[0]) + " \n")), (str(materials[1]) + " \n"), (str(materials[2]) + " \n"), (str(materials[3]) + " \n"), (str(materials[4]) + " \n")]
        save1.writelines(savestring)
        save1.close()
        if exists_save1 is True:
            save1 = open("./save1.txt", "w+")
        else:
            save1 = open("./save1.txt", "a+")
        print("game saved in save slot 1.")
    elif str(save_slot) == '2':
        save_slot_check(2)
        if save_warn == True:
            question = input("you will be overwriting a save with a game on it are you shure what you are doing is intendid? 'yes or 'no'")
            if question != "yes":
                interface_loop()
        if exists_save2 is True:
            save3 = open("./save3.txt", "w+")
        else:
            save3 = open("./save3.txt", "a+")
        save2.seek(0)
        savestring = [(str(str(materials[0]) + " \n")), (str(materials[1]) + " \n"), (str(materials[2]) + " \n"), (str(materials[3]) + " \n"), (str(materials[4]) + " \n")]
        save2.writelines(savestring)
        save2.close()
        if exists_save2 is True:
            save1 = open("./save2.txt", "w+")
        else:
            save1 = open("./save2.txt", "a+")
        print("game saved in save slot 2.")
    elif str(save_slot) == '3':
        save_slot_check(3)
        if save_warn == True:
            question = input("you will be overwriting a save with a game on it are you shure what you are doing is intendid? 'yes or 'no'")
            if question != "yes":
                interface_loop()
        if exists_save2 is True:
            save3 = open("./save3.txt", "w+")
        else:
            save3 = open("./save3.txt", "a+")
        save3.seek(0)
        savestring = [(str(str(materials[0]) + " \n")), (str(materials[1]) + " \n"), (str(materials[2]) + " \n"), (str(materials[3]) + " \n"), (str(materials[4]) + " \n")]
        save3.writelines(savestring)
        save3.close()
        if exists_save2 is True:
            save3 = open("./save3.txt", "w+")
        else:
            save3 = open("./save3.txt", "a+")
        print("game saved in save slot 3.")
    else:
        print("canceling")
   
def load_save(save_slot):
    global materials, save1, save2, save3
    if str(save_slot) == '1':
        save1.seek(0)
        save_slot_data = save1.readline(0)
        materials[0] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[1] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[2] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[3] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[4] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
    elif str(save_slot) == '2':
        save2.seek(0)
        save_slot_data = save2.readline(0)
        materials[0] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[1] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[2] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[3] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[4] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
    elif str(save_slot) == '3':
        save3.seek(0)
        save_slot_data = save3.readline(0)
        materials[0] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[1] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[2] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[3] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))
        materials[4] = int((save_slot_data[4].replace("'", "")).replace(" \n", ""))

tod = ['00000| ', '|00000', '0|0000 ', '00|000', '000|00', '0000|0']

def options():
    global materials, TOD
    print("""
----material levels----
    ==Wood:""")
    print("    =" + str(materials[0]))
    print("    =Food:")
    print("    =" + str(materials[1]))
    print("    =fire level:")
    print("    =" + str(materials[3]))
    print("    =Time Of Day:")
    print("    =" + str(TOD))
    print("    =you sleep when the Time of day gets to 7 or more.")
    print("""----what will you do?----
    = adventure
    = chop wood
    = hunt
    = stoke the fire
    = look auround
    = sleep
    = save and qut
    = save
    = load
----DO NOT RUN----
    =poop""")

# maximum materials: wood: 300 food: 400 gold: 70
# default materials: wood: 10 food: 10 fire: 5 gold: 0 location: 0
# for order of recources: wood, food, gold, fire, location
# lb = lil bebe lt = lil teen lp = lil papa
# BP = BIG PAPA TGH = TITAN GOD HYBRYD

def biomedifficulty(place=(materials[4])):
    global difficulty
    if place == 'forest':
        if difficulty == 'lb':
            elf_rng_lb()
        elif difficulty == 'lt':
            elf_rng_lt()
        elif dificulty == 'lp':
            elf_rng()
        elif difficulty == 'BP':
            elf_rng_BP()
        elif difficulty == 'TGH':
            elf_rng_TGH()
    elif place == 'swamp':
        if difficulty == 'lb':
            sTupID_kObalDS_lb()
        elif difficulty == 'lt':
            sTupID_kObalDS_lt()
        elif dificulty == 'lp':
            sTupID_kObalDS()
        elif difficulty == 'BP':
            sTupID_kObalDS_BP()
        elif difficulty == 'TGH':
            sTupID_kObalDS_TGH()
    elif place == 'mountin':
        if difficulty == 'lb':
            dwarf_rng_lb()
        elif difficulty == 'lt':
            dwarf_rng_lt()
        elif dificulty == 'lp':
            dwarf_rng()
        elif difficulty == 'BP':
            dwarf_rng_BP()
        elif difficulty == 'TGH':
            dwarf_rng_TGH()
    elif place == 'volcanoe':
        if difficulty == 'lb':
            Kranky_lb()
        elif difficulty == 'lt':
            Kranky_lt()
        elif dificulty == 'lp':
            Kranky()
        elif difficulty == 'BP':
            Kranky_BP()
        elif difficulty == 'TGH':
            Kranky_TGH()
    else:
        if difficulty == 'lb':
            home_lb()
        elif difficulty == 'lt':
            home_lt()
        elif dificulty == 'lp':
            Kranky()
        elif difficulty == 'BP':
            home_BP()
        elif difficulty == 'TGH':
            home_TGH()

def dificulty():
    global difficulty, materials
    if difficulty == 'lil bebe':
        difficulty = 'lb'
        materials = [1000, 1000, 1000, 100, 0]
    elif difficulty == 'lil teen':
        difficulty = 'lt'
        materials = [10, 10, 10, 5, 0]
    elif difficulty == 'lil papa':
        difficulty = "lp"
        materials = [5, 5, 5, 4, 2]
    elif difficulty == 'BIG PAPA':
        difficulty = "BP"
        materials = [3, 3, 0, 3, 4]
    elif difficulty == 'TITAN GOD HYBRYD':
        difficulty = "TGH"
        materials = [1, 1, 0, 1, 3]
    else:
        print("""difficulty options:
        lil bebe
        lil teen
        lil papa
        BIG PAPA
        TITAN GOD HYBRYD""")
        difficulty = str(input("chose your difficulty: "))
        dificulty()
dificulty()

def rng_difficulty(function_location):
    global rng
    if difficulty == 'lb' and function_location == 'food':
        rng = random.randint(5, 10)
    elif difficulty == 'lt' and function_location == 'food':
        rng = random.randint(4, 7)
    elif difficulty == 'lp' and function_location == 'food':
        rng = random.randint(2, 4)
    elif difficulty == 'BP' and function_location == 'food':
        rng = random.randint(2, 3)
    elif difficulty == 'TGH' and function_location == 'food':
        rng = random.randint(1, 2)
    elif difficulty == 'lb' and function_location == 'wood':
        rng = random.randint(5, 10)
    elif difficulty == 'lt' and function_location == 'wood':
        rng = random.randint(4, 7)
    elif difficulty == 'lp' and function_location == 'wood':
        rng = random.randint(3, 5)
    elif difficulty == 'BP' and function_location == 'wood':
        rng = random.randint(2, 3)
    elif difficulty == 'TGH' and function_location == 'wood':
        rng = random.randint(1, 2)
    elif difficulty == 'lb' and function_location == 'wood':
        rng = random.randint(5, 10)
    elif difficulty == 'lt' and function_location == 'wood':
        rng = random.randint(4, 7)
    elif difficulty == 'lp' and function_location == 'wood':
        rng = random.randint(3, 5)
    elif difficulty == 'BP' and function_location == 'wood':
        rng = random.randint(2, 3)
    elif difficulty == 'TGH' and function_location == 'wood':
        rng = random.randint(1, 2)
    elif difficulty == 'lb' and function_location == 'wood':
        rng = random.randint(5, 10)
    elif difficulty == 'lt' and function_location == 'wood':
        rng = random.randint(4, 7)
    elif difficulty == 'lp' and function_location == 'wood':
        rng = random.randint(3, 5)
    elif difficulty == 'BP' and function_location == 'wood':
        rng = random.randint(2, 3)
    elif difficulty == 'TGH' and function_location == 'wood':
        rng = random.randint(1, 2)
    elif difficulty == 'lb' and function_location == 'fire':
        rng = random.randint(5, 10)
    elif difficulty == 'lt' and function_location == 'fire':
        rng = random.randint(4, 7)
    elif difficulty == 'lp' and function_location == 'fire':
        rng = random.randint(3, 5)
    elif difficulty == 'BP' and function_location == 'fire':
        rng = random.randint(2, 3)
    elif difficulty == 'TGH' and function_location == 'fire':
        rng = random.randint(1, 2)

# 1 = mountins, 2 = forest, 3 = volcanoe, 4 = swamp, 0 = base_camp

question = ''
kill = False
location = 0
day = 1
score = 0
TOD = 0

ho = 'are home to the dwarves?'
mo = ' of the mountan.'
h = ', adventure'

def modify_materials(material, quantity):
    global materials
    if material == 'wood':
        materials[0] = quantity
    elif material == 'food':
        materials[1] = quantity
    elif material == 'gold':
        materials[2] = quantity
    elif material == 'fire':
        materials[3] = quantity
    elif material == 'location':
        materials[4] = quantity

def home_lb():
    global materials
    piss = 1
    if piss == 1:
        trade = random.randint(1, 3)
        if trade == 1:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 1 food for 4 wood
                2. 2 food for 8 wood
                3. 3 food for 16 wood
                witch one do you chose.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 1:
                        print('sold!')
                        modify_materials('food', (materials[1] - 1))
                        modify_materials('wood', (materials[0] + 4))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 2:
                        print('sold!')
                        modify_materials('food', (materials[1] - 2))
                        modify_materials('wood', (materials[0] + 8))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 3:
                        print('sold!')
                        modify_materials('food', (materials[1] - 3))
                        modify_materials('wood', (materials[0] + 16))
                else:
                    print('nevermind then.')
        elif trade == 2:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 6 food for 32 wood
                2. 7 food for 40 wood
                3. 8 food for 48 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 6:
                        print('sold!')
                        modify_materials('food', (materials[1] - 6))
                        modify_materials('wood', (materials[0] + 32))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 7:
                        print('sold!')
                        modify_materials('food', (materials[1] - 7))
                        modify_materials('wood', (materials[0] + 40))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 8:
                        print('sold!')
                        modify_materials('food', (materials[1] - 8))
                        modify_materials('wood', (materials[0] + 48))
                else:
                    print('nevermind then.')
        elif trade == 3:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 9 food for 64 wood
                2. 10 food for 128 wood
                3. 11 food for 256 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 9:
                        print('sold!')
                        modify_materials('food', (materials[1] - 9))
                        modify_materials('wood', (materials[0] + 64))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 10:
                        print('sold!')
                        modify_materials('food', (materials[1] - 10))
                        modify_materials('wood', (materials[0] + 128))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 11:
                        print('sold!')
                        modify_materials('food', (materials[1] - 11))
                        modify_materials('wood', (materials[0] + 256))
                    else:
                        print('not enough food!')
                else:
                    print('nevermind then.')

def home_lt():
    global materials
    injury = random.randint(1, 2)
    if injury == 1:
        injury = random.randint(0, 5)
        if injury == 0:
            print('Some bandits come and steel youre wood')
            modify_materials('wood', (materials[0] - 2))
            print('- 3 to wood')
        elif injury == 1:
            print('Some bandidts come and steel your food.')
            modify_materials('food', (materials[1] - 2))
            print('- 3 to food')
        elif injury == 2:
            print('Some bandits come and steel your recouces')
            modify_materials('wood', (materials[0] - 2))
            modify_materials('food', (materials[1] - 2))
            print('- 2 to wood and food')
        elif injury == 3:
            print('Some travelers come and steel your food.')
            modify_materials('food', (materials[1] - 2))
            print('- 3 to food')
        elif injury == 4:
            print('Some travelers come and stell your wood')
            modify_materials('wood', (materials[0] - 2))
            print('- 3 to wood')
        elif injury == 5:
            print('Some travelers come and steel your recouces')
            modify_materials('wood', (materials[0] - 2))
            modify_materials('food', (materials[1] - 2))
            print('- 3 to wood and food')
    else:
        trade = random.randint(1, 3)
        if trade == 1:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 1 food for 2 wood
                2. 2 food for 4 wood
                3. 3 food for 6 wood
                witch one do you chose.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 1:
                        print('sold!')
                        modify_materials('food', (materials[1] - 1))
                        modify_materials('wood', (materials[0] + 2))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 2:
                        print('sold!')
                        modify_materials('food', (materials[1] - 2))
                        modify_materials('wood', (materials[0] + 6))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 3:
                        print('sold!')
                        modify_materials('food', (materials[1] - 3))
                        modify_materials('wood', (materials[0] + 9))
                else:
                    print('nevermind then.')
        elif trade == 2:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 6 food for 12 wood
                2. 7 food for 14 wood
                3. 8 food for 16 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 6:
                        print('sold!')
                        modify_materials('food', (materials[1] - 6))
                        modify_materials('wood', (materials[0] + 12))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 7:
                        print('sold!')
                        modify_materials('food', (materials[1] - 7))
                        modify_materials('wood', (materials[0] + 14))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 8:
                        print('sold!')
                        modify_materials('food', (materials[1] - 8))
                        modify_materials('wood', (materials[0] + 16))
                else:
                    print('nevermind then.')
        elif trade == 3:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 9 food for 18 wood
                2. 10 food for 20 wood
                3. 11 food for 22 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 9:
                        print('sold!')
                        modify_materials('food', (materials[1] - 9))
                        modify_materials('wood', (materials[0] + 18))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 10:
                        print('sold!')
                        modify_materials('food', (materials[1] - 10))
                        modify_materials('wood', (materials[0] + 20))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 11:
                        print('sold!')
                        modify_materials('food', (materials[1] - 11))
                        modify_materials('wood', (materials[0] + 22))
                    else:
                        print('not enough food!')
                else:
                    print('nevermind then.')

def home_BP():
    global materials
    injury = random.randint(1, 2)
    if injury == 1:
        injury = random.randint(0, 5)
        if injury == 0:
            print('Some bandits come and steel youre wood')
            modify_materials('wood', (materials[0] - 4))
            print('- 3 to wood')
        elif injury == 1:
            print('Some bandidts come and steel your food.')
            modify_materials('food', (materials[1] - 4))
            print('- 3 to food')
        elif injury == 2:
            print('Some bandits come and steel your recouces')
            modify_materials('wood', (materials[0] - 4))
            modify_materials('food', (materials[1] - 4))
            print('- 2 to wood and food')
        elif injury == 3:
            print('Some travelers come and steel your food.')
            modify_materials('food', (materials[1] - 4))
            print('- 3 to food')
        elif injury == 4:
            print('Some travelers come and stell your wood')
            modify_materials('wood', (materials[0] - 4))
            print('- 3 to wood')
        elif injury == 5:
            print('Some travelers come and steel your recouces')
            modify_materials('wood', (materials[0] - 4))
            modify_materials('food', (materials[1] - 4))
            print('- 3 to wood and food')
    else:
        trade = random.randint(1, 3)
        if trade == 1:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 1 food for 1 wood
                2. 2 food for 2 wood
                3. 3 food for 3 wood
                witch one do you chose.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 1:
                        print('sold!')
                        modify_materials('food', (materials[1] - 1))
                        modify_materials('wood', (materials[0] + 1))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 2:
                        print('sold!')
                        modify_materials('food', (materials[1] - 2))
                        modify_materials('wood', (materials[0] + 2))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 3:
                        print('sold!')
                        modify_materials('food', (materials[1] - 3))
                        modify_materials('wood', (materials[0] + 3))
                else:
                    print('nevermind then.')
        elif trade == 2:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 6 food for 6 wood
                2. 7 food for 7 wood
                3. 8 food for 8 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 6:
                        print('sold!')
                        modify_materials('food', (materials[1] - 6))
                        modify_materials('wood', (materials[0] + 6))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 7:
                        print('sold!')
                        modify_materials('food', (materials[1] - 7))
                        modify_materials('wood', (materials[0] + 7))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 8:
                        print('sold!')
                        modify_materials('food', (materials[1] - 8))
                        modify_materials('wood', (materials[0] + 8))
                else:
                    print('nevermind then.')
        elif trade == 3:
            print('some travelers want to trade.')
            print('do you accept? ("yes" or "no")')
            ask = str(input('> '))
            if ask == 'yes':
                print('''deals:
                1. 9 food for 9 wood
                2. 10 food for 10 wood
                3. 11 food for 11 wood

                witch one.''')
                ask = str(input('> '))
                if ask == '1':
                    if materials[1] >= 9:
                        print('sold!')
                        modify_materials('food', (materials[1] - 9))
                        modify_materials('wood', (materials[0] + 9))
                    else:
                        print('not enogh food.')
                elif ask == '2':
                    if materials[1] >= 10:
                        print('sold!')
                        modify_materials('food', (materials[1] - 10))
                        modify_materials('wood', (materials[0] + 10))
                    else:
                        print('not enough food.')
                elif ask == '3':
                    if materials[1] >= 11:
                        print('sold!')
                        modify_materials('food', (materials[1] - 11))
                        modify_materials('wood', (materials[0] + 11))
                    else:
                        print('not enough food!')
                else:
                    print('nevermind then.')

def home_TGH():
    global materials
    injury = random.randint(1, 2)
    if injury == 1:
        injury = random.randint(0, 5)
        if injury == 0:
            print('Some bandits come and steel youre wood')
            modify_materials('wood', (materials[0] - 10))
            print('- 10 to wood')
        elif injury == 1:
            print('Some bandidts come and steel your food.')
            modify_materials('food', (materials[1] - 10))
            print('- 10 to food')
        elif injury == 2:
            print('Some bandits come and steel your recouces')
            modify_materials('wood', (materials[0] - 10))
            modify_materials('food', (materials[1] - 10))
            print('- 10 to wood and food')
        elif injury == 3:
            print('Some travelers come and steel your food.')
            modify_materials('food', (materials[1] - 10))
            print('- 10 to food')
        elif injury == 4:
            print('Some travelers come and stell your wood')
            modify_materials('wood', (materials[0] - 10))
            print('- 10 to wood')
        elif injury == 5:
            print('Some travelers come and steel your recouces')
            modify_materials('wood', (materials[0] - 10))
            modify_materials('food', (materials[1] - 10))
            print('- 10 to wood and food')
    else:
        injury = random.randint(0, 5)
        if injury == 0:
            print('Some bandits come and steel youre wood')
            modify_materials('wood', (materials[0] - 20))
            print('- 20 to wood')
        elif injury == 1:
            print('Some bandidts come and steel your food.')
            modify_materials('food', (materials[1] - 20))
            print('- 20 to food')
        elif injury == 2:
            print('Some bandits come and steel your recouces')
            modify_materials('wood', (materials[0] - 20))
            modify_materials('food', (materials[1] - 20))
            print('- 20 to wood and food')
        elif injury == 3:
            print('Some travelers come and steel your food.')
            modify_materials('food', (materials[1] - 20))
            print('- 20 to food')
        elif injury == 4:
            print('Some travelers come and stell your wood')
            modify_materials('wood', (materials[0] - 20))
            print('- 20 to wood')
        elif injury == 5:
            print('Some travelers come and steel your recouces')
            modify_materials('wood', (materials[0] - 20))
            modify_materials('food', (materials[1] - 20))
            print('- 20 to wood and food')

def elf_rng_lb():
    global materials
    rng = random.randint(1, 2)
    if rng == 1:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 1 wood for 3 gold
            2. 2 wood for 4 gold
            3. 3 wood for 5 gold

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[0] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 1))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[0] >= 6:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 2))
                    modify_materials('gold', (materials[2] + 4))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[0] >= 9:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 3))
                    modify_materials('gold', (materials[2] + 5))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 2:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 0 gold for 3 food
            2. 1 gold for 6 food
            3. 2 gold for 9 food

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('food', (materials[1] + 3))
                    modify_materials('gold', (materials[2] - 0))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('food', (materials[1] + 6))
                    modify_materials('gold', (materials[2] - 1))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[2] >= 3:
                    print('sold!')
                    modify_materials('food', (materials[0] + 9))
                    modify_materials('gold', (materials[2] - 2))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')

def elf_rng_lt():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 3 wood for 1 gold
            2. 6 wood for 2 gold
            3. 9 wood for 3 gold

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[0] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 3))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[0] >= 6:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 6))
                    modify_materials('gold', (materials[2] + 2))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[0] >= 9:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 9))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 2:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 1 gold for 3 food
            2. 2 gold for 6 food
            3. 3 gold for 9 food

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 3))
                    modify_materials('gold', (materials[2] - 1))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 6))
                    modify_materials('gold', (materials[2] - 2))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[2] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 9))
                    modify_materials('gold', (materials[2] - 3))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 3:
        rng == random.randint(1, 3)
        if rng == 1:
            print('some goblins steel your wood.')
            modify_materials('wood', (materials[0] - 2))
        elif rng == 2:
            print('some goblins steel your food')
            modify_materials('food', (materials[1] - 2))
        elif rng == 3:
            print('some goblins steel youre food.')
            modify_materials('food', (materials[1] - 1))
            modify_materials('wood', (materials[0] - 1))

def elf_rng_BP():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 4 wood for 0 gold
            2. 7 wood for 1 gold
            3. 10 wood for 2 gold

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[0] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 4))
                    modify_materials('gold', (materials[2] + 0))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[0] >= 6:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 7))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[0] >= 9:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 10))
                    modify_materials('gold', (materials[2] + 2))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 2:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 2 gold for 3 food
            2. 3 gold for 6 food
            3. 4 gold for 9 food

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 3))
                    modify_materials('gold', (materials[2] - 2))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 6))
                    modify_materials('gold', (materials[2] - 3))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[2] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 9))
                    modify_materials('gold', (materials[2] - 4))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 3:
        rng == random.randint(1, 3)
        if rng == 1:
            print('some goblins steel your wood.')
            modify_materials('wood', (materials[0] - 4))
        elif rng == 2:
            print('some goblins steel your food')
            modify_materials('food', (materials[1] - 4))
        elif rng == 3:
            print('some goblins steel youre food.')
            modify_materials('food', (materials[1] - 3))
            modify_materials('wood', (materials[0] - 3))

def elf_rng_TGH():
    global materials
    rng = random.randint(3, 3)
    if rng == 3:
        rng == random.randint(1, 3)
        if rng == 1:
            print('some goblins steel your wood.')
            modify_materials('wood', (materials[0] - 6))
        elif rng == 2:
            print('some goblins steel your food')
            modify_materials('food', (materials[1] - 6))
        elif rng == 3:
            print('some goblins steel youre food.')
            modify_materials('food', (materials[1] - 8))
            modify_materials('wood', (materials[0] - 8))

def sTupID_kObalDS_lb():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        # trade food
        print('the kobalds want to trade with you.')
        print('do you acept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 1 food for 3 gold
            2. 2 food for 4 gold
            3. 3 food for 5 gold

            witch one do you do?''')
            question = str(input('> '))
            if question == '1':
                if materials[1] >= 3:
                    print('sold!')
                    modify_materials('food', (materials[1] - 1))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enough recources.')
            elif question == '2':
                if materials[1] >= 6:
                    print('sold!')
                    modify_materials('food', (materials[1] - 2))
                    modify_materials('gold', (materials[2] + 4))
                else:
                    print('not enough recources.')
            elif question == '3':
                if materials[1] >= 9:
                    print('sold!')
                    modify_materials('food', (materials[1] - 3))
                    modify_materials('gold', (materials[2] + 5))
                else:
                    print('not enough recources.')
            else:
                print('nevermind then')
        else:
            print('never mind')

def sTupID_kObalDS_lt():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        # trade food
        print('the kobalds want to trade with you.')
        print('do you acept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 2 food for 2 gold
            2. 3 food for 3 gold
            3. 6 food for 4 gold

            witch one do you do?''')
            question = str(input('> '))
            if question == '1':
                if materials[1] >= 3:
                    print('sold!')
                    modify_materials('food', (materials[1] - 2))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enough recources.')
            elif question == '2':
                if materials[1] >= 6:
                    print('sold!')
                    modify_materials('food', (materials[1] - 3))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enough recources.')
            elif question == '3':
                if materials[1] >= 9:
                    print('sold!')
                    modify_materials('food', (materials[1] - 6))
                    modify_materials('gold', (materials[2] + 4))
                else:
                    print('not enough recources.')
            else:
                print('nevermind then')
        else:
            print('never mind')
    elif rng == 2:
        print('some kobalds stole your food.')
        modify_materials('food', (materials[1] - 2))
    elif rng == 3:
        print('some kobalds stole your food.')
        modify_materials('wood', (materials[0] - 2))

def sTupID_kObalDS_BP():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        # trade food
        print('the kobalds want to trade with you.')
        print('do you acept?')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 4 food for 1 gold
            2. 7 food for 2 gold
            3. 10 food for 3 gold

            witch one do you do?''')
            question = str(input('> '))
            if question == '1':
                if materials[1] >= 3:
                    print('sold!')
                    modify_materials('food', (materials[1] - 4))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enough recources.')
            elif question == '2':
                if materials[1] >= 6:
                    print('sold!')
                    modify_materials('food', (materials[1] - 7))
                    modify_materials('gold', (materials[2] + 2))
                else:
                    print('not enough recources.')
            elif question == '3':
                if materials[1] >= 9:
                    print('sold!')
                    modify_materials('food', (materials[1] - 10))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enough recources.')
            else:
                print('nevermind then')
        else:
            print('never mind')
    elif rng == 2:
        print('some kobalds stole your food.')
        modify_materials('food', (materials[1] - 4))
    elif rng == 3:
        print('some kobalds stole your food.')
        modify_materials('wood', (materials[0] - 4))

def sTupID_kObalDS_TGH():
    global materials
    rng = random.randint(2, 3)
    if rng == 2:
        print('some kobalds stole your food.')
        modify_materials('food', (materials[1] - 10))
    elif rng == 3:
        print('some kobalds stole your food.')
        modify_materials('wood', (materials[0] - 10))

def Kranky_lb():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('some fire elementals burn your wood.')
        modify_materials('wood', (materials[0] - 1))
    elif rng == 2:
        print('some fire elementals burn your food.')
        modify_materials('food', (materials[1] - 1))
    elif rng == 3:
        print('some fire elementals burn your food and the wood')
        modify_materials('food', (materials[1] - 1))
        modify_materials('wood', (materials[0] - 1))

def Kranky_lt():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('some fire elementals burn your wood.')
        modify_materials('wood', (materials[0] - 2))
    elif rng == 2:
        print('some fire elementals burn your food.')
        modify_materials('food', (materials[1] - 2))
    elif rng == 3:
        print('some fire elementals burn your food and the wood')
        modify_materials('food', (materials[1] - 2))
        modify_materials('wood', (materials[0] - 2))

def Kranky_BP():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('some fire elementals burn your wood.')
        modify_materials('wood', (materials[0] - 3))
    elif rng == 2:
        print('some fire elementals burn your food.')
        modify_materials('food', (materials[1] - 3))
    elif rng == 3:
        print('some fire elementals burn your food and the wood')
        modify_materials('food', (materials[1] - 3))
        modify_materials('wood', (materials[0] - 3))

def Kranky_TGH():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('some fire elementals burn your wood.')
        modify_materials('wood', (materials[0] - 5))
    elif rng == 2:
        print('some fire elementals burn your food.')
        modify_materials('food', (materials[1] - 5))
    elif rng == 3:
        print('some fire elementals burn your food and the wood')
        modify_materials('food', (materials[1] - 5))
        modify_materials('wood', (materials[0] - 5))

def dwarf_rng_lb():
    global materials
    trade = random.randint(1, 3)
    if trade == 1:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        deal = str(input('> '))
        if deal == 'Y':
            print('''Deals:
            1. 1 gold for 6 food
            2. 1 gold for 9 wood
            3. 1 wood for 10 gold
            4. 1 food for 10 gold

            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 9))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 1:
                    modify_materials('gold', (materials[2] + 10))
                    modify_materials('wood', (materials[0] - 1))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 1:
                    modify_materials('gold', (materials[2] + 10))
                    modify_materials('food', (materials[1] - 1))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
        else:
            print('nevermind then.')
    elif trade == 2:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 1 gold for 8 food
            2. 1 gold for 8 wood
            3. 2 wood for 10 gold
            4. 2 food for 10 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 10))
                    modify_materials('wood', (materials[0] - 1))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('food', (materials[1] - 10))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
    elif trade == 3:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 1 gold for 8 food
            2. 1 gold for 8 wood
            3. 2 wood for 10 gold
            4. 2 food for 10 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 3:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 10))
                    modify_materials('wood', (materials[0] - 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[2] >= 6:
                    modify_materials('gold', (materials[2] + 10))
                    modify_materials('food', (materials[1] - 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')

def dwarf_rng_lt():
    global materials
    trade = random.randint(1, 3)
    if trade == 1:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        deal = str(input('> '))
        if deal == 'Y':
            print('''Deals:
            1. 1 gold for 3 food
            2. 1 gold for 3 wood
            3. 3 wood for 1 gold
            4. 3 food for 1 gold

            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('wood', (materials[0] - 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('food', (materials[1] - 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
        else:
            print('nevermind then.')
    elif trade == 2:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 1 gold for 8 food
            2. 1 gold for 8 wood
            3. 2 wood for 10 gold
            4. 2 food for 10 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('food', (materials[1] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('wood', (materials[0] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('wood', (materials[0] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('food', (materials[1] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
    elif trade == 3:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 2 gold for 8 food
            2. 2 gold for 8 wood
            3. 3 wood for 10 gold
            4. 3 food for 10 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 3:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('food', (materials[1] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('wood', (materials[0] + 8))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 3))
                    modify_materials('wood', (materials[0] - 10))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[2] >= 6:
                    modify_materials('gold', (materials[2] + 3))
                    modify_materials('food', (materials[1] - 10))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')

def dwarf_rng_BP():
    global materials
    trade = random.randint(1, 3)
    if trade == 1:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        deal = str(input('> '))
        if deal == 'Y':
            print('''Deals:
            1. 1 gold for 2 food
            2. 1 gold for 2 wood
            3. 2 wood for 1 gold
            4. 2 food for 1 gold

            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('wood', (materials[0] - 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('food', (materials[1] - 2))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
        else:
            print('nevermind then.')
    elif trade == 2:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 1 gold for 4 food
            2. 1 gold for 4 wood
            3. 2 wood for 1 gold
            4. 2 food for 1 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('wood', (materials[0] - 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 6:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('food', (materials[1] - 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
    elif trade == 3:
        print('some dawrves want to trade ')
        print('do you acept? ("yes" or "no")')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 2 gold for 4 food
            2. 2 gold for 4 wood
            3. 3 wood for 1 gold
            4. 3 food for 1 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 3:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('food', (materials[1] + 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('wood', (materials[0] + 4))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 3))
                    modify_materials('wood', (materials[0] - 1))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[2] >= 6:
                    modify_materials('gold', (materials[2] + 3))
                    modify_materials('food', (materials[1] - 1))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')

def dwarf_rng_TGH():
    rng = random.randint(1, 4)
    if rng == 1:
        print("the deamon dwarves have stolen your food!")
        print("-20 to your food pile.")
        modify_materials('food', (materials[1] - 20))
    elif rng == 2:
        print("the deamon dwarves have burned your wood!")
        print("-20 to your wood pile.")
        modify_materials('wood', (materials[0] - 20))
    elif rng == 3:
        print("the deamon dwarves have stolen your food and burned your wood!")
        print("-20 to your food and wood pile.")
        modify_materials('food', (materials[1] - 20))
        modify_materials('wood', (materials[0] - 20))
    elif rng == 4:
        print('you have to poo!')
        print("- 40 to wood and food!")
        modify_materials('wood', (materials[0] - 40))
        modify_materials('food', (materials[1] - 40))

wood_level = 0
food_level = 0
wood_count = 0
food_count = 0

def foodd():
    global materials, TOD, food_level, food_count
    if materials[1] <= 200:
        TOD = TOD + 2
        rng = random.randint((2 + food_level), (4 + food_level))
        print("you get " + str(rng) + " more food!")
        modify_materials('food', (materials[1] + rng))
        food_count = food_count + 2
        if food_count >= 10:
            food_count = 0
            food_level = food_level + 1

def woodd():
    global materials, TOD, wood_level, wood_count
    if materials[0] <= 200:
        TOD = TOD + 3
        rng = random.randint((3 + wood_level), (5 + wood_level))
        print("you get " + str(rng) + " more wood!")
        modify_materials('wood', (materials[0] + rng))
        wood_count = wood_count + 2
        if wood_count >= 10:
            wood_count = 0
            wood_level == wood_level + 1

def checkrecources():
    global materials
    if materials[1] < 0:
        materials[1] = 0
    if materials[0] < 0:
        materials[0] = 0
    if materials[2] < 0:
        materials[2] = 0
    if materials[1] < 0:
        materials[1] = 0
    if materials[0] < 0:
        materials[0] = 0
    if materials[2] < 0:
        materials[2] = 0

def elf_rng():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('the elfen city wuld like to bargen with you.')
        print('do you accept? ("yes" or "no")')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 3 wood for 1 gold
            2. 6 wood for 2 gold
            3. 9 wood for 3 gold

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[0] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 3))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[0] >= 6:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 6))
                    modify_materials('gold', (materials[2] + 2))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[0] >= 9:
                    print('sold!')
                    modify_materials('wood', (materials[0] - 9))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 2:
        print('the elfen city would like to bargen with you.')
        print('do you accept? ("yes" or "no")')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 1 gold for 3 food
            2. 2 gold for 6 food
            3. 3 gold for 9 food

            what do you buy.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 3))
                    modify_materials('gold', (materials[2] - 1))
                else:
                    print('not enogh wood.')
            elif question == '2':
                if materials[2] >= 2:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 6))
                    modify_materials('gold', (materials[2] - 2))
                else:
                    print('not enogh wood.')
            elif question == '3':
                if materials[2] >= 3:
                    print('sold!')
                    modify_materials('wood', (materials[0] + 9))
                    modify_materials('gold', (materials[2] - 3))
                else:
                    print('not enogh wood.')
            else:
                print('nevermind then.')
    elif rng == 3:
        rng == random.randint(1, 3)
        if rng == 1:
            print('some goblins steel your wood.')
            modify_materials('wood', (materials[0] - 3))
        elif rng == 2:
            print('some goblins steel your food')
            modify_materials('food', (materials[1] - 3))
        elif rng == 3:
            print('some goblins steel youre food.')
            modify_materials('food', (materials[1] - 2))
            modify_materials('wood', (materials[0] - 2))

def sTupID_kObalDS():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        # trade food
        print('the kobalds want to trade with you.')
        print('do you acept? ("yes" or "no")')
        question = str(input('> '))
        if question == 'y':
            print('''deals:
            1. 3 food for 1 gold
            2. 6 food for 2 gold
            3. 9 food for 3 gold

            witch one do you do?''')
            question = str(input('> '))
            if question == '1':
                if materials[1] >= 3:
                    print('sold!')
                    modify_materials('food', (materials[1] - 3))
                    modify_materials('gold', (materials[2] + 1))
                else:
                    print('not enough recources.')
            elif question == '2':
                if materials[1] >= 6:
                    print('sold!')
                    modify_materials('food', (materials[1] - 6))
                    modify_materials('gold', (materials[2] + 2))
                else:
                    print('not enough recources.')
            elif question == '3':
                if materials[1] >= 9:
                    print('sold!')
                    modify_materials('food', (materials[1] - 9))
                    modify_materials('gold', (materials[2] + 3))
                else:
                    print('not enough recources.')
            else:
                print('nevermind then')
        else:
            print('never mind')
    elif rng == 2:
        print('some kobalds stole your food.')
        modify_materials('food', (materials[1] - 3))
    elif rng == 3:
        print('some kobalds stole your food.')
        modify_materials('wood', (materials[0] - 3))

def Kranky():
    global materials
    rng = random.randint(1, 3)
    if rng == 1:
        print('some fire elementals burn your wood.')
        modify_materials('wood', (materials[0] - 3))
    elif rng == 2:
        print('some fire elementals burn your food.')
        modify_materials('food', (materials[1] - 2))
    elif rng == 3:
        print('some fire elementals burn your food and the wood')
        modify_materials('food', (materials[1] - 2))
        modify_materials('wood', (materials[0] - 2))

def camp_events():
    print("piss")

def dwarf_rng():
    global materials
    trade = random.randint(1, 3)
    if trade == 1:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        deal = str(input('> '))
        if deal == 'Y':
            print('''Deals:
            1. 1 gold for 3 food
            2. 1 gold for 3 wood
            3. 3 wood for 1 gold
            4. 3 food for 1 gold

            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('food', (materials[1] + 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 1:
                    modify_materials('gold', (materials[2] - 1))
                    modify_materials('wood', (materials[0] + 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('wood', (materials[0] - 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 3:
                    modify_materials('gold', (materials[2] + 1))
                    modify_materials('food', (materials[1] - 3))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
        else:
            print('nevermind then.')
    elif trade == 2:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 2 gold for 6 food
            2. 2 gold for 6 wood
            3. 6 wood for 2 gold
            4. 6 food for 2 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('food', (materials[1] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('wood', (materials[0] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('wood', (materials[0] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[1] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('food', (materials[1] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')
    elif trade == 3:
        print('some dawrves want to trade ')
        print('do you acept?')
        print('Y or N')
        trade = str(input('> '))
        if trade == 'Y':
            print('''Deals:
            1. 2 gold for 6 food
            2. 2 gold for 6 wood
            3. 6 wood for 2 gold
            4. 6 food for 2 gold
            Witch one do you accept?
            chose: 1, 2, 3, 4. For deals.''')
            question = str(input('> '))
            if question == '1':
                if materials[2] >= 3:
                    modify_materials('gold', (materials[2] - 3))
                    modify_materials('food', (materials[1] + 9))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '2':
                if materials[2] >= 2:
                    modify_materials('gold', (materials[2] - 2))
                    modify_materials('wood', (materials[0] + 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '3':
                if materials[0] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('wood', (materials[0] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            elif question == '4':
                if materials[2] >= 6:
                    modify_materials('gold', (materials[2] + 2))
                    modify_materials('food', (materials[1] - 6))
                    print('Sold!')
                else:
                    print("You don't have the materials.")
            else:
                print('Nevermind then.')

def adventure():
    global materials, ho, mo
    print('directions: North, South, East, West')
    direction = str(input('Direction: '))
    if direction == 'North':
        if materials[1] >= 50 and materials[0] >= 45:
            # mountans w dwarves
            print('Wuld you like to go over to the mountans thab nt ' + ho)
            option = str(input('> '))
            if option == 'Yes':
                modify_materials('location', 1)
                modify_materials('fire', 5)
                print('As you finish the climb up the major parts' + mo)
                print('You dicide to set up camp.')
        else:
            print('you do not have enough wood or/and food')
            print('''min wood: 45.
            min food: 50''')
    elif direction == 'South':
        if materials[1] >= 50 and materials[0] >= 45:
            print('Wuld you like to go over to the mountans that ' + ho)
            option = str(input('> '))
            if option == 'Yes':
                modify_materials('location', 2)
                modify_materials('fire', 5)
                print('As you finish the climb up the major parts' + mo)
                print('You dicide to set up camp.')
                modify_materials('location', 2)
        else:
            print('you do not have enough wood or/and food')
    elif direction == 'East':
        if materials[1] >= 50 and materials[0] >= 45:
            print('Wuld you like to go over to the volcanoe?')
            option = str(input('> '))
            if option == 'Yes':
                modify_materials('location', 3)
                modify_materials('fire', 5)
                print('As you finish the climb up the volcanoe.')
                print('You dicide to set up camp.')
        else:
            print('you do not have enough wood or/and food')
    elif direction == 'West':
        if materials[1] >= 50 and materials[0] >= 45:
            print('Wuld you like to go over to the swamp?')
            option = str(input('> '))
            if option == 'Yes':
                modify_materials('location', 4)
                modify_materials('fire', 5)
                print('As you finish the climb up swampy hills.')
                print('You dicide to set up camp.')
        else:
            print('you do not have enough wood or/and food')

def check_fire():
    global mterials, kill
    if materials[3] >= 10:
        modify_materials('fire', 10)
    elif materials[3] <= 0:
        kill = True

def game_over():
    global kill
    print('game over.')
    kill = True
    sys.exit()

def sleep():
    global materials
    biomedifficulty()
    if materials[1] < 3 and materials[3] <= 3:
        print('you die of lack of food and your fire going out.')
        game_over()
    elif materials[1] < 3:
        print('you die of starvation.')
        game_over()
    elif materials[3] <= 3:
        print('the fire went out.')
        game_over()
    else:
        modify_materials('fire', (materials[3] - 3))
        modify_materials('food', (materials[1] - 3))
        print('''that day you dicide to go to sleep.
        The next morning you, see that the fire is a litle dimmer.''')

def time_check():
    global TOD
    if TOD >= 7:
        TOD = 0
        sleep()

def interface_loop():
    global materials, TOD, score, day, kill, rng, options
    while kill is False:
        time_check()
        check_fire()
        checkrecources()
        options()
        question = input('> ')
        if question == str('help'):
            print('''commands:
            adventure, recouces, wood, food, stoke, sleep, look''')
        elif question == str('stoke the fire'):
            if materials[0] >= 3:
                TOD = TOD + 1
                print('your fire burnes a litle brighter.')
                rng_difficulty('fire')
                modify_materials('fire', (materials[3] + rng))
                modify_materials('wood', (materials[0] - 3))
            else:
                print('You do not have enough wood.')
        elif question == "save":
            save(input("""witch save slot? (1-3)
4 to cancel"""))
        elif question == "load":
            load_save(input("witch save slot? '1-3'"))
        elif question == str('adventure'):
            adventure()
        elif question == str('recources'):
            print('wood: ' + materials[0])
            print('food: ' + materials[1])
            print('gold: ' + materials[2])
            print('fire level: ' + materials[3])
        elif question == str('chop wood'):
            woodd()
        elif question == str("hunt"):
            foodd()
        elif question == str("sleep"):
            sleep()
        elif question == str("look"):
            print("look where?")
            print("""look towards the...
            mountins
            forest
            volcanoe
            swamp""")
            question = str(input("> "))
            if question == "mountins":
                rng = random.randint(1, 3)
                if rng == 1:
                    print("you see the dwarves mining inside ther mountin.")
                elif rng == 2:
                    print("you see the dwarves trading whith eachother.")
                elif rng == 3:
                    print("you cant seem to find the dwarves.")
            elif question == "forest":
                rng = random.randint(1, 3)
                if rng == 1:
                    print("you see the elves singing to ther great god tree.")
                elif rng == 2:
                    print("you see the elves trading whith eachother.")
                elif rng == 3:
                    print("you cant see past the giant forest trees.")
            elif question == "volcanoe":
                rng = random.randint(1, 3)
                if rng == 1:
                    print("""you can see the elementals
                    patrolling the blistering hot volcanoe.""")
                elif rng == 2:
                    print("the volcanoe is very peacefull today.")
                elif rng == 3:
                    print("the volcanoe is getting mad about something!")
            elif question == "swamp":
                rng = random.randint(1, 3)
                if rng == 1:
                    print("""you cant see through the stoOpId
                    amount of bog-trees in the swamp.""")
                elif rng == 2:
                    print("""you see the kobalts planing something
                    to do whith pots and pans.""")
                elif rng == 3:
                    print("nothing is realy happening in the swamp today.")
            else:
                print("you cant look there.")
        elif question == "poop":
            print("""You got diarea?
-40 wood, and -40 food.""")
            modify_materials('food', (materials[1] - 40))
            modify_materials('wood', (materials[0] - 40))
        elif question == "save and quit":
            saveslot = input("which save slot: ")
            if saveslot == "1":
                save(1)
            elif saveslot == "2":
                save(2)
            elif saveslot == "3":
                save(3)
        else:
            print('no sutch action')
    quit()

print("""the one and only develapor for this game:
Isaac Clark
game testers:
Gavin Clark
Austin Clark
Emily Clark
Rick
aprox "fireplace.py" development duration:
1.5 years""")

interface_loop()

def lore():
    print("""the lore of fireplace.py
fire-elementals

Fire-elementals attack against bandits.

reinforcements are arriving.

Flamefalls is a tripwire that detects any hostile elementals that enter the clearing and breaks the siege if it happens.

When fire-elementals attack we take action and smash them with flamestrikes in the following order.

Reserve-fire-elementals, pass-banner-fire-elementals, attack-banner-fire-elementals, pass-banner-fire-elementals.

Then we move back, reinforcing those that are fighting and gathering resources (also referred to as the “turtle’s nest”).

We will save so much time in the long run with this setup!

Then we move back to continue protecting the defenses and working on the special weapon for extra support.

Similar to the “flames” battle-tree we use a special battle-tree for producing flame-elementals.

Firebat

Firebat is a trap-specific character that is recommended only for skilled users. The reason being is that the player will have to plan the attack carefully because he has a very limited resource pool. His melee attack has three different attack points and his archery only has two.

We use a neat battle-tree to reinforce the battle-tree and the other zones that we reinforce.

We can just smash firebat with the drill and escape.

Taking the firebat out of the battle-tree gives the player an easier time on fire-elementals.

But if we destroy the firebat we won’t have a special character anymore that can destroy these elementals.

So we wait for him to come back from an exploit so we can finally destroy him.

When the fire-elementals come from the bottom of the forest, we take them by surprise and slash the firebat to bits.

In order to do that we just have to fire-elementals attack the firebat.

They work well against firebat because they are very large.
And thats where MY story began...

Fullscreen

If you are using a GPU with more than a bit of power then you might want to lower the resolution.

High resolution might drain your battery and can have a high performance impact in performance and/or framerate.

Like in console-games, let’s take a look at the fullscreen-process of this battle-tree.

If you are using a GPU with more than a bit of power then you might want to lower the resolution.

High resolution might drain your battery and can have a high performance impact in performance and/or framerate.

Many may argue that we shouldn’t play a game in such a low-resolution.

But I personally enjoy my game at high-resolution.

Why?

Lower-resolution doesn’t take a lot of processing power and takes less time when scrolling.

An extra character will take longer to show up in the battle-tree.

Is it worth it?

Well… we can do it with a lot of work but we will save so much time.

Here’s another neat battle-tree idea I came up with.

If we destroy the enemy, the defenders we win!""")