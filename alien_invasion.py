"""创建一系列整个有序都要用到的对象"""
import sys
import pygame
from pygame.sprite import Group

from alien import Alien
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("西理工大作战！")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Attack XAUT")

    # 创建一个用于存储游戏统计信息的实例，并且创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 测试语句，测试子弹是否删除，成功后就注释掉
            # print(len(bullets))
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
