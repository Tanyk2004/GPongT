import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Moving Square")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Square properties
square_size = 50
x, y = width // 2, height // 2
speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the blue square
    pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit pygame
pygame.quit()
sys.exit()
