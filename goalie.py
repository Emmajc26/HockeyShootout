import pygame
from settings import HEIGHT, GOALIE_SPEED, RED


class Goalie:
    def __init__(self):
        self.width = 30
        self.height = 80

        self.rect = pygame.Rect(
            900,
            HEIGHT // 2 - self.height // 2,
            self.width,
            self.height
        )

        self.speed = GOALIE_SPEED
        self.direction = 1

    def update(self):
        self.rect.y += self.speed * self.direction

        # Bounce off top/bottom of crease
        if self.rect.top <= 200:
            self.direction = 1

        if self.rect.bottom >= 500:
            self.direction = -1

    def save(self, puck):
        return self.rect.colliderect(puck.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)