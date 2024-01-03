import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player_width, player_height = 100, 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Ball
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move the ball
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Collision detection
    if (
        ball_y + ball_radius > player_y
        and player_x < ball_x < player_x + player_width
    ):
        ball_y = 0
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(screen, RED, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)


