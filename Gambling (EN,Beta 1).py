# -*- coding : UTF-8 -*-
# Gambling
# Language: English
# Version: Development Beta 1
# Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.

import sys,time,os,random

nothing = '######'; one = '0#####'; two = '00####'; three = '000###'
four = '0000##'; five = '00000#'; six = '000000'

dice = [nothing, one, two, three, four, five, six]
commands = ('p','e')
gamecmds = ("big","middle","small","even","odd","xiaoqizuishuai")
home_cmds = ('p','e','h')

shellcmds = ("coin","addcoin","","exit","setcoin")

money = 10000

class Dicenum:
    def __init__(self,num):
        if num % 2 == 0:
            self.odd_even = "even"
        else:
            self.odd_even = "odd"
        if num == 1 or num == 2:
            self.bms = "small"
        elif num == 3 or num == 4:
            self.bms = "middle"
        else:
            self.bms = "big"

def show_game_info(dice_num):
    os.system("cls")
    print("Welcome to the gambling game!\t\t\t\t\t\tCoin：$" + str(money))
    print("")
    print(dice[dice_num])
    print("")

def shell():
    global money
    money += 500
    print("Gambling v0.0.1 - Debugging Shell")
    print("Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.")
    print("")
    while True:
        cmd = input("debug>")
        coms = cmd.split(" ")
        if coms[0] not in shellcmds:
            print("Invalid command.\n")
        if coms[0] == "coin":
            print(money)
            print("")
        elif coms[0] == "addcoin":
            try:
                adc = int(coms[1])
            except IndexError:
                print("Missing argument: coin number\n")
            else:
                money += adc
        elif coms[0] == "setcoin":
            try:
                adc = int(coms[1])
            except IndexError:
                print("Missing argument: coin number\n")
            else:
                money = adc
        elif coms[0] == "exit":
            return
        
    

def play():
    global money
    os.system("cls")
    show_game_info(0)
    cmd = input("Each game costs $500,continue?(\"p\" for continue, \"e\" for exit) ")
    while cmd not in commands:
        print("Take it seriously! Be careful about the FBI Red Warning!")
        cmd = input("Each game costs $500,continue?(\"p\" for continue, \"e\" for exit) ")
    if cmd == 'p':
        pass
    elif cmd == 'e':
        return 2
    money -= 500
    if money < 0:
        print("Sorry, you lost all your money gambling. You will be forcedly quitted...")
        time.sleep(3)
        return 1
    os.system("cls")
    show_game_info(0)
    first = input("Big, middle or small? ")
    
    while first not in gamecmds:
        print("Take it seriously! Be careful about the FBI Red Warning!")
        first = input("Big, middle or small? ")
    if first == "xiaoqizuishuai":
        os.system("cls")
        shell()
        os.system("cls")
        return 3
        
    second = input("Odd or even? ")
    while second not in gamecmds:
        print("Take it seriously! Be careful about the FBI Red Warning!")
        second = input("Odd or even? ")
    for i in range(1,21):
        os.system("cls")
        if i % 6 == 0:
            show_game_info(6)
        else:
            show_game_info(i % 6)
        print("Rolling the dice...")
    os.system("cls")
    num = random.randint(1,6)
    show_game_info(num)
    print("Get number:" + str(num))
    num = Dicenum(num)
    gamejudge = 0
    if num.bms == first:
        gamejudge += 1
    if num.odd_even == second:
        gamejudge += 1
    
    if gamejudge == 2:
        print("All correct! You've got 1000 dollars!")
        money += 1000
    elif gamejudge == 1:
        print("You are half right! You've got 500 dollars!")
        money += 500
    else:
        print("You are so lame! Nothing is right, so you've got nothing!")
    time.sleep(3)
    return 0


def show_doc():
    print("This is a dice rolling game. Each of the number on the dice has two attributes:")
    print("Big, middle, small; Odd, even.")
    print("")
    print("Odd and even are easy to explain. 1, 3 and 5 are odd, 2, 4 and 6 are even.")
    print("Big, middle and small mean the big, middle and small number in the odd set and the even set.")
    print("So, every number can be shown by two attributes.")
    print("Like: 1=small odd, 4=middle even.")
    print("The game will select a random number. You need to guess the attrubutes of the number.")
    print("If you guess half right, you'll get 500 dollars. If you guess all right, you'll get 1000 dollars.")
    print("Each game costs 500 dollars.")
    print("At first you have 10000 dollars. If you use them up, game over!")
    print("")
    input("Press \"Enter\" to quit...")


def main():
    global money
    os.system("cls")
    print("Loading...")
    time.sleep(1)
    print("Initializing...")
    time.sleep(0.5)
    
    while True:
        os.system("cls")
        print("Gambling")
        print("")
        cmd = input("\"p\" to play, \"h\" to view help document, \"e\" to exit ")
        while cmd not in home_cmds:
            print("Take it seriously! Be careful about the FBI Red Warning!")
            cmd = input("\"p\" to play, \"h\" to view help document, \"e\" to exit ")
        if cmd == "p" or cmd == "P":
            money = 10000
            ret = play()
            while ret == 0 or ret == 3:
                ret = play()
        elif cmd == "h" or cmd == "H":
            os.system("cls")
            show_doc()
        elif cmd == "e" or cmd == "E":
            return

if __name__ == "__main__":
    main()
