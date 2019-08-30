import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (202, 33, 40)
YELLOW = (251, 209, 9)
BLUE = (53, 74, 127)

pygame.init()
screen_size = (1024, 768)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mondrian generator")

clock = pygame.time.Clock()


def generate_picture():
    xs = sorted([random.randrange(0, 1024, 32) for _ in range(0, 6)])
    ys = sorted([random.randrange(0, 768, 32) for _ in range(0, 6)])
    squares = []
    for _ in range(2, 10):
        i = random.randint(0, 6 - 2)
        x1 = xs[i]
        x2 = xs[i + 1]
        y1 = ys[i]
        y2 = ys[i + 1]
        squares.append({
            'rect': pygame.Rect(x1, y1, x2 - x1, y2 - y1),
            'color': random.choice([RED, YELLOW, BLUE])
        })
    return xs, ys, squares


def draw_picture(xs, ys, squares):
    for square in squares:
        pygame.draw.rect(screen, square['color'], square['rect'])
    for x in xs:
        pygame.draw.line(screen, BLACK, (x, 0), (x, 768), 4)
    for y in ys:
        pygame.draw.line(screen, BLACK, (0, y), (1024, y), 4)


xs, ys, squares = generate_picture()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xs, ys, squares = generate_picture()

    screen.fill(WHITE)

    draw_picture(xs, ys, squares)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
