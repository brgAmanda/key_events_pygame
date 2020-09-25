import pygame, os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Eventos de tecla com Pygame")

image1 = pygame.image.load(os.path.join('images', 'bike.png')).convert()
image2 = pygame.image.load(os.path.join('images', 'lightning.png')).convert()

YImage2 = 0
run = True
index = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:  #KEYUP
            if event.key == pygame.K_SPACE and index == 0:
                screen.blit(image1, (250, 250))
                pygame.display.flip()
                index = 1

            elif event.key == pygame.K_RETURN and index == 1:
                screen.blit(image2, (250, YImage2))
                pygame.display.flip()
                index = 2

            elif event.key == pygame.K_DOWN and index == 2:
                while YImage2 <= 250: 
                    YImage2 += 1
                    screen.fill(0)
                    screen.blit(image2, (250, YImage2))
                    pygame.display.flip()


pygame.quit()
