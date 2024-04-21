import pygame
import json

pygame.init ()


BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80
CREAM = (255,253,244)
YELLOW = (255,255,237)
GREEN = (224, 252, 224)
PINK = (255,238,238)
ORANGE = (255,210,198)
BLUE= (176,224,230)
PURPLE = (217,210,235)
GREY = 	(251,247,245)

class Program:
    def __init__(self):
        pygame.init ()
           
        self.screen = pygame.display.set_mode ()
        self.dimensions = pygame.display.get_window_size()
        self.width = self.dimensions [0]
        self.height = self.dimensions [1]
        self.title_font = pygame.font.SysFont ('rockwell', 50)
        self.prompt_font = pygame.font.SysFont ('rockwell', 40)
        self.text_font = pygame.font.SysFont ('rockwell', 35)
        self.name_font = pygame.font.SysFont ("rockwell", 15)
        self.price_font = pygame.font.SysFont ("rockwell", 13)
        self.instructions_font = pygame.font.SysFont ("rockwell", 20)

        self.skin_concerns = ["pores", "acne and blemishes", "oiliness", "dryness", "fine lines and wrinkles", "skin irritation", "dullness", "uneven texture", "dark spots"]
        self.skin_types = ["normal", "combination", "oily", "sensitive", "dry"]
       
        self.concern_buttons = []
        self.type_buttons = []
        self.oil_cleanser_buttons = []       
        self.cleanser_buttons = []
       
        self.create_concern_buttons ()
        self.create_type_buttons ()
        
        self.selected_concerns = set ()
        self.selected_type = None
        self.clicked_button = None
        self.selected_products = []

    def create_concern_buttons (self):
        
        for i, concern in enumerate(self.skin_concerns[:2]):
            x = (self.width //5)- (BUTTON_WIDTH)
            y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = concern
           
            self.concern_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
       
        for i, concern in enumerate(self.skin_concerns[2:4]):
            x = (self.width //5) * 2- (BUTTON_WIDTH)
            y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = concern
           
            self.concern_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
           
        for i, concern in enumerate(self.skin_concerns[4:6]):
            x = (self.width //5) * 3.25 - (BUTTON_WIDTH)
            y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = concern
           
            self.concern_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
           
        for i, concern in enumerate(self.skin_concerns[6:8]):
            x = (self.width //5) * 4.5 - (BUTTON_WIDTH)
            y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = concern
           
            self.concern_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))

    def create_type_buttons (self):


        for i, type in enumerate(self.skin_types[:2]):
            x = (self.width //5) - (BUTTON_WIDTH//2) + 150
            y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = type
           
            self.type_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
       
        for i, type in enumerate(self.skin_types[2:3]):        
            x = (self.width //5) * 2 - (BUTTON_WIDTH//2) + 150
            y = (i + 5.5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
           
            text = type
           
            self.type_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
   
        for i, type in enumerate(self.skin_types[3:5]):
                x = (self.width //5) * 3 - (BUTTON_WIDTH//2) + 150
                y = (i + 5) * (self.height // (len(self.skin_concerns) + 1)) + 50 + 30 * i
            
                text = type
            
                self.type_buttons.append(Button(text, (x, y), (BUTTON_WIDTH, BUTTON_HEIGHT)))
            
    def run (self):
        self.screen.fill(CREAM)
        welcome_text = self.title_font.render("Welcome to Skincare Deviser", True, "black")
        welcome_box = welcome_text.get_rect(center=(self.width // 2, self.height//2))
        self.screen.blit(welcome_text, welcome_box)
        pygame.display.flip ()
        pygame.time.delay (2000)
        self.concerns_run ()
       
    def concerns_run(self):
            self.screen.fill(CREAM)
            concerns_prompt = self.prompt_font.render("Choose three skin concerns you want to address", True, "black")
            concerns_box = concerns_prompt.get_rect(center=(self.width // 2, self.height//2 - 100))
            self.screen.blit(concerns_prompt , concerns_box)
               
            for button in self.concern_buttons:
                button.draw_prompt_buttons(self.screen, text_font = self.text_font)
               
            self.prompt_displayed = True    
            pygame.display.flip ()
           
            running = True
            while running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit ()
                            exit ()
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                for button in self.concern_buttons:
                                    if button.is_clicked (event.pos):
                                        if button.text not in self.selected_concerns:
                                            self.selected_concerns.add(button.text)
                                            if len(self.selected_concerns) == 3:
                                                self.types_run ()
                                                break
                                                                               
    def types_run (self):  
            self.screen.fill(CREAM)
            type_prompt = self.prompt_font.render("What is your skin type?", True, "black")
            type_box = type_prompt.get_rect(center=(self.width // 2, self.height//2 - 100))
            self.screen.blit(type_prompt,type_box)
           
            for button in self.type_buttons:
                button.draw_prompt_buttons(self.screen, text_font = self.text_font)
               
            self.prompt_displayed = True    
            pygame.display.flip ()


            while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit ()
                            exit ()
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                for button in self.type_buttons:
                                    selected_type =  button.is_clicked (event.pos)
                                    if selected_type:
                                        self.selected_type = selected_type
                                        self.oil_cleanser_run()
                                        break
    
    def create_product_buttons (self, suggestions, color, x_button_spacing, x_offset, instruction_text):

            self.screen.fill (color)
            button_size = (70,50)
            y_button_spacing = 170
            x_button_spacing = x_button_spacing
            max_suggestions_in_row = 3
            x_offset = x_offset
            y_offset = 330
            image_size = (90,120)
            current_row = 0
            current_column = 0
            product_buttons = []
            hover_areas = []
            
            for i, text in enumerate(instruction_text):
                text_surface = self.instructions_font.render(text, True, "black")
                text_rect = text_surface.get_rect(center=(self.width // 2, 50 + i * 50))
                self.screen.blit(text_surface, text_rect)
                
            for i, suggestion in enumerate (suggestions):

                button_position = (x_offset + current_column * (button_size[0] + x_button_spacing), 
                                   y_offset + current_row * (button_size [1] + y_button_spacing),
                                   )
            
                button_text = suggestion ['name']
                button = Button (button_text, button_position, button_size)
                price_text = suggestion ["price"]
                button.draw_suggestions (self.screen, self.name_font, self.price_font, button_text, price_text)
                button_image = pygame.image.load(suggestion ["image"])
                button_image = pygame.transform.scale (button_image,image_size)

                hover_text = self.create_hover_text ([suggestion])
                image = Hover (button_image, button_position, button_size, hover_text)
                image.image_dimensions(self.screen,button_image)
                
                product_buttons.append (button) 
                hover_areas.append (image)
                
                current_column += 1
                if current_column >= max_suggestions_in_row:
                    current_row +=1
                    current_column = 0     
            return product_buttons, hover_areas
   
    def create_hover_text (self, suggestions):
        
        hover_text = ""
        for i, suggestion in enumerate(suggestions):
            
            ingredient_1 = suggestion["ingredient 1"] + ": " + suggestion["ingredient 1 function"]
            ingredient_2 = suggestion["ingredient 2"] + ": " + suggestion["ingredient 2 function"]
            ingredient_3 = suggestion["ingredient 3"] + ": " + suggestion["ingredient 3 function"]
            
            hover_text += ingredient_1 + '\n' + ingredient_2 + '\n' + ingredient_3 
    
        return hover_text
    
    def oil_cleanser_run (self):
        instruction_text = [
                "An oil cleanser is essential for cleaning off oil-based impurities like makeup and sunscreen",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category = "Oil Cleansers")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, YELLOW, 390, 210, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            for button in product_buttons:
                                
                                if button.is_clicked (event.pos):
                                    clicked_index = product_buttons.index(button)
                                    clicked_product = suggestions [clicked_index]
                                    self.selected_products.append(clicked_product)
                                    self.cleanser_run ()
                                    return
                                
                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white", hover_area.hover_text)
                                hovering = True
                        if not hovering:
                            self.create_product_buttons (suggestions, YELLOW, 390, 210,instruction_text)
                        
                        pygame.display.flip ()
    
    def cleanser_run (self):
        instruction_text = [
                "Water-based facial cleansers are essential for cleaning off water-based impurities",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category= "Cleansers")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, GREEN, 385, 230, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for button in product_buttons:
                            
                            if button.is_clicked (event.pos):
                                clicked_index = product_buttons.index(button)
                                clicked_product = suggestions [clicked_index]
                                self.selected_products.append(clicked_product)
                                self.toner_run ()
                                return

                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white",hover_area.hover_text)
                                hovering = True
                        if not hovering:
                             self.create_product_buttons (suggestions, GREEN, 385, 230, instruction_text)
                        pygame.display.flip ()
              
    def toner_run (self):
        instruction_text = [
                "Toners penetrate the skin to remove dead skin cells and hydrate the skin",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category= "Toners")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, PINK, 385, 230, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for button in product_buttons:
                            if button.is_clicked (event.pos):
                                clicked_index = product_buttons.index(button)
                                clicked_product = suggestions [clicked_index]
                                self.selected_products.append(clicked_product)
                                self.serum_run ()
                                return

                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white",hover_area.hover_text)
                                hovering = True
                        if not hovering:
                             self.create_product_buttons (suggestions, PINK, 385, 230, instruction_text)
                        pygame.display.flip ()
              
    def serum_run (self):
        instruction_text = [
                "Serums contain concentrated ingredients to target specific skin concerns",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category= "Serums")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, ORANGE, 390, 230, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for button in product_buttons:
                            if button.is_clicked (event.pos):
                                clicked_index = product_buttons.index(button)
                                clicked_product = suggestions [clicked_index]
                                self.selected_products.append(clicked_product)
                                self.moisturizer_run ()
                                return

                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white",hover_area.hover_text)
                                hovering = True
                        if not hovering:
                             self.create_product_buttons (suggestions, ORANGE, 390, 230, instruction_text)
                        pygame.display.flip ()
              
    def moisturizer_run (self):
        instruction_text = [
                "Moisturizers are essential for ensuring that skin is hydrated, preventing excess oil and breakouts",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category= "Moisturizers")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, PURPLE, 420, 210, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for button in product_buttons:
                                if button.is_clicked (event.pos):
                                    clicked_index = product_buttons.index(button)
                                    clicked_product = suggestions [clicked_index]
                                    self.selected_products.append(clicked_product)
                                    self.sunscreen_run ()
                                    return

                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white", hover_area.hover_text)
                                hovering = True
                        if not hovering:
                             self.create_product_buttons (suggestions, PURPLE, 420, 210, instruction_text)
                        pygame.display.flip ()  
              
    def sunscreen_run (self):
        instruction_text = [
                "Sunscreens are a necessary tool for protecing skin against harmful UV rays and free radical damage",
                "The suggestions below are tailored to your skin. Choose one that best suits you.",
                "Tip: Hover over pictures to read about the top three ingredients"
            ]
        
        suggestions = self.get_product_suggestions (category= "Sunscreens")
        product_buttons, hover_areas = self.create_product_buttons (suggestions, BLUE, 430, 220, instruction_text)
        pygame.display.flip ()
       
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for button in product_buttons:
                            if button.is_clicked (event.pos):
                                clicked_index = product_buttons.index(button)
                                clicked_product = suggestions [clicked_index]
                                self.selected_products.append(clicked_product)
                                self.final_routine_run ()
                                return

                    elif event.type == pygame.MOUSEMOTION:      
                        hovering = False                  
                        for hover_area in hover_areas:
                            if hover_area.is_hovered (pygame.mouse.get_pos ()):
                                self.create_hover_text (suggestions)
                                hover_area.draw_hover_boxes (self.screen, "white",hover_area.hover_text)
                                hovering = True
                        if not hovering:
                             self.create_product_buttons (suggestions, BLUE, 430, 220, instruction_text)
                        pygame.display.flip ()  
          
              
    def get_product_suggestions (self, category):
        
        suggestions = []
        with open('data.json', 'r') as f:
                data = json.load(f)

        products = data.get(category, [])

        selected_type = self.selected_type.lower()
         
        for product in products:
                if any(concern in product.get("skin concerns", []) for concern in self.selected_concerns): 
                    if selected_type in product.get("skin type", []) or "all skin types" in product.get("skin type", []):
                        suggestions.append(product)
        return suggestions
    
    def final_routine_run (self):

        instruction_text = [
                "Congratulations! You've built your skincare routine!" '\n'
                "Here are the products you've chosen:"
            ]
        
        suggestions = self.selected_products
        product_buttons, hover_areas = self.create_product_buttons (suggestions, GREY, 400, 220, instruction_text)
    
        exit_button = Button ("Exit", (self.width //2 + 270, self.height - 80), (200,50))
        return_button = Button ("Return to Start", (self.width //2 - 500, self.height - 80), (200,50))
        
        pygame.display.flip ()
        
        
        while True:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit ()
                        exit ()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if exit_button.is_clicked (event.pos):
                            pygame.quit ()
                            exit ()
                        elif return_button.is_clicked (event.pos):
                            self.selected_products = []
                            self.run ()
                    
                    exit_button.draw_prompt_buttons (self.screen, self.text_font)
                    return_button.draw_prompt_buttons(self.screen, self.text_font)
                
                pygame.display.flip ()        

class Button:
    def __init__(self, text, position, size):
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect (position,size)
        self.selected = False
    
    def draw_prompt_buttons(self, surface, text_font):
        
        font = text_font
       
        text_surface = font.render(self.text, True, "black")
       
        text_rect = text_surface.get_rect(center = (self.position [0] + self.size [0] //2,self.position [1] + self.size [1] //2 ))

        surface.blit(text_surface, text_rect)
   
    def draw_suggestions(self, surface, text_font, price_font, text, price_text):
        
        name_surface = text_font.render(text, True, "black")     
        name_rect = name_surface.get_rect(center = self.rect.center)
   
        price_surface = price_font.render(price_text, True, "black")
        price_rect = price_surface.get_rect(center=(self.rect.centerx, self.rect.centery + 20))
        
        surface.blit(name_surface, name_rect)
        surface.blit(price_surface, price_rect)
        
    def is_clicked(self, pos):
        clicked = self.position[0] < pos[0] < self.position[0] + self.size[0] and \
               self.position[1] < pos[1] < self.position[1] + self.size[1]
        if clicked:
            self.selected = True
            return self.text
        return None
  
class Hover:
    def __init__ (self, image, position, size, hover_text):
        self.image = image
        self.rect = pygame.Rect(position,size)
        self.hovered = False
        self.hover_text = hover_text
    def image_dimensions (self, surface, image):
       self.image_rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery - 70))
       surface.blit(image,self.image_rect)
    
    def draw_hover_boxes (self, surface, hover_color, hover_text):
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
        self.hovered = self.image_rect.collidepoint (mouse_pos)
        return self.hovered

program = Program()
program.run()
