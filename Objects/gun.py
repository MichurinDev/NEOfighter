import pygame
from Functions.load_image_func import load_image
from global_vars import *
from Objects.bullet import Bullet
import json
import os


class Gun(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, Player) -> None:
        pygame.sprite.Sprite.__init__(gun_group)

        self.pos_x = pos_x
        self.pos_y = pos_y

        # Количество патронов
        if "settings.json" in os.listdir("./Data"):
            with open(SETTINGS_JSON) as f:
                settings = json.load(f)

            self.cartridges_counter = settings["saves"]["count_ammo"]

        else:
            self.cartridges_counter = 20

        # Игрок, имеющий это оружие
        self.player = Player

        # Направление стрельбы
        self.rotate_side = "right"

        self.image = load_image('./Sprites/gun.png')

        self.rect = self.image.get_rect().move(
            self.pos_x * PLATFORM_WIDTH, self.pos_y * PLATFORM_HEIGHT)

        self.new_game = True

    def shoot(self):
        # Если у игрока имеется оружие и хватает патронов..
        if self.cartridges_counter > 0 and self.player.get_weapon:

            bullet = Bullet(self.rect.centerx, self.rect.centery, self.player)
            bullets.add(bullet)

            self.cartridges_counter -= 1

    def update(self, screen):
        # Проверка на то, запустилась ли новая игра
        with open(SETTINGS_JSON) as f:
            settings = json.load(f)

        cur_cartridges = settings["saves"]["count_ammo"]
        cur_having = settings["saves"]["have_gun"]

        if cur_cartridges == 20 and not (cur_having) and self.new_game:

            self.player.get_weapon = False
            self.cartridges_counter = 20
            self.rect = self.image.get_rect().move(
                self.pos_x * PLATFORM_WIDTH, self.pos_y * PLATFORM_HEIGHT)
            self.new_game = False

        if self.player.get_weapon:
            # Привязка оружия к координатам игрока
            self.rect.y = self.player.rect.y + 35
            bullets.update(screen)

            if self.player.right:

                if self.rotate_side != "right":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "right"
                self.rect.x = self.player.rect.x + 20

            else:

                if self.rotate_side != "left":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rotate_side = "left"
                self.rect.x = self.player.rect.x - 20
        else:
            # Подбор оружия
            if self.rect.x - 20 <= self.player.rect.x <= self.rect.x + 20 and\
                    self.rect.y - 70 <= self.player.rect.y <= self.rect.y + 70:
                self.player.get_weapon = True

        screen.blit(self.image, self.rect)
