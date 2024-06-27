import pygame #I am using Pygame as the game engine for this projec

class pip():
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((800,480)) #I create a win object containing the display screen size

        pygame.display.set_caption("PipBoy") # This sets the window's name

        pygame_icon = pygame.image.load("icon.png") # This creates an object from a png
        pygame.display.set_icon(pygame_icon) # This takes that object and sets it as the icon for the app

        #------ The Following are just formating settings-------
        text_zise= 30 # Text side of the tab letters
        text_font = pygame.font.SysFont("Monofonto",text_zise) # setting two font settings
        text_font1 = pygame.font.SysFont("Monofonto", 25)
        linewidth = 2 # Setting the width of the line that runs across the top
        self.running = True
        self.actions = {"i": False, "k": False, "m": False, "n": False}
        clock = pygame.time.Clock()
        clock.tick()

    def pip_loop(self):
        while self.running:
            self.get_events()
            #self.update()
           # self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    self.actions['i'] = True
                if event.key == pygame.K_k:
                    self.actions['k'] = True
                if event.key == pygame.K_m:
                    self.actions['m'] = True
                if event.key == pygame.K_n:
                    self.actions['n'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i:
                    self.actions['i'] = True
                if event.key == pygame.K_k:
                    self.actions['k'] = True
                if event.key == pygame.K_m:
                    self.actions['m'] = True
                if event.key == pygame.K_n:
                    self.actions['n'] = True

if __name__ == "__main__":
    g = pip()
    while g.running:
        g.pip_loop()