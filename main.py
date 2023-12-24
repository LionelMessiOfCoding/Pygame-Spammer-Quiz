import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spam Quiz")
FPS = 60

TURQUOISE = (50, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BAR_WIDTH = 20
BAR_HEIGHT = 380

BAR_BACKGROUND = pygame.Rect(20, 50, 30, 400)
BAR = pygame.Rect(25, 60, BAR_WIDTH, BAR_HEIGHT)
BAR_COVER = pygame.Rect(25, 60, BAR_WIDTH, BAR_HEIGHT)
BAR_SAFETY_LINE = pygame.Rect(25, 280, BAR_WIDTH, 5)


def draw_window():
    WIN.fill(TURQUOISE)
    pygame.draw.rect(WIN, BLACK, BAR_BACKGROUND)
    pygame.draw.rect(WIN, RED, BAR)
    pygame.draw.rect(WIN, BLACK, BAR_COVER)
    pygame.draw.rect(WIN, GREEN, BAR_SAFETY_LINE)
    pygame.display.update()

def resize_bar_cover():
    if BAR_COVER.height >= 200:
        BAR_COVER.height -= 25
    elif BAR_COVER.height < 200 and BAR_COVER.height >= 15:
        BAR_COVER.height -= 15

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        if BAR_COVER.height <= BAR_HEIGHT - 1:
            BAR_COVER.height += 1

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    resize_bar_cover()


        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()