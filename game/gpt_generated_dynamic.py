import game.globals
import random
import pygame
from game.game import GameClass

def random_obstacle_spawner(gameReference):  # Spawns intermittent barriers on the screen.
    if not hasattr(gameReference, "obstacle_timer"):
        gameReference.obstacle_timer = 0
    if not hasattr(gameReference, "obstacle_direction"):
        gameReference.obstacle_direction = random.choice([-1, 1])

    obstacle_speed = 2
    gameReference.obstacle_timer += 1

    # Every 5 seconds, introduce a new obstacle
    if gameReference.obstacle_timer == 300:
        obstacle_height = random.randint(50, 100)
        new_obstacle = pygame.Rect(
            random.choice([GameClass.WIDTH // 2 - 200, GameClass.WIDTH // 2 + 200]),
            random.randint(50, GameClass.HEIGHT - obstacle_height - 50),
            GameClass.PADDLE_WIDTH,
            obstacle_height
        )
        gameReference.game_obstacles.append(new_obstacle)
        print(f"Obstacle spawned at: {new_obstacle}")
        gameReference.obstacle_timer = 0

    for obstacle in gameReference.game_obstacles:
        obstacle.x += gameReference.obstacle_direction * obstacle_speed

        # Bounce the obstacle off the side walls
        if obstacle.left < 0 or obstacle.right > GameClass.WIDTH:
            gameReference.obstacle_direction = -gameReference.obstacle_direction

        # If collision with ball occurs
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[0] = -gameReference.direction[0]
            print(f"Collision with obstacle at: {obstacle}")

# Summary: Introduced a `random_obstacle_spawner` function that spawns obstacles randomly on the field every 5 seconds. The obstacles move horizontally and can cause collisions with the ball, making the game more challenging by introducing erratic ball behavior when it hits one of these obstacles.

def surprise_obstacles(gameReference):  # Introduces randomly appearing obstacles on the field to make gameplay harder
    print("Adding surprise obstacles")
    if len(gameReference.game_obstacles) < 4:
        obstacle_width, obstacle_height = 20, 100
        new_obstacle = pygame.Rect(
            random.randint(200, GameClass.WIDTH - 200), random.randint(0, GameClass.HEIGHT - obstacle_height),
            obstacle_width, obstacle_height
        )
        gameReference.game_obstacles.append(new_obstacle)

    for obstacle in gameReference.game_obstacles:
        if gameReference.ball.colliderect(obstacle):
            print("Ball hits obstacle!")
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.direction[1] = -gameReference.direction[1]

        if gameReference.left_paddle.colliderect(obstacle):
            print("Left paddle crashes into obstacle!")
            gameReference.left_score -= 1
            gameReference.game_obstacles.remove(obstacle)

        if gameReference.right_paddle.colliderect(obstacle):
            print("Right paddle crashes into obstacle!")
            gameReference.right_score -= 1
            gameReference.game_obstacles.remove(obstacle)

# Summary: Added a function to introduce surprise obstacles on the field which the ball and paddles can collide with. This increases difficulty by randomizing obstacle locations during gameplay, adding elements that players need to avoid, while also impacting scores upon collisions.

def introduce_obstacles(gameReference):  # Adds moving obstacles on the playing field
    if len(gameReference.game_obstacles) == 0:
        # Introduce a new obstacle only if none exists
        obstacle_width = 60
        obstacle_height = 20
        obstacle = pygame.Rect((gameReference.WIDTH - obstacle_width) // 2, (gameReference.HEIGHT - obstacle_height) // 2, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(obstacle)
    for obstacle in gameReference.game_obstacles:
        obstacle.y += 2
        if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            obstacle.y *= -1
        if gameReference.ball.colliderect(obstacle):
            gameReference.ball.y *= -1  # Change ball's Y direction on collision
        if obstacle.bottom > gameReference.HEIGHT or obstacle.top < 0:
            obstacle.y *= -1  # Reverse direction when hitting top/bottom of screen
    print(f"Obstacles: {gameReference.game_obstacles}")

# Summary: Introduced obstacles that move vertically on the screen. When the ball hits an obstacle, its vertical direction reverses, adding an additional challenge to the game.

def add_obstacle(gameReference):  # Introduces a moving obstacle in the middle of the screen that bounces the ball
    if not gameReference.game_obstacles:
        print("Adding an obstacle!")
        obstacle_width = 20
        obstacle_height = 150
        obstacle_x = (gameReference.WIDTH - obstacle_width) // 2
        obstacle_y = (gameReference.HEIGHT - obstacle_height) // 2
        moving_obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(moving_obstacle)
        gameReference.obstacle_direction = [1, 1]

    for obstacle in gameReference.game_obstacles:
        obstacle.y += gameReference.obstacle_direction[1] * 2

        if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            gameReference.obstacle_direction[1] = -gameReference.obstacle_direction[1]

        if gameReference.ball.colliderect(obstacle):
            print("Ball collided with the obstacle!")
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.increase_speed()

# Summary: Added a function `add_obstacle` that places a moving rectangular obstacle in the middle of the screen. The obstacle moves vertically and bounces the ball back, increasing the ball’s speed upon collision. This makes the game more challenging by adding another dynamic element that players must account for.

def moving_barrier(gameReference):  # Introduces a moving barrier on the field
    barrier_width, barrier_height = 15, 120
    barrier_speed = 2

    if not hasattr(gameReference, 'barrier'):
        gameReference.barrier = pygame.Rect((GameClass.WIDTH - barrier_width) // 2, (GameClass.HEIGHT - barrier_height) // 2, barrier_width, barrier_height)
        gameReference.barrier_direction = 1

    gameReference.barrier.y += barrier_speed * gameReference.barrier_direction

    if gameReference.barrier.top <= 0 or gameReference.barrier.bottom >= GameClass.HEIGHT:
        gameReference.barrier_direction *= -1

    if gameReference.ball.colliderect(gameReference.barrier):
        print("Ball hit the barrier!")
        gameReference.direction[0] = -gameReference.direction[0]
    
    pygame.draw.rect(gameReference.screen, GameClass.GRAY, gameReference.barrier)

# Summary: Added a moving barrier that travels up and down the field, potentially blocking the ball's path and making the game more challenging. The barrier's direction inverts when it hits the top or bottom edge of the game area.


def add_moving_obstacles(gameReference):  # Introduces moving obstacles that make the game more challenging
    obstacle_width, obstacle_height = 20, 20
    speed = 5

    # Ensure only specific number of obstacles are present, and if not, add one
    if len(gameReference.game_obstacles) < 3:
        new_obstacle = pygame.Rect(random.randint(100, GameClass.WIDTH - 100), random.randint(100, GameClass.HEIGHT - 100), obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)
        print("New obstacle added at:", new_obstacle)

    # Move each obstacle and ensure they bounce off the walls
    for obstacle in gameReference.game_obstacles:
        obstacle.y += speed

        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
            speed = -speed
            print("Obstacle bouncing back due to hitting the boundary:", obstacle)

        # Check collision with ball
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[1] = -gameReference.direction[1]
            gameReference.direction[0] *= -1
            print("Ball collision with obstacle:", obstacle)

        # Remove obstacles that went off screen for any reason
        if obstacle.x < 0 or obstacle.x > GameClass.WIDTH or obstacle.y < 0 or obstacle.y > GameClass.HEIGHT:
            gameReference.game_obstacles.remove(obstacle)
            print("Obstacle removed:", obstacle)

# Summary: Introduced moving obstacles in the game that continuously bounce vertically between boundaries. The obstacles increase the game’s difficulty by adding an additional layer of interaction with the ball. The ball's direction is changed when a collision with an obstacle occurs.

def introduce_moving_obstacles(gameReference):  # Introduces moving obstacles to hinder ball movement
    obstacle_width = 20
    obstacle_height = 60
    speed = 5

    obstacle = pygame.Rect(random.randint(20, gameReference.WIDTH - 40), random.randint(20, gameReference.HEIGHT - 80), obstacle_width, obstacle_height)
    gameReference.game_obstacles.append(obstacle)

    move_in_y_direction = random.choice([True, False])

    def move_obstacle():
        if move_in_y_direction:
            obstacle.y += speed if obstacle.y + speed < gameReference.HEIGHT - obstacle_height else -speed
        else:
            obstacle.x += speed if obstacle.x + speed < gameReference.WIDTH - obstacle_width else -speed

    move_obstacle()

    for obstacle in gameReference.game_obstacles:
        if obstacle.colliderect(gameReference.ball):
            print("Ball collided with obstacle!")
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.direction[1] = -gameReference.direction[1]

# Summary: Added a new function `introduce_moving_obstacles` introducing moving obstacles on the game field that collide with the ball, reversing its direction, making the game more challenging and dynamic.

def add_moving_obstacle(gameReference):  # Add a moving obstacle that the ball must avoid
    if len(gameReference.game_obstacles) == 0:
        obstacle_width = 20
        obstacle_height = 100
        starting_x = (gameReference.WIDTH - obstacle_width) // 2
        starting_y = (gameReference.HEIGHT - obstacle_height) // 2
        gameReference.game_obstacles.append(pygame.Rect(starting_x, starting_y, obstacle_width, obstacle_height))
    
    for obstacle in gameReference.game_obstacles:
        obstacle.y += 5 * gameReference.direction[1]

        if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            gameReference.direction[1] *= -1

        if gameReference.ball.colliderect(obstacle):
            print("Collision with obstacle!")
            gameReference.direction[0] = -gameReference.direction[0]  # Reverse ball direction
            
            gameReference.increase_speed()  # Increase speed to make the game more challenging
            
            gameReference.ball.x += gameReference.direction[0] * abs(gameReference.globals.ball_speed_x)
            gameReference.ball.y += gameReference.direction[1] * abs(gameReference.globals.ball_speed_y)
        
        print(f"Obstacle position: (x: {obstacle.x}, y: {obstacle.y})")

# Summary: Introduced a moving obstacle that interacts with the ball and increases the game's difficulty and complexity.
