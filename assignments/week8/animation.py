import pygame
import random
import math

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
NUM_CATS = 5

# Init Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wizard Cat Animation")
clock = pygame.time.Clock()

# Load and scale image
original_img = pygame.image.load("wizard_cat.jpeg").convert_alpha()
original_img = pygame.transform.scale(original_img, (80, 80))

# Cat class definition
class Cat:
    def __init__(self):
        # Random initial position
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        # Random speed
        self.speed = random.uniform(1, 3)
        # Random direction in radians
        self.angle = random.uniform(0, 2 * math.pi)
        # Optional: circular motion parameters
        self.circle_radius = random.randint(30, 100)
        self.circle_center_x = self.x
        self.circle_center_y = self.y
        self.circle_angle = random.uniform(0, 2 * math.pi)
        self.circle_speed = random.uniform(0.01, 0.05)

        # Tint variation
        tint = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.image = original_img.copy()
        tint_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint + (0,))
        self.image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

    def update(self):
        # Circular motion update
        self.circle_angle += self.circle_speed
        self.x = self.circle_center_x + math.cos(self.circle_angle) * self.circle_radius
        self.y = self.circle_center_y + math.sin(self.circle_angle) * self.circle_radius

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

# Create list of cat instances
cats = [Cat() for _ in range(NUM_CATS)]

# Main loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for cat in cats:
        cat.update()
        cat.draw(screen)

    pygame.display.flip()

pygame.quit()
exit()