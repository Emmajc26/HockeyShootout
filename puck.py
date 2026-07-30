"""import pygame
from settings import WIDTH, HEIGHT


class Puck:
    def __init__(self):
        self.speed = 12

        # Load the puck image
        self.image = pygame.image.load(
            "assets/images/Puck.png"
        ).convert_alpha()

        # Resize it
        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        # Create the collision rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.shooting = False
        self.owner = None
        self.original_image = self.image
        self.angle = 0

    def update(self, player):

        if self.owner == player and not self.shooting:
            self.rect.centerx = player.rect.right +5
            self.rect.centery = player.rect.centery + 25

        # Only move if the puck has actually been shot.
        elif self.shooting:
            self.rect.x += self.speed

            # Reset after leaving the screen.
            if self.rect.left > WIDTH:
                self.reset()
        self.angle += 15

        

        # Otherwise, do nothing.
        # The puck simply stays where it is on the ice.

    def pickup(self, player):
        # Pick up the puck if the player skates over it.
        if self.owner is None and not self.shooting:
            if self.rect.colliderect(player.rect):
                self.owner = player

    def shoot(self):
        # Shoot only if the player has possession.
        if self.owner is not None and not self.shooting:
            self.owner = None
            self.shooting = True

    def reset(self):
        self.shooting = False
        self.owner = None
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)"""
import pygame
from settings import WIDTH, HEIGHT


class Puck:
    def __init__(self):
        self.speed = 12

        # Load the puck image
        self.image = pygame.image.load(
            "assets/images/Puck.png"
        ).convert_alpha()

        # Resize it
        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        # Store original image for rotation later
        self.original_image = self.image
        self.angle = 0

        # Create collision rectangle
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.shooting = False
        self.owner = None

    def update(self, player):

        # Keep puck on the player's stick
        if self.owner == player and not self.shooting:

            if player.facing_right:
                # Stick is on the right side
                self.rect.centerx = player.rect.right + 5
                self.rect.centery = player.rect.centery + 25

            else:
                # Stick is on the left side
                self.rect.centerx = player.rect.left - 5
                self.rect.centery = player.rect.centery + 25

        # Move puck after shooting
        elif self.shooting:
            self.rect.x += self.speed

            # Reset after leaving the rink
            if self.rect.left > WIDTH:
                self.reset()

    def pickup(self, player):
        # Pick up puck when player touches it
        if self.owner is None and not self.shooting:
            if self.rect.colliderect(player.rect):
                self.owner = player

    def shoot(self):
        # Shoot only if player owns puck
        if self.owner is not None and not self.shooting:
            self.owner = None
            self.shooting = True

    def reset(self):
        self.shooting = False
        self.owner = None
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)