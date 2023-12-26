import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Functionality")

# Colours
TURQUOISE = (50, 100, 100)
GREEN = (50, 200, 50)
RED = (50, 10, 10)

# Game Constants
FPS = 60
VEL = 3
JUMP_SPEED = 5
JUMP_MAX_HEIGHT = 100
GRAVITY = 10

# Rect Constants
PLAYER_HEIGHT, PLAYER_WIDTH = 50, 50

# Rects
platform_rect = pygame.Rect(0, 400, 900, 100)
player_rect = pygame.Rect(100, 400-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

def draw_window():
    WIN.fill(TURQUOISE)
    pygame.draw.rect(WIN, GREEN, platform_rect)
    pygame.draw.rect(WIN, RED, player_rect)
    pygame.display.update()

def handle_player_movement(keys_pressed, jump, fall):
    if keys_pressed[pygame.K_a]:
        player_rect.x -= VEL
    if keys_pressed[pygame.K_d]:
        player_rect.x += VEL
    # if keys_pressed[pygame.K_w] and not jump:
    #     jump = True
    if keys_pressed[pygame.K_s] and not platform_rect.colliderect(player_rect):
        player_rect.y += VEL
    if jump:
        handle_jump(jump, fall)

def handle_jump(jump, fall):
    if player_rect.y < platform_rect.y - PLAYER_HEIGHT - JUMP_MAX_HEIGHT:
        fall = True
    if not fall:
        player_rect.y -= JUMP_SPEED
    else:
        player_rect.y += GRAVITY
        if platform_rect.colliderect(player_rect):
            jump = False
            fall = False

    # if fall:
    #     player_rect.y += GRAVITY
    # else:
    #     player_rect.y -= JUMP_SPEED
    
    # if player_rect.y < platform_rect.y - PLAYER_HEIGHT - JUMP_MAX_HEIGHT:
    #     fall = True
    # if platform_rect.colliderect(player_rect) and fall:
    #     jump = False
    #     fall = False


def main():
    jump = False
    fall = False

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    jump = True
                    handle_jump(jump, fall)
        
        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, jump, fall)

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()