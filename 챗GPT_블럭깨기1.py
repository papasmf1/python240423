import pygame
import sys
import math

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 400, 12
BLOCK_WIDTH, BLOCK_HEIGHT = 60, 20
BALL_DIAMETER = 10
BALL_RADIUS = BALL_DIAMETER // 2
PADDLE_Y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PADDLE_COLOR = BLUE
BALL_COLOR = WHITE

# Block class
class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)

# Ball class
class Ball:
    def __init__(self, x, y, speed, direction_angle):
        self.rect = pygame.Rect(x, y, BALL_DIAMETER, BALL_DIAMETER)
        self.speed = speed
        self.direction = direction_angle

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        direction_radians = math.radians(self.direction)

        self.rect.x += self.speed * math.cos(direction_radians)
        self.rect.y -= self.speed * math.sin(direction_radians)

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_DIAMETER:
            self.direction = (180 - self.direction) % 360

        if self.rect.y < 0:
            self.direction = (360 - self.direction) % 360

        if self.rect.y > SCREEN_HEIGHT - BALL_DIAMETER:
            return True

        return False

# Paddle class
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(0, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if key[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# Game initialization
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

blocks = []
for i in range(5):
    for j in range(7):
        blocks.append(Block(j * (BLOCK_WIDTH + 10) + 35, i * (BLOCK_HEIGHT + 5) + 35))

paddle = Paddle()
ball = Ball(SCREEN_WIDTH // 2, PADDLE_Y - BALL_DIAMETER, 3, 45)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block.rect)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle.rect)
    pygame.draw.rect(screen, BALL_COLOR, ball.rect)

    if ball.update():
        ball = Ball(SCREEN_WIDTH // 2, PADDLE_Y - BALL_DIAMETER, 3, 45)

    paddle.update()

    for block in blocks:
        if ball.rect.colliderect(block.rect):
            diff = (block.rect.x + BLOCK_WIDTH // 2) - (ball.rect.x + BALL_RADIUS)
            ball.bounce(diff)
            blocks.remove(block)
            break

    pygame.display.update()
    clock.tick(FPS)
