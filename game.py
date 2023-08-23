import pygame
import numpy as np
import time
from button import Button
from patterns import Paterns
from label import Label

# constants

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (45, 181, 88)
COLOR_ALIVE_NEXT = (63, 255, 125)
HOVER = (255, 255, 255)

FONT = pygame.font.SysFont("Arial", 30)

pygame.init()
screen = pygame.display.set_mode((800, 600))


# marks the field you're currently hovering over
def set_hover(screen, cells, size_cell, mouse_pos, color):
    for row, col in np.ndindex(cells.shape):
        rec = pygame.rect.Rect((col * size_cell, row * size_cell), (size_cell - 1, size_cell - 1))

        if rec.collidepoint(mouse_pos) and cells[row, col] == 0:
            pygame.draw.rect(screen, color, rec)
        elif cells[row, col] == 0:
            pygame.draw.rect(screen, COLOR_BG, rec)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, False, text_color)
    screen.blit(img, (x, y))


# updates the current generation based on "game of life" rules and draws it
def update_gen(screen, cells, size_cell, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                if with_progress:
                    updated_cells[row, col] = 1
                    color = COLOR_ALIVE_NEXT

        else:
            if alive == 3:
                if with_progress:
                    updated_cells[row, col] = 1
                    color = COLOR_ALIVE_NEXT

        rec = pygame.rect.Rect((col * size_cell, row * size_cell), (size_cell - 1, size_cell - 1))

        pygame.draw.rect(screen, color, rec)

    return updated_cells


def main():
    # buttons
    generations = 0
    start_button = Button(80, 30, 650, 90, "    start", True)
    pause_button = Button(80, 30, 650, 160, "   pause", True)
    clear_button = Button(80, 30, 650, 230, "   clear", True)
    spaceship_button = Button(80, 30, 650, 330, " spaceship", True)
    pulsar_button = Button(80, 30, 650, 380, "   pulsar", True)
    vampire_button = Button(80, 30, 650, 430, " vampire", True)
    firework_button = Button(80, 30, 650, 480, " firework", True)
    random_button = Button(80, 30, 650, 530, " random", True)

    cells = np.zeros((60, 60))
    screen.fill(COLOR_GRID)
    update_gen(screen, cells, 10)
    pygame.display.update()

    select_mode = False  # chose a field to draw a precasted pattern there
    pause_mode = False  # pause
    pattern = None

    running = False

    while True:
        # check for button action

        for button in Button.buttons:
            button.draw()
            if button.check_click() and not button.clicked:
                button.clicked = True
                if button == start_button:
                    running = True
                    pause_mode = False
                elif button == pause_button:
                    running = False
                    pause_mode = True
                elif button == clear_button:
                    running = False
                    pause_mode = False
                    generations = 0
                    cells = np.zeros((60, 60))
                    update_gen(screen, cells, 10)
                elif button == spaceship_button:
                    select_mode = True
                    pattern = "spaceship"
                elif button == pulsar_button:
                    select_mode = True
                    pattern = "pulsar"
                elif button == vampire_button:
                    select_mode = True
                    pattern = "vampire"
                elif button == firework_button:
                    pattern = "firework"
                    select_mode = True
                elif button == random_button:
                    pattern = "random"

            if not button.check_click() and button.clicked:
                button.clicked = False

        # check for pygame events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEMOTION and not select_mode:
                # white hover when in "edit mode"
                mouse_pos = pygame.mouse.get_pos()
                set_hover(screen, cells, 10, mouse_pos, HOVER)
            if event.type == pygame.MOUSEMOTION and select_mode:
                # red hover when in "select mode"
                mouse_pos = pygame.mouse.get_pos()
                set_hover(screen, cells, 10, mouse_pos, "red")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

            if pygame.mouse.get_pressed()[0] and not running:
                pos = pygame.mouse.get_pos()
                if pattern == "random":
                    Paterns.draw_random(cells, pos)
                    pattern = None
                elif not select_mode:
                    # draw custom patterns
                    if pos[0] < 600:
                        cells[pos[1] // 10, pos[0] // 10] = 1
                        update_gen(screen, cells, 10)
                        pygame.display.update()
                else:
                    # looks for current pattern to draw a precasted pattern
                    match pattern:
                        case "spaceship":
                            if pos[0] < 600:
                                if select_mode:
                                    select_mode = False
                                Paterns.draw_spaceship(cells, pos)
                        case "pulsar":
                            if pos[0] < 600:
                                if select_mode:
                                    select_mode = False
                                Paterns.draw_pulsar(cells, pos)
                        case "vampire":
                            if pos[0] < 600:
                                if select_mode:
                                    select_mode = False
                                Paterns.draw_vampire(cells, pos)
                        case "firework":
                            if pos[0] < 600:
                                if select_mode:
                                    select_mode = False
                                Paterns.draw_firework(cells, pos)

        if not running:
            if select_mode:
                text = Label(650, 20, "Mode: Select")

            elif pause_mode:
                text = Label(650, 20, f"Generations: {generations}")
            else:
                text = Label(650, 20, "Mode: Edit")


        else:
            text = Label(650, 20, f"Generations: {generations} ")

        if running:
            cells = update_gen(screen, cells, 10, with_progress=True)
            pygame.display.update()

            time.sleep(0.01)
            generations += 1

        pygame.display.update()
        patterns_label = Label(650, 300, "Patterns")


if __name__ == "__main__":
    main()
