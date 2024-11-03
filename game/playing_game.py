import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
paddle_speed = 5

# Ball settings
BALL_SIZE = 15
ball_speed_x, ball_speed_y = 3, 3
speed_increase_factor = 0.5  # Amount to increase speed each collision
max_ball_speed = 7           # Maximum speed cap for the ball

# Create paddles and ball
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Score tracking
left_score = 0
right_score = 0
winning_score = 5  # Set a winning score

# set up dynamic mechanics
dynamic_fns = []

# functions for control
def check_player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

def ai_movement():
    # AI Movement
    if left_paddle.centery < ball.centery and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if left_paddle.centery > ball.centery and left_paddle.top > 0:
        left_paddle.y -= paddle_speed

def check_collisions():
    global ball_speed_y, ball_speed_x, right_score, left_score
    # Ball collision with top and bottom, with boundary correction
    if ball.top <= 0:
        ball.top = 0
        ball_speed_y = -ball_speed_y
    elif ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x
        increase_speed()

    # Ball reset if it goes out of bounds
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    elif ball.right >= WIDTH:
        left_score += 1
        reset_ball()

def check_win():
    # Check for winning condition
    if left_score >= winning_score:
        print("Left Player Wins!")
        pygame.quit()
        sys.exit()
    elif right_score >= winning_score:
        print("Right Player Wins!")
        pygame.quit()
        sys.exit()

def increase_speed():
    global ball_speed_x, ball_speed_y
    if abs(ball_speed_x) < max_ball_speed:
        ball_speed_x += speed_increase_factor * (1 if ball_speed_x > 0 else -1)
    if abs(ball_speed_y) < max_ball_speed:
        ball_speed_y += speed_increase_factor * (1 if ball_speed_y > 0 else -1)

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    # Reset speed with a random direction
    ball_speed_x = 3 * random.choice((1, -1))
    ball_speed_y = 3 * random.choice((1, -1))
    
def updateScreen():
    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    font = pygame.font.Font(None, 36)
    score_text = f"{left_score} - {right_score}"
    text = font.render(score_text, True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

def add_dynamic_mechanic():
    function_code, summary = generate_ai_function(left_score + right_score)
    if function_code:
        # Load and execute the new mechanic
        new_mechanic = load_function_from_code(function_code, "new_mechanic")
        dynamic_mechanics.append(new_mechanic)  # Store the mechanic
        print(summary)  # Display summary in the game
        # Call the new mechanic if it’s callable
        if callable(new_mechanic):
            new_mechanic()  # Execute the new mechanic

# General variable modification function for the AI
def modify_variable(variable_name, new_value):
    if variable_name in globals():
        globals()[variable_name] = new_value
    else:
        print(f"Variable '{variable_name}' not found.")
        
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    check_player_movement()
    ai_movement()
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    check_collisions()
    check_win()
    updateScreen()

    pygame.display.flip()
    pygame.time.Clock().tick(60)