import pygame, os

win = pygame.display.set_mode((600, 600))
img = pygame.image.load(os.path.join(os.getcwd(), 'movemap.png'))
win.fill((0, 0, 0))
win.blit(img, (0, 0))
pygame.display.update()

run = True

while run:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            print(pos, win.get_at(pos), sep='\t\t')
            
            
            
            
pygame.quit()