import pygame
import random
pygame.init()
pygame.font.init()

#clock for time frames
clock = pygame.time.Clock()
FPS = 60

# now set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pulsar")

# set the background
def backgrounds(name):
    image = pygame.image.load("black.png")
    _,_,WIDTH,HEIGHT = image.get_rect()
    Tiles =[]
    for i in range(width//WIDTH +1):
        for j in range(height//HEIGHT +1):
            pos = (i*WIDTH, j*HEIGHT)
            Tiles.append(pos)
    return Tiles,image
def draw(window,background,bg_image):
    for Tile in background:
        window.blit(bg_image,Tile)

background,bg_image = backgrounds("black.png")

#spaceship
img = pygame.image.load("spaceships.png")
spaceship_img = pygame.transform.scale(img,(img.get_width()//8, img.get_height()//8))
spaceship_rect = spaceship_img.get_rect()
spaceship_rect.centerx = width // 2
spaceship_rect.bottom = height - 10
spaceship_speed = 7

#asteriod
img2 = pygame.image.load("asteroid.png")
asteroid_img = pygame.transform.scale(img2, (img2.get_width()//4, img2.get_height()//4))
asteroids = []
asteroid_speed = 6
spawn_delay =  800
last_spawn = pygame.time.get_ticks()

# defining a custom class to store asteriod information
class Asteriod:
    def __init__(self,rect):
        self.rect = rect
        self.scored = False


font = pygame.font.Font(None, 36)

menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            menu = False
    draw(window,background,bg_image)

    title = font.render("Pulsar", True, (255,255,255))
    instructions = font.render("Press Space to Start", True, (255,255,255))
    title_rect = title.get_rect(center = (width// 2, height//2 -80))
    instructions_rect = instructions.get_rect(center = (width//2, height//2 +20))
    window.blit(title,title_rect)
    window.blit(instructions,instructions_rect)
    pygame.display.update()

    clock.tick(FPS)

#game main loop
running = True
gameover = False
score = 0
gameover_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw(window,background,bg_image)

    if not gameover:
        asteroid_speed = 6 + score//5
        spawn_delay = max(300, 800 - score*10)
        #spaceship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship_rect.x -= spaceship_speed
        if keys[pygame.K_RIGHT]:
                spaceship_rect.x += spaceship_speed

            # spawning new asteriods
        now = pygame.time.get_ticks()
        if now-last_spawn > spawn_delay:
            last_spawn = now
            rect = asteroid_img.get_rect()
            rect.x = random.randint(0,width-rect.width)
            rect.y = -rect.height
            asteroids.append(Asteriod(rect))

            #asteroid collision and movement
        for a in asteroids:
            a.rect.y += asteroid_speed
            if a.rect.colliderect(spaceship_rect):
                 lives -= 1
                asteroids.remove(a)

                if lives <= 0:
                    gameover = True
                #score if passed
            if a.rect.y> spaceship_rect.bottom and not a.scored:
                a.scored = True
                score += 1
            # remove offscreen asteriods
        asteroids = [a for a in asteroids if a.rect.y<height]

            #Draw the screen, spaceships and asteriods
        window.blit(spaceship_img, spaceship_rect)
        for a in asteroids:
            window.blit(asteroid_img, a.rect)
        lives_text = font.render(f"Lives : {lives}", True , (255,0,0))
        lives_rect = lives_text.get_rect(topright = (width-10 , 10))
        window.blit(lives_text , lives_rect)
        score_text = font.render(f"score : {score}", True , (255,0,0))
        score_rect = score_text.get_rect(topleft = (10,10))
        window.blit(score_text , score_rect)


    else:
        gameover_timer += 1
        font = pygame.font.Font(None,36)
        gameovertext = font.render("GAME OVER",True,(255,0,0))
        scoretext = font.render(f"Score: {score}", True, (255,0,0))
        window.blit(gameovertext, (width//2-80,height//2-10))
        window.blit(scoretext, (width//2-50, height//2+10))
        if gameover_timer > FPS *2:
            running = False
    pygame.display.update()
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()











