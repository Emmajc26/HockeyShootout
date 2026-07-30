import pygame
from settings import *
from player import Player
from puck import Puck
from goalie import Goalie
from goal import Goal
from scoreboard import Scoreboard
from rink import draw_rink

MENU = 0
PLAYING = 1
GAME_OVER = 2


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hockey Shootout")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = MENU

        pygame.font.init()

        self.title_font = pygame.font.SysFont("Arial", 64)
        self.text_font = pygame.font.SysFont("Arial", 32)

        self.restart()

    def restart(self):
        self.player = Player()
        self.puck = Puck()
        self.goalie = Goalie()
        self.goal = Goal()
        self.scoreboard = Scoreboard()

    def draw_menu(self):
        self.screen.fill(LIGHT_BLUE)

        title = self.title_font.render("HOCKEY SHOOTOUT", True, BLACK)
        start = self.text_font.render("Press SPACE to Start", True, BLACK)

        self.screen.blit(
            title,
            (WIDTH // 2 - title.get_width() // 2, 180)
        )

        self.screen.blit(
            start,
            (WIDTH // 2 - start.get_width() // 2, 320)
        )

    def draw_game_over(self):
        self.screen.fill(LIGHT_BLUE)

        title = self.title_font.render("GAME OVER", True, RED)

        score = self.text_font.render(
            f"Goals Scored: {self.scoreboard.score}",
            True,
            BLACK
        )

        restart = self.text_font.render(
            "Press R to Play Again",
            True,
            BLACK
        )

        quit_text = self.text_font.render(
            "Press ESC to Quit",
            True,
            BLACK
        )

        self.screen.blit(
            title,
            (WIDTH // 2 - title.get_width() // 2, 160)
        )

        self.screen.blit(
            score,
            (WIDTH // 2 - score.get_width() // 2, 260)
        )

        self.screen.blit(
            restart,
            (WIDTH // 2 - restart.get_width() // 2, 340)
        )

        self.screen.blit(
            quit_text,
            (WIDTH // 2 - quit_text.get_width() // 2, 390)
        )

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:

                    # MENU
                    if self.state == MENU:

                        if event.key == pygame.K_SPACE:
                            self.restart()
                            self.state = PLAYING

                    # PLAYING
                    elif self.state == PLAYING:

                        if event.key == pygame.K_SPACE:

                            if (
                                not self.puck.shooting
                                and self.scoreboard.shots > 0
                            ):
                                self.scoreboard.shot_taken()
                                self.puck.shoot()

                    # GAME OVER
                    elif self.state == GAME_OVER:

                        if event.key == pygame.K_r:
                            self.restart()
                            self.state = PLAYING

                        elif event.key == pygame.K_ESCAPE:
                            self.running = False

            if self.state == PLAYING:

                self.player.move()
                self.puck.pickup(self.player)
                self.puck.update(self.player)
                self.goalie.update()

                if self.puck.shooting:

                    if self.goalie.save(self.puck):
                        self.puck.reset()

                    elif self.goal.scored(self.puck):
                        self.scoreboard.goal()
                        self.puck.reset()

                if self.scoreboard.shots <= 0:
                    self.state = GAME_OVER

            if self.state == MENU:

                self.draw_menu()

            elif self.state == PLAYING:

                draw_rink(self.screen)

                self.goal.draw(self.screen)
                self.goalie.draw(self.screen)
                self.player.draw(self.screen)
                self.puck.draw(self.screen)
                self.scoreboard.draw(self.screen)

            elif self.state == GAME_OVER:

                self.draw_game_over()

            pygame.display.flip()
