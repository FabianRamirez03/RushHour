import pygame
import board
class Piece(pygame.sprite.Sprite):
    def __init__(self,x,y,width, height, letter, direction,typePiece, image):
        super(Piece, self).__init__()
        self.image = image
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        if direction == "h":
            self.letter = letter.upper()
        else:
            self.letter = letter.lower()
        self.direction = direction
        self.type = typePiece
        self.xMatrixPos = None
        self.yMatrixPos = None
        self.rectDraw = None

    def draw(self, surface):
        # draw piece on screen
        rect = pygame.rect.Rect(self.rect.x, self.rect.y, self.width, self.height)
        pygame.draw.rect(surface, board.get_piece_color(self.letter), rect)

    def delete(self):
        self.rect.x = 1000
        self.rect.y = 1000
        self.clicked = False
