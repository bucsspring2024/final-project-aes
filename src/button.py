import pygame

class Button:
    
    """Represents the clickable button object
    Attributes:
        text (str): The text displayed on the button.
        position (tuple): The position of the button.
        size (tuple): The size of the button. 
        rect (pygame.Rect): The rectangular area of the button. 
        selected (bool): Indicates whether the button was selected or not. 
    
    """
    def __init__(self, text, position, size):
        """Initializes the Button object

        Args:
            text (str): The text displayed on the button.
            position (tuple): The position of the button.
            size (tuple): The size of the button. 
            
        """
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect (position,size)
        self.selected = False
    
    def draw_prompt_buttons(self, surface, text_font):
        """Draws the prompt buttons on screen

        Args:
            surface (pygame.surface.Surface): The surface to draw the button on. 
            text_font (pygame.font.Font): The font the button text is written in. 
        
        """
        
        font = text_font
       
        text_surface = font.render(self.text, True, "navy blue")
       
        text_rect = text_surface.get_rect(center = (self.position [0] + self.size [0] //2,self.position [1] + self.size [1] //2 ))

        surface.blit(text_surface, text_rect)
   
    def draw_suggestions(self, surface, text_font, price_font, text, price_text):
        """Draws the suggestion and price text

        Args:
            surface (pygame.surface.Surface): The surface to draw the text on. 
            text_font (pygame.font.Font): The font the suggestion text is written in. 
            price_font (pygame.font.Font): The font the price text is written in. 
            text (str): The displayed suggestion text.
            price_text (str): The displayed price text.
        """
        name_surface = text_font.render(text, True, "black")     
        name_rect = name_surface.get_rect(center = self.rect.center)
   
        price_surface = price_font.render(price_text, True, "black")
        price_rect = price_surface.get_rect(center=(self.rect.centerx, self.rect.centery + 20))
        
        surface.blit(name_surface, name_rect)
        surface.blit(price_surface, price_rect)
        
    def is_clicked(self, pos):
        """Checks if the button is clicked. 

        Args:
            pos (tuple): The position that the mouse is clicked. 

        Returns:
            str or None: The text of the button if clicked, None if not clicked. 
        """
        clicked = self.position[0] < pos[0] < self.position[0] + self.size[0] and \
               self.position[1] < pos[1] < self.position[1] + self.size[1]
        if clicked:
            self.selected = True
            return self.text
        return None