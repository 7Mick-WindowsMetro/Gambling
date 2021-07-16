# -*- coding : UTF-8 -*-
# Gambling
# Language: Simplified Chinese
# Version: Development Beta 2 (v0.0.2)
# Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.

# Please take care of my hair! And welcome to my GitHub:
# https://github.com/7Mick-WindowsMetro


import sys,time,os,random,pickle

shellswitch = False

nothing = '######'; one = '0#####'; two = '00####'; three = '000###'
four = '0000##'; five = '00000#'; six = '000000'

dice = (nothing, one, two, three, four, five, six)
commands = ('p','e')
gamecmds = ("大","中","小","双","单","xiaoqizuishuai")
home_cmds = ('p','e','h','s')

shellcmds = ("coin","addcoin","","exit","setcoin","setlevel","level","setname","name")

info = []

money = None



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

def show_game_info(dice_num,level):
    global info,money
    os.system("cls")
    print("欢迎进入赌博游戏场！\t\t\t\t\t\t余额：$" + str(money) + "\n")
    print("玩家：" + info[0])
    print("等级：Lv." + str(level))
    print("")
    print(dice[dice_num])
    print("")

def settings():
    os.system("cls")
    print("设置")
    print("您的昵称："+info[0]+"\n")
    while True:
        name=input("输入您的新昵称（按回车键退出）")
        if name=="":
            return
        info[0]=name
        os.system("cls")
        print("设置")
        print("您的昵称："+info[0]+"\n")

def shell(gamecost):
    os.system("cls")
    global money,info
    money += gamecost
    print("Gambling v0.0.3 - Debugging Shell")
    print("Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.")
    print("")
    while True:
        cmd = input("debug>")
        coms = cmd.split(" ")
        if coms[0] not in shellcmds:
            print("Illegal command.\n")
        if coms[0] == "coin":
            print(str(money)+"\n")
        elif coms[0] == "addcoin":
            try:
                adc = int(coms[1])
            except Exception:
                print("Invalid syntax.\n")
            else:
                money += adc
                print("")
        elif coms[0] == "setcoin":
            try:
                adc = int(coms[1])
            except Exception:
                print("Invalid syntax.\n")
            else:
                money = adc
                print("")
        elif coms[0] == "setlevel":
            try:
                newlv = int(coms[1])
            except Exception:
                print("Invalid syntax.\n")
            else:
                info[1]=newlv
                print("")
        elif coms[0]=="level":
            print(str(info[1])+"\n")
        elif coms[0]=="setname":
            try:
                newname=coms[1]
            except Exception:
                print("Invalid syntax.\n")
            else:
                info[0]=newname
                print("")
        elif coms[0]=="name":
            print(info[0]+"\n")
        elif coms[0] == "exit":
            info[2]=money
            return
        
    

def play():
    global money,info
    os.system("cls")
    rawlevel = info[1]
    level=int(rawlevel)
    if level >= 11:
        print("哇，你是赌神！您已经达成了Level达到11的成就，即将将您的Level重置为1...")
        info[1]=1
        rawlevel=info[1]
        level=int(rawlevel)
        time.sleep(3)
        os.system("cls")
    gamecost = int(500-(level-1)*50)
    show_game_info(0,level)
    cmd = input("每次游戏需要花费$"+ str(gamecost) +"，继续吗？（按p继续，按e退出）")
    
    while cmd not in commands:
        print("不要乱输命令！当心FBI红色警告！")
        cmd = input("每次游戏需要花费$"+ str(gamecost) +"，继续吗？（按p继续，按e退出）")
    if cmd == 'p':
        pass
    elif cmd == 'e':
        return 2
    money -= gamecost
    if money < 0:
        os.system("cls")
        show_game_info(0,level)
        print("抱歉，你已经输光了，将被强制退出游戏...")
        time.sleep(3)
        return 1
    os.system("cls")
    show_game_info(0,level)
    first = input("押大、押中还是押小？")
    
    while first not in gamecmds:
        print("不要乱输命令！当心FBI红色警告！")
        first = input("押大、押中还是押小？")
    if first == "xiaoqizuishuai":
        shell(gamecost)
        os.system("cls")
        return 3
        
    second = input("押单还是押双？")
    while second not in gamecmds:
        print("不要乱输命令！当心FBI红色警告！")
        second = input("押单还是押双？")
    for i in range(1,21):
        os.system("cls")
        if i % 6 == 0:
            show_game_info(6,level)
        else:
            show_game_info(i % 6,level)
        print("掷骰子中...")
    os.system("cls")
    num = random.randint(1,6)
    show_game_info(num,level)
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
        rawlevel+=1
    elif gamejudge == 1:
        print("猜对一半！你得到500美元！")
        money += 500
        rawlevel+=0.5
    else:
        print("不行啊，你全猜错了，一分没有！")
    print("按任意键继续...")
    os.system("pause >NUL")
    info[1]=rawlevel
    level=int(rawlevel)
    return 0


def show_doc():
    print("这是一个掷骰子的游戏。骰子的6个点数分别有几种属性：")
    print("大、中、小；单、双。")
    print("")
    print("单和双很好解释，1、3、5为单，2、4、6为双。")
    print("大、中、小指的是在单、双两个集合中最大、中间、最小的那个。")
    print("通俗来说：")
    print("1、2为小，3、4为中，5、6为大。")
    print("也就是说，每个点数都可以用对应的两个属性来表示。")
    print("如：1=小单，4=中双")
    print("程序会自动生成一个随机数，你需要猜这个数的属性，猜对就可以赢钱。")
    print("猜对一半可以赢500美元，全猜对得1000美元。")
    print("每次游戏入场费为500美元。")
    print("初始状态有10000美元，用完则游戏结束。")
    print("")
    print("按任意键退出...")
    os.system("pause >NUL")


def main():
    global money
    money=info[2]
    username = info[0]
    level=int(info[1])
    os.system("cls")
    print("Loading...")
    time.sleep(1)
    print("Initializing...")
    time.sleep(0.5)
    
    while True:
        username = info[0]
        level=int(info[1])
        os.system("cls")
        print("天天爱博彩")
        print("欢迎，" + str(username) + "\n\n等级：Lv." + str(level) + "\n\n余额："+str(money))
        print("")
        cmd = input("按p进入游戏，按h显示帮助，按s进入设置，按e退出。")
        while cmd not in home_cmds:
            print("不要乱输命令！当心FBI红色警告！")
            cmd = input("按p进入游戏，按h显示帮助，按s进入设置，按e退出。")
        if cmd.lower() == 'p':
            
            ret = play()
            info[2]=money
            while ret == 0 or ret == 3:
                ret = play()
                info[2]=money
        elif cmd.lower() == 'h':
            os.system("cls")
            show_doc()
        elif cmd.lower() == 'e':
            return
        elif cmd.lower() == 's':
            settings()

# Main Entry Point
if __name__ == "__main__":
    binpath = os.path.expanduser("~\\usrinfo.dat")
    if os.path.exists(binpath):
        with open(binpath,"rb") as f:
            try:
                info = pickle.load(f)
                if not isinstance(info,list) or not len(info) == 3:
                    raise ValueError("User information file error!")
            except ValueError as err:
                print("错误：" + str(err))
    else:
        with open(binpath,"wb") as f:
            info = ["Guest",1,10000]
            pickle.dump(info,f)
    if shellswitch:
        money = 9500
        shell()
    else:
        main()
        with open(binpath,"wb") as f:
            pickle.dump(info,f)
# [username,level]
