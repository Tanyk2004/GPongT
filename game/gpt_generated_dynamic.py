import game.globals
import random
import pygame

import random

def introduce_random_obstacles():  # Adds random obstacles to the playing field to increase game difficulty
    obstacle_amount = random.randint(1, 3)
    screen = pygame.display.get_surface()
    obstacles = [pygame.Rect(random.randint(100, GameClass.WIDTH - 100), random.randint(50, GameClass.HEIGHT - 50), 20, 100) for _ in range(obstacle_amount)]
    for obstacle in obstacles:
        pygame.draw.rect(screen, GameClass.WHITE, obstacle)

def increase_paddle_speed_randomly():  # Occasionally increases the paddle speed for both players
    if random.choice([True, False]):
        game.globals.paddle_speed += random.uniform(0.5, 1.5)

def decrease_ball_size_every_hit():  # Decreases the size of the ball with each paddle hit, making it harder to hit
    if game.globals.ball_speed_x > 0:  # assuming the ball hit the right paddle
        GameClass.BALL_SIZE = max(5, GameClass.BALL_SIZE - 1)
    else:  # assuming the ball hit the left paddle
        GameClass.BALL_SIZE = max(5, GameClass.BALL_SIZE - 1)

# Summary: Introduced random obstacles to increase difficulty, added a mechanic to increase paddle speed randomly, and made the ball size decrease on paddle hit to add challenge.

def add_random_obstacles():  # Adds random obstacles to the game field that the ball needs to avoid
    import random
    if 'obstacles' not in game.globals:
        game.globals.obstacles = [pygame.Rect(random.randint(100, GameClass.WIDTH-100), random.randint(100, GameClass.HEIGHT-100), 20, 20) for _ in range(3)]
    for obstacle in game.globals.obstacles:
        pygame.draw.rect(GameClass.WHITE, GameClass.BLACK, obstacle)

def check_obstacle_collisions():  # Checks if the ball collides with the obstacles and deflects its direction
    for obstacle in game.globals.obstacles:
        if obstacle.colliderect(game_instance.ball):
            game_instance.direction[0] = -game_instance.direction[0]
            game_instance.direction[1] = -game_instance.direction[1]
            break

def change_ball_speed():  # Randomly changes the ball's speed during the game
    import random
    if random.randint(0, 100) < 5:
        game.globals.ball_speed_x = random.choice([-1, 1]) * random.uniform(2, game.globals.max_ball_speed)
        game.globals.ball_speed_y = random.choice([-1, 1]) * random.uniform(2, game.globals.max_ball_speed)

# Summary: Added functions to introduce random obstacles and dynamic ball speed changes to make the game more challenging. 

def spawn_random_obstacles():  # Spawns random obstacles on the playing field that changes every few seconds
    if not hasattr(spawn_random_obstacles, "obstacles"):
        spawn_random_obstacles.obstacles = []
    if random.random() < 0.01:  
        x_pos = random.randint(150, GameClass.WIDTH - 150)
        y_pos = random.randint(50, GameClass.HEIGHT - 50)
        new_obstacle = pygame.Rect(x_pos, y_pos, 20, 20)
        spawn_random_obstacles.obstacles.append(new_obstacle)
    for obstacle in spawn_random_obstacles.obstacles:
        pygame.draw.rect(GameClass.WHITE, obstacle)
    spawn_random_obstacles.obstacles = [ob for ob in spawn_random_obstacles.obstacles if ob.colliderect(GameClass.WIDTH, GameClass.HEIGHT)]

def manage_ball_speed_fluctuation():  # Let the ball fluctuate speeds randomly to increase unpredictability
    if not hasattr(manage_ball_speed_fluctuation, "ticks"):
        manage_ball_speed_fluctuation.ticks = 0
        manage_ball_speed_fluctuation.original_speed_x = game.globals.ball_speed_x
    manage_ball_speed_fluctuation.ticks += 1
    if manage_ball_speed_fluctuation.ticks % 120 == 0:  # Changes speed every 2 seconds
        fluctuation = random.choice([-1, 1]) * random.uniform(0.5, 2.0) 
        game.globals.ball_speed_x += fluctuation
        game.globals.ball_speed_x = max(min(game.globals.ball_speed_x, game.globals.max_ball_speed), -game.globals.max_ball_speed)

def dynamic_paddle_shrink():  # Gradually shrinks the paddle size over time to make gameplay harder
    if not hasattr(dynamic_paddle_shrink, "counter"):
        dynamic_paddle_shrink.counter = 0
    dynamic_paddle_shrink.counter += 1
    if dynamic_paddle_shrink.counter % 300 == 0 and GameClass.PADDLE_HEIGHT > 20:  # Every 5 seconds
        GameClass.PADDLE_HEIGHT -= 5  # Reduce paddle height

# Summary: Added random obstacles to the arena, ball speed fluctuations, and paddle shrinkage to make the game more challenging.

    obstacle = pygame.Rect(GameClass.WIDTH // 2 - 10, GameClass.HEIGHT // 2 - 50, 20, 100)
    obstacle_speed = 5
    while True:
        obstacle.y += obstacle_speed
        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
            obstacle_speed = -obstacle_speed
        pygame.draw.rect(screen, GameClass.WHITE, obstacle)
        ball_collision_with_obstacle(obstacle)
        pygame.time.delay(50)

def ball_collision_with_obstacle(obstacle):  # Handles collision between the ball and the moving obstacle.
    if ball.colliderect(obstacle):
        game.globals.ball_speed_x = -game.globals.ball_speed_x
        direction[0] = -direction[0]

def dynamic_paddle_shrink_expand():  # Changes paddle size when a point is scored.
    if game.globals.right_score % 2 == 0:
        GameClass.right_paddle.height = max(50, GameClass.right_paddle.height - 10)
    if game.globals.left_score % 2 == 0:
        GameClass.left_paddle.height = max(50, GameClass.left_paddle.height - 10)

# Summary: Added a moving obstacle that can deflect the ball, and implemented a dynamic feature where paddle sizes decrease every two points scored, increasing difficulty. 

def add_obstacle():  # Adds a moving obstacle in the center of the game area
    obstacle_width, obstacle_height = 20, 100
    obstacle = pygame.Rect(GameClass.WIDTH // 2 - obstacle_width // 2, GameClass.HEIGHT // 2 - obstacle_height // 2, obstacle_width, obstacle_height)
    obstacle_speed_y = 5

    def move_obstacle():
        nonlocal obstacle_speed_y
        obstacle.y += obstacle_speed_y
        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
            obstacle_speed_y = -obstacle_speed_y

    def draw_obstacle(screen):
        pygame.draw.rect(screen, GameClass.WHITE, obstacle)

    def check_collision_with_ball(ball):
        if ball.colliderect(obstacle):
            game.globals.ball_speed_x = -game.globals.ball_speed_x

    return move_obstacle, draw_obstacle, check_collision_with_ball

def shrink_paddles_on_score(right_score):  # Shrinks paddles each time the right player scores
    shrink_factor = 5
    if right_score > 0 and right_score % 2 == 0:
        if GameClass.left_paddle.height > shrink_factor:
            GameClass.left_paddle.height -= shrink_factor
        if GameClass.right_paddle.height > shrink_factor:
            GameClass.right_paddle.height -= shrink_factor

def double_ball_speed_over_time():  # Doubles the ball speed every 30 seconds
    last_time = pygame.time.get_ticks()
    if pygame.time.get_ticks() > last_time + 30000:  # 30 seconds
        if abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
            game.globals.ball_speed_x *= 2
        if abs(game.globals.ball_speed_y) < game.globals.max_ball_speed:
            game.globals.ball_speed_y *= 2
        last_time = pygame.time.get_ticks()

# Summary: Introduced a moving obstacle in the game, a mechanism to shrink paddles when the right player scores, and a time-based speed increase for the ball.
