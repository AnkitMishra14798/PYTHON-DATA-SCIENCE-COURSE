from ast import keyword
from turtle import speed
from g2 import HEIGHT

WIDTH = 1000
HEIGHT = 500

p = Actor('chick', (100,100))
e = Actor('walrus', (500,200))

p.speed = 3
e.speed = 2

def player_movement():
    if keyword.W:
        p.y -=p.speed
    if keyword.S:
        p.y += p.speed
    if keyword.A:
        p.y -= p.speed
    if keyword.D:
        p.y += p.speed

# boundry handling

if p.x < 0:
    p.x = WIDTH
if p.x > WIDTH:
    p.x = 0
if p.y < 0:
    p.y = HEIGHT
if p.y > HEIGHT:
    p.y = 0


def enemy_movement():
    if p.y > e.y:
        e.y += speed
        e.speed
    if p.y <= e.y:
        e.y -= e.speed
    if p.y > e.x:
        e.x += e.speed
    if p.y <= e.x:
        e.x -= e.speed
    
def draw():
    screen.clear()
    e.draw()
    p.draw()

def update():
    player_movement()
    enemy_movement()


WIDTH = 1000
HEIGHT = 500

p = Actor('chick', (100,100))
e = Actor('walrus', (500,200))

p.speed = 3
e.speed = 2

def player_movement():....
def enemy_movement():
     