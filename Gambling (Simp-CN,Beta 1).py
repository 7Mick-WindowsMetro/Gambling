# -*- coding : UTF-8 -*-
# Gambling
# Language: Simplified Chinese
# Version: Development Beta 1 (v0.0.1)
# Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.

import sys,time,os,random

nothing = '######'; one = '0#####'; two = '00####'; three = '000###'
four = '0000##'; five = '00000#'; six = '000000'

dice = [nothing, one, two, three, four, five, six]
commands = ('p','e')
gamecmds = ("大","中","小","双","单","xiaoqizuishuai")
home_cmds = ('p','e','h')

shellcmds = ("coin","addcoin","","exit","setcoin")

money = 10000

class Dicenum:
    def __init__(self,num):
        if num % 2 == 0:
            self.odd_even = "双"
        else:
            self.odd_even = "单"
        if num == 1 or num == 2:
            self.bms = "小"
        elif num == 3 or num == 4:
            self.bms = "中"
        else:
            self.bms = "大"

def show_game_info(dice_num):
    os.system("cls")
    print("欢迎进入赌博游戏场！\t\t\t\t\t\t余额：$" + str(money))
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
    cmd = input("每次游戏需要花费$500，继续吗？（按p继续，按e退出）")
    while cmd not in commands:
        print("不要乱输命令！当心FBI红色警告！")
        cmd = input("每次游戏需要花费$500，继续吗？（按p继续，按e退出）")
    if cmd == 'p':
        pass
    elif cmd == 'e':
        return 2
    money -= 500
    if money < 0:
        print("抱歉，你已经输光了，将被强制退出游戏...")
        time.sleep(3)
        return 1
    os.system("cls")
    show_game_info(0)
    first = input("押大、押中还是押小？")
    
    while first not in gamecmds:
        print("不要乱输命令！当心FBI红色警告！")
        first = input("押大、押中还是押小？")
    if first == "xiaoqizuishuai":
        os.system("cls")
        shell()
        os.system("cls")
        return 3
        
    second = input("押单还是押双？")
    while second not in gamecmds:
        print("不要乱输命令！当心FBI红色警告！")
        second = input("押单还是押双？")
    for i in range(1,21):
        os.system("cls")
        if i % 6 == 0:
            show_game_info(6)
        else:
            show_game_info(i % 6)
        print("掷骰子中...")
    os.system("cls")
    num = random.randint(1,6)
    show_game_info(num)
    print("获得数字：" + str(num))
    num = Dicenum(num)
    gamejudge = 0
    if num.bms == first:
        gamejudge += 1
    if num.odd_even == second:
        gamejudge += 1
    
    if gamejudge == 2:
        print("全部猜对！你赢得了1000美元！")
        money += 1000
    elif gamejudge == 1:
        print("猜对一半！你得到500美元！")
        money += 500
    else:
        print("不行啊，你全猜错了，一分没有！")
    time.sleep(3)
    return 0


def show_doc():
    print("这是一个掷骰子的游戏。骰子的6个点数分别有几种属性：")
    print("大、中、小；单、双。")
    print("")
    print("单和双很好解释，1、3、5为单，2、4、6为双。")
    print("大、中、小指的是在单、双两个集合中最大、中间、最小的那个。")
    print("也就是说，每个点数都可以用对应的两个属性来表示。")
    print("如：1=小单，4=中双")
    print("程序会自动生成一个随机数，你需要猜这个数的属性，猜对就可以赢钱。")
    print("猜对一半可以赢500美元，全猜对得1000美元。")
    print("每次游戏入场费为500美元。")
    print("初始状态有10000美元，用完则游戏结束。")
    print("")
    input("按回车键退出...")


def main():
    global money
    os.system("cls")
    print("Loading...")
    time.sleep(1)
    print("Initializing...")
    time.sleep(0.5)
    
    while True:
        os.system("cls")
        print("天天爱博彩")
        print("")
        cmd = input("按p进入游戏，按h显示帮助，按e退出。")
        while cmd not in home_cmds:
            print("不要乱输命令！当心FBI红色警告！")
            cmd = input("按p进入游戏，按h显示帮助，按e退出。")
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
