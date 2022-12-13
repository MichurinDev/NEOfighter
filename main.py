import pygame

'''
Objects
'''


class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width  # Длина кнопки
        self.height = height  # Ширина кнопки
        self.inactive_color = inactive_color  # Базовый цвет
        self.active_color = active_color  # Цвет при наведении

    def draw(self, btn_x, btn_y, btn_text=None, action=None):
        global alreadyPressed

        mouse = pygame.mouse.get_pos()  # Позиция мыши
        click = pygame.mouse.get_pressed()  # Обработка нажатия на кнопку мыши

        # Если курсор в пределах кнопки..
        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height:
            # Отрисовываем кнопку с цветом <active_color>
            pygame.draw.rect(
                screen,
                self.active_color,
                (btn_x, btn_y, self.width, self.height)
            )

            # Если по ней кликнули ЛКМ и ключ action задан
            if click[0] and action is not None:
                alreadyPressed = True
            else:
                if alreadyPressed:
                    action()
                    alreadyPressed = False

        # А ели за пределами кнопки..
        else:
            # Отрисовываем кнопку со стандартным цветом
            pygame.draw.rect(
                screen,
                self.inactive_color,
                (btn_x, btn_y, self.width, self.height)
            )

        _fontSize = 30
        # Отрисовываем текст на кнопке
        text_on_btn = pygame.font.Font(
                                    FONT,
                                    _fontSize
                                    )\
            .render(btn_text, True, COLORS['second_text'])
        screen.blit(
            text_on_btn,
            (btn_x + (self.width // 2 - text_on_btn.get_width() // 2),
                btn_y + (self.height // 2 - text_on_btn.get_height() // 2))
                )


def start_scr_loader():
    global ACTIVE_SCREEN
    ACTIVE_SCREEN = 'start'


def start_screen(screen, text_on_screen, text_on_button):
    """
    Конечный экран игры, на котором отображается надпись <text_on_screen>
    и кнопка перезапуска
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        text_on_button, lvl_1_loader)


def lvl_1_loader():
    global ACTIVE_SCREEN
    ACTIVE_SCREEN = 'lvl_1'


def lvl_1(screen):
    """
    Уровень 1
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render("Level 1", True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go to Lvl 2 ->", lvl_2_loader)


def lvl_2_loader():
    global ACTIVE_SCREEN
    ACTIVE_SCREEN = 'lvl_2'


def lvl_2(screen):
    """
    Уровень 2
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render("Level 2", True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        (width - btn_width - 5) // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go Win ->", win_scr_loader)

    btn2 = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn2.draw(
        (width + btn_width + 5) // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go Lose ->", lose_scr_loader)


def win_scr_loader():
    global ACTIVE_SCREEN
    ACTIVE_SCREEN = 'win'


def lose_scr_loader():
    global ACTIVE_SCREEN
    ACTIVE_SCREEN = 'lose'


def end_screen(screen, text_on_screen, text_on_button):
    """
    Конечный экран игры, на котором отображается надпись <text_on_screen>
    и кнопка перезапуска
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        text_on_button, start_scr_loader)


'''
Variables
'''

# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257"
}

FONT = './Fonts/retro-land-mayhem.ttf'  # Шрифт
ACTIVE_SCREEN = 'start'  # начальная сцена
alreadyPressed = False  # Переменная для считывании состоянии кнопки


"""
Main loop
"""

# Запускаем сие чудо
if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfighter")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Менеджер сцен
        if ACTIVE_SCREEN == "start":
            start_screen(screen, "NEOfighter", "Start Game!")
        elif ACTIVE_SCREEN == 'lvl_1':
            lvl_1(screen)
        elif ACTIVE_SCREEN == 'lvl_2':
            lvl_2(screen)
        elif ACTIVE_SCREEN == 'lose':
            end_screen(screen, "You Lose!", "Restart")
        elif ACTIVE_SCREEN == 'win':
            end_screen(screen, "You Win!", "Restart")
        pygame.display.flip()

    pygame.quit()
