import pygame
from settings import BLACK


class Scoreboard:

    def __init__(self):
        pygame.font.init()

        self.score = 0
        self.shots = 10

        self.font = pygame.font.SysFont("Arial", 30)
    def goal(self):
        if self.shots > 0:
            self.score += 1
            self.shots -= 1

    def miss(self):
        if self.shots > 0:
            self.shots -= 1
    def shot_taken(self):
        if self.shots > 0:
            self.shots -= 1
    def draw(self, screen):

        score = self.font.render(
            f"Goals: {self.score}",
            True,
            BLACK
        )

        shots = self.font.render(
            f"Shots Left: {self.shots}",
            True,
            BLACK
        )

        screen.blit(score, (20, 20))
        screen.blit(shots, (20, 60))