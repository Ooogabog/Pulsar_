import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))

num = 2
num = num +1
print(num)

run = True

imgload = pygame.image.load("asteroid.png")
img = pygame.transform.scale(imgload,(imgload.get_width()//4, imgload.get_height()//4))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        window.blit(img,(0,0))
        pygame.display.update()
pygame.quit()