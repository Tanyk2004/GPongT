import math
import game.globals
import pygame
import sys
import random
from game.wildcard_functions import wildcard_function, load_and_execute_functions
from llm.change_files import read_file, write_to_python_file, read_functions_from_file, append_to_python_file, get_summary
from llm.gpt_api import GPT
import time


class GameClass:
    
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    BALL_COLOR = (190,190,190)
    RED = (255, 0 ,0)
    GREEN = (0, 255, 0)
    
    PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
    BALL_SIZE = 15

    def __init__(self):   
        """
        Initializes the game by setting up the display, paddles, ball, and other game variables.
        """
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.screen = pygame.display.set_mode((GameClass.WIDTH, GameClass.HEIGHT))
        game.globals.screen = self.screen
        pygame.display.set_caption("Pong Game")

        self.left_paddle = pygame.Rect(30, (GameClass.HEIGHT - GameClass.PADDLE_HEIGHT) // 2, GameClass.PADDLE_WIDTH, GameClass.PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(GameClass.WIDTH - 30 - GameClass.PADDLE_WIDTH, (GameClass.HEIGHT - GameClass.PADDLE_HEIGHT) // 2, GameClass.PADDLE_WIDTH, GameClass.PADDLE_HEIGHT)
        self.ball = pygame.Rect(GameClass.WIDTH // 2, GameClass.HEIGHT // 2, GameClass.BALL_SIZE, GameClass.BALL_SIZE)
        self.functions = []
        self.game_obstacles = []
        # Score tracking
        self.left_score = 0
        self.right_score = 0
        self.winning_score = 5  # Set a winning score
        self.direction = [1, 1]
        self.current_text = ""
        self.paddle_color = GameClass.WHITE
        self.ball_color = GameClass.BALL_COLOR
        self.current_file_number = 0
    # functions for control
    def check_player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.right_paddle.top > 0:
            self.right_paddle.y -= game.globals.paddle_speed
        if keys[pygame.K_DOWN] and self.right_paddle.bottom < GameClass.HEIGHT:
            self.right_paddle.y += game.globals.paddle_speed

    def ai_movement(self):
        # AI Movement
        if self.left_paddle.centery < self.ball.centery and self.left_paddle.bottom < self.HEIGHT:
            self.left_paddle.y += game.globals.paddle_speed
        if self.left_paddle.centery > self.ball.centery and self.left_paddle.top > 0:
            self.left_paddle.y -= game.globals.paddle_speed

    def check_collisions(self):
        # Ball collision with top and bottom, with boundary correction
        if self.ball.top <= 0:
            self.ball.top = 0
            # game.globals.ball_speed_y = -game.globals.ball_speed_y
            self.direction[1] = -self.direction[1]
        elif self.ball.bottom >= GameClass.HEIGHT:
            self.ball.bottom = GameClass.HEIGHT
            # game.globals.ball_speed_y = -game.globals.ball_speed_y
            self.direction[1] = -self.direction[1]

        # Ball collision with paddles
        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            # game.globals.ball_speed_x = -game.globals.ball_speed_x
            self.direction[0] = -self.direction[0]
            self.increase_speed()
        
        point_scored = False
        # Ball reset if it goes out of bounds
        if self.ball.left <= 0:
            self.right_score += 1
            point_scored = True
        elif self.ball.right >= GameClass.WIDTH:
            self.left_score += 1
            point_scored = True
        
        if (point_scored):
            self.reset_ball()
            
            if self.check_win():
                return True
            self.llm_call()
        return False

    # TODO: refactor by putting this into the gpt_api class
    def llm_call(self):
        #make the llm generate a function and update gpt_gen_dy
        font = pygame.font.Font(None, 36)
        text = font.render("Loading...", True, GameClass.WHITE)
        self.screen.blit(text, (GameClass.WIDTH // 2 - text.get_width() // 2, 50))
        pygame.display.flip()
        game_file_state = read_file("./game/game.py")
        prompt = read_file("./llm/prompt.txt") + game_file_state
        user_prompt = read_file("./llm/user_prompt.txt")

        resp = GPT().text_completion(system_prompt=prompt, user_prompt=user_prompt)
        new_resp = ""
        for line in resp.split("\n"):
            if '```' not in line:
                new_resp += line + "\n"
        
        new_resp = "\n" + new_resp
        append_to_python_file(new_resp, "game/gpt_generated_dynamic.py")
        try:
            self.current_text = get_summary("./game/gpt_generated_dynamic.py")
        except Exception as e:
            self.current_text = "I FORGOR TO WRITE A SUMMARY T_T"
        
        #load newly generated function (asynch ???)
        # TODO: maybe we can load and store one at a time instead of all every time?
        self.functions = load_and_execute_functions("game.gpt_generated_dynamic")

    def display_summary_message(self, summary_text):  # Displays a message on the screen for a set duration
        font = pygame.font.Font(None, 24)
        max_width = GameClass.WIDTH - 40
        lines = []
        words = summary_text.split()
        current_line = ""
        for word in words:
            test_line = current_line + " " + word
            text_surface = font.render(test_line, True, GameClass.BALL_COLOR)
            if text_surface.get_width() < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        y_offset = GameClass.HEIGHT - 60 - (len(lines) - 1) * 24
        for line in lines:
            text = font.render(line, True, GameClass.BALL_COLOR)
            self.screen.blit(text, (GameClass.WIDTH // 2 - text.get_width() // 2, y_offset))
            y_offset += 24
        pygame.display.flip()

    def display_win_loss(self, left_score, right_score):
        # Clear the screen with a blank color
        self.screen.fill(GameClass.BLACK)

        # Determine the win/loss message
        font = pygame.font.Font(None, 60)
        if left_score > right_score:
            score_text = "You Lose!"
            text = font.render(score_text, True, GameClass.RED)
        else:
            score_text = "You Win!"
            text = font.render(score_text, True, GameClass.GREEN)

        # Draw the message at the center of the screen
        self.screen.blit(text, (GameClass.WIDTH // 2 - text.get_width() // 2, GameClass.HEIGHT // 2 - text.get_height() // 2))

        # Update the display
        pygame.display.flip()
        pygame.time.delay(3000)  # Show the message for 3 seconds

    def check_win(self):
        # Check for winning condition
        if self.left_score >= self.winning_score:
            print("Left Player Wins!")
            self.display_win_loss(self.left_score, self.right_score)
            time.sleep(3)
            return True
        elif self.right_score >= self.winning_score:
            self.display_win_loss(self.left_score, self.right_score)
            time.sleep(3)
            return True
        return False

    def increase_speed(self):
        if abs(game.globals.ball_speed_x) < game.globals.max_ball_speed:
            game.globals.ball_speed_x += game.globals.speed_increase_factor * (1 if game.globals.ball_speed_x > 0 else -1)
        if abs(game.globals.ball_speed_y) < game.globals.max_ball_speed:
            game.globals.ball_speed_y += game.globals.speed_increase_factor * (1 if game.globals.ball_speed_y > 0 else -1)

    def reset_ball(self):
        self.ball.x, self.ball.y = GameClass.WIDTH // 2, GameClass.HEIGHT // 2
        # Reset speed with a random direction
        game.globals.ball_speed_x = 3 * random.choice((1, -1))
        game.globals.ball_speed_y = 3 * random.choice((1, -1))

    def entry_point(self):
        #load gpt added function before game loop
        
        background = pygame.image.load('./static/background_old.png')
        pygame.mixer.music.load('./static/background_music.mp3')
        pygame.mixer.music.play(-1)
    
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            for function in self.functions:
                try:
                    function(self)
                except Exception as e:
                    pass

            self.check_player_movement()
            self.ai_movement()
            
            # Ball movement
            self.ball.x += self.direction[0] * abs(game.globals.ball_speed_x)
            self.ball.y += self.direction[1] *abs(game.globals.ball_speed_y)

            # Drawing
            self.screen.blit(background, (0, 0))
            pygame.draw.rect(self.screen, self.paddle_color, self.left_paddle)
            pygame.draw.rect(self.screen, self.paddle_color, self.right_paddle)
            pygame.draw.ellipse(self.screen, self.ball_color, self.ball)
            for obstacle in self.game_obstacles:
                if obstacle is not None and isinstance(obstacle, pygame.Rect):
                    pygame.draw.rect(self.screen, GameClass.WHITE, obstacle)
                
                elif obstacle is not None:
                    pygame.draw.ellipse(self.screen, GameClass.WHITE, obstacle)
            if (self.check_collisions()):
                break

            # Display scores
            font = pygame.font.Font(None, 36)
            score_text = f"{self.left_score} - {self.right_score}"
            text = font.render(score_text, True, GameClass.WHITE)
            self.screen.blit(text, (GameClass.WIDTH // 2 - text.get_width() // 2, 20))
            self.display_summary_message(self.current_text)

            pygame.display.flip()
            pygame.time.Clock().tick(60)
        pygame.quit()
        sys.exit()