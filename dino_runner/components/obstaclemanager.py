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
                if not game.player.shield:
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        game.player.has_lives = True
                        self.obstacles.pop()
                        start_transition_time = pygame.time.get_ticks()
                        game.player.lives_transition_time = start_transition_time + 1000
                        #if not game.player.shield:
                        #game.playing = False 
                        #game.death_count +=1
                        #break 
                    else:
                        pygame.time.delay(500)
                        game.death_count += 1
                        #self.obstacles.remove(obstacle) 
                        game.playing = False
                        break

    def draw(self, screen):
        for obstacle in self.obstacles: 
            obstacle.draw(screen)

    def score(self):
        score, score_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score, score_rect)

