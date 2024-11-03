import game.globals
import random
import pygame
from game.game import GameClass
import math

def change_paddle_size_based_on_score(gameReference):  # Change paddle sizes based on score difference to increase difficulty
    score_difference = abs(gameReference.left_score - gameReference.right_score)
    new_paddle_height = max(20, gameReference.left_paddle.height - score_difference * 5)

    gameReference.left_paddle = pygame.Rect(
        gameReference.left_paddle.x, 
        gameReference.left_paddle.y, 
        gameReference.left_paddle.width, 
        new_paddle_height
    )

    gameReference.right_paddle = pygame.Rect(
        gameReference.right_paddle.x, 
        gameReference.right_paddle.y, 
        gameReference.right_paddle.width, 
        new_paddle_height
    )

# Summary: Added a function to dynamically change the paddles' Height based on the score difference between the two players. This change makes gameplay more challenging as it becomes harder to hit the ball with smaller paddles as the score difference increases.

import random
import pygame

def introduce_moving_obstacle(gameReference):  # Introduces a moving obstacle in the middle of the screen
    obstacle_width = 20
    obstacle_height = 100
    max_obstacles = 3
    if len(gameReference.game_obstacles) < max_obstacles:
        new_obstacle = pygame.Rect((gameReference.WIDTH - obstacle_width) // 2, random.randint(0, gameReference.HEIGHT - obstacle_height), obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)

    for obstacle in gameReference.game_obstacles:
        # Move obstacles up and down
        if isinstance(obstacle, pygame.Rect):
            obstacle.y += random.choice([-2, 2])
            if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
                obstacle.y -= 4  # Change direction if it hits the screen boundaries

# Summary: Introduced a moving obstacle into the Pong game that randomly moves up and down in the middle of the screen, making it harder to score by introducing additional collision possibilities.

def add_moving_obstacle(gameReference):  # Adds a moving obstacle that moves horizontally across the screen
    obstacle_width = 15
    obstacle_height = 100
    obstacle_starting_x = gameReference.WIDTH // 4
    obstacle_speed = 5

    # Initialize obstacle if it doesn't exist
    if not hasattr(gameReference, 'moving_obstacle'):
        gameReference.moving_obstacle = pygame.Rect(obstacle_starting_x, (gameReference.HEIGHT - obstacle_height) // 2, obstacle_width, obstacle_height)
        gameReference.obstacle_direction = 1

    # Update obstacle position
    gameReference.moving_obstacle.x += obstacle_speed * gameReference.obstacle_direction
    if gameReference.moving_obstacle.right >= gameReference.WIDTH - obstacle_starting_x or gameReference.moving_obstacle.left <= obstacle_starting_x:
        gameReference.obstacle_direction *= -1

    # Draw the moving obstacle
    pygame.draw.rect(gameReference.screen, (255, 0, 0), gameReference.moving_obstacle)

# Summary: Introduced a new gameplay mechanic by adding a moving horizontal obstacle. The obstacle moves back and forth across the screen, creating additional difficulty for players as they have to avoid it while rallying the ball.

def add_random_obstacles(gameReference):  # Adds random obstacles to increase game difficulty
    if len(gameReference.game_obstacles) < 3:  # Limit the number of obstacles on the screen
        obstacle_width = 20
        obstacle_height = random.randint(50, 150)
        obstacle_x = random.randint(GameClass.WIDTH // 4, GameClass.WIDTH * 3 // 4)
        obstacle_y = random.randint(50, GameClass.HEIGHT - 50 - obstacle_height)
        new_obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)
        
    # Optional: Refresh obstacles periodically
    if random.randint(0, 500) == 1:  # Randomly remove an obstacle and potentially add a new one
        gameReference.game_obstacles.pop(random.randint(0, len(gameReference.game_obstacles) - 1))
        new_obstacle_width = 20
        new_obstacle_height = random.randint(50, 150)
        new_obstacle_x = random.randint(GameClass.WIDTH // 4, GameClass.WIDTH * 3 // 4)
        new_obstacle_y = random.randint(50, GameClass.HEIGHT - 50 - new_obstacle_height)
        new_obstacle = pygame.Rect(new_obstacle_x, new_obstacle_y, new_obstacle_width, new_obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)

# Summary: Added `add_random_obstacles` function to introduce dynamic obstacles that periodically change, increasing the game difficulty and keeping the gameplay fresh.

def introduce_moving_obstacle(gameReference):  # Introduce a moving obstacle that bounces up and down
    if not hasattr(gameReference, 'obstacle_position'):
        gameReference.obstacle_position = [GameClass.WIDTH // 2, GameClass.HEIGHT * 0.3]
        gameReference.obstacle_movement = 3  # initial speed of obstacle
    
    gameReference.obstacle_position[1] += gameReference.obstacle_movement
    
    if gameReference.obstacle_position[1] <= 0 or gameReference.obstacle_position[1] >= GameClass.HEIGHT - 20:
        gameReference.obstacle_movement *= -1

    moving_obstacle = pygame.Rect(gameReference.obstacle_position[0], gameReference.obstacle_position[1], 20, 100)

    gameReference.game_obstacles.append(moving_obstacle)
    
    # Draw the obstacle
    pygame.draw.rect(gameReference.screen, GameClass.RED, moving_obstacle)
    
    # Check collision with the ball
    if gameReference.ball.colliderect(moving_obstacle):
        gameReference.direction[0] = -gameReference.direction[0]
        gameReference.increase_speed()


# Summary: Introduced a moving vertical obstacle in the center of the game, making it harder to score points by requiring players to avoid collision with the obstacle. This obstacle bounces up and down, adding an extra layer of challenge. 

def spawn_obstacle(gameReference):  # Introduce random obstacles in the game area
    obstacle_width = 15
    obstacle_height = random.randint(50, 150)
    x_position = random.choice([random.randint(100, 300), random.randint(500, 700)])
    y_position = random.randint(50, gameReference.HEIGHT - obstacle_height - 50)
    
    new_obstacle = pygame.Rect(x_position, y_position, obstacle_width, obstacle_height)
    
    gameReference.game_obstacles.append(new_obstacle)
    if len(gameReference.game_obstacles) > 3:  # limit the number of obstacles
        gameReference.game_obstacles.pop(0)

# Summary: Added a function `spawn_obstacle` that introduces randomly sized obstacles in random positions in the game area to make the game more challenging, limiting the number of obstacles to a maximum of 3.
