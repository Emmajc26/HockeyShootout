import pygame
from settings import WIDTH, HEIGHT

# Colors
ICE = (225, 245, 255)
RED = (220, 40, 40)
BLUE = (50, 100, 255)
GOAL_RED = (180, 0, 0)
WHITE = (255, 255, 255)


def draw_rink(screen):
    # Ice
    screen.fill(ICE)

    # Boards
    pygame.draw.rect(screen, WHITE, (10, 10, WIDTH - 20, HEIGHT - 20), 8)

    # Center red line
    pygame.draw.line(
        screen,
        RED,
        (WIDTH // 2, 10),
        (WIDTH // 2, HEIGHT - 10),
        5
    )

    # Blue lines
    pygame.draw.line(
        screen,
        BLUE,
        (WIDTH * 0.25, 10),
        (WIDTH * 0.25, HEIGHT - 10),
        5
    )

    pygame.draw.line(
        screen,
        BLUE,
        (WIDTH * 0.75, 10),
        (WIDTH * 0.75, HEIGHT - 10),
        5
    )

    # Center faceoff circle
    pygame.draw.circle(
        screen,
        RED,
        (WIDTH // 2, HEIGHT // 2),
        60,
        4
    )

    pygame.draw.circle(
        screen,
        RED,
        (WIDTH // 2, HEIGHT // 2),
        6
    )

    # Offensive zone faceoff circles
    left_x = int(WIDTH * 0.15)
    right_x = int(WIDTH * 0.85)

    top_y = int(HEIGHT * 0.28)
    bottom_y = int(HEIGHT * 0.72)

    for x in (left_x, right_x):
        for y in (top_y, bottom_y):
            pygame.draw.circle(
                screen,
                RED,
                (x, y),
                40,
                3
            )

            pygame.draw.circle(
                screen,
                RED,
                (x, y),
                4
            )

    # Goal crease (right side)
    pygame.draw.arc(
        screen,
        BLUE,
        (
            WIDTH - 80,
            HEIGHT // 2 - 60,
            80,
            120
        ),
        1.57,
        4.71,
        4
    )

    # Goal line
    pygame.draw.line(
        screen,
        GOAL_RED,
        (WIDTH - 45, HEIGHT // 2 - 75),
        (WIDTH - 45, HEIGHT // 2 + 75),
        4
    )