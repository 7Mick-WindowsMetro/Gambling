# -*- coding : UTF-8 -*-
# Gambling GUI
# Language: Simplified Chinese
# Version: v1.0
# Copyright Hangzhou Sevensoft Technology 2021 All rights reserved.

# Please take care of my hair! And welcome to my GitHub:
# https://github.com/7Mick-WindowsMetro
import pygame,sys,pickle,os,random,tkinter

init_path = r"resources\sevensoft.png"
background_path = r"resources\background.jpg"
playbutton_path = r"resources\playbutton.png"
icon_path = r"resources\icon.ico"

big_path = r"resources\big.png"
middle_path = r"resources\middle.png"
small_path = r"resources\small.png"
odd_path = r"resources\odd.png"
even_path = r"resources\even.png"

big_pressed_path = r"resources\bigpressed.png"
middle_pressed_path = r"resources\middlepressed.png"
small_pressed_path = r"resources\smallpressed.png"
odd_pressed_path = r"resources\oddpressed.png"
even_pressed_path = r"resources\evenpressed.png"

rollButton_path = r"resources\roll.png"
backButton_path = r"resources\back.png"

#Broadcast
bmsPressed = 0
oePressed = 0
#--

info = []

#(169, 441)

dice_paths = [r"resources\dice" + str(i) + ".png" for i in range(1,7)]
class Dicenum:
    def __init__(self,num):
        if num % 2 == 0:
            self.odd_even = 2
        else:
            self.odd_even = 1
        if num == 1 or num == 2:
            self.bms = 3
        elif num == 3 or num == 4:
            self.bms = 2
        else:
            self.bms = 1

class Button(pygame.sprite.Sprite):
    def __init__(self,button,pressedbutton,rect,id):
        self.image = button
        self.pimage = pressedbutton
        self.rect = rect
        self.isChanged = False
        self.id=id


def in_rect(mouse_pos,rect):
    x,y = mouse_pos
    rx,ry,rw,rh = rect
    if rx <= x <= rx + rw and ry <= y <= ry + rh:
        return True
    
    return False

var = None


def play():
    global screen,clock,background,background_rect
    global bButton,mButton,sButton,oButton,eButton
    global bButtonP,mButtonP,sButtonP,oButtonP,eButtonP
    global big_rect,middle_rect,small_rect,odd_rect,even_rect
    global backButton_path
    global bmsPressed,oePressed
    global binpath,info
    global rollButton

    havemoney = True

    
    rawlevel = info[1]
    level = int(rawlevel)

    screen.blit(background,background_rect)
    backButton = pygame.image.load(backButton_path)
    backButton_rect = backButton.get_rect()
    backButton_rect.center = (70,70)
    screen.blit(backButton,backButton_rect)
    welcome = font.render("欢迎进入赌博游戏场！",14,(255,0,0))
    welcome_rect = welcome.get_rect()
    welcome_rect.center = (150,25)
    screen.blit(welcome,welcome_rect)

    rollButton_rect = rollButton.get_rect()
    rollButton_rect.center = (100,325)
    screen.blit(rollButton,rollButton_rect)
    
    dice = [pygame.transform.scale(pygame.image.load(i),(100,100)) for i in dice_paths]
    dice_rect = [i.get_rect() for i in dice]
    for i in dice_rect:
        i.center=(100,215)
    
    big_rect.center = (260, 180)
    middle_rect.center = (400, 180)
    small_rect.center = (540, 180)
    odd_rect.center = (320, 320)
    even_rect.center = (480, 320)
    
    
    screen.blit(dice[0],dice_rect[0])
    sfont = pygame.font.SysFont("SimHei",20)
    inforend = sfont.render("等级：Lv."+str(info[1])+"      金币：$"+str(info[2]),True,(255,0,0))
    inforend_rect = inforend.get_rect()
    inforend_rect.left = 300
    inforend_rect.top = 50
    screen.blit(inforend,inforend_rect)
    big = Button(bButton,bButtonP,big_rect,1)
    middle = Button(mButton,mButtonP,middle_rect,2)
    small = Button(sButton,sButtonP,small_rect,3)
    odd = Button(oButton,oButtonP,odd_rect,1)
    even = Button(eButton,eButtonP,even_rect,2)
    
    bmsButtons = [big,middle,small]
    oeButtons = [odd,even]
    for i in bmsButtons:
        screen.blit(i.image,i.rect)
    for i in oeButtons:
        screen.blit(i.image,i.rect)

    prompt = sfont.render("等待投掷骰子...",True,(0,0,0))
    prompt_rect = prompt.get_rect()
    prompt_rect.center = (170, 440)
    if info[2] < 500-(level-1)*50:
        prompt = sfont.render("啊哦！你没钱了！你将被强制退出游戏...",True,(255,0,0))
        info[2] = 10000
        havemoney = False
    
    screen.blit(prompt,prompt_rect)
    enter()
    while True:
        clock.tick(1000)
        if info[1] >= 11:
            info[2] += 100000
            info[1] = 1
            overrend1 = sfont.render("哇！你是赌神！你的等级已经达到了11，",True,(255,0,0))
            overrend1_rect = overrend1.get_rect()
            overrend1_rect.center = (320,400)
            overrend2 = sfont.render("你会获得100000元的奖励，即将将你的等级重设为1...",True,(255,0,0))
            overrend2_rect = overrend2.get_rect()
            overrend2_rect.center = (320,450)
            screen.blit(overrend1,overrend1_rect)
            screen.blit(overrend2,overrend2_rect)
            pygame.display.flip()
            pygame.time.delay(3000)
            leave()
            return 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info[1] = level
                with open(binpath,"wb") as f:
                    pickle.dump(info,f)
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and havemoney:
                print(pygame.mouse.get_pos())
                for i in bmsButtons:
                    if in_rect(pygame.mouse.get_pos(),i.rect):
                        if i.isChanged:
                            screen.blit(i.image,i.rect)
                            i.isChanged = False
                            bmsPressed = 0
                        else:
                            screen.blit(i.pimage,i.rect)
                            i.isChanged = True
                            bmsPressed = i.id
                for i in oeButtons:
                    if in_rect(pygame.mouse.get_pos(),i.rect):
                        if i.isChanged:
                            screen.blit(i.image,i.rect)
                            i.isChanged = False
                            oePressed = 0
                        else:
                            screen.blit(i.pimage,i.rect)
                            i.isChanged = True
                            oePressed = i.id

                if in_rect(pygame.mouse.get_pos(),rollButton_rect) and bmsPressed and oePressed:
                        
                    info[2] -= 500 - (level - 1) * 50
                    screen.blit(background,background_rect)
                    screen.blit(backButton,backButton_rect)
                    inforend = sfont.render("等级：Lv."+str(info[1])+"      金币：$"+str(info[2]),True,(255,0,0))
                    screen.blit(inforend,inforend_rect)
                    screen.blit(rollButton,rollButton_rect)
                    screen.blit(welcome,welcome_rect)
                    for i in bmsButtons:
                        if bmsPressed != i.id:
                            screen.blit(i.image,i.rect)
                        else:
                            screen.blit(i.pimage,i.rect)
                    for i in oeButtons:
                        if oePressed != i.id:
                            screen.blit(i.image,i.rect)
                        else:
                            screen.blit(i.pimage,i.rect)
                    for i in range(100):
                        clock.tick(60)
                        screen.blit(dice[i%6],dice_rect[i%6])
                        pygame.display.update()
                    
                    num = random.randint(1,6)
                    screen.blit(dice[num-1],dice_rect[num-1])
                    # pygame.display.update()
                    dnum = Dicenum(num)
                    gamejudge = 0
                    if bmsPressed == dnum.bms:
                        gamejudge += 1
                    if oePressed == dnum.odd_even:
                        gamejudge += 1
                    
                    if gamejudge == 2:
                        info[2] += 1000
                        rawlevel += 1
                        prompt = sfont.render("恭喜！你全部猜对了，获得1000金币！",True,(0,255,0))
                    elif gamejudge == 1:
                        info[2] += 500
                        rawlevel += 0.5
                        prompt = sfont.render("你猜对了一半哦！获得500金币！",True,(0,0,255))
                    
                    else:
                        prompt = sfont.render("你太逊~ 全猜错了，一分不给！嘿嘿嘿~",True,(255,0,0))
                    
                    level = int(rawlevel)
                    info[1] = level
                    
                    screen.blit(background,background_rect)
                    screen.blit(backButton,backButton_rect)
                    inforend = sfont.render("等级：Lv."+str(info[1])+"      金币：$"+str(info[2]),True,(255,0,0))
                    screen.blit(inforend,inforend_rect)
                    screen.blit(rollButton,rollButton_rect)
                    screen.blit(welcome,welcome_rect)
                    for i in bmsButtons:
                        if bmsPressed != i.id:
                            screen.blit(i.image,i.rect)
                        else:
                            screen.blit(i.pimage,i.rect)
                    for i in oeButtons:
                        if oePressed != i.id:
                            screen.blit(i.image,i.rect)
                        else:
                            screen.blit(i.pimage,i.rect)
                    screen.blit(dice[num-1],dice_rect[num-1])
                    if level < 11:
                        screen.blit(prompt,prompt_rect)
                    print("Flipped")
                
                if in_rect(pygame.mouse.get_pos(),backButton_rect):
                    leave()
                    return 0
                    

        for i in bmsButtons:
            if bmsPressed != i.id and i.isChanged:
                i.isChanged = False
                screen.blit(i.image,i.rect)
        for i in oeButtons:
            if oePressed != i.id and i.isChanged:
                i.isChanged = False
                screen.blit(i.image,i.rect)
        pygame.display.flip()
        

def leave():
    global screen,clock,binpath
    prscreen=screen.convert()
    prscreen_rect = prscreen.get_rect()
    for i in range(255,-1,-1):
        clock.tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(binpath,"wb") as f:
                    pickle.dump(info,f)
                sys.exit(0)
        screen.fill((0,0,0))
        prscreen.set_alpha(i)
        screen.blit(prscreen,prscreen_rect)
        pygame.display.flip()



def enter():
    global screen,clock,binpath
    prscreen=screen.convert()
    prscreen_rect = prscreen.get_rect()
    for i in range(255):
        clock.tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(binpath,"wb") as f:
                    pickle.dump(info,f)
                sys.exit(0)
        screen.fill((0,0,0))
        prscreen.set_alpha(i)
        screen.blit(prscreen,prscreen_rect)
        pygame.display.flip()

def main():
    global screen,binpath,info
    screen.fill((255,255,255))
    screen.blit(background,background_rect)
    rend = font.render("天天爱博彩",True,(0,0,0))
    rend_rect = rend.get_rect()
    rend_rect.center=(320,20)
    screen.blit(rend,rend_rect)
    playbutton_rect.center=(320,240)
    screen.blit(playbutton,playbutton_rect)
    sfont = pygame.font.SysFont("SimHei",20)
    inforend = sfont.render(" 欢迎，"+info[0]+"      等级：Lv."+str(info[1])+"      金币："+str(info[2]),True,(0,0,255))
    inforend_rect = inforend.get_rect()
    inforend_rect.top = 50
    screen.blit(inforend,inforend_rect)
    
    if info[1] >= 11:
        info[2] += 100000
        info[1] = 1
        overrend1 = sfont.render("哇！你是赌神！你的等级已经达到了11，",True,(255,0,0))
        overrend1_rect = overrend1.get_rect()
        overrend1_rect.center = (320,400)
        overrend2 = sfont.render("你会获得100000元的奖励，即将将你的等级重设为1...",True,(255,0,0))
        overrend2_rect = overrend2.get_rect()
        overrend2_rect.center = (320,450)
        screen.blit(overrend1,overrend1_rect)
        screen.blit(overrend2,overrend2_rect)
        enter()
        pygame.time.delay(3000)
        leave()
        return 1
    enter()
    while True:
        clock.tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(binpath,"wb") as f:
                    pickle.dump(info,f)
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if in_rect(pygame.mouse.get_pos(),playbutton_rect):
                    print("Play button clicked")
                    leave()
                    play()
                    return 0
                
                    
                    
        pygame.display.flip()

def enter_animation():
    global initialize,init_rect
    screen.fill((0,0,0))
    screen.blit(initialize,init_rect)
    enter()
    pygame.time.delay(3000)
    leave()


if __name__ == '__main__':
    pygame.init()
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("天天爱博彩")
    size = width,height = 640,480
    screen = pygame.display.set_mode(size)
    initialize = pygame.image.load(init_path).convert()
    init_rect = initialize.get_rect()
    background = pygame.image.load(background_path)
    background_rect = background.get_rect()
    playbutton = pygame.image.load(playbutton_path)
    playbutton_rect = playbutton.get_rect()
    clock=pygame.time.Clock()
    font = pygame.font.SysFont("SimHei",28)
    bButton = pygame.image.load(big_path)
    mButton = pygame.image.load(middle_path)
    sButton = pygame.image.load(small_path)
    oButton = pygame.image.load(odd_path)
    eButton = pygame.image.load(even_path)

    big_rect = bButton.get_rect()
    middle_rect = mButton.get_rect()
    small_rect = sButton.get_rect()
    odd_rect = oButton.get_rect()
    even_rect = eButton.get_rect()

    bButtonP = pygame.image.load(big_pressed_path)
    mButtonP = pygame.image.load(middle_pressed_path)
    sButtonP = pygame.image.load(small_pressed_path)
    oButtonP = pygame.image.load(odd_pressed_path)
    eButtonP = pygame.image.load(even_pressed_path)

    rollButton = pygame.transform.scale(pygame.image.load(rollButton_path),(150,75))

    
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
    enter_animation()
    while True:
        main()

    