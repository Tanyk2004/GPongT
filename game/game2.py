import pygame
import sys

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
speed_increase_factor = 0.8  # Amount to increase speed each frame
increase_interval = 100  # Increase speed every 300 frames (5 seconds at 60 FPS)

# Create paddles and ball
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Score tracking
left_score = 0
right_score = 0
winning_score = 5  # Set a winning score

# Frame counter for speed increase
frame_count = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed

    # AI Movement
    if right_paddle.centery < ball.centery and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed
    if right_paddle.centery > ball.centery and right_paddle.top > 0:
        right_paddle.y -= paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    # Ball reset if it goes out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    elif ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2

    # Check for winning condition
    if left_score >= winning_score:
        print("Left Player Wins!")
        pygame.quit()
        sys.exit()
    elif right_score >= winning_score:
        print("Right Player Wins!")
        pygame.quit()
        sys.exit()

    # Increase ball speed over time
    frame_count += 1
    if frame_count % increase_interval == 0:
        ball_speed_x += speed_increase_factor
        ball_speed_y += speed_increase_factor

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

    pygame.display.flip()
    pygame.time.Clock().tick(60)

