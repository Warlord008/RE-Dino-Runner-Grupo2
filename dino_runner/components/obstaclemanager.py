import pygame
from dino_runner.components import text_utils
from dino_runner.components.cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS

class obstaclemanager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles)==0:
            self.obstacles.append(cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if (game.player.dino_rect.colliderect(obstacle.rect)):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles: 
            obstacle.draw(screen)

    def score(self):
        score, score_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score, score_rect)

