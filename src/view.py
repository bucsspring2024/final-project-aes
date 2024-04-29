import pygame

class View ():
    """Class representing the view of the program.
        Attributes:
            width (int): The width of the screen.
            height (int): The height of the screen.
            screen: The pygame display surface
    """
    
    def __init__(self, width, height):
        """Initializes the View object with the width and height. 

        Args:
            width (int): The width of the screen. 
            height (int): The height of the screen. 
        """
        
        self.width = width 
        self.height = height 
        self.screen = pygame.display.set_mode ()
        
    def draw_text (self, text, font, color, position):
        """Draws the text on the screen. 

        Args:
            text (str): The text to be drawn on screen. 
            font: The font the text is written in. 
            color: The text's color. 
            position (tuple): The position where the text should be drawn.
        """
        text_surface = font.render (text, True, color)
        
        text_rect = text_surface.get_rect (center = position)
        self.screen.blit (text_surface, text_rect)