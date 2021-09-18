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
red = (255, 0, 0)
yellow=(255,255,102)
image=pygame.image.load(r"C:\Users\karthik\Desktop\images\bg.png")
x1=0
y1=0
sp=pygame.image.load(r"C:\Users\karthik\Desktop\images\superhero.png")

def hero(x,y):
    dis.blit(sp,(x, y))
x = dis_w/2
y = dis_h/2
x_chg=0
y_chg=0 
font= pygame.font.Font('freesansbold.ttf',32)

def scr(count):
    
        score = font.render('Score:'+ str( count ),True,yellow)

        dis.blit(score,(0,0))
e=0

font1= pygame.font.Font('freesansbold.ttf',50)
def g():
    if gameovr==True:
            gover = font1.render('GAME OVER',True,red)
            dis.blit(gover,(250,250))

a=pygame.image.load(r"C:\Users\karthik\Desktop\images\asteroid.png")
def r(x2,y2):
        
         dis.blit(a,(x2,y2))
x2=random.randint(0,800)
y2=0
x2_chg=10
y2_chg=10
a1=pygame.image.load(r"C:\Users\karthik\Desktop\images\asteroid (2).png")
def r1(x3,y3):
        if e>=80:  
            dis.blit(a1,(x3,y3))
x3=random.randint(0,800)
y3=0
x3_chg=15
y3_chg=15
a2=pygame.image.load(r"C:\Users\karthik\Desktop\images\asteroid (3).png")
   
def r2(x4,y4):
        
            dis.blit(a2,(x4,y4))
x4=random.randint(0,800)
y4=900
x4_chg=15
y4_chg=15
a3=pygame.image.load(r"C:\Users\karthik\Desktop\images\asteroid (4).png")

def r3(x5,y5):
    if e>=200:     
        dis.blit(a3,(x5,y5))
x5=random.randint(0,800)
y5=0
x5_chg=25
y5_chg=25 

a4=pygame.image.load(r"C:\Users\karthik\Desktop\images\asteroid (5).png")
def r4(x6,y6):
    if e>=400:
        dis.blit(a4,(x6,y6))

x6=random.randint(0,800)
y6=0
x6_chg=10
y6_chg=10

def col(x,y,x2,y2,x3,y3,x5,y5,x6,y6):
    dis= math.sqrt((math.pow(x2-x,2)) + (math.pow(y2-y,2)))
    dis1=math.sqrt((math.pow(x3-x,2)) + (math.pow(y3-y,2)))
    dis2=math.sqrt((math.pow(x5-x,2)) + (math.pow(y5-y,2)))
    dis3=math.sqrt((math.pow(x6-x,2)) + (math.pow(y6-y,2)))
    
    if dis <=68 or dis1 <=74 or dis2 <=68 or dis3 <=80:
         return True


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
           
        if x<=-50:
            x=0
            
            
        elif x>=750:
            x=700
            
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
    if e>=80:
        x3 += x3_chg
        y3 += y3_chg  
    if  x3<=0  :
        x3_chg=5
            
            
    elif x3>=736  :
        x3_chg= -20
    
    if y3<=0:
        y3_chg=20

    elif y3>=600:
        y3=-5
    
    x4 += x4_chg
    y4 += y4_chg  
    if  x4<=0  :
        x4_chg=5
            
            
    elif x4>=736  :
        x4_chg= -5
    
    if y4<=0:
        y4_chg=5

    elif y4>=600:
        y4=-5
    
    if e>=200:
        x5 += x5_chg
        y5 += y5_chg  
    if  x5<=0  :
        x5_chg=25
            
            
    elif x5>=736  :
        x5_chg=-25
    
    if y5<=0:
        y5_chg=25

    elif y5>=580:
        y5_chg=-25
    if e>=400:
        x6 += x6_chg
        y6 += y6_chg  
    if  x6<=0  :
        x6_chg=25
            
            
    elif x6>=736  :
        x6_chg=-25
    
    if y6<=0:
        y6_chg=25

    elif y6>=580:
        y6=x6
    
    b=col(x,y,x2,y2,x3,y3,x5,y5,x6,y6)
    if b is True:
         
        gameovr=True
    
    clock.tick(10)
    dis.blit(image,(x1,y1))
    hero(x,y)
    r(x2,y2)
    r1(x3,y3)
    r2(x4,y4)
    r3(x5,y5)
    r4(x6,y6)
    g()
    scr(e)
    
    pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
