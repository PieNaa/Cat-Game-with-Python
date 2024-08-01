from threading import Timer
# import black
# import click
import pygame
import random

Read_Stat_file = open("Status.txt", "r")
Read_Default_Stat_file = open("Status_Default.txt", "r")
STAT_VAL = Read_Stat_file.readlines()
DEFAULT_STAT_VAL = Read_Default_Stat_file.readlines()

for i in range(len(STAT_VAL)) :
    STAT_VAL[i] = float(STAT_VAL[i])

    #   ------------ CALLING INDEX ------------
    #   P_Health i = 0         #M_Health i = 1
    #   Energy i = 2           #Hunger i = 3
    #   PooPoo i = 4           #Sanitary i = 5         
    #   INT i = 6              #Money i = 7

def Stat_Bar(Scence,surface) :
    Scence.stat_bar = (pygame.image.load("images\Stat_Bar.png"))
    surface.blit(Scence.stat_bar,(0,0))

    for i in range(8) :
        Scence.font = pygame.font.SysFont("arial.ttf", 24)
        Scence.text = Scence.font.render(str(int(STAT_VAL[i])), True, "black")
        textRect = Scence.text.get_rect()
        textRect.center = (190+i*60,600-70)
        surface.blit(Scence.text,textRect)


def RE_STAT() :
    for i in range(len(DEFAULT_STAT_VAL)) :
        STAT_VAL[i] = float(DEFAULT_STAT_VAL[i])

def STAT_UPDATE(time) :
    if STAT_VAL[0] < 100 and STAT_VAL[3] >= 50 :        # IF HP NOT FULL BUT HUNGER >= 50
        if time % 2 == 0 :
            STAT_VAL[2] += 1                            # 1 HP REGEN PER 2 SEC

    if STAT_VAL[2] > 0:                                 # IF STILL HAVE ENERGY
        if time % 10 == 0 :
            STAT_VAL[2] -= 1
    else :                                              # OUT OF ENERGY KHUAY WILL USE HUNGER INSTEAD
        if time % 5 == 0 :
            STAT_VAL[3] -= 1

    if STAT_VAL[3] > 0 :                                # HUNGER > 0
        if time % 15 == 0 :
            STAT_VAL[3] -= 1 
    else :                                              # HUNGER < 0
        if time % 5 == 0 :
            STAT_VAL[0] -= 1                            # KHUAY IS STARVING TO DIE

    if STAT_VAL[5] > 0 :                                # Sanitary > 0
        if time % 8 == 0 :
            STAT_VAL[5] -= 1                            
    else :                                              # Sanitary < 0
        if time % 5 == 0 :
            STAT_VAL[0] -= 1                            # KHUAY IS DIRTY TO DIE 

    if STAT_VAL[4] > 50 :                               # POO > 50 -> POO TO MUCH
        if time % 5 == 0 :
            STAT_VAL[1] -= 1                            # POO TOO MUCH -> KHUAY HAS DEPRESSION

    if STAT_VAL[1] < 50 :
        if time % 15 == 0 :                             # KHUAY HAS DEPRESSION AND GONNA DIE
            STAT_VAL[0] -= 1
            if STAT_VAL[1] < 20 :                       # SUPER DEPRESSION AND GONNA DIE FASTER
                STAT_VAL[0] -= 1

    if STAT_VAL[1] < 100:
        if time % 5 == 0 :
            if STAT_VAL[0] >= 75 :                      # KHUAY IS HEALYTHY -> KHUAY IS HAPPY
                STAT_VAL[1] += 1
            if STAT_VAL[3] >= 75 :                      # KHUAY IS FULL -> KHUAY IS HAPPY
                STAT_VAL[1] += 1
            if STAT_VAL[4] <= 50 :                      # KHUAY DOESN'T WANT TO POOPOO -> KHUAY IS HAPPY
                STAT_VAL[1] += 1
            if STAT_VAL[7] >= 1000 :                    # KHUAY IS RICH -> KHUAY IS HAPPY
                STAT_VAL[1] += 1

    if STAT_VAL[0] < 100:
        if time % 20 == 0 :
            if STAT_VAL[1] >= 75 :                      # KHUAY IS HAPPY -> KHUAY IS HEALYTHY
                STAT_VAL[0] += 1

    for i in range(8) :                                 # CHECK STAT VAL NOT BE ABLE TO BE LESS THAN 0
        if STAT_VAL[i] < 0:
            STAT_VAL[i] = 0

    for i in range(6) :                                 # CHECK STAT VAL NOT BE ABLE TO BE MORE THAN 100 EXCEPT MONEY
        if STAT_VAL[i] > 100:
            STAT_VAL[i] = 100


def Random_Num() :
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return(num1,num2)

def typing_ans(Scence,surface,ans) :
    Scence.font = pygame.font.SysFont("arial.ttf", 60)
    Scence.text_ans = Scence.font.render(ans, True, "white")
    textRect_ans = Scence.text_ans.get_rect()
    textRect_ans.center = (557,195)
    surface.blit(Scence.text_ans,textRect_ans)

def click_sound() :
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\click_1.wav"))

def random_sound() :
    a = random.randint(1, 4)
    if a == 1 :
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds\like_1.wav"))
    elif a == 2 :
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds\like_2.wav"))
    elif a == 3 :
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds\like_3.wav"))
    else :
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds\like_4.wav"))

def correct():
    if STAT_VAL[6] < 50 :
        STAT_VAL[7] += 10
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruay.wav"))
    elif STAT_VAL[6] < 100 :
        STAT_VAL[7] += 20
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruay.wav"))
    elif STAT_VAL[6] < 150 :
        STAT_VAL[7] += 50
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruay_Laew.wav"))
    else :
        STAT_VAL[7] += 100
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruay_Laew.wav"))
    STAT_VAL[6] += 5

def incorrect() :
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruean.wav"))
    STAT_VAL[6] -= 1

class food:
    def __init__(self, price, P_Health, M_Health, enerygy, hunger, poopoo) :
        self.price = price
        self.P_Health = P_Health
        self.M_Health = M_Health
        self.energy = enerygy
        self.hunger = hunger
        self.poopoo = poopoo

    def buy_food(self) :
        if STAT_VAL[7] >= self.price :
            STAT_VAL[7] -= self.price
            STAT_VAL[0] += self.P_Health
            STAT_VAL[1] += self.M_Health
            STAT_VAL[2] += self.energy
            STAT_VAL[3] += self.hunger
            STAT_VAL[4] += self.poopoo
            STAT_VAL[5] -= 2
            random_sound()
        else :
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds\Ruean.wav"))

    def show_price(self,Scence,surface) :
        Scence.font = pygame.font.SysFont("arial.ttf", 48)
        Scence.text_price = Scence.font.render("Price : "+str(self.price)+" THB", True, "Black")
        textRect_price = Scence.text_price.get_rect()
        textRect_price.center = (400,30)
        surface.blit(Scence.text_price,textRect_price)

food_list = []
food_list.append(food(49,5,10,10,30,30))
food_list.append(food(159,10,10,15,50,25))
food_list.append(food(999,55,10,25,50,15))
food_list.append(food(29,10,10,10,10,15))
food_list.append(food(199,5,25,10,10,10))
food_list.append(food(555,-20,99,25,1,5))

class Scene:
    def on_draw(self, surface): pass
    def on_event(self, event): pass

class Manager:
    def __init__(self, caption, width, height, icon, flags=0):
        pygame.display.set_caption(caption)
        pygame.display.set_icon(icon)
        pygame.mixer.set_num_channels(2) # 0 = click effect
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.running = False
        self.scene = Scene()
        self.timer = 0
        self.time_sec = 0

    def main_loop(self):
        self.running = True
        while self.running:
            self.timer = pygame.time.get_ticks()
            if self.timer//1000 > self.time_sec :
                self.time_sec = self.timer//1000
                STAT_UPDATE(self.time_sec)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.scene.on_event(event)

            self.scene.on_draw(self.surface)
            pygame.display.flip()

class Intro(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\intro_bg.png")
        self.button = pygame.image.load("images\Button_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.button,((800-279)//2,600-209-20))

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if pygame.mixer.music.get_busy() == False :
            pygame.mixer.music.load("sounds\music_1.wav")  
            pygame.mixer.music.play()

        if event.type == pygame.MOUSEBUTTONUP:
            if posX >= (800-279)//2 and posX <= 800-279 and posY >= 600-209-20 and posY <= 600-20 :
                pygame.mixer.music.unload()
                click_sound()
                self.manager.scene = Main_Room(self.manager)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pygame.mixer.music.unload() 
                click_sound()
                RE_STAT()

class Main_Room(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\main_room_bg.png")
        self.Kh_Cat = pygame.image.load("images\Khuay_1.png")
        self.Kh_Cat_on_Bed = pygame.image.load("images\Khuay_2.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat,((800-300)//2,600-400-60))
        Stat_Bar(self,surface)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_2.wav")  
                pygame.mixer.music.play() 
            
            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 24 and posX <= 320 and posY >= 240 and posY <=406 :     
                    pygame.mixer.music.unload() 
                    click_sound()
                    self.manager.scene = Main_Room_on_Bed(self.manager) 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.unload() 
                    click_sound()
                    self.manager.scene = Intro(self.manager)

                if event.key == pygame.K_LEFT:
                    pygame.mixer.music.unload() 
                    click_sound()
                    self.manager.scene = Class_Room(self.manager)

                if event.key == pygame.K_RIGHT:
                    click_sound()
                    self.manager.scene = Bath_Room(self.manager)

                if event.key == pygame.K_DOWN:
                    click_sound()
                    self.manager.scene = Dining_Room(self.manager)

class Main_Room_on_Bed(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\main_room_sleeping.png")
        self.sleeping_time = 0
        self.sleeping_time_sec = 0
 
    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        Stat_Bar(self,surface)

    def on_event(self, event):
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\Sleeping_Sound.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP :
                self.sleeping_time = 0
                self.sleeping_time_sec = 0
                pygame.mixer.music.unload()
                click_sound()
                #self.sleeping_time = 5000
                self.manager.scene = Main_Room(self.manager)

        self.sleeping_time = pygame.time.get_ticks()
        if self.sleeping_time//1000 > self.sleeping_time_sec and STAT_VAL[2] <= 100:
                self.sleeping_time_sec = self.sleeping_time//1000
                STAT_VAL[2] += 2 # SLEEP TO EARN ENERGY


class Bath_Room(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Bath_room.png")
        self.Kh_Cat = pygame.image.load("images\Khuay_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat,((800-300)//2,600-400-60))
        Stat_Bar(self,surface)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_2.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 25 and posX <= 333 and posY >= 270 and posY <=410 :     
                    click_sound()
                    pygame.mixer.music.unload() 
                    self.manager.scene = Bath_Room_in_Bath(self.manager)

                if posX >= 583 and posX <= 712 and posY >= 128 and posY <=390 :     
                    click_sound()
                    pygame.mixer.music.unload() 
                    self.manager.scene = Bath_Room_on_poo(self.manager)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                click_sound()
                self.manager.scene = Main_Room(self.manager)

class Bath_Room_in_Bath(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Bath_room.png")
        self.Kh_Cat_in_Bath = pygame.image.load("images\Khuay_2.png")
        self.Bath_tub = pygame.image.load("images\Bath_tub.png")
        self.bath_time = 0
        self.bath_time_sec = 0

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat_in_Bath,(93,150))
        surface.blit(self.Bath_tub,(-155,1))
        Stat_Bar(self,surface)

    def on_event(self, event):    
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\Bath_Sound.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                self.bath_time = 0
                self.bath_time_sec = 0
                pygame.mixer.music.unload() 
                click_sound() 
                self.manager.scene = Bath_Room(self.manager) 

        self.bath_time = pygame.time.get_ticks()
        if self.bath_time//1000 > self.bath_time_sec and STAT_VAL[5] < 100:
                self.bath_time_sec = self.bath_time//1000
                STAT_VAL[5] += 5 # SLEEP TO EARN ENERGY

class Bath_Room_on_poo(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Bath_room.png")
        self.Kh_Cat_on_poo = pygame.image.load("images\Khuay_2.png")
        #self.button = pygame.image.load("images\Button_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat_on_poo,(93+457+15,150-40-10))
        Stat_Bar(self,surface)

    def on_event(self, event):    
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :
            if event.type == pygame.MOUSEBUTTONUP:
                click_sound()
                pygame.mixer.music.load("sounds\Flush_Sound.wav")  
                pygame.mixer.music.play() 
                self.manager.scene = Bath_Room(self.manager)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("sounds\Fart_Sound.wav")  
                    pygame.mixer.music.play()
                    if STAT_VAL[4] > 0 :
                        STAT_VAL[4] -= 1 
                        STAT_VAL[5] -= 0.25
                    else :
                        STAT_VAL[4] = 0

class Class_Room(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Class_room_1.png")
        self.Kh_Cat = pygame.image.load("images\Khuay_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat,((800-300)//2,600-400-60))
        Stat_Bar(self,surface)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :            
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_Classroom.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 81 and posX <= 81+80 and posY >= 94 and posY <=84+80 :     
                    click_sound() 
                    self.manager.scene = Class_Room_Plus(self.manager)

                if posX >= 81+160 and posX <= 81+80+160 and posY >= 94 and posY <=84+80 :     
                    click_sound() 
                    self.manager.scene = Class_Room_Minus(self.manager)
                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    click_sound()
                    pygame.mixer.music.unload() 
                    self.manager.scene = Main_Room(self.manager)
   
class Class_Room_Plus(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.SURFACE = 0
        self.background = pygame.image.load("images\Class_room_PLUS.png")
        self.Kh_Cat = pygame.image.load("images\Khuay_1.png")
        self.num1,self.num2 = Random_Num()
        self.ans = ""
        self.Ans_Box = False
        self.font = pygame.font.SysFont("arial.ttf", 60)
        self.text_num1 = self.font.render(str(int(self.num1)), True, "white")
        self.text_num2 = self.font.render(str(int(self.num2)), True, "white")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat,((800-300)//2,600-400-60))
        textRect_num1 = self.text_num1.get_rect()
        textRect_num2 = self.text_num1.get_rect()
        textRect_num1.center = (461,107)
        textRect_num2.center = (612,107)
        surface.blit(self.text_num1,textRect_num1)
        surface.blit(self.text_num2,textRect_num2)
        Stat_Bar(self,surface)
        typing_ans(self,surface,self.ans)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :            
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_Classroom.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 497 and posX <= 497+120 and posY >= 155 and posY <=155+80 :     
                    click_sound()
                    self.Ans_Box = True              

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    click_sound() 
                    self.manager.scene = Class_Room(self.manager)
                if self.Ans_Box == True :
                    if event.key == pygame.K_BACKSPACE: 
                        self.ans = self.ans[:-1]
                    elif event.key == pygame.K_RETURN: 
                        self.Ans_Box = False
                        if int(self.ans) == int(self.num1) + int(self.num2) :
                            correct()
                            self.manager.scene = Class_Room_Plus(self.manager)
                        else :
                            incorrect()
                        self.ans = ""
                        
                    elif len(self.ans) < 4 : 
                        self.ans += event.unicode

class Class_Room_Minus(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.SURFACE = 0
        self.background = pygame.image.load("images\Class_room_MINUS.png")
        self.Kh_Cat = pygame.image.load("images\Khuay_1.png")
        self.num1,self.num2 = Random_Num()
        self.ans = ""
        self.Ans_Box = False
        self.font = pygame.font.SysFont("arial.ttf", 60)
        self.text_num1 = self.font.render(str(int(self.num1)), True, "white")
        self.text_num2 = self.font.render(str(int(self.num2)), True, "white")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.Kh_Cat,((800-300)//2,600-400-60))
        textRect_num1 = self.text_num1.get_rect()
        textRect_num2 = self.text_num1.get_rect()
        textRect_num1.center = (461,107)
        textRect_num2.center = (612,107)
        surface.blit(self.text_num1,textRect_num1)
        surface.blit(self.text_num2,textRect_num2)
        Stat_Bar(self,surface)
        typing_ans(self,surface,self.ans)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)
        
        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)

        else :            
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_Classroom.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 497 and posX <= 497+120 and posY >= 155 and posY <=155+80 :     
                    click_sound()
                    self.Ans_Box = True              

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    click_sound() 
                    self.manager.scene = Class_Room(self.manager)
                if self.Ans_Box == True :
                    if event.key == pygame.K_BACKSPACE: 
                        self.ans = self.ans[:-1]
                    elif event.key == pygame.K_RETURN: 
                        self.Ans_Box = False
                        if int(self.ans) == int(self.num1) - int(self.num2) :
                            correct()
                            self.manager.scene = Class_Room_Minus(self.manager)
                        else :
                            incorrect()
                        self.ans = ""
                        
                    elif len(self.ans) < 4 : 
                        self.ans += event.unicode                 

class Dining_Room(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Dining_room.png")
        self.food_pic = []
        self.food_pic.append(pygame.image.load("images\Food_1.png"))
        self.food_pic.append(pygame.image.load("images\Food_2.png"))
        self.food_pic.append(pygame.image.load("images\Food_3.png"))
        self.food_pic.append(pygame.image.load("images\Food_4.png"))
        self.food_pic.append(pygame.image.load("images\Food_5.png"))
        self.food_pic.append(pygame.image.load("images\Food_6.png"))
        self.arrow_left = pygame.image.load("images\Arrow_left_1.png")
        self.arrow_right = pygame.image.load("images\Arrow_right_1.png")
        self.page = 0

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.arrow_left,(0,0))
        surface.blit(self.arrow_right,(0,0))
        surface.blit(self.food_pic[self.page],(0,0))
        Stat_Bar(self,surface)
        food_list[self.page].show_price(self,surface)

    def on_event(self, event):
        posX,posY = pygame.mouse.get_pos()
        if STAT_VAL[0] <= 0:
            pygame.mixer.music.unload() 
            self.manager.scene = Game_Over(self.manager)

        elif STAT_VAL[0] > 99 and STAT_VAL[6] >= 300 and STAT_VAL[7] >= 5000 :
            pygame.mixer.music.unload() 
            self.manager.scene = Win(self.manager)
            
        else :
            if pygame.mixer.music.get_busy() == False :
                pygame.mixer.music.load("sounds\music_2.wav")  
                pygame.mixer.music.play() 

            if event.type == pygame.MOUSEBUTTONUP:
                if posX >= 333 and posX <= 468 and posY >= 439 and posY <= 499 :     
                    click_sound()
                    food_list[self.page].buy_food()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                click_sound()
                self.manager.scene = Main_Room(self.manager)

            if event.key == pygame.K_LEFT:
                click_sound()
                if self.page > 0 :
                    self.page -= 1
                else :
                    self.page = 5
            if event.key == pygame.K_RIGHT:
                click_sound()
                if self.page == 5 :
                    self.page = 0
                else :
                    self.page += 1

class Game_Over(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Game_Over.png")
        #self.button = pygame.image.load("images\Button_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))

    def on_event(self, event):
        if pygame.mixer.music.get_busy() == False :
            pygame.mixer.music.load("sounds\GAME_OVER.wav")  
            pygame.mixer.music.play() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.unload() 
                click_sound()
                RE_STAT()
                self.manager.scene = Intro(self.manager)

class Win(Scene):
    def __init__(self, manager):
        self.manager = manager
        self.background = pygame.image.load("images\Game_Win.png")
        #self.button = pygame.image.load("images\Button_1.png")

    def on_draw(self, surface):
        surface.blit(self.background,(0,0))

    def on_event(self, event):
        if pygame.mixer.music.get_busy() == False :
            pygame.mixer.music.load("sounds\Win.wav")  
            pygame.mixer.music.play() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.unload() 
                click_sound()
                RE_STAT()
                self.manager.scene = Intro(self.manager)

if __name__ == "__main__":
    #check_stat()
    pygame.init() 
    icon = pygame.image.load("images\icon.png")
    manager = Manager("Khuay", 800, 600, icon)
    manager.scene = Intro(manager)
    manager.main_loop()
    pygame.quit()
    Read_Stat_file.close()
    Edit_Stat_file = open("Status.txt", "w")
    for i in range(8) :
        Edit_Stat_file.write(str(STAT_VAL[i])+"\n")
    Edit_Stat_file.close()
    Read_Default_Stat_file.close()