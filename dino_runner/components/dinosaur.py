from typing_extensions import Self
import pygame

from dino_runner.utils.constants import RUNNING

class dinosaur():
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.image = RUNNING
        self.dino_rect = self.image


