import pygame
import random



WIDTH = 800
HEIGHT = 600                                         #WIDTH AND HEIGHT OF SCREEN AND REFRESH RATE 
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,355)                                   #COLORS
GREEN = (0,255,0)


pygame.init()                                        #PYGAME OBJECT
pygame.mixer.init()                               #REQUIRED FOR SOUND

screen = pygame.display.set_mode((WIDTH, HEIGHT))             #WINDOW CREATION
pygame.display.set_caption('MY GAME')
clock = pygame.time.Clock()                                                      #SPEED HANDELING 

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
                                                                                                                    #BULLETS FOR PLAYER TO SHOOT 
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)                             #INHERITS
        self.image = pygame.Surface((  50,40))                         #SOMTHING TO DRAW ON
        self.image.fill(GREEN)
         
        self.rect = self.image.get_rect()                            #RECT MANIPULATES RECTANGLES
        self.rect.centerx = WIDTH/2                                          #PUTS IN CENTER OF SCREEN 
        self.rect.bottom = HEIGHT-10                                   #PUTS TEN PLAVES FROM BOTTOM OF SCREEN
        
        self.speedx = 0
 
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
            
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0                             #MOVES SPRITE AND ENSURES IT DOES NOT RUN OF THE SCREEN 
            
    
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
    
        
            
        
            
        
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)                                                                  #THIS SPAWNS IN ENEMIES AND INHERITS FROM SPRITE
        self.image = pygame.Surface((30,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
                                                                                                                                    #MAKES THEM DROP FROM TOP
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(5,10)
    def update(self):
        self.rect.y += self.speedy
        
        if self.rect.top > HEIGHT +10:                                 #DEALS WITH WHEN THEY DROP TO THEM BOTTOM 
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)       #MAKES SURE THEY DROP FROM TOP
            self.rect.y = random.randrange(-100,-40)                  #APPEARS WITHIN LIMITS OF THE SCREEN
            self.speedy = random.randrange(10 ,15 )            #SPEED 

            



all_sprites = pygame.sprite.Group()                            #ALLOWS YOU TO HOLD AND MANAGE MULTIPLE SPRITE OBJECTS 

mobs = pygame.sprite.Group()

bullets = pygame.sprite.Group()

player = Player()

mob = Mob()

for i in range(8):         #SET AMOUNT OF MOBS SWPANING
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    


all_sprites.add(player)

running = True
while running:                                                               #THIS IS NEEDE TO STOP THE GAME 
    clock.tick(FPS)                                                             #KEEPS GAME THE RIGHT SPEED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                                                       #AS YOU WANT THE LOOP TO STOP THE GAME AT THE RIGHT TIME PY GAME KEEPS 
        elif event.type == pygame.QUIT:                                  #TRACK OF EVENT USING LOOPS EVENTS ARE INPUT PROCESSES
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    hits = pygame.sprite.spritecollide(player,mobs,False)
    
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    
    if hits:
        running = False
        
    
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()                              #FLIPS SCREEN NECESSARY AFTER DRAWRING 

pygame.quit()

        
        

        
        
        
            

         