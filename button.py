import pygame
import time

pygame.init()
FONT = pygame.font.SysFont("Georgia", 18)


class Button:

    buttons = []

    def __init__(self, width, height, x, y, text, enabled, clicked=False):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled
        self.draw()
        self.clicked = clicked
        self.buttons.append(self)

    def draw(self):
        import game
        button_text = FONT.render(self.text, True, "black")
        button = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        if self.enabled:
            if self.check_hover():
                pygame.draw.rect(game.screen, "white", button, 0, 5)
            else:
                pygame.draw.rect(game.screen, "gray", button, 0, 5)
            game.screen.blit(button_text, (self.x + 3, self.y + 3))
        else:
            pygame.draw.rect(game.screen, (64, 64, 64), button, 0, 5)
            game.screen.blit(button_text, (self.x + 3, self.y + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        if left_click and button.collidepoint(mouse_pos) and self.enabled:
            return True

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        if button.collidepoint(mouse_pos) and self.enabled:
            return True

    def set_clicked(self,val):
        self.clicked = val
