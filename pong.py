# Import pygame and sys modules
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display dimensions
WIDTH, HEIGHT = 600, 400
# Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set the ball's speed
BALL_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the window
pygame.display.set_caption("Pong")

# Initialize ball position in the middle of the screen
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
# Set initial ball movement speed
ball_speed_x, ball_speed_y = BALL_SPEED, BALL_SPEED

# Define paddle dimensions
paddle_width, paddle_height = 15, 60

# Set initial paddle positions
left_paddle_x, right_paddle_x = 10, WIDTH - 25
left_paddle_y, right_paddle_y = HEIGHT // 2 - paddle_height // 2, HEIGHT // 2 - paddle_height // 2

# Set the paddle's speed
paddle_speed = 7

# Initialize scores for the left and right players
score_left, score_right = 0, 0

# Create a font object
font = pygame.font.Font(None, 36)

# Define a function to reset the ball to the center and start moving again
def reset_ball():
    return WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Detect key presses
    keys = pygame.key.get_pressed()
    # Move left paddle up
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    # Move left paddle down
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    # Move right paddle up
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    # Move right paddle down
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if (left_paddle_x < ball_x < left_paddle_x + paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height) \
    or (right_paddle_x < ball_x < right_paddle_x + paddle_width and right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Score update when ball passes left or right edge
    if ball_x <= 0:
        score_right += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
    if ball_x >= WIDTH:
        score_left += 1
        ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()

    # Drawing the game state
    screen.fill(BLACK)
    # Draw left and right paddles
    pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x - 10, ball_y - 10, 20, 20))
    # Display the score
    score_display = font.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 40, 10))

    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)
