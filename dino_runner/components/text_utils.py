import pygame
FONT_STYLE = ('freesansbold.ttf', 30)
black_color = (0,0,0) 

def get_score_element(points):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Points: ' + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900,70)
    
    return text, text_rect