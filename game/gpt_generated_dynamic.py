import game.globals
import random
import pygame
from game.game import GameClass
import math

def introduce_gravity_effect(gameReference):  # Introduce a gravity effect on the ball
    if game.globals.ball_speed_y < game.globals.max_ball_speed:
        game.globals.ball_speed_y += 0.1  # Increase the vertical speed slightly to simulate gravity

def paddle_size_variation(gameReference):  # Change paddles size over time to make the game harder
    time_elapsed = pygame.time.get_ticks()
    new_height = GameClass.PADDLE_HEIGHT - (time_elapsed // 5000) * 5
    if new_height < 40:  # Set a minimum height for the paddles
        new_height = 40
    gameReference.left_paddle.height = new_height
    gameReference.right_paddle.height = new_height

# Summary: Added gravity effect on the ball to simulate a downward pull, making it harder to keep control. Additionally, progressively reduce paddle sizes over time, adding more challenge the longer the game continues.

def introduce_random_wormhole(gameReference):  # Introduces a wormhole that teleports the ball to a random location on the screen
    if random.randint(0, 200) < 3:  # Randomly create a wormhole with a small probability
        wormhole_pos = (random.randint(0, gameReference.WIDTH - gameReference.BALL_SIZE), 
                        random.randint(0, gameReference.HEIGHT - gameReference.BALL_SIZE))
        gameReference.ball.x, gameReference.ball.y = wormhole_pos

# Summary: Added a new function `introduce_random_wormhole` that randomly teleports the ball to a new position on the screen, introducing unpredictability and increasing the game's difficulty.

def deflecting_obstacles(gameReference):  # Adds deflecting obstacles in the game
    obstacle_count = 3
    obstacle_width = 10
    obstacle_height = 80
    gap_between_obstacles = (gameReference.HEIGHT - obstacle_count * obstacle_height) // (obstacle_count + 1)
    
    if not gameReference.game_obstacles:
        for i in range(obstacle_count):
            y_pos = gap_between_obstacles + i * (obstacle_height + gap_between_obstacles)
            obstacle = pygame.Rect((gameReference.WIDTH // 2 - obstacle_width // 2), y_pos, obstacle_width, obstacle_height)
            gameReference.game_obstacles.append(obstacle)

# Summary: Added a function to introduce deflecting vertical obstacles in the middle of the game, increasing complexity by bouncing the ball unexpectedly.

def speed_boost_zones(gameReference):  # Introduces speed boost zones that temporarily increase the ball's speed
    boost_zone_width, boost_zone_height = 50, 50
    boost_zones = [
        pygame.Rect((gameReference.WIDTH // 4) - boost_zone_width // 2, (gameReference.HEIGHT // 4) - boost_zone_height // 2, boost_zone_width, boost_zone_height),
        pygame.Rect((gameReference.WIDTH * 3 // 4) - boost_zone_width // 2, (gameReference.HEIGHT * 3 // 4) - boost_zone_height // 2, boost_zone_width, boost_zone_height)
    ]

    ball_center = gameReference.ball.center
    for zone in boost_zones:
        if zone.collidepoint(ball_center):
            gameReference.direction[0] *= 1.2
            gameReference.direction[1] *= 1.2
            break  # Only activate one boost at a time

    for zone in boost_zones:
        pygame.draw.rect(gameReference.screen, (255, 100, 100), zone, 2)

# Summary: Introduced 'speed_boost_zones' which place speed boost areas on the field, increasing the ball's speed when it passes through them.

def shrink_area(gameReference):  # Shrinks the playable area over time to increase difficulty
    shrink_rate = 0.05  # Amount to shrink per frame
    min_shrink = 100  # Minimum playable width/height
    
    # Calculate new dimensions
    new_width = max(gameReference.WIDTH - shrink_rate, min_shrink)
    new_height = max(gameReference.HEIGHT - shrink_rate, min_shrink)
    
    # Calculate offset for centering the shrunken area
    x_offset = (gameReference.WIDTH - new_width) // 2
    y_offset = (gameReference.HEIGHT - new_height) // 2
    
    # Adjust screen dimensions
    gameReference.screen = pygame.display.set_mode((int(new_width), int(new_height)))
    
    # Adjust paddle positions and dimensions if affected
    if gameReference.left_paddle.right > new_width + x_offset:
        gameReference.left_paddle.right = new_width + x_offset
    if gameReference.right_paddle.left < x_offset:
        gameReference.right_paddle.left = x_offset
    
    # Boundary correction if ball goes out of new bounds
    if gameReference.ball.left < x_offset:
        gameReference.ball.left = x_offset
    elif gameReference.ball.right > new_width + x_offset:
        gameReference.ball.right = new_width + x_offset
    
    if gameReference.ball.top < y_offset:
        gameReference.ball.top = y_offset
    elif gameReference.ball.bottom > new_height + y_offset:
        gameReference.ball.bottom = new_height + y_offset

# Summary: Introduced a feature where the playable area slowly shrinks over time, adding difficulty by limiting movement space.

def random_ball_teleport(gameReference):  # Randomly teleport the ball to a new location on the screen
    if random.randint(1, 200) == 1:  # Approximately 0.5% chance per frame
        gameReference.ball.x = random.randint(0, gameReference.screen.get_width() - gameReference.ball.width)
        gameReference.ball.y = random.randint(0, gameReference.screen.get_height() - gameReference.ball.height)

# Summary: Added a function to randomly teleport the ball to a new position, creating an unpredictable challenge.

def increase_ball_speed_over_time(gameReference):  # Gradually increase ball speed over time
    # Calculate the amount of time the game has been running
    time_elapsed = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds

    # Increase the ball speed incrementally over time
    time_based_speed_increase = 0.1 * time_elapsed  # Increase ball speed by 0.1 units per second

    # Ensure the ball speed does not exceed the maximum allowed speed
    if abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
        game.globals.ball_speed_x += time_based_speed_increase * (1 if game.globals.ball_speed_x > 0 else -1)
    if abs(game.globals.ball_speed_y) < game.globals.max_ball_speed:
        game.globals.ball_speed_y += time_based_speed_increase * (1 if game.globals.ball_speed_y > 0 else -1)

# Summary: Added a function that gradually increases ball speed over time, making the game more challenging as time passes.
