import pygame
import random
import math
import time

pygame.init()
dis_w=800
dis_h=600
dis = pygame.display.set_mode((dis_w, dis_h))
gameovr=False
pygame.display.set_caption('TRAIN YOUR HERO')
clock = pygame.time.Clock()
#red = (255, 0, 0)
#blue=(0,255,255)
yellow=(255,255,102)

image=pygame.image.load(r"C:\Users\Inder Raj\Downloads\star1.jpg")

x1=0
y1=0




sp=pygame.image.load(r"C:\Users\Inder Raj\Downloads\blackh-removebg-preview_1__1_-removebg-preview.png")

def hero(x,y):
    dis.blit(sp,(x, y))
    
        
pygame.display.update() 
x = dis_w/2
y = dis_h/2
x_chg=0
y_chg=0    
#font_style = pygame.font.SysFont(None, 50)
#def message(mem,color):
  #  mesg = font_style.render(mem, True, color)
   # dis.blit(mesg, [dis_w/2, dis_h/2])

rock=pygame.image.load(r"C:\Users\Inder Raj\Downloads\rock (2).png")

def r(x2,y2):
    dis.blit(rock,(x2,y2))
pygame.display.update() 
x2=random.randint(0,800)
y2=0
x2_chg=10   
y2_chg=10
rock1=pygame.image.load(r"C:\Users\Inder Raj\Downloads\asteroid.png")
def r1(x3,y3):
    dis.blit(rock1,(x3,y3))
pygame.display.update() 
x3=random.randint(0,800)
y3=0
x3_chg=5   
y3_chg=5
rock2=pygame.image.load(r'C:\Users\Inder Raj\Downloads\asteroid (3).png')
def r2(x4,y4):
    dis.blit(rock2,(x4,y4))
x4=random.randint(0,800)
y4=0
x4_chg=20   
y4_chg=20
pygame.display.update()

font= pygame.font.Font('freesansbold.ttf',32)
#sx=0
#sy=0

def scr(count):
    
        score = font.render('Score:'+ str( count ),True,yellow)

        dis.blit(score,(0,0))


def kar(x,y,x3,y3,x4,y4):
     
    dis= math.sqrt((math.pow(x3-x,2)) + (math.pow(y3-y,2)))
    dis1= math.sqrt((math.pow(x2-x,2)) + (math.pow(y2-y,2)))
    dis2= math.sqrt((math.pow(x4-x,2)) + (math.pow(y4-y,2)))
    if dis < 27 or dis1 < 23 or dis2 < 30:
            return True
    
    
    

e=0   
while not gameovr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameovr=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_chg = -30
                y_chg = 0
            elif event.key == pygame.K_RIGHT:
                x_chg = 30
                y_chg =0
        
            elif event.key == pygame.K_UP:
                y_chg = -30
                x_chg = 0
            elif event.key == pygame.K_DOWN:
                y_chg = 30
                x_chg = 0
        
        x += x_chg
        y += y_chg
           
        if x<=0  :
            x=0
            
            
        elif x>=736  :
            x=736
            
        if y<=0:
            y=0
        elif y>=540:
            y=490  
    e +=1 
    x2 += x2_chg
    y2 += y2_chg
        
    if x2<=0  :
        x2_chg=10
            
            
    elif x2>=736  :
        x2_chg= -10
    
    if y2<=0:
        y2_chg=10
        
    elif y2>=600:
        y2=-x2
    
    x3 += x3_chg
    y3 += y3_chg
        
    if x3<=0  :
        x3_chg=5
            
            
    elif x3>=736  :
        x3_chg= -5
    
    if y3<=0:
        y3_chg=30
        
    elif y3>=600:
        y3=-30

    x4 += x4_chg
    y4 += y4_chg
    if x4<=0  :
        x4_chg= 30

            
            
    elif x4>=736  :
        x4_chg= -30
    
    if y4<=0:
        y4_chg=300
        
    elif y4>=600:
        y4=x4
    b=kar(x,y,x3,y3,x4,y4)
    
    if b is True:
        gameovr=True
        print("yes")
    
    clock.tick(10)
    dis.blit(image,(x1,y1))
    r(x2,y2)
    r1(x3,y3)
    r2(x4,y4)
    #scr(sx,sy)
    scr(e)
    hero(x,y)
    
    
    pygame.display.update()
 

   
pygame.quit()
quit()