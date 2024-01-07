# Import all the necessary packages
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game window
width = 800
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
left_paddle_pos = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle_pos = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Set up the ball
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3
ball_pos = pygame.Rect(width // 2 - ball_radius // 2, height // 2 - ball_radius // 2, ball_radius, ball_radius)
ball_direction = random.choice([-1, 1])

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and right_paddle_pos.y > 0:
        right_paddle_pos.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_pos.y < height - paddle_height:
        right_paddle_pos.y += paddle_speed

    # Move the left paddle (controlled by the system)
    if left_paddle_pos.centery < ball_pos.centery:
        left_paddle_pos.y += paddle_speed
    elif left_paddle_pos.centery > ball_pos.centery:
        left_paddle_pos.y -= paddle_speed

    # Move the ball
    ball_pos.x += ball_speed_x * ball_direction
    ball_pos.y += ball_speed_y

    # Check for collisions with walls
    if ball_pos.y <= 0 or ball_pos.y >= height - ball_radius:
        ball_speed_y *= -1

    # Check for scoring
    if ball_pos.x <= 0 or ball_pos.x >= width - ball_radius:
        # Reset ball position
        ball_pos.x = width // 2 - ball_radius // 2
        ball_pos.y = height // 2 - ball_radius // 2

        # Reset ball speed
        ball_speed_x = 3
        ball_speed_y = 3
        ball_direction = random.choice([-1, 1])

    # Check for collisions with paddles
    if ball_pos.colliderect(left_paddle_pos) or ball_pos.colliderect(right_paddle_pos):
        ball_direction *= -1

    # Clear the window
    window.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(window, WHITE, left_paddle_pos)
    pygame.draw.rect(window, WHITE, right_paddle_pos)
    pygame.draw.ellipse(window, WHITE, ball_pos)

    # Update the window
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
sys.exit()
