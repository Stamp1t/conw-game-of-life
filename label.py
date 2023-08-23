import pygame

pygame.init()
FONT = pygame.font.SysFont("Georgia", 18)


class Label:
    def __init__(self, x, y, text, enabled=True):
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled
        self.draw_text()

    def draw_text(self):
        import game
        if self.enabled:
            label_text = FONT.render(self.text, True, "red")
        else:
            label_text = FONT.render(self.text, True, "red")

        label = pygame.rect.Rect((self.x, self.y), (200, 30))
        pygame.draw.rect(game.screen, (40, 40, 40), label, 0, 0)
        game.screen.blit(label_text, (self.x + 3, self.y + 3))

