import game.globals
import random
import pygame

import random

def introduce_random_obstacles(game):  # Introduce random obstacles on the playing field
    if 'obstacles' not in dir(game):
        game.obstacles = [pygame.Rect(random.randint(100, 700), random.randint(50, 550), 15, 15) for _ in range(3)]
    for obstacle in game.obstacles:
        pygame.draw.rect(game.screen, game.WHITE, obstacle)
    game.functions.append(lambda: move_obstacles(game))

def move_obstacles(game):  # Move the obstacles up and down over time
    for obstacle in game.obstacles:
        if hasattr(obstacle, 'move_up') and obstacle.move_up:
            if obstacle.top > 0:
                obstacle.y -= 1
            else:
                obstacle.move_up = False
        else:
            if obstacle.bottom < game.HEIGHT:
                obstacle.y += 1
            else:
                obstacle.move_up = True
        if game.ball.colliderect(obstacle):
            game.direction[0] = -game.direction[0]
            game.screen.fill(game.BLACK)

def change_ball_size(game):  # Periodically change the ball size to increase difficulty
    if 'ball_timer' not in dir(game):
        game.ball_timer = 0
    game.ball_timer += 1
    if game.ball_timer > 300:
        game.ball.inflate_ip(random.choice([-5, 5]), random.choice([-5, 5]))
        game.ball_timer = 0
    game.functions.append(lambda: check_ball_size_limit(game))

def check_ball_size_limit(game):  # Ensure the ball size stays within limits
    if game.ball.width < 10:
        game.ball.inflate_ip(5, 5)
    if game.ball.width > 30:
        game.ball.inflate_ip(-5, -5)

def reverse_paddle_controls_temp(game):  # Temporarily reverse paddle controls for increased challenge
    if 'reverse_timer' not in dir(game):
        game.reverse_timer = random.randint(500, 1000)
    if game.reverse_timer <= 0:
        original_speed = game.globals.paddle_speed
        game.globals.paddle_speed = -original_speed
        pygame.time.set_timer(pygame.USEREVENT, 500)  # Temporary change
    elif game.reverse_timer > 0:
        game.reverse_timer -= 1
    if game.reverse_timer == 0 and game.globals.paddle_speed < 0:
        game.globals.paddle_speed = abs(game.globals.paddle_speed)

# Summary: Introduced random obstacles that interact with the ball, periodic ball size changes, and temporary reversed paddle controls.

import random

def spawn_obstacle():  # Introduces a stationary obstacle in the game field
    obstacle_width, obstacle_height = 20, 100
    min_x, max_x = GameClass.WIDTH * 0.25, GameClass.WIDTH * 0.75
    min_y, max_y = 50, GameClass.HEIGHT - 150
    obstacle_x = random.randint(min_x, max_x)
    obstacle_y = random.randint(min_y, max_y)
    self.obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

def check_obstacle_collision(ball, obstacle):  # Checks for collision with the obstacle and alters the ball's path
    if ball.colliderect(obstacle):
        self.direction[0] *= -1  # Reverse ball's horizontal direction upon collision
        self.direction[1] *= -1  # Reverse ball's vertical direction upon collision

def render_obstacle(screen, obstacle):  # Renders the obstacle on the screen
    pygame.draw.rect(screen, (255, 0, 0), obstacle)  # Draw the obstacle in red color


def change_paddle_size_on_score(score_left, score_right):  # Adjusts paddle size based on player's score to increase difficulty
    if score_left > score_right:
        GameClass.left_paddle.height = max(50, GameClass.PADDLE_HEIGHT - (score_left - score_right) * 5)
    elif score_right > score_left:
        GameClass.right_paddle.height = max(50, GameClass.PADDLE_HEIGHT - (score_right - score_left) * 5)

def activate_speed_boost_on_key_press():  # Activates a temporary speed boost when a specific key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game.globals.ball_speed_x = min(game.globals.max_ball_speed, game.globals.ball_speed_x * 1.5)
        game.globals.ball_speed_y = min(game.globals.max_ball_speed, game.globals.ball_speed_y * 1.5)

def introduce_random_obstacles():  # Introduces random obstacles on the field that bounce the ball off in a random angle
    obstacles = [pygame.Rect(random.randint(200, 600), random.randint(150, 450), 20, 20) for _ in range(3)]
    for obstacle in obstacles:
        pygame.draw.rect(GameClass.screen, GameClass.WHITE, obstacle)
        if GameClass.ball.colliderect(obstacle):
            GameClass.direction[0] = -GameClass.direction[0]
            GameClass.direction[1] = -GameClass.direction[1] * random.choice([-1, 1])

# Summary: Added a function to change paddle size according to score, a speed boost on key press, and random obstacles that alter ball direction.

def add_moving_obstacles():  # Introduces moving obstacles on the field to increase game difficulty
    obstacle_width, obstacle_height = 20, 60
    obstacle_speed_x = 2
    if 'obstacles' not in game.globals:
        game.globals['obstacles'] = [pygame.Rect(GameClass.WIDTH // 4, GameClass.HEIGHT // 2, obstacle_width, obstacle_height),
                                     pygame.Rect(GameClass.WIDTH // 4 * 3, GameClass.HEIGHT // 2, obstacle_width, obstacle_height)]
    for obstacle in game.globals['obstacles']:
        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
            obstacle_speed_x *= -1
        obstacle.y += obstacle_speed_x

def check_obstacle_collision():  # Checks for collisions between the ball and the moving obstacles
    if 'obstacles' in game.globals:
        for obstacle in game.globals['obstacles']:
            if game.globals.ball.colliderect(obstacle):
                game.globals.direction[0] = -game.globals.direction[0]

def draw_obstacles():  # Draws the moving obstacles on the game screen
    if 'obstacles' in game.globals:
        for obstacle in game.globals['obstacles']:
            pygame.draw.rect(game.globals.screen, GameClass.WHITE, obstacle)

# Summary: Introduced moving obstacles on the field to periodically alter the ball's direction when collided with, adding a new layer of challenge and unpredictability to the Pong game.

import random

def spawn_power_ups():  # Randomly spawns power-up items on the game field
    power_up_types = ['increase_ball_speed', 'decrease_ball_speed', 'shrink_paddle', 'grow_paddle']
    return {'type': random.choice(power_up_types), 'x': random.randint(50, 750), 'y': random.randint(50, 550)}

def apply_power_up(power_up):  # Applies the effects of the collected power-up
    if power_up['type'] == 'increase_ball_speed':
        if abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
            game.globals.ball_speed_x += 1 * (1 if game.globals.ball_speed_x > 0 else -1)
        if abs(game.globals.ball_speed_y) < game.globals.max_ball_speed:
            game.globals.ball_speed_y += 1 * (1 if game.globals.ball_speed_y > 0 else -1)
    elif power_up['type'] == 'decrease_ball_speed':
        game.globals.ball_speed_x -= 1 * (1 if game.globals.ball_speed_x > 0 else -1)
        game.globals.ball_speed_y -= 1 * (1 if game.globals.ball_speed_y > 0 else -1)
    elif power_up['type'] == 'shrink_paddle':
        GameClass.left_paddle.height = max(GameClass.left_paddle.height - 10, 20)
        GameClass.right_paddle.height = max(GameClass.right_paddle.height - 10, 20)
    elif power_up['type'] == 'grow_paddle':
        GameClass.left_paddle.height = min(GameClass.left_paddle.height + 10, 200)
        GameClass.right_paddle.height = min(GameClass.right_paddle.height + 10, 200)

def check_power_ups_collision(power_ups):  # Checks for collision between paddles and power-ups
    for power_up in power_ups:
        if GameClass.left_paddle.colliderect(pygame.Rect(power_up['x'], power_up['y'], 20, 20)):
            apply_power_up(power_up)
            power_ups.remove(power_up)
        elif GameClass.right_paddle.colliderect(pygame.Rect(power_up['x'], power_up['y'], 20, 20)):
            apply_power_up(power_up)
            power_ups.remove(power_up)

# Summary: Introduced a random power-up feature that affects ball speed and paddle size, increasing game complexity.

def spawn_additional_ball():  # Introduces an additional ball into play for increased difficulty
    if len(game.globals.additional_balls) < 1:
        new_ball = pygame.Rect(GameClass.WIDTH // 2, GameClass.HEIGHT // 2, GameClass.BALL_SIZE, GameClass.BALL_SIZE)
        game.globals.additional_balls.append(new_ball)

def move_additional_balls():  # Manages movement for additional balls
    for ball in game.globals.additional_balls:
        ball.x += game.globals.ball_speed_x
        ball.y += game.globals.ball_speed_y

def check_additional_ball_collisions():  # Handles collisions of additional balls with paddles and bounds
    for ball in game.globals.additional_balls:
        if ball.top <= 0 or ball.bottom >= GameClass.HEIGHT:
            game.globals.ball_speed_y = -game.globals.ball_speed_y

        if ball.colliderect(GameClass.left_paddle) or ball.colliderect(GameClass.right_paddle):
            game.globals.ball_speed_x = -game.globals.ball_speed_x
            game.globals.speed_increase_factor += 0.05

        if ball.left <= 0 or ball.right >= GameClass.WIDTH:
            game.globals.additional_balls.remove(ball)
            if ball.left <= 0:
                GameClass.right_score += 1
            elif ball.right >= GameClass.WIDTH:
                GameClass.left_score += 1

# Summary: Added additional balls to the game for increased difficulty, their movement, and collision handling.

import random

def activate_random_obstacle():  # Introduces a moving obstacle that changes direction randomly
    obstacle_size = 30
    obstacle = pygame.Rect(GameClass.WIDTH // 2, GameClass.HEIGHT // 2, obstacle_size, obstacle_size)
    obstacle_speed_x, obstacle_speed_y = 2, 2

    def move_obstacle():
        nonlocal obstacle_speed_x, obstacle_speed_y
        obstacle.x += obstacle_speed_x
        obstacle.y += obstacle_speed_y

        if obstacle.left <= 0 or obstacle.right >= GameClass.WIDTH:
            obstacle_speed_x *= -1
        if obstacle.top <= 0 or obstacle.bottom >= GameClass.HEIGHT:
            obstacle_speed_y *= -1

    def detect_collision_with_ball():
        if obstacle.colliderect(game.ball):
            game.direction[0] *= -1
            game.direction[1] *= -1

    def draw_obstacle():
        pygame.draw.rect(game.screen, GameClass.WHITE, obstacle)

    def update_obstacle():
        move_obstacle()
        detect_collision_with_ball()
        draw_obstacle()

    return update_obstacle

def activate_speed_boost_zone():  # Creates a speed boost zone that increases ball speed when passed
    zone = pygame.Rect(GameClass.WIDTH // 4, GameClass.HEIGHT // 3, GameClass.WIDTH // 2, GameClass.HEIGHT // 3)
    boost_applied = False

    def check_for_boost():
        nonlocal boost_applied
        if zone.colliderect(game.ball) and not boost_applied:
            game.globals.ball_speed_x *= 1.5
            game.globals.ball_speed_y *= 1.5
            boost_applied = True
        elif not zone.colliderect(game.ball):
            boost_applied = False

    def draw_zone():
        pygame.draw.rect(game.screen, (100, 100, 100), zone, 2)

    def update_speed_boost_zone():
        check_for_boost()
        draw_zone()

    return update_speed_boost_zone

def activate_reverse_control_zone():  # Introduces a zone where player controls are inverted momentarily
    reverse_zone = pygame.Rect(GameClass.WIDTH // 2, GameClass.HEIGHT // 4, 100, GameClass.HEIGHT // 2)
    
    def apply_reverse_effect():
        if reverse_zone.colliderect(game.ball):
            game.globals.paddle_speed *= -1
        else:
            game.globals.paddle_speed = abs(game.globals.paddle_speed)
    
    def draw_reverse_zone():
        pygame.draw.rect(game.screen, (150, 0, 0), reverse_zone, 2)

    def update_reverse_control_zone():
        apply_reverse_effect()
        draw_reverse_zone()

    return update_reverse_control_zone


import random

def spawn_obstacle():  # Spawns an obstacle that moves horizontally across the screen, adding difficulty
    obstacle_width = 20
    obstacle_height = 80
    obstacle_speed_x = random.choice([-2, 2]) 
    obstacle = pygame.Rect(GameClass.WIDTH // 4, GameClass.HEIGHT // 2 - obstacle_height // 2, obstacle_width, obstacle_height)

    def move_obstacle():
        nonlocal obstacle
        if obstacle.left <= 0 or obstacle.right >= GameClass.WIDTH:
            obstacle_speed_x = -obstacle_speed_x
        obstacle.x += obstacle_speed_x
        if obstacle.colliderect(GameClass.ball):
            # Reverse ball direction if it hits the obstacle
            game.globals.ball_speed_x = -game.globals.ball_speed_x
            game.globals.ball_speed_y = -game.globals.ball_speed_y
        pygame.draw.rect(GameClass.screen, GameClass.WHITE, obstacle)

    return move_obstacle

def shrink_paddles_on_score():  # Reduces paddle size each time a point is scored, increasing difficulty gradually
    def adjust_paddle():
        shrink_factor = 5
        if GameClass.left_score or GameClass.right_score: 
            GameClass.left_paddle.height = max(20, GameClass.PADDLE_HEIGHT - shrink_factor * GameClass.left_score)
            GameClass.right_paddle.height = max(20, GameClass.PADDLE_HEIGHT - shrink_factor * GameClass.right_score)
    return adjust_paddle

def random_ball_effects():  # Introduces random effects to the ball's behavior at intervals
    effect_interval = 500  # milliseconds
    last_effect_time = pygame.time.get_ticks()

    def apply_effect():
        nonlocal last_effect_time
        current_time = pygame.time.get_ticks()
        if current_time - last_effect_time >= effect_interval:
            last_effect_time = current_time
            effect = random.choice(["speed_up", "slow_down", "random_direction"])
            if effect == "speed_up" and abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
                game.globals.ball_speed_x *= 1.5
                game.globals.ball_speed_y *= 1.5
            elif effect == "slow_down":
                game.globals.ball_speed_x *= 0.5
                game.globals.ball_speed_y *= 0.5
            elif effect == "random_direction": 
                game.globals.ball_speed_x *= random.choice([-1, 1])
                game.globals.ball_speed_y *= random.choice([-1, 1])
    
    return apply_effect

# Summary: Added functions to increase game difficulty, including spawning horizontal obstacles, shrinking paddles on scores, and randomizing ball effects.
