# -*- coding: utf-8 -*-
import pygame as pg
import sys, random

# Konstanter
WIDTH = 400
HEIGHT = 600

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames per second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (130, 130, 130)
LIGHTBLUE = (120, 120, 255)

# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True

# Verdier for spilleren
w = 60 # bredde
h = 80 # høyde

# Startposisjon
x = WIDTH//2
y = HEIGHT - h -10

#Henter inn bilde til spilleren
player_img = pg.image.load("bucket.png")

#Henter bilde for bakgrunn
background_img = pg.image.load("background_snow_2-3.png")

#Tilpasser bakgrunnsbilde til skjermstørrelse
background_img = pg.transform.scale(background_img, SIZE)

# Henter font
font = pg.font.SysFont('Arial', 26)

# Antall poeng
points = 0

# Funksjon som viser antall poeng
def display_points():
    text_img = font.render(f"Antall poeng: {points}", True, WHITE)
    surface.blit(text_img, (20, 10))

def display_lives():
    lives_img = font.render(f"Antall liv: {lives}", True, WHITE)
    surface.blit(lives_img, (WIDTH-120, 10))

class Ball:
    def __init__(self):
        self.r = 25
        #self.x = WIDTH//2
        self.x = random.randint(self.r, WIDTH-self.r)
        self.y = -self.r
        self.vy =5
        self.ball_img = pg.image.load("orange.png")
        
    def update(self):
        self.vy = self.vy*1.005**(points/5)
        self.y += self.vy
    
    def draw(self):
        #pg.draw.circle(surface, WHITE, (self.x, self.y), self.r)
        #self.ball_img = pg.transform.scale(self.ball_img, (self.r))
        #surface.blit(self.ball_img, (self.x, self.y))
        scaled_image = pg.transform.scale(self.ball_img, (2*self.r, 2*self.r))
        surface.blit(scaled_image, (self.x - self.r, self.y - self.r))
        
lives = 3

# Lager et ball-objekt
ball = Ball()

# Spill-løkken
while run:
    # Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    # Går gjennom henselser (events)
    for event in pg.event.get():
        # Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes
            
            
    # Bruker bakgrunssbilde
    surface.blit(background_img, (0,0) )
    
    # Hastigheten til spilleren
    vx = 0
    
    # Henter knappene fra tastaturet som trykkes på
    keys = pg.key.get_pressed()
    
    # Sjekker om ulike taster trykkes på
    if keys[pg.K_LEFT] and x>0:
        vx = -5
        
    elif keys[pg.K_RIGHT] and x+w<WIDTH:
        vx = 5

    # Oppdaterer posisjonen til rektangelet
    x += vx
    
    
    # Ball
    ball.update()
    ball.draw()
    
    # Sjekker kollisjon
    if ball.y > y and x < ball.x < x+w:
        points += 1 # Øker antall poeng
        ball = Ball()
        
    # Sjekker om vi ikke klarer å fange ballen
    if ball.y + ball.r > HEIGHT:
        lives-=1
        ball = Ball()
        if lives == 0:
            print("Du klarte ikke å fange ballen")
            print(f"Du fikk {points} poeng")
            run = False # Game over
        
    
    # Spiller
    #pg.draw.rect(surface, GREY, [x, y, w, h])
    surface.blit(player_img, (x,y))
    display_lives()
    # Viser antall poeng på skjermen
    display_points()

    # "Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()


# Avslutter pygame
pg.quit()
sys.exit()