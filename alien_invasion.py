import pygame

from Game.settings import Settings
from Game.ship import Ship
import Game.game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    # start main loop
    while True:
        # keyboard and mouse events
        gf.check_events()

        gf.update_screen(ai_settings, screen, ship)


run_game()

