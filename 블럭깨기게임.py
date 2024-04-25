import pygame
import random

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 패들 클래스 정의
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 580

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

        if self.rect.x > 700:
            self.rect.x = 700

# 공 클래스 정의
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 200
        self.speed_x = random.choice([-3, 3])
        self.speed_y = -3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - 10:
            self.speed_x *= -1

        if self.rect.y <= 0:
            self.speed_y *= -1

# 블럭 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# 게임 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("블럭 깨기 게임")

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# 패들 생성
paddle = Paddle()
all_sprites.add(paddle)

# 블럭 생성
block_width = 70
block_height = 20
for row in range(5):
    for column in range(10):
        block = Block(GREEN, block_width, block_height)
        block.rect.x = column * (block_width + 2) + 5
        block.rect.y = row * (block_height + 2) + 50
        all_sprites.add(block)
        blocks.add(block)

# 공 생성
ball = Ball()
all_sprites.add(ball)

# 게임 루프
running = True
clock = pygame.time.Clock()
FPS = 30  # FPS 값 조절

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 로직
    all_sprites.update()

    # 충돌 체크
    hit_blocks = pygame.sprite.spritecollide(ball, blocks, True)
    if len(hit_blocks) > 0:
        ball.speed_y *= -1

    # 패들과의 충돌 체크
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y *= -1

    # 게임 종료 조건
    if ball.rect.y >= SCREEN_HEIGHT:
        running = False

    # 그리기
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)  # FPS 조절

pygame.quit()
