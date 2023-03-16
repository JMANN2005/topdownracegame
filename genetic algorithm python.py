import pygame
import math
from pygame.locals import *
from threading import Thread
pygame.init()
win = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("car go brooomm")
pos = 0

class Car():
    def __init__ (self, x, y,addDirection):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        self.angle = math.pi
        self.turn = math.pi/4
        self.vel = 5
        self.surface = pygame.image.load('simplecar(2).jpg').convert()
        self.size = (self.width,self.height)
        self.scaled = pygame.transform.scale(self.surface, self.size)
        self.img = pygame.transform.rotate(self.scaled, (-self.angle / (math.pi/180)))
        self.dead = False
        self.score = 0
        self.addDirection = addDirection
        self.moves = 0
        self.instructions = []
        self.pos = 0
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= self.turn
        
        if keys[pygame.K_RIGHT]:
            self.angle += self.turn
        
        if keys[pygame.K_UP]:
            self.y -= self.vel*math.cos(self.angle)
            self.x += self.vel*math.sin(self.angle)
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel*math.cos(self.angle)
            self.x -= self.vel*math.sin(self.angle)
    def fwd(self):
        self.y -= self.vel*math.cos(self.angle)
        self.x += self.vel*math.sin(self.angle)
    def left(self):
        self.angle -= self.turn
    def halfleft(self):
        self.angle -= self.turn/2
    def right(self):
        self.angle += self.turn
    def halfright(self):
        self.angle += self.turn/2
    def draw(self):
        self.img = pygame.transform.rotate(self.scaled, (-self.angle / (math.pi/180)))
        win.blit(self.img, (self.x, self.y))
    def setmoves(self):
        self.instructions = truemovelist.copy()
        self.instructions.append(self.addDirection)
    def nextmove(self):
        try:
            if (self.instructions[self.moves] == 0):
                self.left()
            elif (self.instructions[self.moves] == 1):
                self.halfleft()
            elif (self.instructions[self.moves] == 2):
                self.right()
            elif (self.instructions[self.moves] == 3):
                self.halfright()
            self.moves +=1
        except:
            self.moves += 1
    def reset(self):
        self.x = 60
        self.y = 400
        self.angle = math.pi
        self.moves = 0
        self.score = 0
        self.dead = False
        self.pos = 0
        
    
        
class Wall():
    def __init__(self, x, y, width,height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = 155,5,5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(win, self.color,self.rect)
    def setColor(self,color):
        self.color = color
    def collision(self):
        global pos
        for car in cars:
            bounds = pygame.Rect(car.x, car.y, car.width, car.height)
            if(self.rect.colliderect(bounds) and car.dead == False):
                car.dead = True
                car.pos = pos
                pos += 1
        
    
cars = []
cars.append(Car(60,400,0))
cars.append(Car(60,400,1))
cars.append(Car(60,400,2))
cars.append(Car(60,400,3))
cars.append(Car(60,400,4))
walls = []
#1200,600 screen
#x, y, width, height
#border
walls.append(Wall(0,0,1200,20))
walls.append(Wall(0,0,20,600))
walls.append(Wall(1180,0,20,600))
walls.append(Wall(0,580,1200,20))
#centers
walls.append(Wall(150,125,900,20)) #2
walls.append(Wall(150,125,100,325)) #1
walls.append(Wall(150,450,800,40)) #3
walls.append(Wall(400,260,850,20)) #5
walls.append(Wall(400,260,200,100)) #4
walls.append(Wall(900,390,200,100)) #6
walls.append(Wall(1125,0,75,75))

finish = Wall(20,380,130,10)
white = 255,255,255
finish.setColor(white)

truemovelist = []
for car in cars:
    car.setmoves()
    

black = 0,0,0
run = True
delay = 1
def changeDelay():
    global delay
    while True:
        delay = int(input())
changedelay = Thread(target = changeDelay)
changedelay.start()

while run:
        pygame.time.delay(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill(black)
        for car in cars:
            if car.dead == False:
                car.score += 1
                car.fwd()
                car.nextmove()
                car.draw()
        for wall in walls:
            wall.draw()
            wall.collision()
        
        reset = True
        for car in cars:
            if car.dead == False:
                reset = False
        #0,1,2,3,4
        if reset == True:
            for car in cars:
                if car.pos == 4:
                    truemovelist.append(car.addDirection)
                elif car.pos == 3:
                    streightBest = cars[4].score - car.score
            
            if cars[4].pos == 4:
                for i in range(0,streightBest):
                    truemovelist.append(4)
                
            for car in cars:
                car.setmoves()
                car.reset()
                reset = False
                pos = 0
                
                
        
        finish.draw()
        
        pygame.display.update()
pygame.quit()