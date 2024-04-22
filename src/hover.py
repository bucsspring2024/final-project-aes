import pygame

class Hover:
    """Creates and organizes hover boxes. 
    Attributes:
        image (pygame.surface.Surface): The image corresponding to each suggestion.
        rect (pygame.Rect): The rectangular area for the hover box. 
        hovered (bool): Indicates if the mouse is currently hovering over the hover area.
        hover_text (str): Text contained in the hover box.
        image_rect (pygame.Rect): The rectangular area occupied by the image within the hover box. 
    
    """
    
    def __init__ (self, image, position, size, hover_text):
        """Intializes a Hover object.

        Args:
            image (pygame.surface.Surface): The image corresponding to each suggestion.
            position (tuple): The position of each hover box.
            size (tuple): The size of each hover box.
            hover_text (str): The text displayed in the hover box.
        
        """
        self.image = image
        self.rect = pygame.Rect(position,size)
        self.hovered = False
        self.hover_text = hover_text

    def image_dimensions (self, surface, image):
        """ Set dimensions and positions of images within hover boxes. 
        Args:
            surface (pygame.surface.Surface): The surface to blit the image onto. 
            image (pygame.surface.Surface): The image displayed withing the hover boxes. 
        
        """
        self.image_rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery - 70))
        surface.blit(image,self.image_rect)
    
    def draw_hover_boxes (self, surface, hover_color, hover_text):
        """Draws the hover box and organizes the specific text displayed.

        Args:
            surface (pygame.surface.Surface): The surface the hover box is drawn on.
            hover_color (tuple): The color of the hover box.
            hover_text (str): The tezt displayed in the box.
        
        """
        
        if self.hovered:

            hover_rect = pygame.Rect (self.rect.right-100, self.rect.top-60, 350, 220)
            pygame.draw.rect (surface, hover_color, hover_rect)
            
            pop_up_font = pygame.font.SysFont ("rockwell", 13)
            bold_pop_up_font = pygame.font.SysFont ("rockwell", 13, bold=True)
            line_height = pop_up_font.get_linesize ()
            y = hover_rect.top + 10
               
            max_width = hover_rect.width - 20 

            for original_line in hover_text.split ('\n'):
                
                words = original_line.split ()
                current_line = ''
                
                for word in words:
                    
                    test_line = current_line + word + ' '
                
                    if pop_up_font.size (test_line)[0] <= max_width:
                        current_line = test_line
                        
                    else:
                        
                        if ':' in current_line:
                            ingredient_name, ingredient_function = current_line.split(':')
                            bold_surface = bold_pop_up_font.render(ingredient_name.strip() + ': ', True, "black")
                            pop_up_surface = pop_up_font.render(ingredient_function.strip(), True, "black")
                            bold_rect = bold_surface.get_rect()
                            surface.blit(bold_surface, (hover_rect.left + 10, y))
                            surface.blit(pop_up_surface, (hover_rect.left + 10 + bold_rect.width, y))
                        
                        else:
                            pop_up_surface = pop_up_font.render(current_line.strip(), True, "black")
                            surface.blit(pop_up_surface, (hover_rect.left + 10, y))
                        y += line_height
                        current_line = word + ' '
                        
                if current_line:
                    
                    if ':' in current_line:
                        ingredient_name, ingredient_function = current_line.split(':')
                        bold_surface = bold_pop_up_font.render(ingredient_name.strip() + ': ', True, "black")
                        pop_up_surface = pop_up_font.render(ingredient_function.strip(), True, "black")
                        bold_rect = bold_surface.get_rect()
                        surface.blit(bold_surface, (hover_rect.left + 10, y))
                        surface.blit(pop_up_surface, (hover_rect.left + 10 + bold_rect.width, y))
                    
                    else:
                        pop_up_surface = pop_up_font.render(current_line.strip(), True, "black")
                        surface.blit(pop_up_surface, (hover_rect.left + 10, y))
                    y += line_height 
                
    def is_hovered (self, mouse_pos):
        """Checks if mouse is hovering over the hover area.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: True when the area is hovered over, False if not hovered here. 
        
        """
        self.hovered = self.image_rect.collidepoint (mouse_pos)
        return self.hovered