from settings import *
from pytmx.util_pygame import load_pygame 
from os.path import join

from sprites import Sprite

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("awsome pokimoon")

        # shi group
        self.all_sprtied = pygame.sprite.Group()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'hosue')

    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join( 'data', 'maps', 'world.tmx')) }
        

    def setup(self, tmx_map, player_start_pos):
        for x,y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf , self.all_sprtied)

    def run (self):
        while True:
            #merow event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            # SHI GAME LOGIC
            self.all_sprtied.draw(self.display_surface)

            pygame.display.update() 
if __name__ == '__main__':
    game = Game()
    game.run()




