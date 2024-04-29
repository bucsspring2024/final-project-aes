import pygame
from src.controller import Skincare_Genie

def main():
    pygame.init()
    app = Skincare_Genie ()
    app.run()
    
if __name__ == '__main__':
    main()