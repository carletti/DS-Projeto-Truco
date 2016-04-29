# -*- coding: utf-8 -*-
""""Glossário com os comandos básicos do pygame""""


#Tela do jogo
class PyMain:
    def __init__(self, width, height):
        pygame.init()
        self.width = #number
        self.height = #number
        sel/f.screen = pygame.display.set_mode((self.width, self.height))
    
    def MainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
if __name__ = "__main":
    MainWindow = PyMain()
    MainWindow.MainLoop()
    
#Movimento das cartas:
""" class Cards(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image('card.ping', -1)
            self.pellets = 0
        
        def LoadSprites(self):
            self.card = Card()
            self.card_sprites = pygame.sprite.RendePlain((self.card))
        
        self.LoadSprites()
        self.card_sprites.draw(self.screen)
        pygame.display.flip()""""

#Ações:
if event.type == pygame.QUIT:
    sys.exit()
elif event.type == MOUSEBUTTONDOWN:
    self.card.move(event.key) #código 'rascunho'