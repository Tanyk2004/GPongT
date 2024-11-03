import game.globals
import random
import pygame
from game.game import GameClass

def introduce_obstacle(gameReference):  # Add random moving obstacle to the game
    import random

    if len(gameReference.game_obstacles) < 1:  # Ensure only one obstacle at a time
        obstacle_width = 20
        obstacle_height = 100
        x_position = random.randint(200, GameClass.WIDTH - 200)
        y_position = random.randint(50, GameClass.HEIGHT - 150)
        
        obstacle = pygame.Rect(x_position, y_position, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(obstacle)
        gameReference.obstacle_speed_x = random.choice((-1, 1))  # Moving speed and direction
        gameReference.obstacle_speed_y = random.choice((-1, 1))
        print("Obstacle created at x:", x_position, " y:", y_position)

def move_obstacle(gameReference):  # Move obstacle within screen boundaries
    if gameReference.game_obstacles:
        obstacle = gameReference.game_obstacles[0]
        obstacle.x += gameReference.obstacle_speed_x
        obstacle.y += gameReference.obstacle_speed_y

        if obstacle.left <= 0 or obstacle.right >= GameClass.WIDTH:  # Change direction on collision with wall
            gameReference.obstacle_speed_x = -gameReference.obstacle_speed_x
            print("Obstacle changed horizontal direction")

        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:  # Change direction on collision with wall
            gameReference.obstacle_speed_y = -gameReference.obstacle_speed_y
            print("Obstacle changed vertical direction")

def detect_obstacle_collision(gameReference):  # Detect collision of ball with the obstacle and reverse direction if collided
    if gameReference.game_obstacles:
        obstacle = gameReference.game_obstacles[0]
        if gameReference.ball.colliderect(obstacle):
            print("Collision with obstacle detected")
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.direction[1] = -gameReference.direction[1]

# Summary: Introduced a moving obstacle inside the game which the ball can collide with. The obstacle is randomly generated and affects the ball's direction when collided.

def introduce_obstacles(gameReference):  # Introduces static obstacles that the ball can bounce off
    if not gameReference.game_obstacles:
        print("Introducing obstacles to the game.")
        # Create two obstacles as pygame Rect objects for example
        obstacle1 = pygame.Rect(GameClass.WIDTH // 4, GameClass.HEIGHT // 3, 20, 100)
        obstacle2 = pygame.Rect(GameClass.WIDTH * 3 // 4, GameClass.HEIGHT * 2 // 3, 20, 100)
        gameReference.game_obstacles.extend([obstacle1, obstacle2])
    else:
        # Check collisions with obstacles
        for obstacle in gameReference.game_obstacles:
            if gameReference.ball.colliderect(obstacle):
                # Reverse ball direction upon collision
                print("Ball collided with obstacle.")
                gameReference.direction[0] = -gameReference.direction[0]

def dynamic_speed_increase(gameReference):  # Increases speed dynamically based on score ratio
    print(f"Current scores -> Left: {gameReference.left_score}, Right: {gameReference.right_score}")
    if gameReference.left_score > gameReference.right_score + 1:
        print("Left player is leading by more than 1 point, increasing ball speed.")
        game.globals.ball_speed_x += 0.5
        game.globals.ball_speed_y += 0.5
    elif gameReference.right_score > gameReference.left_score + 1:
        print("Right player is leading by more than 1 point, increasing ball speed.")
        game.globals.ball_speed_x += 0.5
        game.globals.ball_speed_y += 0.5

def shrinking_paddles(gameReference):  # Shrinks paddles gradually over time to increase difficulty
    if pygame.time.get_ticks() % 10000 < 20:  # Every 10 seconds
        print("Shrinking paddles for increased difficulty.")
        if gameReference.left_paddle.height > 60:  # Set a minimum paddle size
            gameReference.left_paddle.height -= 5
        if gameReference.right_paddle.height > 60:  # Set a minimum paddle size
            gameReference.right_paddle.height -= 5

# Summary: Introduced new elements to the game: static obstacles that the ball bounces off, dynamic speed increases when players are leading by more than 1 point, and paddles that shrink over time to enhance difficulty.

import random

def random_obstacles(gameReference):  # Introduces random obstacles on the field
    if len(gameReference.game_obstacles) < 3:
        for _ in range(3 - len(gameReference.game_obstacles)):
            obstacle_type = random.choice(["rect", "circle"])
            if obstacle_type == "rect":
                new_obstacle = pygame.Rect(
                    random.randint(0, gameReference.WIDTH - 50),
                    random.randint(0, gameReference.HEIGHT - 50),
                    20,
                    100
                )
            else:
                new_obstacle = pygame.Rect(
                    random.randint(0, gameReference.WIDTH - 50),
                    random.randint(0, gameReference.HEIGHT - 50),
                    60,
                    60
                )
            gameReference.game_obstacles.append(new_obstacle)
            print("Added new obstacle:", new_obstacle)

def obstacle_collision(gameReference):  # Detects collision between the ball and the obstacles
    for obstacle in gameReference.game_obstacles:
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.direction[1] = -gameReference.direction[1]
            gameReference.increase_speed()
            print("Ball hit an obstacle!")

def moving_obstacles(gameReference):  # Moves the obstacles randomly within the game boundaries
    for obstacle in gameReference.game_obstacles:
        if isinstance(obstacle, pygame.Rect):
            obstacle.x += random.choice([-1, 1])
            obstacle.y += random.choice([-1, 1])

        # Boundaries checking and correction
        if obstacle.x <= 0 or obstacle.right >= gameReference.WIDTH:
            obstacle.x -= random.choice([-1, 1]) * 2

        if obstacle.y <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            obstacle.y -= random.choice([-1, 1]) * 2

        print("Moved obstacle:", obstacle)

# Summary: Added random obstacles to the game that move around the field and collide with the ball, making the game more challenging.

def moving_obstacle(gameReference):  # Adds a moving obstacle in the center of the screen to block the ball
    # Check if an obstacle needs to be created
    if not gameReference.game_obstacles:
        # Create a new obstacle rectangle at the center of the screen
        initial_obstacle = pygame.Rect(
            gameReference.WIDTH // 2 - 50, gameReference.HEIGHT // 2 - 10, 100, 20)
        gameReference.game_obstacles.append(initial_obstacle)
        print("Added a new moving obstacle")

    # Move the existing obstacle
    for obstacle in gameReference.game_obstacles:
        obstacle.y += 2 * gameReference.direction[1]
        if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            obstacle.y -= 4 * gameReference.direction[1]

    # Check for collision with the ball
    for obstacle in gameReference.game_obstacles:
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[1] *= -1
            print("Ball hit the moving obstacle")

def increment_speed_on_multiple_paddle_hits(gameReference, hit_count_threshold=3):  # Increases ball speed after consecutive paddle hits
    # Initialize hit counter
    if not hasattr(gameReference, '_paddle_hit_count'):
        gameReference._paddle_hit_count = 0

    # Increment hit count on paddle collision
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        gameReference._paddle_hit_count += 1
    else:
        gameReference._paddle_hit_count = 0

    # Check if ball speed should be increased
    if gameReference._paddle_hit_count >= hit_count_threshold:
        gameReference.increase_speed()
        gameReference._paddle_hit_count = 0
        print("Ball speed increased after multiple paddle hits")

def temporary_paddle_slowdown(gameReference, cooldown_frames=180):  # Temporarily slows down paddle speed after hitting the ball
    # Initialize cooldown frame counter
    if not hasattr(gameReference, '_cooldown_counter'):
        gameReference._cooldown_counter = 0

    # Slow down paddles for a number of frames after the ball is hit
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        game.globals.paddle_speed = 2
        gameReference._cooldown_counter = cooldown_frames
        print("Paddle speed reduced temporarily")

    # Restore normal speed after cooldown period
    if gameReference._cooldown_counter > 0:
        gameReference._cooldown_counter -= 1
    if gameReference._cooldown_counter == 0 and game.globals.paddle_speed < 5:
        game.globals.paddle_speed = 5
        print("Paddle speed restored to normal")
# Summary: Added three new functions to enhance Pong game difficulty: `moving_obstacle` introduces a moving obstacle on the screen, `increment_speed_on_multiple_paddle_hits` increases ball speed after multiple paddle collisions, and `temporary_paddle_slowdown` temporarily reduces paddle speed after hitting the ball for added challenge.


def introduce_obstacle(gameReference):  # Introduces a moving obstacle in the center of the screen that the ball can bounce off
    if not hasattr(gameReference, 'moving_obstacle'):
        gameReference.moving_obstacle = pygame.Rect(GameClass.WIDTH // 2 - 15, GameClass.HEIGHT // 2 - 75, 30, 30)
        gameReference.obstacle_direction = random.choice([-1, 1])

    # Move the obstacle up and down
    gameReference.moving_obstacle.y += 3 * gameReference.obstacle_direction

    if gameReference.moving_obstacle.top <= 0 or gameReference.moving_obstacle.bottom >= GameClass.HEIGHT:
        gameReference.obstacle_direction *= -1

    # Check collision between the ball and the obstacle
    if gameReference.ball.colliderect(gameReference.moving_obstacle):
        gameReference.direction[0] *= -1
        print("Ball hit the moving obstacle!")

    pygame.draw.rect(gameReference.screen, GameClass.GRAY, gameReference.moving_obstacle)

def change_paddle_size_based_on_score(gameReference):  # Adjusts the paddle size according to the player's scores
    left_factor = max(1, 5 - gameReference.left_score)
    right_factor = max(1, 5 - gameReference.right_score)

    if gameReference.left_paddle.height != GameClass.PADDLE_HEIGHT // left_factor:
        gameReference.left_paddle.height = GameClass.PADDLE_HEIGHT // left_factor
        print(f"Left paddle size changed to {gameReference.left_paddle.height}")
    if gameReference.right_paddle.height != GameClass.PADDLE_HEIGHT // right_factor:
        gameReference.right_paddle.height = GameClass.PADDLE_HEIGHT // right_factor
        print(f"Right paddle size changed to {gameReference.right_paddle.height}")

def simulate_wind_effect(gameReference):  # Adds a wind effect that slightly alters the ball's path
    wind_force = random.choice([-1, 0, 1])
    gameReference.ball.x += wind_force
    print(f"Wind force applied: {wind_force}")

# Summary: Introduced a moving obstacle in the center of the field, adjusted paddle sizes based on player scores, and added a random wind effect that changes the ball's trajectory.

def spinning_obstacle(gameReference):  # Introduces a spinning obstacle in the middle of the screen
    obstacle_radius = 50
    obstacle_center = (gameReference.WIDTH // 2, gameReference.HEIGHT // 2)
    obstacle_angle_speed = 5  # Speed of rotating in degrees

    current_time = pygame.time.get_ticks()
    obstacle_angle = (current_time // 10) % 360  # Rotate the obstacle over time

    obstacle_x = obstacle_center[0] + obstacle_radius * math.cos(math.radians(obstacle_angle))
    obstacle_y = obstacle_center[1] + obstacle_radius * math.sin(math.radians(obstacle_angle))

    gameReference.game_obstacles.append(pygame.Rect(obstacle_x, obstacle_y, 10, 10))

    # Implement obstacle interaction with the ball
    for obstacle in gameReference.game_obstacles:
        if gameReference.ball.colliderect(obstacle):
            game.globals.ball_speed_x = -game.globals.ball_speed_x
            game.globals.ball_speed_y = -game.globals.ball_speed_y
            break
            
    print("Spinning obstacle added!")

def random_paddle_boost(gameReference):  # Randomly increases paddle speed for a short period
    boost_duration = 2000  # Duration in milliseconds
    boost_active = hasattr(gameReference, 'boost_end_time') and pygame.time.get_ticks() < gameReference.boost_end_time

    if not boost_active and random.random() < 0.01:  # 1% chance per frame to activate boost
        gameReference.boost_end_time = pygame.time.get_ticks() + boost_duration
        gameReference.original_paddle_speed = game.globals.paddle_speed
        game.globals.paddle_speed *= 2  # Double the paddle speed
        print("Paddle boost activated!")

    if boost_active and pygame.time.get_ticks() >= gameReference.boost_end_time:
        game.globals.paddle_speed = gameReference.original_paddle_speed  # Reset paddle speed
        del gameReference.boost_end_time
        print("Paddle boost ended.")


def disappearing_ball(gameReference):  # Makes the ball disappear temporarily from time to time
    disappear_duration = 1000  # Duration in milliseconds
    visible = hasattr(gameReference, 'disappear_end_time') and pygame.time.get_ticks() < gameReference.disappear_end_time

    if not visible and random.random() < 0.005:  # 0.5% chance per frame to activate disappearance
        gameReference.disappear_end_time = pygame.time.get_ticks() + disappear_duration
        gameReference.ball_color = GameClass.BLACK  # Change to background color to simulate disappearance
        print("Ball disappeared!")

    if visible and pygame.time.get_ticks() >= gameReference.disappear_end_time:
        gameReference.ball_color = GameClass.BALL_COLOR  # Reset ball color to make it visible
        del gameReference.disappear_end_time
        print("Ball reappeared.")


# Summary: Added three new functions that introduce unique gameplay mechanics— a spinning obstacle, random paddle boosts, and temporary ball disappearance. These elements are designed to enhance the challenge and entertainment value of the game.
