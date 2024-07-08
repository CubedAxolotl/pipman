import pygame #I am using Pygame as the game engine for this projec

pygame.init() #Initializing Pygame

win = pygame.display.set_mode((800,480)) #I create a win object containing the display screen size

pygame.display.set_caption("PipBoy") # This sets the window's name

pygame_icon = pygame.image.load("icon.png") # This creates an object from a png
pygame.display.set_icon(pygame_icon) # This takes that object and sets it as the icon for the app

#------ The Following are just formating settings-------
font30 = pygame.font.SysFont("Monofonto",30) # setting two font settings
font25 = pygame.font.SysFont("Monofonto", 25)
font20 = pygame.font.SysFont("Monofonto", 20)
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
    win.fill(colors["5"])
    pygame.draw.lines(win, colors['1'], False, ((0,25),(85,25), (85,15), (205,15),(205,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (110, 5, 70,16))
    draw_text("STAT", font30, colors['1'], 120,5)
    draw_text("ITEMS", font30, colors['1'], 260,5)
    draw_text("DATA", font30, colors['1'], 420,5)
    draw_text("RADIO", font30, colors['1'], 580,5)

    if subTabSelec["stat"] == 0: #checks if subTabSelect is 0 and displays the subtab
        #subtabs
        draw_text("STATUS", font25, colors['1'], 115,33)
        draw_text("SPECIAL", font25, colors['2'], 190,33)
        draw_text("PERKS", font25, colors['3'], 275,33)

        #bottom bar
        pygame.draw.rect(win, colors["3"], (0,460, 150, 470))
        pygame.draw.rect(win, colors["3"], (153,460, 494, 470)) ### Rectangles
        pygame.draw.rect(win, colors["3"], (650,460, 700, 470))

        draw_text("HP 171/171", font25, colors['1'], 20,463)
        draw_text("Level 19", font25, colors['1'], 180,463)  ### Letters
        draw_text("AP    80", font25, colors['1'], 680,463)

        pygame.draw.lines(win, colors["1"], True, ((250,465), (626, 465), (626, 475), (250,475)), linewidth) ### Lvl Bar

        pygame.draw.rect(win, colors["3"], (210,365, 75,75))
        pygame.draw.rect(win, colors["3"], (290,365, 50,75))

        pygame.draw.rect(win, colors["3"], (360,365, 75,75))
        pygame.draw.rect(win, colors["3"], (440,365, 50,75))
        pygame.draw.rect(win, colors["3"], (495,365, 50,75))
        pygame.draw.rect(win, colors["3"], (550,365, 50,75))

        pygame.draw.rect(win, colors["test"], (335,80, 128,256))

        pygame.draw.rect(win, colors["1"], (362,345, 70,10))
        pygame.draw.rect(win, colors["1"], (480,260, 70,10))
        pygame.draw.rect(win, colors["1"], (480,130, 70,10))
        pygame.draw.rect(win, colors["1"], (245,130, 70,10))
        pygame.draw.rect(win, colors["1"], (245,260, 70,10))
        pygame.draw.rect(win, colors["1"], (362,60, 70,10))
    if subTabSelec["stat"] == 1:
        draw_text("STATUS", font25, colors['2'], 40,33)
        draw_text("SPECIAL", font25, colors['1'], 115,33)
        draw_text("PERKS", font25, colors['2'], 200,33)

        #bottom bar
        pygame.draw.rect(win, colors["3"], (0,460, 150, 470))
        pygame.draw.rect(win, colors["3"], (153,460, 494, 470)) ### Rectangles
        pygame.draw.rect(win, colors["3"], (650,460, 700, 470))

        draw_text("HP 171/171", font25, colors['1'], 20,463)
        draw_text("Level 19", font25, colors['1'], 180,463)  ### Letters
        draw_text("AP    80", font25, colors['1'], 680,463)

        pygame.draw.lines(win, colors["1"], True, ((250,465), (626, 465), (626, 475), (250,475)), linewidth) ### Lvl Bar
    if subTabSelec["stat"] == 2:
        draw_text("SPECIAL", font25, colors['2'], 30,33)
        draw_text("PERKS", font25, colors['1'], 115,33)

        #bottom bar
        pygame.draw.rect(win, colors["3"], (0,460, 150, 470))
        pygame.draw.rect(win, colors["3"], (153,460, 494, 470)) ### Rectangles
        pygame.draw.rect(win, colors["3"], (650,460, 700, 470))

        draw_text("HP 171/171", font25, colors['1'], 20,463)
        draw_text("Level 19", font25, colors['1'], 180,463)  ### Letters
        draw_text("AP    80", font25, colors['1'], 680,463)

        pygame.draw.lines(win, colors["1"], True, ((250,465), (626, 465), (626, 475), (250,475)), linewidth) ### Lvl Bar


def ITEM():
    win.fill(colors["5"])
    pygame.draw.lines(win, colors['1'], False, ((0,25),(230,25), (230,15), (356,15),(356,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (250, 5, 86,16))
    draw_text("STAT", font30, colors['1'], 120,5)
    draw_text("ITEMS", font30, colors['1'], 260,5)
    draw_text("DATA", font30, colors['1'], 420,5)
    draw_text("RADIO", font30, colors['1'], 580,5)

def DATA():
    win.fill(colors["5"])
    pygame.draw.lines(win, colors['1'], False, ((0,25),(381,25), (381,15), (517,15),(517,25),(800,25)),linewidth)
    pygame.draw.rect(win, colors['5'], (410, 5, 76,16))
    draw_text("STAT", font30, colors['1'], 120,5)
    draw_text("ITEMS", font30, colors['1'], 260,5)
    draw_text("DATA", font30, colors['1'], 420,5)
    draw_text("RADIO", font30, colors['1'], 580,5)     

def RADIO():
    win.fill(colors["5"])
    pygame.draw.lines(win, colors['1'], False, ((0,25),(541,25), (541,15), (683,15),(683,25),(800,25)),linewidth) # This draws a solid line that travels from one side of the screen to the other
    pygame.draw.rect(win, colors['5'], (570, 5, 86,16)) # This draws a black rectangle, color5 is black, leaving a empty space for the text
    draw_text("STAT", font30, colors['1'], 120,5) # These draw the title of the tabs
    draw_text("ITEMS", font30, colors['1'], 260,5)
    draw_text("DATA", font30, colors['1'], 420,5)
    draw_text("RADIO", font30, colors['1'], 580,5)

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
    global tabBools
    global subTabSelec

    if tabBools['stat']:
        if subTabSelec["stat"] < subTabBounds["statR"]:  
            subTabSelec["stat"] += 1
    elif tabBools["item"]:
        if subTabSelec["item"] < subTabBounds["itemR"]:  
            subTabSelec["item"] += 1
    elif tabBools["data"]:
        if subTabSelec["data"] < subTabBounds["dataR"]:  
            subTabSelec["data"] += 1

def subTabMinus():
    global tabBools
    global subTabSelec

    if tabBools['stat']:
        if subTabSelec["stat"] > subTabBounds["statL"]:  
            subTabSelec["stat"] -= 1
    elif tabBools["item"]:
        if subTabSelec["item"] > subTabBounds["itemL"]:  
            subTabSelec["item"] -= 1
    elif tabBools["data"]:
        if subTabSelec["data"] > subTabBounds["dataL"]:  
            subTabSelec["data"] -= 1

# This is our while loo, where everything the program does go down
while run:
    clock.tick(100) #Sets a fps
    pygame.display.update() #updates display
    for event in pygame.event.get(): # This event handler check various key presses
        if event.type == pygame.QUIT: # If the X button in the is hit then it stops running
            run = False        
        keyDetect() # keys are detected
        tabRender() # the screen is updated.
        mousepos = pygame.mouse.get_pos()
        print(mousepos)
 # ------------- Thangs to know ----------
 # Keep while run as neat a possible
 # while run is not good rn, there is a bunch of nested else if
 # These should be put on their own function 
 # Don't draw inside of while run, it will get messy
 # Drawing is layered, things you draw first will be in the layer bellow others
 # This also means you need to fill the screan before changing to another tab, otherwise it would stack drawings

 # Meoww


pygame.quit()