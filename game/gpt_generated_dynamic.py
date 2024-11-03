import game.globals
import random
import pygame
from game.game import GameClass

def add_moving_obstacle(gameReference):  # Introduces a moving obstacle in the center of the field
    if len(gameReference.game_obstacles) == 0:
        # Create a new obstacle if none exists
        obstacle_width, obstacle_height = 15, 100
        new_obstacle = pygame.Rect((gameReference.WIDTH - obstacle_width) // 2, (gameReference.HEIGHT - obstacle_height) // 2, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)
        gameReference.obstacle_direction = 1

    for obstacle in gameReference.game_obstacles:
        if isinstance(obstacle, pygame.Rect):
            # Move obstacle vertically
            obstacle.y += 3 * gameReference.obstacle_direction
            if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
                gameReference.obstacle_direction *= -1

            # Check ball collision with obstacle
            if gameReference.ball.colliderect(obstacle):
                print("Ball hit the obstacle!")
                gameReference.direction[0] *= -1
                gameReference.increase_speed()

def decrease_paddle_size_on_hit(gameReference):  # Decreases player's paddle size each time the ball hits the paddle
    if gameReference.ball.colliderect(gameReference.left_paddle):
        print("Ball hit the left paddle!")
        new_height = max(20, gameReference.left_paddle.height - 10)
        gameReference.left_paddle.height = new_height
    if gameReference.ball.colliderect(gameReference.right_paddle):
        print("Ball hit the right paddle!")
        new_height = max(20, gameReference.right_paddle.height - 10)
        gameReference.right_paddle.height = new_height

def change_ball_color_on_bounce(gameReference):  # Randomly changes the ball's color whenever it bounces off a paddle
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        print("Ball color changed on bounce!")
        gameReference.ball_color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

# Summary: Added three new functions to the Pong game. 'add_moving_obstacle' introduces a moving obstacle that the ball can collide with to change direction and increase its speed. 'decrease_paddle_size_on_hit' shrinks the paddle size by 10 pixels every time the ball hits it, to add challenge. 'change_ball_color_on_bounce' changes the color of the ball to a random color each time it bounces off a paddle for visual effect.

import random

def add_random_obstacle(gameReference):  # Spawns random obstacles on the field that change ball direction on collision
    if len(gameReference.game_obstacles) < 3:  # Limit to 3 obstacles
        obstacle_type = random.choice(["rect", "circle"])
        if obstacle_type == "rect":
            new_obstacle = pygame.Rect(
                random.randint(100, GameClass.WIDTH - 100),
                random.randint(50, GameClass.HEIGHT - 50),
                random.randint(20, 50), random.randint(20, 50)
            )
        else:
            new_obstacle = pygame.Rect(
                random.randint(100, GameClass.WIDTH - 100),
                random.randint(50, GameClass.HEIGHT - 50),
                random.randint(20, 50), random.randint(20, 50)
            )
        gameReference.game_obstacles.append(new_obstacle)
        print(f"Added new obstacle at {new_obstacle.topleft}")

def check_obstacle_collision(gameReference):  # Checks for collisions between the ball and obstacles
    for obstacle in gameReference.game_obstacles:
        if obstacle is not None and gameReference.ball.colliderect(obstacle):
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.direction[1] = -gameReference.direction[1]
            print("Ball collided with obstacle, changing direction")

def increase_difficulty_on_score(gameReference):  # Increases the game difficulty based on the score
    total_score = gameReference.left_score + gameReference.right_score
    if total_score % 5 == 0 and total_score != 0:
        game.globals.paddle_speed += 0.5  # Increase paddle speed
        game.globals.speed_increase_factor += 0.1  # Increase ball speed factor
        print("Increased difficulty: paddle speed and ball speed factor enhanced")

# Summary: Introduced random obstacles that change the ball's direction, checked for such collisions, and increased game difficulty by enhancing paddle speed and ball speed factors based on the score.

def introduce_obstacle(gameReference):  # Introduces a random moving obstacle
    if len(gameReference.game_obstacles) < 1:
        # Add a single obstacle initially
        obstacle = pygame.Rect(random.randint(100, GameClass.WIDTH - 100), random.randint(100, GameClass.HEIGHT - 100), 20, 20)
        gameReference.game_obstacles.append(obstacle)
        gameReference.obstacle_speed = [random.choice([-2, 2]), random.choice([-2, 2])]
    else:
        # Update position of moving obstacle
        for obstacle in gameReference.game_obstacles:
            obstacle.x += gameReference.obstacle_speed[0]
            obstacle.y += gameReference.obstacle_speed[1]
            if obstacle.left <= 0 or obstacle.right >= GameClass.WIDTH:
                gameReference.obstacle_speed[0] = -gameReference.obstacle_speed[0]
            if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
                gameReference.obstacle_speed[1] = -gameReference.obstacle_speed[1]

            # Check collision with ball
            if gameReference.ball.colliderect(obstacle):
                print("Ball hit an obstacle!")
                gameReference.direction[0] = -gameReference.direction[0]
                gameReference.direction[1] = -gameReference.direction[1]

def shrinking_paddles(gameReference):  # Shrinks paddles each time the ball hits them
    if gameReference.ball.colliderect(gameReference.left_paddle):
        print("Left paddle hit!")
        gameReference.left_paddle.height = max(gameReference.left_paddle.height - 5, 20)
    if gameReference.ball.colliderect(gameReference.right_paddle):
        print("Right paddle hit!")
        gameReference.right_paddle.height = max(gameReference.right_paddle.height - 5, 20)

def random_ball_speed_increase(gameReference):  # Randomly increases ball speed for a short duration
    if random.random() < 0.01:  # 1% chance per frame
        print("Random speed increase!")
        original_speed_x = gameReference.direction[0] * abs(game.globals.ball_speed_x)
        original_speed_y = gameReference.direction[1] * abs(game.globals.ball_speed_y)
        game.globals.ball_speed_x += random.randint(1, 3) * gameReference.direction[0]
        game.globals.ball_speed_y += random.randint(1, 3) * gameReference.direction[1]
        gameReference.ball.x += game.globals.ball_speed_x
        gameReference.ball.y += game.globals.ball_speed_y
        game.globals.ball_speed_x = original_speed_x
        game.globals.ball_speed_y = original_speed_y

# Summary: Introduced three new features to increase game difficulty. introduce_obstacle adds a moving obstacle to the screen that deflects the ball on impact. shrinking_paddles reduce the size of paddles on ball contact, making it harder to play over time. random_ball_speed_increase introduces a rare random event where the ball speed temporarily increases, adding unexpected challenges for players.

def add_moving_obstacle(gameReference):  # Adds a moving obstacle that the ball can collide with
    if not gameReference.game_obstacles:
        obstacle_width, obstacle_height = 20, 100
        obstacle = pygame.Rect((GameClass.WIDTH // 2) - (obstacle_width // 2), (GameClass.HEIGHT // 2) - (obstacle_height // 2), obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(obstacle)
    
    for obstacle in gameReference.game_obstacles:
        if isinstance(obstacle, pygame.Rect):
            obstacle.y += 5
            if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
                obstacle.y *= -1
        
            if gameReference.ball.colliderect(obstacle):
                game.globals.ball_speed_x *= -1
                gameReference.direction[0] *= -1
                print('Ball collided with an obstacle!')

def shrink_paddles_on_collision(gameReference):  # Shrinks paddle size when the ball hits it
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        if gameReference.left_paddle.height > 20:
            gameReference.left_paddle.height -= 5
        if gameReference.right_paddle.height > 20:
            gameReference.right_paddle.height -= 5
        print("Paddles shrunk after ball collision!")

def change_ball_color_on_speed_increase(gameReference):  # Changes ball color when its speed increases
    initial_color = gameReference.ball_color
    speed_thresholds = [(10, (255, 0, 0)), (15, (0, 255, 0)), (20, (0, 0, 255))]
    new_color = initial_color
    for threshold, color in speed_thresholds:
        if abs(game.globals.ball_speed_x) > threshold or abs(game.globals.ball_speed_y) > threshold:
            new_color = color
    if gameReference.ball_color != new_color:
        gameReference.ball_color = new_color
        print(f'Ball color changed to: {new_color}')

# Summary: Added three new functions to enhance the Pong game. `add_moving_obstacle` adds vertical-moving obstacles that the ball can collide with, changing its direction. `shrink_paddles_on_collision` causes paddles to shrink after ball hits, making returns more difficult. `change_ball_color_on_speed_increase` changes the ball's color as its speed increases, providing visual feedback on difficulty.

def introduce_moving_obstacles(gameReference):  # Add moving obstacles in the middle of the playing field
    obstacle_speed = 2
    obstacle_width = 20
    obstacle_height = 50
    
    # Initialize obstacles if not already done
    if not gameReference.game_obstacles:
        for i in range(3):
            obstacle = pygame.Rect(
                gameReference.WIDTH // 2 - obstacle_width // 2,
                (i + 1) * gameReference.HEIGHT // 4 - obstacle_height // 2,
                obstacle_width,
                obstacle_height
            )
            gameReference.game_obstacles.append(obstacle)
    
    # Move the obstacles up and down
    for obstacle in gameReference.game_obstacles:
        obstacle.y += obstacle_speed * gameReference.direction[1]
        if obstacle.top <= 0 or obstacle.bottom >= gameReference.HEIGHT:
            obstacle_speed = -obstacle_speed
        
        # Check collision with the ball
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[0] = -gameReference.direction[0]  # Reverse ball direction on collision
            print("Ball collided with an obstacle!")

def increase_ball_speed_periodically(gameReference):  # Gradually increase ball speed every few seconds
    time_now = pygame.time.get_ticks()
    if time_now % 5000 <= 16:  # Every 5 seconds
        if abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
            game.globals.ball_speed_x += 1 * (1 if game.globals.ball_speed_x > 0 else -1)
            print(f"Ball speed increased! New ball_speed_x: {game.globals.ball_speed_x}")
        if abs(game.globals.ball_speed_y) < game.globals.max_ball_speed:
            game.globals.ball_speed_y += 1 * (1 if game.globals.ball_speed_y > 0 else -1)
            print(f"Ball speed increased! New ball_speed_y: {game.globals.ball_speed_y}")

def change_ball_color_on_hit(gameReference):  # Change the color of the ball every time it hits a paddle
    original_color = gameReference.ball_color
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        gameReference.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(f"Ball color changed to: {gameReference.ball_color}")
    else:
        gameReference.ball_color = original_color

# Summary: Introduced three functions: 1) `introduce_moving_obstacles` to add moving obstacles in the field; 2) `increase_ball_speed_periodically` to gradually increase ball speed; 3) `change_ball_color_on_hit` to change the ball's color upon hitting paddles, adding visual feedback.

def sporadic_obstacles(gameReference):  # Introduces random obstacles on the field
    if random.randint(0, 100) < 5:  # 5% chance every frame
        obstacle_x = random.randint(100, 700)  # Position obstacle randomly on x-axis
        obstacle_y = random.randint(50, 550)  # Position obstacle randomly on y-axis
        # obstacle size, leaving some room so it doesn't go off screen
        obstacle_width = random.randint(10, 30)
        obstacle_height = random.randint(10, 30)
        new_obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)
    print("Obstacles on field:", len(gameReference.game_obstacles))

def change_ball_velocity(gameReference):  # Changes ball's velocity at random intervals
    if random.randint(0, 100) < 5:  # 5% chance every frame
        game.globals.ball_speed_x *= random.choice([0.5, 1.5])
        game.globals.ball_speed_y *= random.choice([0.5, 1.5])
    print("Ball speed X, Y: ", game.globals.ball_speed_x, game.globals.ball_speed_y)

def paddle_size_dynamic_change(gameReference):  # Dynamically alters paddle size
    gameReference.left_paddle.height = game.globals.speed_increase_factor * random.randint(80, 120)
    gameReference.right_paddle.height = game.globals.speed_increase_factor * random.randint(80, 120)
    print("Paddle Sizes - Left: ", gameReference.left_paddle.height, " Right: ", gameReference.right_paddle.height)

# Summary: Added three functions to increase difficulty. "sporadic_obstacles" introduces random obstacles on the field. "change_ball_velocity"
# changes the speed of the ball at random intervals. "paddle_size_dynamic_change" changes the size of the paddles dynamically.

def obstacle_challenge(gameReference):  # Introduces a moving obstacle to the game
    print("Adding or moving an obstacle.")

    # Create a new obstacle if none exist
    if len(gameReference.game_obstacles) == 0:
        obstacle_width, obstacle_height = 50, 10
        new_obstacle = pygame.Rect(
            random.randint(100, gameReference.WIDTH - 100), 
            random.randint(gameReference.HEIGHT//4, 3 * gameReference.HEIGHT//4), 
            obstacle_width, 
            obstacle_height
        )
        gameReference.game_obstacles.append(new_obstacle)
    else:
        # Move the existing obstacle
        for obstacle in gameReference.game_obstacles:
            obstacle.y += 5
            if obstacle.y >= gameReference.HEIGHT or obstacle.y <= 0:
                obstacle.y *= -1

    # Check for collisions between ball and obstacle
    for obstacle in gameReference.game_obstacles:
        if gameReference.ball.colliderect(obstacle):
            print("Ball collided with an obstacle.")
            gameReference.direction[0] = -gameReference.direction[0]

def change_ball_color_on_paddle_collision(gameReference):  # Changes ball color on paddle collision
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        print("Ball hit a paddle; changing color.")
        gameReference.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def shrink_paddle_on_miss(gameReference):  # Shrinks a paddle when it misses the ball
    if gameReference.ball.left <= 0:
        print("Left paddle missed; shrinking paddle.")
        gameReference.left_paddle.height = max(30, gameReference.left_paddle.height - 10)

    elif gameReference.ball.right >= gameReference.WIDTH:
        print("Right paddle missed; shrinking paddle.")
        gameReference.right_paddle.height = max(30, gameReference.right_paddle.height - 10)

# Summary: 
- **obstacle_challenge** adds an obstacle in the middle of the field that the ball can bounce off, with its position adjusted dynamically during play.
- **change_ball_color_on_paddle_collision** changes the ball's color every time it hits a paddle, adding a unique visual effect.
- **shrink_paddle_on_miss** decreases the height of a paddle when it fails to hit the ball, making it more challenging for the player.

def introduce_moving_obstacles(gameReference):  # Introduces moving obstacles to the game field
    if len(gameReference.game_obstacles) < 3:
        obstacle_width, obstacle_height = 20, 80
        new_obstacle = pygame.Rect(random.randint(100, GameClass.WIDTH - 100), random.randint(100, GameClass.HEIGHT - 100), obstacle_width, obstacle_height)
        gameReference.game_obstacles.append(new_obstacle)
    
    for obstacle in gameReference.game_obstacles:
        if obstacle.centery < gameReference.ball.centery and obstacle.bottom < GameClass.HEIGHT:
            obstacle.y += 3
        if obstacle.centery > gameReference.ball.centery and obstacle.top > 0:
            obstacle.y -= 3
        
        if gameReference.ball.colliderect(obstacle):
            gameReference.direction[0] = -gameReference.direction[0]
            gameReference.increase_speed()
    print("Moving obstacles updated")

def change_paddle_color_on_collision(gameReference):  # Change paddle color when the ball collides with it
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        if gameReference.paddle_color == GameClass.WHITE:
            gameReference.paddle_color = GameClass.GRAY
        else:
            gameReference.paddle_color = GameClass.WHITE
        print("Paddle color changed")

def shrinking_paddle_effect(gameReference):  # Gradually shrinks the paddles the more they hit the ball
    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        if gameReference.left_paddle.height > 60 and gameReference.right_paddle.height > 60:
            gameReference.left_paddle.height -= 2
            gameReference.right_paddle.height -= 2
        print("Paddle height reduced")

# Summary: Added three new functions: a moving obstacle mechanic that bounces the ball, a color-changing effect on paddle collision with the ball, and a shrinking paddle effect as the paddles hit the ball repeatedly, increasing game difficulty.

def introduce_moving_obstacle(gameReference):  # Introduces a moving obstacle in the middle of the field
    if not hasattr(gameReference, 'moving_obstacle'):
        obstacle_width, obstacle_height = 20, 80
        gameReference.moving_obstacle = pygame.Rect(
            GameClass.WIDTH // 2 - obstacle_width // 2, 0, 
            obstacle_width, obstacle_height
        )
        gameReference.obstacle_direction = 1

    gameReference.moving_obstacle.y += gameReference.obstacle_direction * 5
    if gameReference.moving_obstacle.top <= 0 or gameReference.moving_obstacle.bottom >= GameClass.HEIGHT:
        gameReference.obstacle_direction *= -1

    if gameReference.ball.colliderect(gameReference.moving_obstacle):
        gameReference.direction[0] = -gameReference.direction[0]
        print("Ball hits the moving obstacle! Direction reversed.")

def change_paddle_size_on_score(gameReference):  # Changes paddle size upon scoring
    if gameReference.left_score != gameReference.previous_left_score:
        gameReference.left_paddle.height -= 10
        gameReference.previous_left_score = gameReference.left_score
        print("Left paddle decreased in size.")

    if gameReference.right_score != gameReference.previous_right_score:
        gameReference.right_paddle.height -= 10
        gameReference.previous_right_score = gameReference.right_score
        print("Right paddle decreased in size.")

def randomize_ball_color(gameReference):  # Randomizes the ball color after each paddle hit
    if hasattr(gameReference, 'ball_previous_collision') and gameReference.ball_previous_collision:
        return

    if gameReference.ball.colliderect(gameReference.left_paddle) or gameReference.ball.colliderect(gameReference.right_paddle):
        gameReference.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        gameReference.ball_previous_collision = True
        print("Ball color changed to:", gameReference.ball_color)
    else:
        gameReference.ball_previous_collision = False

# Summary: Introduced a moving obstacle in the field that bounces the ball when hit, modified paddle height to decrease upon scoring, and added a mechanic to change the ball color randomly upon paddle collision.
