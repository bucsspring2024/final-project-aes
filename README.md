[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588375&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Skincare Wizard
## CS110 Final Project  << Spring, 2024 >>

## Team Members

Arlene Shaji

***

## Project Description

The program asks the users about their main skin concerns and skin type and generates product suggestions based on this information. The users can choose products to add to their final routine using the ingredient and price information displayed. 

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
|  2                   | Skin Concern Selection | Click on acne and blemishes, pores, and oiliness from the list and after the final is chosen, it switches to the next screen.      |
| 3                    | Skin Type Selection    |  Click on sensitive from the list and after it is chosen, it switches to the next screen. 
| 4                    | Product Selection    |  Hover over the image of the Anua oil cleanser and the Kose oil cleanser and make sure the ingredients are specific to each product. Click on the Anua cleanser from the list and after it is chosen, it switches to the next screen. Repeat for every product screen choosing products in this order: Youth to the People cleanser, Tower 28 toner, SKIN 1004 serum, Dr. G moisturizer, and SKIN 1004 sunscreen. 
| 5                    | Final Routine    |  All of the chosen products listed in step 4 are displayed. Hover over the images to make sure the pop-up boxes are displayed with specific ingredients. 
| 6                    | Exit Button  |  Click on the Exit button and verify the application closes. 
| 7                    | Return to Start Button  |  Click on the Return to Start button and verify it goes back to the beginning. Choose new concerns: fine lines and wrinkles, dullness, and uneven texture, and a new skin type: combination. Ensure that the suggestions given are not the same set as the first round. 