import pygame
import webbrowser
import json

# Импортируем глобальные переменные
from global_vars import *

# Импортируем классы
from Objects.button import Button
from Objects.continue_button import ContinueButton
from Objects.wall import Wall
from Objects.player import Player
from Objects.gun import Gun
from Objects.trampoline import Trampoline
from Objects.monster import Monster


def load_level(filename):
    filename = "Data/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, gun, x, y = None, None, 0, 0

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '-':
                Wall(x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)
            elif level[y][x] == "G":
                gun = Gun(x, y, new_player)
            elif level[y][x] == "T":
                Trampoline(x, y)
            elif level[y][x] == "M":
                Monster('down', x, y)
            elif level[y][x] == 'm':
                Monster('flying', x, y)

    return new_player, gun


def load_last_scene():
    with open(SETTINGS_JSON) as f:
        settings = json.load(f)

    settings['scenes']['currency_screen'] = settings['scenes']['last_scene']
    settings['saves']['is_continue'] = True

    with open(SETTINGS_JSON, 'w') as f:
        f.write(json.dumps(settings))


def reset_value_to_scenes_variable(key, value):
    with open(SETTINGS_JSON) as f:
        settings = json.load(f)

    settings['scenes'][key] = value

    with open(SETTINGS_JSON, 'w') as f:
        f.write(json.dumps(settings))


def start_scr_loader():
    reset_value_to_scenes_variable("currency_screen", "start")


def start_screen(screen, text_on_screen, text_on_button_1, text_on_button_2):
    """
    Стартовый экран игры, на котором отображается надпись <text_on_screen>,
    кнопки для старта и продолжения игры
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с названием игры
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = SCREEN_WIDTH // 2 - text.get_width() // 2
    text_y = SCREEN_HEIGHT // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляры класса Button (кнопки для старта и продолжения)
    btn_1 = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
    )

    btn_2 = ContinueButton(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
    )

    # Кнопка с ссылкой на GitHub проекта
    btn_link = Button(
        screen, 50, 50
    )

    # Отрисовываем кнопки на нужных координатах
    btn_1.draw(
        (SCREEN_WIDTH - btn_width - 5) // 2 - btn_width // 2,
        SCREEN_HEIGHT // 2 - btn_height // 2 + 75,
        text_on_button_1, lvl_1_loader)

    btn_2.draw(
        (SCREEN_WIDTH + btn_width + 5) // 2 - btn_width // 2,
        SCREEN_HEIGHT // 2 - btn_height // 2 + 75,
        text_on_button_2, load_last_scene)

    btn_link.draw(
        btn_x=SCREEN_WIDTH - 70,
        btn_y=SCREEN_HEIGHT - 70,
        btn_text=None,
        action=go_link,
        btn_image='./Data/Images/git_icon.png')


def go_link():
    webbrowser.open(gh_link)


def lvl_1_loader():
    with open(SETTINGS_JSON) as f:
        settings = json.load(f)

    settings['saves']['coord_x'] = None
    settings['saves']['coord_y'] = None
    settings['saves']['have_gun'] = False
    settings['saves']['count_ammo'] = 20
    settings['saves']['count_health'] = 100

    with open(SETTINGS_JSON, "w") as f:
        f.write(json.dumps(settings))

    reset_value_to_scenes_variable("currency_screen", "lvl_1")


def lvl_2_loader():
    reset_value_to_scenes_variable("currency_screen", "lvl_2")


def lvl_3_loader():
    reset_value_to_scenes_variable("currency_screen", "lvl_3")


def win_scr_loader():
    reset_value_to_scenes_variable("currency_screen", "win")


def lose_scr_loader():
    reset_value_to_scenes_variable("currency_screen", "lose")


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

    text_x = SCREEN_WIDTH // 2 - text.get_width() // 2
    text_y = SCREEN_HEIGHT // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
    )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        SCREEN_WIDTH // 2 - btn_width // 2,
        SCREEN_HEIGHT // 2 - btn_height // 2 + 75,
        text_on_button, start_scr_loader)
