# ANGOIN Mattéo
# Classe de T13
# 14 octobre 2022
# Jeu "Space Invaders"

# Importation des bibliothèques
import pygame

# Déclaration des variables globales
WIDTH  = 224 * 2
HEIGHT = 256 * 2
BLACK  = (0, 0, 0)

# Déclaration de la classe Game
class Game:
    # Déclaration de la méthode Game.__init__
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Space Invaders')
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.is_main_screen = True
        self.is_game_screen = False
        self.is_over_screen = False
    
    # Déclaration de la méthode Game.display_main_screen
    def display_main_screen(self) -> None:
    
    
    # Déclaration de la métode Game.listen_keys
    def listen_keys(self) -> None:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
              pygame.quit()
            
        if self.is_main_screen and keys[K_UP]:
            pass
        
        
    # Déclaration de la méthode Game.main
    def main(self) -> None:
        self.surface.fill(BLACK) #
        while True:
            if self.is_main_screen:
                self.display_main_screen()
            if self.is_game_screen:
                pass
            if self.is_over_screen:
                pass
            pygame.display.update()
            pygame.time.Clock().tick(60)

# Vérification de l'arborescence
if __name__ == '__main__':
    game = Game()
    game.main()
