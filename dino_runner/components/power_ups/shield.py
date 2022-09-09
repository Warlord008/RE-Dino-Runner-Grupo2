from dino_runner.components.power_ups.powerup import PowerUP
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class shield(PowerUP):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(shield,self).__init__(self.image, self.type)