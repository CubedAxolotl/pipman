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
colors = {"1": (0,238,0), "2": (0,142,0), "3": (0,95,0), "4": (0,47,0), "5": (0,0,0), "test": (255,0,0)}
#Logic
tabBools = {"stat": True, "item": False, "data": False, "radio": False}

subTabSelec = {"stat": 0, "item": 0, "data": 0, "radio": 0} #each tab has different subtabs, this is a list of each (only one rn)

subTabBounds = {"statL": 0, "itemL": 0, "dataL": 0, "radioL": 0, "statR": 2, "itemR": 10, "dataR": 3, "radioR": 0}
# The following 5 funct are to display the tab you are on, look at the radio func to see how they are set up
def STAT():
    pygame.draw.rect(win, colors['5'], ((0,0, 800,27)))
    pygame.draw.lines(win, colors['1'], False, ((0,25),(85,25), (85,15), (205,15),(205,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (110, 5, 70,16))
    draw_text("STAT", text_font, colors['1'], 120,5)
    draw_text("ITEMS", text_font, colors['1'], 260,5)
    draw_text("DATA", text_font, colors['1'], 420,5)
    draw_text("RADIO", text_font, colors['1'], 580,5)

    if subTabSelec == 0: #checks if subTabSelect is 0 and displays the subtab
        test()

def ITEM():
    pygame.draw.rect(win, colors['5'], ((0,0, 800,27)))
    pygame.draw.lines(win, colors['1'], False, ((0,25),(230,25), (230,15), (356,15),(356,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (250, 5, 86,16))
    draw_text("STAT", text_font, colors['1'], 120,5)
    draw_text("ITEMS", text_font, colors['1'], 260,5)
    draw_text("DATA", text_font, colors['1'], 420,5)
    draw_text("RADIO", text_font, colors['1'], 580,5)

def DATA():
    pygame.draw.rect(win, colors['5'], ((0,0, 800,27)))
    pygame.draw.lines(win, colors['1'], False, ((0,25),(381,25), (381,15), (517,15),(517,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (410, 5, 76,16))
    draw_text("STAT", text_font, colors['1'], 120,5)
    draw_text("ITEMS", text_font, colors['1'], 260,5)
    draw_text("DATA", text_font, colors['1'], 420,5)
    draw_text("RADIO", text_font, colors['1'], 580,5)     

def RADIO():
    pygame.draw.rect(win, colors['5'], ((0,0, 800,27)))
    pygame.draw.lines(win, colors['1'], False, ((0,25),(541,25), (541,15), (683,15),(683,25),(800,25)),linewidth) # This draws a solid line that travels from one side of the screen to the other
    pygame.draw.rect(win, colors['5'], (570, 5, 86,16)) # This draws a black rectangle, color5 is black, leaving a empty space for the text
    draw_text("STAT", text_font, colors['1'], 120,5) # These draw the title of the tabs
    draw_text("ITEMS", text_font, colors['1'], 260,5)
    draw_text("DATA", text_font, colors['1'], 420,5)
    draw_text("RADIO", text_font, colors['1'], 580,5)

def test():
    #pygame.draw.rect(win, colors['test'], (115,30, 85,30))
    draw_text("STATUS", text_font1, colors['1'], 115,33)
    draw_text("SPECIAL", text_font1, colors['2'], 190,33)
    draw_text("PERKS", text_font1, colors['3'], 275,33)
    
# This sets the rinning program off, dont delete, otherwise it dont run. Idk why
run = False
# The program starts running
run = True

# Basically moved the key events to this funct
def keyDetect():

        if event.type == pygame.KEYDOWN: # These check for the press of key and call a specifi func
            if event.key == pygame.K_i:
                print("i")
                tabBools["stat"] = True
                tabBools["item"] = False
                tabBools["data"] = False
                tabBools["radio"] = False
                print(tabBools)
            elif event.key == pygame.K_k:
                print("k")
                tabBools["stat"] = False
                tabBools["item"] = True
                tabBools["data"] = False
                tabBools["radio"] = False
                print(tabBools)
            elif event.key == pygame.K_m:
                print("m")
                tabBools["stat"] = False
                tabBools["item"] = False
                tabBools["data"] = True
                tabBools["radio"] = False
                print(tabBools)
            elif event.key == pygame.K_n:
                print("n")
                tabBools["stat"] = False
                tabBools["item"] = False
                tabBools["data"] = False
                tabBools["radio"] = True
                print(tabBools)
            elif event.key == pygame.K_RIGHT: # This dont worky, its a test.
                print("Right") 
                subTabPlus()
                print(subTabSelec)
            elif event.key == pygame.K_LEFT:
                print("Left")
                subTabMinus()
                print(subTabSelec)

# Now that the key events are separate, this will render the tabs based on a bool lis, the list is in line 29
def tabRender():
    if tabBools["stat"]:
        STAT()
    elif tabBools["item"]:
        ITEM()
    elif tabBools["data"]:
        DATA()
    elif tabBools["radio"]:
        RADIO()

def subTabPlus():
    if tabBools['stat']:
        subTabSelec["stat"]= subTabSelec["stat"]+1
    elif tabBools["item"]:
        subTabSelec["item"]= subTabSelec["item"]+1
    elif tabBools["data"]:
        subTabSelec["data"]= subTabSelec["data"]+1

def subTabMinus():
    if tabBools['stat']:
        subTabSelec["stat"]= subTabSelec["stat"]-1
    elif tabBools["item"]:
        subTabSelec["item"]= subTabSelec["item"]-1
    elif tabBools["data"]:
        subTabSelec["data"]= subTabSelec["data"]-1
# This is our while loo, where everything the program does go down
while run:
    clock.tick(100) #Sets a fps
    pygame.display.update() #updates display
    for event in pygame.event.get(): # This event handler check various key presses
        if event.type == pygame.QUIT: # If the X button in the is hit then it stops running
            run = False        
        keyDetect() # keys are detected
        tabRender() # the screen is updated.
 # ------------- Thangs to know ----------
 # Keep while run as neat a possible
 # while run is not good rn, there is a bunch of nested else if
 # These should be put on their own function 
 # Don't draw inside of while run, it will get messy
 # Drawing is layered, things you draw first will be in the layer bellow others
 # This also means you need to fill the screan before changing to another tab, otherwise it would stack drawings

 # Meoww


pygame.quit()