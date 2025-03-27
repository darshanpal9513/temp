import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.5
JUMP_STRENGTH = -8
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_VELOCITY = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird
bird = pygame.Rect(100, HEIGHT // 2, 40, 30)
velocity = 0

# Pipe setup
pipes = []
def create_pipe():
    height = random.randint(100, 400)
    pipes.append(pygame.Rect(WIDTH, height, PIPE_WIDTH, HEIGHT - height))
    pipes.append(pygame.Rect(WIDTH, 0, PIPE_WIDTH, height - PIPE_GAP))

create_pipe()

# Game loop
clock = pygame.time.Clock()
running = True
score = 0
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = JUMP_STRENGTH
    
    # Bird physics
    velocity += GRAVITY
    bird.y += velocity
    
    # Pipe movement
    for pipe in pipes:
        pipe.x -= PIPE_VELOCITY
    
    # Remove old pipes and create new ones
    if pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.pop(0)
        create_pipe()
        score += 1
    
    # Check for collisions
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False
    if bird.y > HEIGHT or bird.y < 0:
        running = False
    
    # Draw bird
    pygame.draw.rect(screen, BLUE, bird)
    
    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    
    # Update display
    pygame.display.update()
    clock.tick(30)

pygame.quit()