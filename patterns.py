import random
import numpy as np


class Paterns:
    @classmethod
    def draw_spaceship(cls, cells, pos):
        import game
        x = pos[0] // 10
        y = pos[1] // 10

        cells[y, x:x + 2] = 1
        cells[y + 1, x - 3:x + 3] = 1
        cells[y + 1, x] = 0
        cells[y + 2, x - 3:x + 2] = 1
        cells[y + 3, x - 2:x + 1] = 1

        game.update_gen(game.screen, cells, 10)

    @classmethod
    def draw_pulsar(cls, cells, pos):
        import game
        x = pos[0] // 10
        y = pos[1] // 10

        cells[y, x - 2:x + 1] = 1
        cells[y + 1: y + 4, x + 1] = 1
        cells[y + 5, x - 2:x + 1] = 1
        cells[y + 1: y + 4, x - 4] = 1

        cells[y - 2, x - 2:x + 1] = 1
        cells[y - 5: y - 2, x + 1] = 1
        cells[y - 7, x - 2:x + 1] = 1
        cells[y - 5: y - 2, x - 4] = 1

        cells[y - 2, x + 4:x + 7] = 1
        cells[y - 5: y - 2, x + 3] = 1
        cells[y - 7, x + 4:x + 7] = 1
        cells[y - 5: y - 2, x + 8] = 1

        cells[y + 5, x + 4:x + 7] = 1
        cells[y + 1: y + 4, x + 3] = 1
        cells[y, x + 4:x + 7] = 1
        cells[y + 1: y + 4, x + 8] = 1

        game.update_gen(game.screen, cells, 10)

    @classmethod
    def draw_vampire(cls, cells, pos):
        import game
        x = pos[0] // 10
        y = pos[1] // 10

        cells[y - 2: y + 2, x] = 1
        cells[y + 2: y + 4, x - 1] = 1
        cells[y + 2: y + 4, x + 1] = 1
        cells[y - 1, x + 1] = 1
        cells[y, x + 2] = 1
        cells[y + 1, x + 3] = 1
        cells[y - 1, x - 1] = 1
        cells[y, x - 2] = 1
        cells[y - 1, x - 3] = 1
        cells[y - 5:y - 2, x + 1] = 1
        cells[y - 5:y - 2, x - 1] = 1
        cells[y - 5, x] = 1

        game.update_gen(game.screen, cells, 10)

    @classmethod
    def draw_firework(cls, cells, pos):
        import game
        x = pos[0] // 10
        y = pos[1] // 10
        cells[y, x - 3:x + 3] = 1
        cells[y - 1, x - 1:x + 1] = 1
        cells[y - 2, x - 2] = 1
        cells[y - 2, x + 1] = 1

        game.update_gen(game.screen, cells, 10)

    @classmethod
    def draw_random(cls, cells, pos):
        import game
        x = pos[0] // 10
        y = pos[1] // 10
        for row, col in np.ndindex(cells.shape):
            cells[row, col] = random.randint(0,1)

        game.update_gen(game.screen, cells, 10)
