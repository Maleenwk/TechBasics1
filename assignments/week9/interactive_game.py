import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gardening Game")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 30)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 155, 0)
BROWN = (139, 69, 19)
BLUE = (0, 191, 255)
YELLOW = (255, 215, 0)


# Base Class
class Plant:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._growth = 0  # 0 = seed, 1 = sprout, 2 = full
        self._watered = False
        self._fertilized = False

    def draw(self, surface):
        raise NotImplementedError("Must be implemented in subclass.")

    def grow(self):
        if self._watered and self._fertilized and self._growth < 2:
            self._growth += 1
            self._watered = False
            self._fertilized = False

    def set_watered(self):
        self._watered = True

    def set_fertilized(self):
        self._fertilized = True

    def get_position(self):
        return (self._x, self._y)

    def get_growth(self):
        return self._growth


# Subclass: Flower
class Flower(Plant):
    def draw(self, surface):
        if self._growth == 0:
            pygame.draw.circle(surface, BROWN, (self._x, self._y), 5)
        elif self._growth == 1:
            pygame.draw.circle(surface, GREEN, (self._x, self._y), 10)
        elif self._growth == 2:
            pygame.draw.circle(surface, YELLOW, (self._x, self._y), 15)
            pygame.draw.circle(surface, BLUE, (self._x, self._y - 15), 5)


# Subclass: Vegetable
class Vegetable(Plant):
    def draw(self, surface):
        if self._growth == 0:
            pygame.draw.rect(surface, BROWN, (self._x - 5, self._y - 5, 10, 10))
        elif self._growth == 1:
            pygame.draw.rect(surface, GREEN, (self._x - 8, self._y - 8, 16, 16))
        elif self._growth == 2:
            pygame.draw.rect(surface, (255, 100, 0), (self._x - 10, self._y - 10, 20, 20))


# Start Screen
def start_screen():
    start_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50)
    while True:
        screen.fill(WHITE)
        title = FONT.render("Welcome to the Gardening Game!", True, GREEN)
        instr1 = FONT.render("Left Click: Plant (alternates Flower/Vegetable)", True, (0, 0, 0))
        instr2 = FONT.render("W: Water | F: Fertilize | Plants grow with both", True, (0, 0, 0))
        instr3 = FONT.render("Goal: Grow as many plants as you can!", True, (0, 0, 0))
        start_text = FONT.render("START", True, WHITE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))
        screen.blit(instr1, (WIDTH // 2 - instr1.get_width() // 2, 200))
        screen.blit(instr2, (WIDTH // 2 - instr2.get_width() // 2, 230))
        screen.blit(instr3, (WIDTH // 2 - instr3.get_width() // 2, 260))

        pygame.draw.rect(screen, GREEN, start_button)
        screen.blit(start_text, (start_button.x + 45, start_button.y + 15))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return


# Game Loop
def main():
    plants = []
    plant_toggle = True  # Alternate between Flower and Vegetable
    start_screen()

    while True:
        screen.fill((200, 255, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if plant_toggle:
                    plants.append(Flower(x, y))
                else:
                    plants.append(Vegetable(x, y))
                plant_toggle = not plant_toggle

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    for plant in plants:
                        plant.set_watered()
                elif event.key == pygame.K_f:
                    for plant in plants:
                        plant.set_fertilized()

        for plant in plants:
            plant.grow()
            plant.draw(screen)

        pygame.display.flip()
        clock.tick(30)


main()