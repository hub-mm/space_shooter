# ./variables/constants.py
import pygame
pygame.init()


# CONSTANTS VARIABLES

# Window size
WINDOW_HEIGHT = pygame.display.Info().current_h - 75
WINDOW_WIDTH = WINDOW_HEIGHT - 200

# Colours
COLOUR_BACKGROUND = (0, 0, 0)
COLOUR_BULLET = (0, 255, 0)

# Window start caption
WINDOW_START_TEXT = 'Welcome to Space Shooter'
# Window start caption
WINDOW_TEXT = 'Space Shooter'
# Window shop caption
WINDOW_SHOP_TEXT = 'Space Shooter Shop'
# Window guide caption
WINDOW_GUIDE_TEXT = 'Space Shooter Guide'
# Window pause caption
WINDOW_GAME_PAUSE = 'Space Shooter Paused'

# Icon image
ICON_IMG_PATH = './img/target.png'

# Alien image
ALIEN_IMG_PATH = './assets/assets_img/alien.png'

# Spaceship
SPACESHIP_IMG_PATH = './assets/assets_img/spaceship.png'
SPACESHIP_INVINCIBLE_IMG_PATH = './assets/assets_img/spaceship_invincible.png'
START_SIZE = (75, 75)
# Start position
X = (WINDOW_WIDTH / 2) - (START_SIZE[0] / 2)
Y = WINDOW_HEIGHT - 85
# Restart position
START_X = (WINDOW_WIDTH / 2) - (START_SIZE[0] / 2)
START_Y = WINDOW_HEIGHT - 85

# Powerups
MIN_SPAWN = 1
MAX_SPAWN = 10
# Heart image
HEART_IMG_PATH = './img/heart.png'
# Coin image
COIN_IMG_PATH = './img/coin.png'
# Invincible image
INVINCIBLE_IMG_PATH = './assets/assets_img/invincible.png'

# Shop
PRICE_SPEED = 50
PRICE_EXTRA_SHOT = 50
PRICE_REDUCE_BULLET_GAP = 50
PRICE_EXTRA_COIN = 200