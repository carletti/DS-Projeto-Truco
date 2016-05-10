import pygame

#definir parametros
FPS = 30
#cores          #R   G    B
WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)

#tamanho da tela
WIDTH = 800
HEIGHT = 600

#tamamho dos elementos
CARD_WIDTH = 120
CARD_HEIGHT = 180

TRUCO_WIDTH  = 80 #botão pra pedir truco
TRUCO_HEIGHT = 80

MANILHA_WIDTH = 120
MANILHA_HEIGHT = 30

DISPLAY_WIDTH = 120
DISPLAY_HEIGHT = 180

NAME_WIDTH = 120 #NAME  - displaynome dos jogadores
NAME_HEIGHT = 30

#####################################################
#definindo classes
class Card:
    def __init__(self, display, x, y, w, h):
        self.display = display
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.display, WHITE, (self.x, self.y, self.w, self.h))

    

class Button:
    def __init__(self, display, x, y, w, h):
        self.display = display
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.display, RED, (self.x, self.y, self.w, self.h))

    def activate(self, surface):
        if pygame.event.get_pressed(MOUSEBUTTONDOWN):
            pass
            #aparecer para o próximo jogador uma tela com: CAIR, FUGIR

class Info:
    def __init__(self, display, x, y, w, h):
        self.display = display
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.display, WHITE,  (self.x, self.y, self.w, self.h))
                         
class Card_Display:
    def __init__(self, display, x, y, w, h):
        self.display = display
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(self.display, YELLOW, (self.x, self.y, self.w, self.h))
        
        
###################################################################################
        
pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Truco')

clock = pygame.time.Clock()


carta1 = Card(display, 200, 400, CARD_WIDTH, CARD_HEIGHT)
carta2 = Card(display, 340, 400, CARD_WIDTH, CARD_HEIGHT)
carta3 = Card(display, 480, 400, CARD_WIDTH, CARD_HEIGHT)

truco = Button(display, 40, 420, TRUCO_WIDTH, TRUCO_HEIGHT)
manilha = Button(display, 650, 40, MANILHA_WIDTH, MANILHA_HEIGHT)

display1 = Card_Display(display, 200, 100, CARD_WIDTH, CARD_HEIGHT)
display2 = Card_Display(display, 340, 100, CARD_WIDTH, CARD_HEIGHT)
display3 = Card_Display(display, 480, 100, CARD_WIDTH, CARD_HEIGHT)
display4 = Card_Display(display, 650, 100, CARD_WIDTH, CARD_HEIGHT)
display5 = Card_Display(display, 60, 100, CARD_WIDTH, CARD_HEIGHT)

info1 = Info(display, 200, 60, NAME_WIDTH, NAME_HEIGHT)
info2 = Info(display, 340, 60, NAME_WIDTH, NAME_HEIGHT)
info3 = Info(display, 480, 60, NAME_WIDTH, NAME_HEIGHT)
info4 = Info(display, 60, 60, NAME_WIDTH, NAME_HEIGHT)



game_over = False

while not game_over:
    display.fill(DARK_GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    carta1.draw()
    carta2.draw()
    carta3.draw()
    
    truco.draw()
    manilha.draw()
    
    display1.draw()
    display2.draw()
    display3.draw()
    display4.draw()
    display5.draw()
    
    info1.draw()
    info2.draw()
    info3.draw()
    info4.draw()

    pygame.display.update()

    clock.tick(FPS)    

pygame.quit()
