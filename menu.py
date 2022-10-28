import pygame

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 60)
TEXT_HIGHLIGHT_COLOR = (150, 250, 150)
TEXT_NORMAL_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 800
FIELD_WIDTH = 10
FIELD_HEIGHT = 10
CELL_WIDTH = 70
CELL_HEIGHT = 70
CELL_R = 30
GRAY = (120, 120, 120)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60

class Button:
    def __init__(self, text, effect, x0=0, y0=0):
        self.text = text
        self.effect = effect
        self.highlight = False
        self.y = y0
        self.x = x0
        self.texts = [
            lambda: font.render(self.text, True, TEXT_NORMAL_COLOR),
            lambda: font.render(self.text, True, TEXT_HIGHLIGHT_COLOR),
        ]

    def draw(self, offsetx, offsety):
        display.blit(self.texts[self.highlight](), (self.x + offsetx, self.y + offsety))

    def check_highlight(self, pos_x, pos_y):
        if (
            self.x <= pos_x <= self.x + self.texts[self.highlight]().get_width()
            and self.y <= pos_y <= self.y + self.texts[self.highlight]().get_height()
        ):
            self.highlight = True
        else:
            self.highlight = False

    def on_click(self):
        if self.highlight:
            self.effect(self)


class Cell:
    def __init__(self, color, x0=0, y0=0):
        self.color = color
        self.y = y0
        self.x = x0
        self.highlight = False

    def draw(self, offsetx, offsety):
        pygame.draw.circle(display, self.color, (offsetx + self.x * CELL_WIDTH + CELL_WIDTH // 2, offsety + self.y * CELL_HEIGHT + CELL_HEIGHT // 2), CELL_R)

    def check_highlight(self, pos_x, pos_y):
        if self.x <= pos_x <= self.x + CELL_WIDTH and self.y <= pos_y <= self.y + CELL_HEIGHT:
            self.highlight = True
        else:
            self.highlight = False

    def on_click(self):
        print("Click")


class Info:
    def __init__(self, getText, x0=lambda: 0, y0=lambda: 0):
        self.highlight = False
        self.y = y0
        self.x = x0
        self.getText = lambda: font.render(
            getText if isinstance(getText, str) else getText(), True, TEXT_NORMAL_COLOR
        )

    def draw(self, offsetx, offsety):
        display.blit(self.getText(), (self.x + offsetx, self.y + offsety))

    def check_highlight(self, pos_x, pos_y):
        if (
            self.x <= pos_x <= self.x + self.getText().get_width()
            and self.y <= pos_y <= self.y + self.getText().get_height()
        ):
            self.highlight = True
        else:
            self.highlight = False

    def on_click(self):
        return


class Menu:
    def __init__(self, buttons, offsetx, offsety):
        self.buttons = buttons
        self.offsetx, self.offsety = offsetx, offsety

    def draw(self):
        self.highlight()
        for y in range(len(self.buttons)):
            self.buttons[y].draw(self.offsetx, self.offsety)

    def highlight(self):
        x, y = pygame.mouse.get_pos()
        for button in self.buttons:
            button.check_highlight(x - self.offsetx, y - self.offsety)

    def on_click(self):
        for button in self.buttons:
            button.on_click()

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
