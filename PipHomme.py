import pygame #I am using Pygame as the game engine for this projec

pygame.init() #Initializing pygame

win = pygame.display.set_mode((800,480)) #I create a win object containing the display screen size

pygame.display.set_caption("PipBoy") # This sets the window's name

pygame_icon = pygame.image.load("icon.png") # This creates an object from a png
pygame.display.set_icon(pygame_icon) # This takes that object and sets it as the icon for the app

clock = pygame.time.Clock() # This sets a uniform fps


#This function is just a function to make drawing text on screen faster
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x,y))

while run:
    clock.tick(100) #Sets a fps
    pygame.display.update() #updates display
    for event in pygame.event.get(): # This event handler check various key presses
        if event.type == pygame.QUIT: # If the X button in the is hit then it stops running
            run = False        
        mousepos = pygame.mouse.get_pos()
        print(mousepos)



pygame.quit()