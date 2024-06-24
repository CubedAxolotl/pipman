import pygame #I am using Pygame as the game engine for this projec

pygame.init() #Initializing Pygame

win = pygame.display.set_mode((800,480)) #I create a win object containing the display screen size

pygame.display.set_caption("PipBoy") # This sets the window's name

pygame_icon = pygame.image.load("icon.png") # This creates an object from a png
pygame.display.set_icon(pygame_icon) # This takes that object and sets it as the icon for the app

#------ The Following are just formating settings-------
text_zise= 30 # Text side of the tab letters
text_font = pygame.font.SysFont("Monofonto",text_zise) # setting two font settings
text_font1 = pygame.font.SysFont("Monofonto", 25)
linewidth = 2 # Setting the width of the line that runs across the top

clock = pygame.time.Clock() # This sets a uniform fps


#This function is just a function to make drawing text on screen faster
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x,y))

#----- The following is just assinging rgb of the color pallete
pipcolor1 = (0,238,0)
pipcolor2 = (0,142,0)
pipcolor3 = (0,95,0)
pipcolor4 = (0,47,0)
pipcolortest = (255,0,0) # This is just red
pipcolor5 = (0,0,0)

#Logic :3
RADIOAC = False
DATAAC = False
STATAC = False
ITEMAC = False

# The following 5 funct are to display the tab you are on, look at the radio func to see how they are set up
def RADIO():
    win.fill(pipcolor5) # In pygame you have to manually refill the screen everytime you draw pic
    pygame.draw.lines(win, pipcolor1, False, ((0,25),(541,25), (541,15), (683,15),(683,25),(800,25)),linewidth) # This draws a solid line that travels from one side of the screen to the other
    pygame.draw.rect(win, pipcolor5, (570, 5, 86,16)) # This draws a black rectangle, color5 is black, leaving a empty space for the text
    draw_text("STAT", text_font, pipcolor1, 120,5) # These draw the title of the tabs
    draw_text("ITEMS", text_font, pipcolor1, 260,5)
    draw_text("NOTES", text_font, pipcolor1, 420,5)
    draw_text("RADIO", text_font, pipcolor1, 580,5)

    RADIOAC = True #Tab status
    DATAAC = False
    ITEMAC = False
    STATAC = False
def DATA():
    win.fill(pipcolor5)
    pygame.draw.lines(win, pipcolor1, False, ((0,25),(381,25), (381,15), (527,15),(527,25),(800,25)),linewidth)
    pygame.draw.rect(win, pipcolor5, (410, 5, 86,16))
    draw_text("STAT", text_font, pipcolor1, 120,5)
    draw_text("ITEMS", text_font, pipcolor1, 260,5)
    draw_text("NOTES", text_font, pipcolor1, 420,5)
    draw_text("RADIO", text_font, pipcolor1, 580,5)     
    RADIOAC = False
    DATAAC = True
    STATAC = False
    ITEMAC = False
def STAT():
    win.fill(pipcolor5)
    pygame.draw.lines(win, pipcolor1, False, ((0,25),(85,25), (85,15), (205,15),(205,25),(800,25)),linewidth)
    pygame.draw.rect(win, pipcolor5, (110, 5, 70,16))
    draw_text("STAT", text_font, pipcolor1, 120,5)
    draw_text("ITEMS", text_font, pipcolor1, 260,5)
    draw_text("NOTES", text_font, pipcolor1, 420,5)
    draw_text("RADIO", text_font, pipcolor1, 580,5)

    RADIOAC = False
    DATAAC = False
    ITEMAC = False
    STATAC = True
def ITEM():
    win.fill(pipcolor5)
    pygame.draw.lines(win, pipcolor1, False, ((0,25),(230,25), (230,15), (356,15),(356,25),(800,25)),linewidth)
    pygame.draw.rect(win, pipcolor5, (250, 5, 86,16))
    draw_text("STAT", text_font, pipcolor1, 120,5)
    draw_text("ITEMS", text_font, pipcolor1, 260,5)
    draw_text("NOTES", text_font, pipcolor1, 420,5)
    draw_text("RADIO", text_font, pipcolor1, 580,5)

    RADIOAC = False
    DATAAC = False
    ITEMAC = True
    STATAC = False
def test():
    #pygame.draw.rect(win, pipcolortest, (115,30, 85,30))
    draw_text("STATUS", text_font1, pipcolor1, 115,33)
    draw_text("SPECIAL", text_font1, pipcolor2, 190,33)
    draw_text("PERKS", text_font1, pipcolor3, 275,33)

# Dont mind this, it dont worky
def subTabIn():
    if DATAAC == True:
        test()

# This sets the rinning program off, dont delete, otherwise it dont run. Idk why
run = False
# The program starts running
run = True

# This is our while loo, where everything the program does go down
while run:
    clock.tick(100) #Sets a fps
    pygame.display.update() #updates display

    for event in pygame.event.get(): # This event handler check various key presses
        if event.type == pygame.QUIT: # If the X button in the is hit then it stops running
            run = False
        if event.type == pygame.KEYDOWN: # These check for the press of key and call a specifi func
            if event.key == pygame.K_i:
                print("i")
                STAT()
            elif event.key == pygame.K_k:
                print("k")
                ITEM()
            elif event.key == pygame.K_m:
                print("m")
                DATA()
            elif event.key == pygame.K_n:
                print("m")
                RADIO()
            elif event.key == pygame.K_RIGHT: # This dont worky, its a test.
                print("Right")
                subTabIn()
                print(DATAAC)
                
            
 # ------------- Thangs to know ----------
 # Keep while run as neat a possible
 # while run is not good rn, there is a bunch of nested else if
 # These should be put on their own function 
 # Don't draw inside of while run, it will get messy
 # Drawing is layered, things you draw first will be in the layer bellow others
 # This also means you need to fill the screan before changing to another tab, otherwise it would stack drawings

 # Meoww

pygame.quit()