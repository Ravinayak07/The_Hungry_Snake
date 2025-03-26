import pygame, random
from random import (
    randint,
)  # The randint() method returns an integer number selected element from the specified range
import time
import os  # The OS module in python provides functions for interacting with the operating system.

# initialize all imported pygame modules
pygame.init()
# dimensions of the window
width = 1366
height = 768
pause_music = 0
# Input_details
name = input("Enter your Name:-")
print("Loading Please Wait", end="")
# time_delay loop
for x in range(15):
    time.sleep(0.2)
    print(". ", end="")

clock = pygame.time.Clock()  # used to limit the runtime speed of the game
# game_screen = pygame.display.set_mode(
#     (width, height), pygame.FULLSCREEN
# )  # for full screen
game_screen = pygame.display.set_mode(
    (1000, 800)
)  # for screen of mentioned dimensions
pygame.display.set_caption("The Hungry Snake ")
icon = pygame.image.load("images/bg_imgs/icon.png")
pygame.display.set_icon(icon)
pygame.display.update()

# Load Images

# snake head
Green_head = pygame.image.load("images/snake/Green_head.png")
Orange_head = pygame.image.load("images/snake/Orange_head.png")
snake_head_1 = Green_head
snake_head_2 = Orange_head

# snake food(fruits)
Apple = pygame.image.load("images/food/Apple.png")
green_apple = pygame.image.load("images/food/green_apple.png")
pine_apple = pygame.image.load("images/food/pine_apple.png")
blueberry = pygame.image.load("images/food/blueberry.png")
strawberry = pygame.image.load("images/food/strawberry.png")

# snake food(eggs)
Green_egg = pygame.image.load("images/food/Green_egg.png")
red_egg = pygame.image.load("images/food/red_egg.png")
yellow_egg = pygame.image.load("images/food/yellow_egg.png")

# snake food(humans)
abhay_food = pygame.image.load("images/food/abhay_food.png")
arjun_food = pygame.image.load("images/food/arjun_food.png")
Ravi_food = pygame.image.load("images/food/Ravi_food.png")

# About pics
about_pic = pygame.image.load("images/bg_imgs/about_pic.jpg")
LPU_logo = pygame.image.load("images/bg_imgs/LPU-logo.png")
ravi = pygame.image.load("images/bg_imgs/ravi.jpg")
abhay = pygame.image.load("images/bg_imgs/abhay.jpg")
arjun = pygame.image.load("images/bg_imgs/arjun.jpg")

# back_ground imgs
welcome = pygame.image.load("images/bg_imgs/welcome.jpg")
menu_pic = pygame.image.load("images/bg_imgs/menu_pic.jpg")
options_pic = pygame.image.load("images/bg_imgs/options_pic.jpg")
opening_pic = pygame.image.load("images/bg_imgs/opening_pic.jpg")
water = pygame.image.load("images/bg_imgs/water.jpg")
game_over_1 = pygame.image.load("images/bg_imgs/game_over_1.jpg")
game_over_2 = pygame.image.load("images/bg_imgs/game_over_2.jpg")
snake_right = pygame.image.load("images/bg_imgs/snake_right.png")
snake_left = pygame.image.load("images/bg_imgs/snake_left.png")

# assigning snake food
food_pic = Ravi_food  # Ravi_food #if u want to change the food then just replace the assigned food pic with any other food pic mentioned above.

# colors
black = (10, 10, 10)
white = (250, 250, 250)
red = (255, 0, 0)
light_red = (255, 49, 16)
b_red = (240, 0, 0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (255, 192, 0)
light_yellow = (255, 255, 0)
purple = (43, 3, 132)
light_purple = (251, 8, 224)
sky_blue = (54, 250, 234)
back_color = sky_blue  # background color of 2 players mode

# fonts
font = pygame.font.SysFont("comicsansms", 50)
smallfont = pygame.font.SysFont("comicsansms", 25)
bigfont = pygame.font.SysFont("comicsansms", 85)

# variables
FPS = 12  # frames per second
block_size = 30
food_size = 32
food_count = 1
direction = "right"
foods = set([])
score = 0
Score = ""

# music
# pygame.mixer is a module for loading and playing sounds
pygame.mixer.init()  # initialize the mixer modules


class Snake:
    def __init__(self, pos, vel, angle, image, color=green):
        self.pos = pos
        self.vel = vel
        self.angle = angle
        self.img = image
        self.list = []
        self.lenght = 1
        self.head = self.img
        self.color = color

    def score_display(self, pos):
        score(self.lenght - 1, pos, self.color)

    def key_event(self, direction):
        self.angle = direction

    def eat(self):
        for food in foods:
            if (
                self.pos[0] > food.pos[0]
                and self.pos[0] < food.pos[0] + food_size
                or self.pos[0] + block_size > food.pos[0]
                and self.pos[0] < food.pos[0] + food_size
            ):
                if (
                    self.pos[1] > food.pos[1]
                    and self.pos[1] < food.pos[1] + food.size
                    or self.pos[1] + block_size > food.pos[1]
                    and self.pos[1] < food.pos[1] + food.size
                ):
                    foods.remove(food)
                    foods.add(randFoodGen())
                    self.lenght += 1

    def update(self):
        gameOver = False

        if (self.angle == "right") and (self.vel[0] != -block_size):
            self.vel[0] = +block_size
            self.vel[1] = 0
            self.head = pygame.transform.rotate(self.img, 270)

        if (self.angle == "left") and (self.vel[0] != block_size):
            self.vel[0] = -block_size
            self.vel[1] = 0
            self.head = pygame.transform.rotate(self.img, 90)

        if (self.angle == "up") and (self.vel[1] != block_size):
            self.head = self.img
            self.vel[1] = -block_size
            self.vel[0] = 0

        if (self.angle == "down") and (self.vel[1] != -block_size):
            self.vel[1] = +block_size
            self.vel[0] = 0
            self.head = pygame.transform.rotate(self.img, 180)

        # update movement
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # build the snake
        snakeHead = []
        snakeHead.append(self.pos[0])
        snakeHead.append(self.pos[1])
        self.list.append(snakeHead)
        if len(self.list) > self.lenght:
            del self.list[0]
        if snakeHead in self.list[:-1]:
            gameOver = True
        # draw the snake
        for XnY in self.list[:-1]:
            pygame.draw.rect(
                game_screen, self.color, [XnY[0], XnY[1], block_size, block_size]
            )
        # draw the snake's head
        game_screen.blit(self.head, (self.list[-1][0], self.list[-1][1]))

        # check if out of boundries
        if (
            self.pos[0] < 0
            or self.pos[0] >= width
            or self.pos[1] < 0
            or self.pos[1] >= height
        ):
            gameOver = True
        return gameOver


class Food:
    def __init__(self, pos, size, image=None):
        self.pos = pos
        self.img = image
        self.size = size

    def draw(self):
        game_screen.blit(self.img, self.pos)


# to calculate score
def score(score, pos, color):
    text = smallfont.render("Score: " + str(score), True, color)
    game_screen.blit(text, pos)


# to display text
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [x, y])


# display snake
def plot_snake(game_screen, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(game_screen, yellow, (x, y), snake_size)


# Message displaying for buttons
def message_display(text, x, y, fs):
    largeText = pygame.font.Font("freesansbold.ttf", fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    game_screen.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


# Message displaying for field
def message_display1(text, x, y, fs, c):
    largeText = pygame.font.Font("freesansbold.ttf", fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    game_screen.blit(TextSurf, TextRect)


def text_objects1(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


def game_controls():
    controlls = True
    game_screen.fill(white)
    message_screen("Controls", green, -120, "large")
    message_screen("Green movement: Arrow keys", green, -30, "small")
    message_screen("Purple movement: W, A, S, D keys", purple, 10, "small")
    message_screen("Pause: P", black, 60, "small")
    while controlls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controlls = False
                elif event.key == pygame.K_ESCAPE:
                    exit()

        controlls = button(
            "Main Menu",
            (width / 2 - 70, height - 150, 140, 50),
            yellow,
            light_yellow,
            action="switch",
        )
        button(
            "exit",
            (width / 2 + 120, height - 150, 100, 50),
            red,
            light_red,
            action="quit",
        )

        clock.tick(30)
        pygame.display.update()


def text_objects10(text, color, size="small"):  # change
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = font.render(text, True, color)
    elif size == "large":
        textSurface = bigfont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, pos, size="small"):
    text_surf, text_rect = text_objects10(msg, color, size)  # change
    text_rect.center = (pos[0] + (pos[2] / 2), pos[1] + (pos[3] / 2))
    game_screen.blit(text_surf, text_rect)


def message_screen(msg, color, y_displace=0, size="small"):
    text_surf, text_rect = text_objects10(msg, color, size)
    text_rect.center = (width / 2), (height / 2) + y_displace
    game_screen.blit(text_surf, text_rect)


def randFoodGen():
    new_food = Food(
        [
            round(random.randrange(food_size, width - food_size) / 10) * 10,
            round(random.randrange(food_size, height - food_size) / 10) * 10,
        ],
        food_size,
        food_pic,
    )
    return new_food


# for mute and unmute
def button2(text, xmouse, ymouse, x, y, width, height, i, a, fs):
    # mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_screen, a, [x - 2.5, y - 2.5, width + 5, height + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(game_screen, i, [x, y, width, height])
    message_display(text, (x + width + x) / 2, (y + height + y) / 2, fs)


def music():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        mouse = pygame.mouse.get_pos()  # get the mouse cursor position
        click = pygame.mouse.get_pressed()  # get the state of the mouse buttons
        game_screen.blit(options_pic, (0, 0))  # draw one image onto another

        if button2(
            "Stop Background Music",
            mouse[0],
            mouse[1],
            (width / 2 - 150),
            200,
            300,
            70,
            green,
            purple,
            25,
        ):
            pygame.mixer.music.pause()
            pause_music = 1
        if button2(
            "Play Background Music",
            mouse[0],
            mouse[1],
            (width / 2 - 150),
            400,
            300,
            70,
            green,
            purple,
            25,
        ):
            pygame.mixer.music.unpause()
            pause_music = 0
        button("Back", mouse[0], mouse[1], 0, 10, 200, 50, red, b_red, 30, 8)

        pygame.display.update()


def about():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game_screen.blit(about_pic, (0, 0))
        game_screen.blit(LPU_logo, (996, 0))
        game_screen.blit(ravi, (280, 420))
        game_screen.blit(arjun, (280, 530))
        game_screen.blit(abhay, (280, 630))
        button("Back", mouse[0], mouse[1], 0, 10, 200, 50, red, light_purple, 30, 8)

        pygame.display.update()


# Options Menu:
def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game_screen.blit(options_pic, (0, 0))
        # Single player button
        button(
            "Single Player",
            mouse[0],
            mouse[1],
            (width / 2 - 150),
            250,
            300,
            50,
            green,
            b_green,
            30,
            5,
        )
        # 2 player button
        button(
            "2 Players",
            mouse[0],
            mouse[1],
            (width / 2) - 150,
            350,
            300,
            50,
            green,
            b_green,
            30,
            6,
        )
        button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red, light_purple, 30, 8)
        pygame.display.update()


def settings():
    flag = True
    while flag == True:
        for event in pygame.event.get():  # get events from the queue
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game_screen.blit(options_pic, (0, 0))
        button(
            "Background music",
            mouse[0],
            mouse[1],
            (width / 2) - 250,
            250,
            500,
            70,
            green,
            purple,
            30,
            9,
        )
        button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red, purple, 30, 8)
        pygame.display.update()


# Buttons:
def button(text, xmouse, ymouse, x, y, width, height, i, a, fs, b):
    if x + width > xmouse > x and y + height > ymouse > y:
        pygame.draw.rect(game_screen, a, [x - 2.5, y - 2.5, width + 5, height + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 2:
                settings()
            elif b == 3:
                about()
            elif b == 4:
                exit()
            elif b == 5:
                play_single()
            elif b == 6:
                play_multi()
            elif b == 8:
                main()
            elif b == 9:
                music()
            else:
                return True

    else:
        pygame.draw.rect(game_screen, i, [x, y, width, height])
    message_display(text, (x + width + x) / 2, (y + height + y) / 2, fs)


def play_single():
    pygame.mixer.music.load("music/single_player.mp3")
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 600
    snake_y = 500
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    score = 0

    init_velocity = 15

    food_x = random.randint(20, width / 2)
    food_y = random.randint(20, height / 2)
    score = 0

    snk_list = []
    snk_length = 1

    fps = 30
    while not exit_game:

        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            game_screen.blit(game_over_1, (0, 0))
            global Score
            Score = str(score)
            text_screen(Score, black, 790, 280)
            button(
                "Back", mouse[0], mouse[1], 1166, 650, 200, 50, red, light_purple, 30, 1
            )
            button(
                "Restart",
                mouse[0],
                mouse[1],
                600,
                650,
                200,
                50,
                (255, 192, 0),
                light_purple,
                30,
                5,
            )
            button(
                "main",
                mouse[0],
                mouse[1],
                0,
                650,
                200,
                50,
                (85, 239, 22),
                light_purple,
                30,
                8,
            )
            pygame.display.update()

        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10
                        snk_length += 5

                    if event.key == pygame.K_SPACE:
                        fps += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                # pygame.mixer.music.load("music/Beep.mp3")
                # crash_sound = pygame.mixer.Sound("music/Beep.mp3")
                # pygame.mixer.Sound.play(crash_sound)

                score += 10
                food_x = random.randint(5, width - 5)
                food_y = random.randint(5, height - 5)
                snk_length += 5

            game_screen.blit(water, (0, 0))
            text_screen("Score: " + str(score), red, 5, 3)

            pygame.draw.circle(game_screen, red, (food_x, food_y), 15)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("music/Crash.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                pygame.mixer.music.load("music/Crash.mp3")
                pygame.mixer.music.play()

            plot_snake(game_screen, yellow, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


def play_multi():
    pygame.mixer.music.load("music/multi_player.mp3")
    pygame.mixer.music.play()
    ravi = True
    while ravi:
        l = False
        s = False
        time = 3000
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ravi = False
                elif event.key == pygame.K_ESCAPE:
                    quit()
        pygame.display.update()
        gameLoop()


def gameLoop():
    check = 0
    global food_count
    gameExit = False
    gameOver = False
    while food_count > len(foods):
        food = randFoodGen()
        foods.add(food)
    snake1 = Snake(
        [((width / 2 - 5 * block_size) / 10) * 10, (height / 20) * 10],
        [0, 0],
        None,
        snake_head_1,
    )
    snake2 = Snake(
        [((width / 2 - 5 * block_size) / 10) * 10, (height / 20) * 10],
        [0, 0],
        None,
        snake_head_2,
        red,
    )

    while not gameExit:
        if food_count > len(foods):
            food = randFoodGen()
            foods.add(food)
        elif food_count < len(foods):
            foods.pop()

        if gameOver == True:
            check = 10
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit()

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            game_screen.blit(game_over_2, (0, 0))
            button(
                "Back", mouse[0], mouse[1], 1166, 650, 200, 50, red, light_purple, 30, 1
            )
            button(
                "Restart",
                mouse[0],
                mouse[1],
                600,
                650,
                200,
                50,
                (255, 192, 0),
                light_purple,
                30,
                6,
            )
            button(
                "main",
                mouse[0],
                mouse[1],
                0,
                650,
                200,
                50,
                (85, 239, 22),
                light_purple,
                30,
                8,
            )
            pygame.display.update()
            flag2 = 10

        for event in pygame.event.get():  # Events LEAD
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Snake1
                    snake1.key_event("left")

                if event.key == pygame.K_RIGHT:
                    snake1.key_event("right")

                if event.key == pygame.K_DOWN:
                    snake1.key_event("down")

                if event.key == pygame.K_UP:
                    snake1.key_event("up")

                if event.key == pygame.K_a:  # Snake2
                    snake2.key_event("left")

                if event.key == pygame.K_d:
                    snake2.key_event("right")

                if event.key == pygame.K_s:
                    snake2.key_event("down")

                if event.key == pygame.K_w:
                    snake2.key_event("up")

                if event.key == pygame.K_e:
                    food_count += 1
                if event.key == pygame.K_q:
                    food_count = 100

        if check == 0:
            game_screen.fill(back_color)
            # game_screen.blit(game_over_2,(0,0))

            for food in foods:
                food.draw()

            if snake1.update() or snake2.update():
                gameOver = True
                pygame.mixer.music.load("music/Crash.mp3")
                pygame.mixer.music.play()
            snake1.score_display([50, 2])
            snake1.eat()
            snake2.score_display([width - 150, 2])
            snake2.eat()

        pygame.display.update()  # Update portions of the screen for software displays

        clock.tick(FPS)
    exit()


def intro():
    pygame.mixer.music.load("music/intro.mpeg")
    pygame.mixer.music.play(-1)
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        game_screen.blit(opening_pic, (0, 0))
        pygame.display.update()
    while True:
        game_screen.blit(welcome, (0, 0))
        game_screen.blit(snake_left, (10, 450))
        game_screen.blit(snake_right, (1096, 450))
        text_screen(name, (211, 84, 0), 600, 320)
        text_screen("Press Enter To Play ", (108, 52, 131), 420, 450)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.update()


# Main Menu
def main():
    if pause_music == 0:
        pygame.mixer.music.load("music/intro.mpeg")
        pygame.mixer.music.play(-1)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    exit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        game_screen.blit(menu_pic, (0, 0))
        button(
            "Start Game",
            mouse[0],
            mouse[1],
            (width / 2 - 200),
            120,
            400,
            80,
            (85, 239, 22),
            light_purple,
            60,
            1,
        )
        button(
            "Settings",
            mouse[0],
            mouse[1],
            (width / 2 - 200),
            240,
            400,
            80,
            (255, 192, 0),
            light_purple,
            60,
            2,
        )
        button(
            "About",
            mouse[0],
            mouse[1],
            (width / 2 - 200),
            370,
            400,
            80,
            (136, 80, 9),
            light_purple,
            60,
            3,
        )
        button(
            "Exit",
            mouse[0],
            mouse[1],
            (width / 2 - 200),
            500,
            400,
            80,
            red,
            light_purple,
            60,
            4,
        )
        pygame.display.update()


def exit():
    pygame.quit()
    quit()


intro()
main()
