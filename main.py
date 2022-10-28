from menu import *


def startEffect(button):
    if button.text == "Start":
        button.text = "Restart"


menu = Menu([Button("Start", startEffect)], 0, 700)
field = Menu(
    [
        Cell(GRAY, i % FIELD_WIDTH, i // FIELD_WIDTH) for i in range(FIELD_WIDTH * FIELD_HEIGHT)
    ], 0, 0)

while True:
    menu.draw()
    menu.highlight()
    field.draw()
    field.highlight()
    pygame.display.update()
    display.fill(BACKGROUND_COLOR)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.on_click()