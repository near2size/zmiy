import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

ddt = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 0, 0),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (255, 165, 0),
    (128, 0, 128),
    (255, 192, 203),
    (165, 42, 42),
    (128, 128, 128),
    (211, 211, 211),
    (169, 169, 169),
    (255, 215, 0),
    (192, 192, 192),
    (64, 224, 208),
    (128, 128, 0),
    (128, 0, 0),
    (0, 0, 128),
    (0, 128, 128),
    (255, 127, 80),
    (0, 255, 0),
    (75, 0, 130),
    (135, 206, 235),
    (238, 130, 238),
    (240, 230, 140),
    (210, 180, 140),
    (245, 245, 220),
    (127, 255, 212),
    (220, 20, 60),
    (250, 128, 114),
    (255, 99, 71),
    (189, 252, 201),
    (255, 218, 185),
    (251, 206, 177),
    (221, 160, 221),
    (230, 230, 250),
    (165, 42, 42)
]
# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (169, 169, 169)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
TURQUOISE = (64, 224, 208)
OLIVE = (128, 128, 0)
MAROON = (128, 0, 0)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
CORAL = (255, 127, 80)
LIME = (0, 255, 0)
INDIGO = (75, 0, 130)
SKY_BLUE = (135, 206, 235)
VIOLET = (238, 130, 238)
KHAKI = (240, 230, 140)
TAN = (210, 180, 140)
BEIGE = (245, 245, 220)
AQUAMARINE = (127, 255, 212)
CRIMSON = (220, 20, 60)
SALMON = (250, 128, 114)
TOMATO = (255, 99, 71)
MINT = (189, 252, 201)
PEACH = (255, 218, 185)
APRICOT = (251, 206, 177)
PLUM = (221, 160, 221)
MAGENTA = (255, 0, 255)
LAVENDER = (230, 230, 250)
BEIGE = (245, 245, 220)
AUBURN = (165, 42, 42)
CRIMSON = (220, 20, 60)

dict_of_color = {
    'белый': (255, 255, 255),
    'красный': (255, 0, 0),
    'зеленый': (0, 255, 0),
    'синий': (0, 0, 255),
    'черный': (0, 0, 0),
    'желтый': (255, 255, 0),
    'голубой': (0, 255, 255),
    'пурпурный': (255, 0, 255),
    'оранжевый': (255, 165, 0),
    'фиолетовый': (128, 0, 128),
    'розовый': (255, 192, 203),
    'коричневый': (165, 42, 42),
    'серый': (128, 128, 128),
    'светло-серый': (211, 211, 211),
    'темно-серый': (169, 169, 169),
    'золотистый': (255, 215, 0),
    'серебряный': (192, 192, 192),
    'бирюзовый': (64, 224, 208),
    'оливковый': (128, 128, 0),
    'каштановый': (128, 0, 0),
    'темно-синий': (0, 0, 128),
    'черно-зеленый': (0, 128, 128),
    'коралловый': (255, 127, 80),
    'лаймовый': (0, 255, 0),
    'индиго': (75, 0, 130),
    'небесно-голубой': (135, 206, 235),
    'фиалковый': (238, 130, 238),
    'хаки': (240, 230, 140),
    'желто-коричневый': (210, 180, 140),
    'бежевый': (245, 245, 220),
    'аквамариновый': (127, 255, 212),
    'малиновый': (220, 20, 60),
    'лососевый': (250, 128, 114),
    'томатный': (255, 99, 71),
    'мятный': (189, 252, 201),
    'персиковый': (255, 218, 185),
    'абрикосовый': (251, 206, 177),
    'сливовый': (221, 160, 221),
    'лавандовый': (230, 230, 250),
    'каштановый': (165, 42, 42)
}

with open('data.txt', 'r', encoding='utf=8') as filedata:
    s = filedata.read().split('\n')
    WINDOW_WIDTH = int(s[0])
    WINDOW_HEIGHT = int(s[1])
    color_of_apple = dict_of_color[(s[2].lower())]
    color_of_zmiy = dict_of_color[(s[3].lower())]
    color_of_back = dict_of_color[(s[4].lower())]
    color_of_text = dict_of_color[(s[5].lower())]
    speedtick = s[6]
    vibor = len(s[7]) - 2

# Определение параметров окна
CELL_SIZE = 20

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Змейка')


# Функция отображения меню
def display_menu():
    font = pygame.font.Font(None, 36)

    play_text = font.render("Играть", True, color_of_text)
    exit_text = font.render("Выход", True, color_of_text)

    play_rect = play_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

    window.blit(play_text, play_rect)
    window.blit(exit_text, exit_rect)

    pygame.display.update()


# Функция игры
def play_game():
    # Инициализация Pygame
    pygame.init()

    # Определение цветов
    # Определение цветов

    # Определение параметров окна
    CELL_SIZE = 20

    # Создание окна
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Змейка')

    # Класс змейки
    class Snake:
        def __init__(self):
            self.length = 1
            self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
            self.color = color_of_zmiy

        def get_head_position(self):
            return self.positions[0]

        def move(self):
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * CELL_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * CELL_SIZE)))
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

        def reset(self):
            global score, maxx
            if int(score) > int(maxx):
                with open('max_score.txt', 'w', encoding='utf8') as file:
                    print(str(score).strip(), file=file)
                    font = pygame.font.Font(None, 36)
                    max_score_text = font.render(f"Max Score: {maxx}", True, color_of_text)
                    window.blit(max_score_text, (10, 30))
            score = 0
            self.length = 1
            self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        def draw(self, surface):
            for p in self.positions:
                if vibor:
                    pygame.draw.rect(surface, self.color, (p[0], p[1], CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(surface, ddt[random.randint(0, len(ddt)) - 1], (p[0], p[1], CELL_SIZE, CELL_SIZE))

    # Класс яблока
    class Apple:
        def __init__(self):
            self.position = (0, 0)
            self.color = color_of_apple
            self.randomize_position()

        def randomize_position(self):
            self.position = (random.randint(0, (WINDOW_WIDTH // CELL_SIZE - 1)) * CELL_SIZE,
                             random.randint(0, (WINDOW_HEIGHT // CELL_SIZE - 1)) * CELL_SIZE)

        def draw(self, surface):
            pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

    # Глобальные переменные
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    # Основной игровой цикл
    def main():
        global score_text, max_score_text, score, maxx
        with open('max_score.txt', 'r', encoding='utf8') as file:
            maxx = file.read().strip('\n')

        running = True
        clock = pygame.time.Clock()
        snake = Snake()
        apple = Apple()
        score = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    snake.direction = LEFT
                if keys[pygame.K_RIGHT]:
                    snake.direction = RIGHT
                if keys[pygame.K_UP]:
                    snake.direction = UP
                if keys[pygame.K_DOWN]:
                    snake.direction = DOWN

            snake.move()
            if snake.get_head_position() == apple.position:
                snake.length += 1
                score += 1
                apple.randomize_position()

            window.fill(color_of_back)
            snake.draw(window)
            apple.draw(window)

            # Отобразить количество собранных яблок
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, color_of_text)
            max_score_text = font.render(f"Max Score: {maxx}", True, color_of_text)
            window.blit(score_text, (10, 10))
            window.blit(max_score_text, (10, 30))

            pygame.display.update()
            clock.tick(int(speedtick))  # Устанавливаем скорость игры

        pygame.quit()

        sys.exit()

    if __name__ == '__main__':
        main()


# Основной цикл
def main():
    running = True
    in_menu = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and in_menu:
                x, y = pygame.mouse.get_pos()
                if WINDOW_WIDTH // 2 - 50 < x < WINDOW_WIDTH // 2 + 50:
                    if WINDOW_HEIGHT // 2 - 70 < y < WINDOW_HEIGHT // 2 - 30:
                        in_menu = False
                        play_game()
                    elif WINDOW_HEIGHT // 2 + 30 < y < WINDOW_HEIGHT // 2 + 70:
                        running = False

        window.fill(color_of_back)

        if in_menu:
            display_menu()

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
