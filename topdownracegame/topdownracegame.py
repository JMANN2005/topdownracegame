import pygame
import math
from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((1200, 600))

pygame.display.set_caption("car go brooomm")
class Car():
    def __init__ (self, x, y, design):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 33
        self.angle = 0
        self.turn = math.pi/45
        self.vel = 5
        self.surface = pygame.image.load(design).convert()
        self.size = (self.width,self.height)
        self.scaled = pygame.transform.scale(self.surface, self.size)
        self.img = pygame.transform.rotate(self.scaled, (-self.angle / (math.pi/180)))
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
    def inputwasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.angle-=math.pi/45
        
        if keys[pygame.K_d]:
            self.angle+=math.pi/45
        
        if keys[pygame.K_w]:
            self.y -= self.vel*math.cos(self.angle)
            self.x += self.vel*math.sin(self.angle)
            
        if keys[pygame.K_s]:
            self.y += self.vel*math.cos(self.angle)
            self.x -= self.vel*math.sin(self.angle)    
    def draw(self):
        self.img = pygame.transform.rotate(self.scaled, (-self.angle / (math.pi/180)))
        win.blit(self.img, (self.x, self.y))
        
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
        bounds = pygame.Rect(car.x, car.y, car.width, car.height)
        if(self.rect.colliderect(bounds)):
            car.x = 46
            car.y = 400
            car.angle = 0
    def collisionwasd(self):
        bounds = pygame.Rect(carwasd.x, carwasd.y, carwasd.width, carwasd.height)
        if(self.rect.colliderect(bounds)):
            carwasd.x = 98
            carwasd.y = 400
            carwasd.angle = 0
        
    
car = Car(46,400,'simplecar(2).jpg')
carwasd = Car(98, 400, 'simplecar(3).jpg')
walls = []
#1200,700 screen
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
walls.append(Wall(400,260,800,20)) #5
walls.append(Wall(400,260,200,100)) #4
walls.append(Wall(900,390,150,100)) #6

finish = Wall(20,380,130,10)
white = 255,255,255
finish.setColor(white)
black = 0,0,0
run = True
while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        win.fill(black)
        car.input()
        carwasd.inputwasd()
        for wall in walls:
            wall.draw()
            wall.collision()
            wall.collisionwasd()
            
        finish.draw()
        car.draw()
        carwasd.draw()
        pygame.display.update()
pygame.quit()