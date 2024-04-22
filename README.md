[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588375&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Skincare Wizard
## CS110 Final Project  << Spring, 2024 >>

## Team Members

Arlene Shaji

***

## Project Description

<< Give an overview of your project >>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design


### Features

1. Personalizes products to skin concerns and skin types 
2. Images for each product 
3. Pop up boxes when hovering over images showing ingredients
4. Allows users to choose their own products 
5. Final screen showing all chosen products and gives option to restart

### Classes

- Skincare_Genie - controller class that handles events and runs the actual program
- Button - creates the clickable buttons for answers to prompts and selecting products
- Hover - draws and organizes text in the pop up boxes and checks if the mouse is hovering over an image

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Welcome Message  | Program is launched and the title is displayed as "Welcome to Skincare Genie" and appears for 2 seconds  |
|  2                   | Skin Concern Selection | Click on three skin concerns from the list and after the final is chosen, it switches to the next screen.      |
| 3                    | Skin Type Selection    |  Click on one skin type from the list and after it is chosen, it switches to the next screen. 
| 4                    | Product Selection    |  Hover over a product image and make sure the ingredients are specific to each product. Click on one product from the list and after it is chosen, it switches to the next screen. Repeat for every product screen. 
| 5                    | Final Routine    |  All of the chosen products are displayed. Hover over the images to make sure the pop-up boxes are displayed with specific ingredients. 
| 6                    | Exit Button  |  Click on the Exit button and verify the application closes. 
| 7                    | Return to Start Button  |  Click on the Return to Start button and verify goes back to the beginning and gives completely new suggestions. 