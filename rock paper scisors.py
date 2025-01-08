# Import modules
import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
ROCK = 1
PAPER = 2
SCISSORS = 3
OPTIONS = [ROCK, PAPER, SCISSORS]
WIN = 1
LOSE = -1
TIE = 0
RESULT = {WIN: "You win!", LOSE: "You lose!", TIE: "It's a tie!"}
ACTION = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}

# Define colors
BLACK = (255, 0, 0)
WHITE = (0, 255, 0)

# Create a window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

# Create a font
font = pygame.font.SysFont("Arial", 32)

# Create a clock
clock = pygame.time.Clock()

# Create a flag to control the game loop
running = True

# Create a variable to store the user's choice
user_choice = None

# Create a variable to store the computer's choice
computer_choice = None

# Create a variable to store the result
result = None

# Create a function to compare the choices and return the result
def compare_choices(user, computer):
    if user == computer:
        return TIE
    elif (user == ROCK and computer == SCISSORS) or (user == PAPER and computer == ROCK) or (user == SCISSORS and computer == PAPER):
        return WIN
    else:
        return LOSE

# Start the game loop
while running:
    # Process events
    for event in pygame.event.get():
        # Handle the QUIT event
        if event.type == pygame.QUIT:
            running = False
        # Handle the MOUSEBUTTONDOWN event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            x, y = pygame.mouse.get_pos()
            # Check if the user clicked on the rock button
            if 100 <= x <= 300 and 200 <= y <= 400:
                user_choice = ROCK
            # Check if the user clicked on the paper button
            elif 350 <= x <= 550 and 200 <= y <= 400:
                user_choice = PAPER
            # Check if the user clicked on the scissors button
            elif 600 <= x <= 800 and 200 <= y <= 400:
                user_choice = SCISSORS
            # If the user made a choice, generate a random choice for the computer
            if user_choice is not None:
                computer_choice = random.choice(OPTIONS)
                # Compare the choices and get the result
                result = compare_choices(user_choice, computer_choice)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the buttons
    pygame.draw.rect(screen, BLACK, (100, 200, 200, 200), 5)
    pygame.draw.rect(screen, BLACK, (350, 200, 200, 200), 5)
    pygame.draw.rect(screen, BLACK, (600, 200, 200, 200), 5)

    # Draw the text
    screen.blit(font.render("Rock", True, BLACK), (175, 300))
    screen.blit(font.render("Paper", True, BLACK), (425, 300))
    screen.blit(font.render("Scissors", True, BLACK), (650, 300))

    # If the user and the computer made their choices, display them
    if user_choice is not None and computer_choice is not None:
        screen.blit(font.render("You chose: " + ACTION[user_choice], True, BLACK), (100, 50))
        screen.blit(font.render("Computer chose: " + ACTION[computer_choice], True, BLACK), (450, 50))
        screen.blit(font.render(RESULT[result], True, BLACK), (350, 500))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()