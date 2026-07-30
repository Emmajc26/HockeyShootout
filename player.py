"""import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED, BLUE, BLACK


class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED

        # Load player image
        self.image = pygame.image.load(
            "assets/images/player.png"
        ).convert_alpha()

        # Resize the image
        self.image = pygame.transform.scale(
            self.image,
            (80, 80)
        )

        # Create a rectangle based on the image
        self.rect = self.image.get_rect()

        self.rect.center = (150, HEIGHT // 2)

        self.speed = PLAYER_SPEED
        self.original_image = pygame.image.load(
        "assets/images/player.png"
        ).convert_alpha()

        self.original_image = pygame.transform.scale(
            self.original_image,
            (80, 80)
            )

        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.center = (150, HEIGHT // 2)
        self.facing_right = True


    def move(self):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Vertical movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player inside the screen
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

            if not self.facing_right:
                self.image = self.original_image
                self.facing_right = True
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

            if self.facing_right:
                self.image = pygame.transform.flip(
                    self.original_image,
                        True,   # Flip horizontally
                        False   # Don't flip vertically
        )
                self.facing_right = False


    def draw(self, screen):
        screen.blit(self.image, self.rect)"""
import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED

class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED

        self.image_right = pygame.image.load(
            "assets/images/player.png"
        ).convert_alpha()

        self.image_right = pygame.transform.scale(
            self.image_right,
            (80, 80)
        )

        self.image_left = pygame.transform.flip(
            self.image_right,
            True,
            False
        )

        # Start facing right
        self.image = self.image_right

        self.rect = self.image.get_rect()
        self.rect.center = (150, HEIGHT // 2)
        self.facing_right=True

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_left
            self.facing_right = False

        # Move right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.facing_right = True

        # Move up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed

        # Move down
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player inside the screen
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)