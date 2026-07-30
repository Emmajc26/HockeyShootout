import pygame
from settings import WIDTH, HEIGHT, GREEN


class Goal:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH - 40,
            HEIGHT // 2 - 75,
            20,
            150
        )

    def scored(self, puck):
        return self.rect.colliderect(puck.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect, 3)