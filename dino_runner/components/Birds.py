from dino_runner.components.obstacles import obstacle
import random

class birds(obstacle):
    def __init__(self,image):
        self.type = random.randint(0,2)    
        super().__init__(image,self.type)
        self.rect.y=380