import sys
from random import choice
import datetime as dt
import os
import pygame

lstsup2 = [0, 0, 0, 0, 0]
lstred2 = []
lstgreen2 = []
lstblue2 = []
lst222 = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
lst12 = [1, 1, 1, 1]
lst22 = [1, 1, 1, 1]
lst32 = [1, 1, 1, 1]
lst42 = [0, 0, 0, 0]
lst52 = [0, 0, 0, 0]
CLK = 70
one_x2 = 160
one_y2 = 380
two_x2 = 160
two_y2 = 330
three_x2 = 160
three_y2 = 280
four_x2 = 160
four_y2 = 230
q = 0
five_x2 = 260
five_y2 = 380
six_x2 = 260
six_y2 = 330
seven_x2 = 260
seven_y2 = 280
eight_x2 = 260
eight_y2 = 230
nine_x = 360
nine_y = 380
ten_x = 360
ten_y = 330
eleven_x = 360
eleven_y = 280
twelve_x = 360
twelve_y = 230
pygame.init()
pygame.display.set_caption('second level')
screen = pygame.display.set_mode((800, 600))
lstsup = [0, 0, 0]
lstred = []
lstgreen = []
lst = [0, 0, 0, 0, 1, 1, 1, 1]
lst1 = [1, 1, 1, 1]
lst2 = [1, 1, 1, 1]
lst3 = [0, 0, 0, 0]
one_x = 260
one_y = 380
two_x = 260
two_y = 330
three_x = 260
three_y = 280
four_x = 260
four_y = 230
five_x = 360
five_y = 380
six_x = 360
six_y = 330
seven_x = 360
seven_y = 280
eight_x = 360
eight_y = 230
pygame.init()
pygame.display.set_caption('first level')



def load_image(name, colorkey=None, fl=False):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((50, 50))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    if fl:
        image = pygame.transform.flip(image, True, False)
    return image


def help2(screen):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    text = font.render(f"Уровни", True, (0, 0, 0))
    text_3 = pygame.font.SysFont('Comic Sans MS', 37).render(f"Результаты", True, (1, 50, 32))
    text_x = 600 // 2 - text.get_width() // 2
    text_y = 400 // 2 - text.get_height() // 2
    screen.blit(text, (text_x + 125, (text_y // 2) + 45))
    screen.blit(text_3, (text_x - 140, (text_y // 2) + 50))


def load_image2(name, colorkey=None, fl=False):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    if fl:
        image = pygame.transform.flip(image, True, False)
    return image


def help(screen, number, time):
    font = pygame.font.SysFont('Comic Sans MS', 35)

    text = font.render(f"Bы прошли уровень {number}", 1, (255, 200, 50))
    text_2 = font.render(f"Время {time}", 1, (255, 186, 0))
    text_3 = pygame.font.SysFont('Comic Sans MS', 30).render(f"Выход", 1, (1, 50, 32))
    text_x = 600 // 2 - text.get_width() // 2
    text_y = 400 // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y // 2 - 50))
    screen.blit(text_2, (text_x + 100, text_y // 2 + 40))
    screen.blit(text_3, (430, 260))


def fanction2(number, time):
    sprite_Button = pygame.sprite.Group()
    pygame.init()
    size = 750, 350
    screen = pygame.display.set_mode(size)
    running = True

    class Button(pygame.sprite.Sprite):
        image = pygame.transform.scale(load_image2("2.jpg"), (100, 50))

        def __init__(self, group, x, y):
            super().__init__(group)
            self.image = Button.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                print('exit')

    class FON(pygame.sprite.Sprite):
        image = pygame.transform.scale(load_image2("1.jpg"), (600, 400))

        def __init__(self, group, x, y):
            super().__init__(group)
            self.image = FON.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    FON(sprite_Button, 0, 0)
    a1 = Button(sprite_Button, 430, 260)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_Button.update(event)
        if not a1.flag:
            running = False
        sprite_Button.draw(screen)
        help(screen, number, time)
        pygame.display.flip()
    pygame.quit()


def help_23(screen):
    font = pygame.font.SysFont('Comic Sans MS', 45)
    text = font.render(f"Уровни", True, (1, 50, 32))
    text_2 = pygame.font.SysFont('Comic Sans MS', 40).render(f"Назад", True, (1, 50, 32))
    c = 100
    for i in range(1, 6):
        screen.blit(font.render(f"{i}", True, (1, 50, 32)), (c, 100))
        c += 100
    screen.blit(text, (230, 20))
    screen.blit(text_2, (420, 230))


def help_43(screen):
    font = pygame.font.SysFont('Comic Sans MS', 32)
    text_2 = pygame.font.SysFont('Comic Sans MS', 35).render(f"Назад", True, (0, 0, 0))
    screen.blit(text_2, (450, 250))
    c = 50
    lstone = [0, 0, 0]
    lsttwo = [0, 0, 0]
    lstthree = [0, 0, 0]
    lstfour = [0, 0, 0]
    lstfive = [0, 0, 0]
    reslst = [lstone, lsttwo, lstthree, lstfour, lstfive]
    for i in range(5):
        screen.blit(font.render(f"{i + 1}", True, (245, 245, 220)), (100, c))
        screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render(str(reslst[i][0]), True,
                                                                    (245, 245, 220)), (140, c + 2))
        screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render(str(reslst[i][1]), True,
                                                                    (245, 245, 220)), (240, c + 2))
        screen.blit(pygame.font.SysFont('Comic Sans MS', 20).render(str(reslst[i][2]), True,
                                                                    (245, 245, 220)), (315, c + 2))
        c += 50
    d = 50
    for i in range(5):
        pygame.draw.line(screen, (245, 245, 220), (90, d), (400, d), 2)
        d += 50
    pygame.draw.line(screen, (245, 245, 220), (130, 20), (130, 280), 2)
    text_41 = pygame.font.SysFont('Comic Sans MS', 15).render(f"Последниее", True, (245, 245, 220))
    screen.blit(text_41, (140, 15))
    text_42 = pygame.font.SysFont('Comic Sans MS', 15).render(f"время", True, (245, 245, 220))
    screen.blit(text_42, (140, 25))
    text_51 = pygame.font.SysFont('Comic Sans MS', 15).render(f"Лучшее", True, (245, 245, 220))
    screen.blit(text_51, (240, 15))
    text_52 = pygame.font.SysFont('Comic Sans MS', 15).render(f"время", True, (245, 245, 220))
    screen.blit(text_52, (240, 25))
    text_61 = pygame.font.SysFont('Comic Sans MS', 15).render(f"Среднее", True, (245, 245, 220))
    screen.blit(text_61, (315, 15))
    text_62 = pygame.font.SysFont('Comic Sans MS', 15).render(f"время", True, (245, 245, 220))
    screen.blit(text_62, (315, 25))


def fanction():
    sprite_Button = pygame.sprite.Group()
    sprite_Button_levels = pygame.sprite.Group()
    sprite_Button_resultats = pygame.sprite.Group()
    pygame.init()
    size = 700, 500
    screen = pygame.display.set_mode(size)
    running = True

    class Button_levels(pygame.sprite.Sprite):
        def __init__(self, group, x, y, image, name):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.name = name
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and not self.name:
                a1.flag = True
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.name == 1 and self.name:
                class Player(pygame.sprite.Sprite):
                    def __init__(self, group, x, y, color):
                        super().__init__(group)
                        self.image = pygame.Surface((54, 50))
                        self.image.fill(color)
                        self.rect = self.image.get_rect()
                        self.rect.center = (x, y)
                        self.flag = True

                    def q(self, x, y):
                        self.rect.center = (x, y)

                rect_sprite = pygame.sprite.Group()

                def load_image(name, colorkey=None):
                    image = pygame.image.load('buttle.jpg')
                    if colorkey is not None:
                        image = image.convert()
                        if colorkey == -1:
                            colorkey = image.get_at((1, 1))
                    else:
                        image = image.convert_alpha()
                    return image

                time = int(str(str(dt.datetime.now().time()).split(':')[-1]).split('.')[0]) + int(
                    str(str(dt.datetime.now().time()).split(':')[1])) * 60 + int(
                    str(str(dt.datetime.now().time()).split(':')[0])) * 360

                class buttle1(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y1
                        y1 = self.rect.y
                        self.count = 1
                        self.b11 = 0
                        self.b12 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y1, q, sup
                            if lst1[3] == 1:
                                self.b11 = 0
                                self.b12 = 0
                                if 'one' in lstred and one_x == 260:
                                    self.b11 += 1
                                if 'one' in lstgreen and one_x == 260:
                                    self.b12 += 1
                                if 'two' in lstred and two_x == 260:
                                    self.b11 += 1
                                if 'two' in lstgreen and two_x == 260:
                                    self.b12 += 1
                                if 'three' in lstred and three_x == 260:
                                    self.b11 += 1
                                if 'three' in lstgreen and three_x == 260:
                                    self.b12 += 1
                                if 'four' in lstred and four_x == 260:
                                    self.b11 += 1
                                if 'four' in lstgreen and four_x == 260:
                                    self.b12 += 1
                                if 'five' in lstred and five_x == 260:
                                    self.b11 += 1
                                if 'five' in lstgreen and five_x == 260:
                                    self.b12 += 1
                                if 'six' in lstred and six_x == 260:
                                    self.b11 += 1
                                if 'six' in lstgreen and six_x == 260:
                                    self.b12 += 1
                                if 'seven' in lstred and seven_x == 260:
                                    self.b11 += 1
                                if 'seven' in lstgreen and seven_x == 260:
                                    self.b12 += 1
                                if 'eight' in lstred and eight_x == 260:
                                    self.b11 += 1
                                if 'eight' in lstgreen and eight_x == 260:
                                    self.b12 += 1
                            if self.b11 != 4 and self.b12 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y1 -= 50
                                        if one_x == 260:
                                            one_y -= 50
                                        if two_x == 260:
                                            two_y -= 50
                                        if three_x == 260:
                                            three_y -= 50
                                        if four_x == 260:
                                            four_y -= 50
                                        if five_x == 260:
                                            five_y -= 50
                                        if six_x == 260:
                                            six_y -= 50
                                        if seven_x == 260:
                                            seven_y -= 50
                                        if eight_x == 260:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y1 += 50
                                        if one_x == 260:
                                            one_y += 50
                                        if two_x == 260:
                                            two_y += 50
                                        if three_x == 260:
                                            three_y += 50
                                        if four_x == 260:
                                            four_y += 50
                                        if five_x == 260:
                                            five_y += 50
                                        if six_x == 260:
                                            six_y += 50
                                        if seven_x == 260:
                                            seven_y += 50
                                        if eight_x == 260:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        if self.count % 2 == 0:
                                            q = 0
                                            self.rect.y += 50
                                            y1 += 50
                                            if one_x == 360:
                                                one_y += 50
                                            if two_x == 360:
                                                two_y += 50
                                            if three_x == 360:
                                                three_y += 50
                                            if four_x == 360:
                                                four_y += 50
                                            if five_x == 360:
                                                five_y += 50
                                            if six_x == 360:
                                                six_y += 50
                                            if seven_x == 360:
                                                seven_y += 50
                                            if eight_x == 360:
                                                eight_y += 50
                                            self.count += 1
                                        else:
                                            global y3, y2
                                            if lst1[3] == 0:
                                                if lst1[2] == 0:
                                                    if lst1[1] == 0:
                                                        if lst1[0] == 0:
                                                            w = 0
                                                            z = 0
                                                            if y2 == 150:
                                                                z = 360
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst1[0] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst1[0] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst1[0] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst1[0] = 1
                                                                    lst2[0] = 0
                                                            elif y3 == 150:
                                                                z = 460
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst1[0] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst1[0] = 1
                                                            if one_y == w and one_x == z:
                                                                one_x = 260
                                                                one_y = 380
                                                            elif two_y == w and two_x == z:
                                                                two_x = 260
                                                                two_y = 380
                                                            elif three_y == w and three_x == z:
                                                                three_x = 260
                                                                three_y = 380
                                                            elif four_y == w and four_x == z:
                                                                four_x = 260
                                                                four_y = 380
                                                            elif five_y == w and five_x == z:
                                                                five_x = 260
                                                                five_y = 380
                                                            elif six_y == w and six_x == z:
                                                                six_x = 260
                                                                six_y = 380
                                                            elif seven_y == w and seven_x == z:
                                                                seven_x = 260
                                                                seven_y = 380
                                                            elif eight_y == w and eight_x == z:
                                                                eight_x = 260
                                                                eight_y = 380
                                                        else:
                                                            w = 0
                                                            z = 0
                                                            q = ''
                                                            if y2 == 150:
                                                                z = 360
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                            elif y3 == 150:
                                                                z = 460
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                            q2 = 0
                                                            if one_x == 260:
                                                                q = 'one'
                                                            elif two_x == 260:
                                                                q = 'two'
                                                            elif three_x == 260:
                                                                q = 'three'
                                                            elif four_x == 260:
                                                                q = 'four'
                                                            elif five_x == 260:
                                                                q = 'five'
                                                            elif six_x == 260:
                                                                q = 'six'
                                                            elif seven_x == 260:
                                                                q = 'seven'
                                                            elif eight_x == 260:
                                                                q = 'eight'
                                                            if one_y == w and one_x == z:
                                                                if 'one' in lstred and q in lstred or \
                                                                        'one' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    one_x = 260
                                                                    one_y = 330
                                                            elif two_y == w and two_x == z:
                                                                if 'two' in lstred and q in lstred or \
                                                                        'two' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    two_x = 260
                                                                    two_y = 330
                                                            elif three_y == w and three_x == z:
                                                                if 'three' in lstred and q in lstred or \
                                                                        'three' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    three_x = 260
                                                                    three_y = 330
                                                            elif four_y == w and four_x == z:
                                                                if 'four' in lstred and q in lstred or \
                                                                        'four' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    four_x = 260
                                                                    four_y = 330
                                                            elif five_y == w and five_x == z:
                                                                if 'five' in lstred and q in lstred or \
                                                                        'five' in lstgreen and q in lstgreen:
                                                                    five_x = 260
                                                                    five_y = 330
                                                            elif six_y == w and six_x == z:
                                                                if 'six' in lstred and q in lstred or \
                                                                        'six' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    six_x = 260
                                                                    six_y = 330
                                                            elif seven_y == w and seven_x == z:
                                                                if 'seven' in lstred and q in lstred or \
                                                                        'seven' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    seven_x = 260
                                                                    seven_y = 330
                                                            elif eight_y == w and eight_x == z:
                                                                if 'eight' in lstred and q in lstred or \
                                                                        'eight' in lstgreen and q in lstgreen:
                                                                    q2 = 1
                                                                    eight_x = 260
                                                                    eight_y = 330
                                                            if q2 == 1:
                                                                if y2 == 150:
                                                                    if lst2[3] == 1:
                                                                        w = 180
                                                                        lst1[1] = 1
                                                                        lst2[3] = 0
                                                                    elif lst2[2] == 1:
                                                                        w = 230
                                                                        lst1[1] = 1
                                                                        lst2[2] = 0
                                                                    elif lst2[1] == 1:
                                                                        w = 280
                                                                        lst1[1] = 1
                                                                        lst2[1] = 0
                                                                    elif lst2[0] == 1:
                                                                        w = 330
                                                                        lst1[1] = 1
                                                                        lst2[0] = 0
                                                                elif y3 == 150:
                                                                    if lst3[3] == 1:
                                                                        w = 180
                                                                        lst3[3] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[2] == 1:
                                                                        w = 230
                                                                        lst3[2] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[1] == 1:
                                                                        w = 280
                                                                        lst3[1] = 0
                                                                        lst1[1] = 1
                                                                    elif lst3[0] == 1:
                                                                        w = 330
                                                                        lst3[0] = 0
                                                                        lst1[1] = 1
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_x == 260:
                                                            q = 'one'
                                                        elif two_x == 260:
                                                            q = 'two'
                                                        elif three_x == 260:
                                                            q = 'three'
                                                        elif four_x == 260:
                                                            q = 'four'
                                                        elif five_x == 260:
                                                            q = 'five'
                                                        elif six_x == 260:
                                                            q = 'six'
                                                        elif seven_x == 260:
                                                            q = 'seven'
                                                        elif eight_x == 260:
                                                            q = 'eight'
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 260
                                                                one_y = 280
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 260
                                                                two_y = 280
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 260
                                                                three_y = 280
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 260
                                                                four_y = 280
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 260
                                                                five_y = 280
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 260
                                                                six_y = 280
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 260
                                                                seven_y = 280
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 260
                                                                eight_y = 280
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst1[2] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst1[2] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst1[2] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst1[2] = 1
                                                                    lst2[0] = 0
                                                            elif y3 == 150:
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst1[2] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst1[2] = 1
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x == 260:
                                                        q = 'one'
                                                    elif two_x == 260:
                                                        q = 'two'
                                                    elif three_x == 260:
                                                        q = 'three'
                                                    elif four_x == 260:
                                                        q = 'four'
                                                    elif five_x == 260:
                                                        q = 'five'
                                                    elif six_x == 260:
                                                        q = 'six'
                                                    elif seven_x == 260:
                                                        q = 'seven'
                                                    elif eight_x == 260:
                                                        q = 'eight'
                                                    if y2 == 150:
                                                        z = 360
                                                        if lst2[3] == 1:
                                                            w = 180
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 460
                                                        if lst3[3] == 1:
                                                            w = 180
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 260
                                                            one_y = 230
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 260
                                                            two_y = 230
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 260
                                                            three_y = 230
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 260
                                                            four_y = 230
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 260
                                                            five_y = 230
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 260
                                                            six_y = 230
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 260
                                                            seven_y = 230
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 260
                                                            eight_y = 230
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst1[3] = 1
                                                                lst2[3] = 0
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst1[3] = 1
                                                                lst2[2] = 0
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst1[3] = 1
                                                                lst2[1] = 0
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst1[3] = 1
                                                                lst2[0] = 0
                                                        elif y3 == 150:
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst1[3] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst1[3] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst1[3] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst1[3] = 1
                            else:
                                lstsup[0] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction2(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction2(1, f'{result // 60}:{q}')

                class buttle2(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle2.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y2
                        y2 = self.rect.y
                        self.count = 1
                        self.b21 = 0
                        self.b22 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y2, q, sup
                            if lst2[3] == 1:
                                self.b21 = 0
                                self.b22 = 0
                                if 'one' in lstred and one_x == 360:
                                    self.b21 += 1
                                if 'one' in lstgreen and one_x == 360:
                                    self.b22 += 1
                                if 'two' in lstred and two_x == 360:
                                    self.b21 += 1
                                if 'two' in lstgreen and two_x == 360:
                                    self.b22 += 1
                                if 'three' in lstred and three_x == 360:
                                    self.b21 += 1
                                if 'three' in lstgreen and three_x == 360:
                                    self.b22 += 1
                                if 'four' in lstred and four_x == 360:
                                    self.b21 += 1
                                if 'four' in lstgreen and four_x == 360:
                                    self.b22 += 1
                                if 'five' in lstred and five_x == 360:
                                    self.b21 += 1
                                if 'five' in lstgreen and five_x == 360:
                                    self.b22 += 1
                                if 'six' in lstred and six_x == 360:
                                    self.b21 += 1
                                if 'six' in lstgreen and six_x == 360:
                                    self.b22 += 1
                                if 'seven' in lstred and seven_x == 360:
                                    self.b21 += 1
                                if 'seven' in lstgreen and seven_x == 360:
                                    self.b22 += 1
                                if 'eight' in lstred and eight_x == 360:
                                    self.b21 += 1
                                if 'eight' in lstgreen and eight_x == 360:
                                    self.b22 += 1
                            if self.b21 != 4 and self.b22 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y2 -= 50
                                        if one_x == 360:
                                            one_y -= 50
                                        if two_x == 360:
                                            two_y -= 50
                                        if three_x == 360:
                                            three_y -= 50
                                        if four_x == 360:
                                            four_y -= 50
                                        if five_x == 360:
                                            five_y -= 50
                                        if six_x == 360:
                                            six_y -= 50
                                        if seven_x == 360:
                                            seven_y -= 50
                                        if eight_x == 360:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y2 += 50
                                        if one_x == 360:
                                            one_y += 50
                                        if two_x == 360:
                                            two_y += 50
                                        if three_x == 360:
                                            three_y += 50
                                        if four_x == 360:
                                            four_y += 50
                                        if five_x == 360:
                                            five_y += 50
                                        if six_x == 360:
                                            six_y += 50
                                        if seven_x == 360:
                                            seven_y += 50
                                        if eight_x == 360:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        global y3, y1
                                        if lst2[3] == 0:
                                            if lst2[2] == 0:
                                                if lst2[1] == 0:
                                                    if lst2[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst2[0] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst2[0] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst2[0] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst2[0] = 1
                                                                lst1[0] = 0
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst2[0] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst2[0] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst2[0] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst2[0] = 1
                                                        if one_y == w and one_x == z:
                                                            one_x = 360
                                                            one_y = 380
                                                        elif two_y == w and two_x == z:
                                                            two_x = 360
                                                            two_y = 380
                                                        elif three_y == w and three_x == z:
                                                            three_x = 360
                                                            three_y = 380
                                                        elif four_y == w and four_x == z:
                                                            four_x = 360
                                                            four_y = 380
                                                        elif five_y == w and five_x == z:
                                                            five_x = 360
                                                            five_y = 380
                                                        elif six_y == w and six_x == z:
                                                            six_x = 360
                                                            six_y = 380
                                                        elif seven_y == w and seven_x == z:
                                                            seven_x = 360
                                                            seven_y = 380
                                                        elif eight_y == w and eight_x == z:
                                                            eight_x = 360
                                                            eight_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 460
                                                            if lst3[3] == 1:
                                                                w = 180
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_x == 360:
                                                            q = 'one'
                                                        elif two_x == 360:
                                                            q = 'two'
                                                        elif three_x == 360:
                                                            q = 'three'
                                                        elif four_x == 360:
                                                            q = 'four'
                                                        elif five_x == 360:
                                                            q = 'five'
                                                        elif six_x == 360:
                                                            q = 'six'
                                                        elif seven_x == 360:
                                                            q = 'seven'
                                                        elif eight_x == 360:
                                                            q = 'eight'
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 360
                                                                one_y = 330
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 360
                                                                two_y = 330
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 360
                                                                three_y = 330
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 360
                                                                four_y = 330
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 360
                                                                five_y = 330
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 360
                                                                six_y = 330
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 360
                                                                seven_y = 330
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 360
                                                                eight_y = 330
                                                        if q2 == 1:
                                                            if y1 == 150:
                                                                if lst1[3] == 1:
                                                                    w = 180
                                                                    lst2[1] = 1
                                                                    lst1[3] = 0
                                                                elif lst1[2] == 1:
                                                                    w = 230
                                                                    lst2[1] = 1
                                                                    lst1[2] = 0
                                                                elif lst1[1] == 1:
                                                                    w = 280
                                                                    lst2[1] = 1
                                                                    lst1[1] = 0
                                                                elif lst1[0] == 1:
                                                                    w = 330
                                                                    lst2[1] = 1
                                                                    lst1[0] = 0
                                                            elif y3 == 150:
                                                                if lst3[3] == 1:
                                                                    w = 180
                                                                    lst3[3] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[2] == 1:
                                                                    w = 230
                                                                    lst3[2] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 0
                                                                    lst2[1] = 1
                                                                elif lst3[0] == 1:
                                                                    w = 330
                                                                    lst3[0] = 0
                                                                    lst2[1] = 1
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if y1 == 150:
                                                        z = 260
                                                        if lst1[3] == 1:
                                                            w = 180
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 460
                                                        if lst3[3] == 1:
                                                            w = 180
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_x == 360:
                                                        q = 'one'
                                                    elif two_x == 360:
                                                        q = 'two'
                                                    elif three_x == 360:
                                                        q = 'three'
                                                    elif four_x == 360:
                                                        q = 'four'
                                                    elif five_x == 360:
                                                        q = 'five'
                                                    elif six_x == 360:
                                                        q = 'six'
                                                    elif seven_x == 360:
                                                        q = 'seven'
                                                    elif eight_x == 360:
                                                        q = 'eight'
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 360
                                                            one_y = 280
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 360
                                                            two_y = 280
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 360
                                                            three_y = 280
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 360
                                                            four_y = 280
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 360
                                                            five_y = 280
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 360
                                                            six_y = 280
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 360
                                                            seven_y = 280
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 360
                                                            eight_y = 280
                                                    if q2 == 1:
                                                        if y1 == 150:
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst2[2] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst2[2] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst2[2] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst2[2] = 1
                                                                lst1[0] = 0
                                                        elif y3 == 150:
                                                            if lst3[3] == 1:
                                                                w = 180
                                                                lst3[3] = 0
                                                                lst2[2] = 1
                                                            elif lst3[2] == 1:
                                                                w = 230
                                                                lst3[2] = 0
                                                                lst2[2] = 1
                                                            elif lst3[1] == 1:
                                                                w = 280
                                                                lst3[1] = 0
                                                                lst2[2] = 1
                                                            elif lst3[0] == 1:
                                                                w = 330
                                                                lst3[0] = 0
                                                                lst2[2] = 1
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if y1 == 150:
                                                    z = 260
                                                    if lst1[3] == 1:
                                                        w = 180
                                                    elif lst1[2] == 1:
                                                        w = 230
                                                    elif lst1[1] == 1:
                                                        w = 280
                                                    elif lst1[0] == 1:
                                                        w = 330
                                                elif y3 == 150:
                                                    z = 460
                                                    if lst3[3] == 1:
                                                        w = 180
                                                    elif lst3[2] == 1:
                                                        w = 230
                                                    elif lst3[1] == 1:
                                                        w = 280
                                                    elif lst3[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_x == 360:
                                                    q = 'one'
                                                elif two_x == 360:
                                                    q = 'two'
                                                elif three_x == 360:
                                                    q = 'three'
                                                elif four_x == 360:
                                                    q = 'four'
                                                elif five_x == 360:
                                                    q = 'five'
                                                elif six_x == 360:
                                                    q = 'six'
                                                elif seven_x == 360:
                                                    q = 'seven'
                                                elif eight_x == 360:
                                                    q = 'eight'
                                                if one_y == w and one_x == z:
                                                    if 'one' in lstred and q in lstred or \
                                                            'one' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        one_x = 360
                                                        one_y = 230
                                                elif two_y == w and two_x == z:
                                                    if 'two' in lstred and q in lstred or \
                                                            'two' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        two_x = 360
                                                        two_y = 230
                                                elif three_y == w and three_x == z:
                                                    if 'three' in lstred and q in lstred or \
                                                            'three' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        three_x = 360
                                                        three_y = 230
                                                elif four_y == w and four_x == z:
                                                    if 'four' in lstred and q in lstred or \
                                                            'four' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        four_x = 360
                                                        four_y = 230
                                                elif five_y == w and five_x == z:
                                                    if 'five' in lstred and q in lstred or \
                                                            'five' in lstgreen and q in lstgreen:
                                                        five_x = 360
                                                        five_y = 230
                                                elif six_y == w and six_x == z:
                                                    if 'six' in lstred and q in lstred or \
                                                            'six' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        six_x = 360
                                                        six_y = 230
                                                elif seven_y == w and seven_x == z:
                                                    if 'seven' in lstred and q in lstred or \
                                                            'seven' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        seven_x = 360
                                                        seven_y = 230
                                                elif eight_y == w and eight_x == z:
                                                    if 'eight' in lstred and q in lstred or \
                                                            'eight' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        eight_x = 360
                                                        eight_y = 230
                                                if q2 == 1:
                                                    if y1 == 150:
                                                        if lst1[3] == 1:
                                                            w = 180
                                                            lst2[3] = 1
                                                            lst1[3] = 0
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                            lst2[3] = 1
                                                            lst1[2] = 0
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                            lst2[3] = 1
                                                            lst1[1] = 0
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                            lst2[3] = 1
                                                            lst1[0] = 0
                                                    elif y3 == 150:
                                                        if lst3[3] == 1:
                                                            w = 180
                                                            lst3[3] = 0
                                                            lst2[3] = 1
                                                        elif lst3[2] == 1:
                                                            w = 230
                                                            lst3[2] = 0
                                                            lst2[3] = 1
                                                        elif lst3[1] == 1:
                                                            w = 280
                                                            lst3[1] = 0
                                                            lst2[3] = 1
                                                        elif lst3[0] == 1:
                                                            w = 330
                                                            lst3[0] = 0
                                                            lst2[3] = 1
                            else:
                                lstsup[1] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction2(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction2(1, f'{result // 60}:{q}')

                class buttle3(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle3.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y3
                        y3 = self.rect.y
                        self.count = 1
                        self.b31 = 0
                        self.b32 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global five_y, five_x, six_y, six_x, seven_y, seven_x, eight_x, eight_y, \
                                one_y, one_x, two_y, two_x, three_y, three_x, four_x, four_y, y3, q, sup
                            if lst3[3] == 1:
                                self.b31 = 0
                                self.b32 = 0
                                if 'one' in lstred and one_x == 460:
                                    self.b31 += 1
                                if 'one' in lstgreen and one_x == 460:
                                    self.b32 += 1
                                if 'two' in lstred and two_x == 460:
                                    self.b31 += 1
                                if 'two' in lstgreen and two_x == 460:
                                    self.b32 += 1
                                if 'three' in lstred and three_x == 460:
                                    self.b31 += 1
                                if 'three' in lstgreen and three_x == 460:
                                    self.b32 += 1
                                if 'four' in lstred and four_x == 460:
                                    self.b31 += 1
                                if 'four' in lstgreen and four_x == 460:
                                    self.b32 += 1
                                if 'five' in lstred and five_x == 460:
                                    self.b31 += 1
                                if 'five' in lstgreen and five_x == 460:
                                    self.b32 += 1
                                if 'six' in lstred and six_x == 460:
                                    self.b31 += 1
                                if 'six' in lstgreen and six_x == 460:
                                    self.b32 += 1
                                if 'seven' in lstred and seven_x == 460:
                                    self.b31 += 1
                                if 'seven' in lstgreen and seven_x == 460:
                                    self.b32 += 1
                                if 'eight' in lstred and eight_x == 460:
                                    self.b31 += 1
                                if 'eight' in lstgreen and eight_x == 460:
                                    self.b32 += 1
                            if self.b31 != 4 and self.b32 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y3 -= 50
                                        if one_x == 460:
                                            one_y -= 50
                                        if two_x == 460:
                                            two_y -= 50
                                        if three_x == 460:
                                            three_y -= 50
                                        if four_x == 460:
                                            four_y -= 50
                                        if five_x == 460:
                                            five_y -= 50
                                        if six_x == 460:
                                            six_y -= 50
                                        if seven_x == 460:
                                            seven_y -= 50
                                        if eight_x == 460:
                                            eight_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y3 += 50
                                        if one_x == 460:
                                            one_y += 50
                                        if two_x == 460:
                                            two_y += 50
                                        if three_x == 460:
                                            three_y += 50
                                        if four_x == 460:
                                            four_y += 50
                                        if five_x == 460:
                                            five_y += 50
                                        if six_x == 460:
                                            six_y += 50
                                        if seven_x == 460:
                                            seven_y += 50
                                        if eight_x == 460:
                                            eight_y += 50
                                        self.count += 1
                                    else:
                                        global y2, y1
                                        if lst3[3] == 0:
                                            if lst3[2] == 0:
                                                if lst3[1] == 0:
                                                    if lst3[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst3[0] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst3[0] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst3[0] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst3[0] = 1
                                                                lst1[0] = 0
                                                        elif y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst2[3] = 0
                                                                lst3[0] = 1
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst2[2] = 0
                                                                lst3[0] = 1
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst2[1] = 0
                                                                lst3[0] = 1
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst2[0] = 0
                                                                lst3[0] = 1
                                                        if one_y == w and one_x == z:
                                                            one_x = 460
                                                            one_y = 380
                                                        elif two_y == w and two_x == z:
                                                            two_x = 460
                                                            two_y = 380
                                                        elif three_y == w and three_x == z:
                                                            three_x = 460
                                                            three_y = 380
                                                        elif four_y == w and four_x == z:
                                                            four_x = 460
                                                            four_y = 380
                                                        elif five_y == w and five_x == z:
                                                            five_x = 460
                                                            five_y = 380
                                                        elif six_y == w and six_x == z:
                                                            six_x = 460
                                                            six_y = 380
                                                        elif seven_y == w and seven_x == z:
                                                            seven_x = 460
                                                            seven_y = 380
                                                        elif eight_y == w and eight_x == z:
                                                            eight_x = 460
                                                            eight_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x == 460:
                                                            q = 'one'
                                                        elif two_x == 460:
                                                            q = 'two'
                                                        elif three_x == 460:
                                                            q = 'three'
                                                        elif four_x == 460:
                                                            q = 'four'
                                                        elif five_x == 460:
                                                            q = 'five'
                                                        elif six_x == 460:
                                                            q = 'six'
                                                        elif seven_x == 460:
                                                            q = 'seven'
                                                        elif eight_x == 460:
                                                            q = 'eight'
                                                        if y2 == 150:
                                                            z = 360
                                                            if lst2[3] == 1:
                                                                w = 180
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                        elif y1 == 150:
                                                            z = 260
                                                            if lst1[3] == 1:
                                                                w = 180
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_y == w and one_x == z:
                                                            if 'one' in lstred and q in lstred or \
                                                                    'one' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                one_x = 460
                                                                one_y = 330
                                                        elif two_y == w and two_x == z:
                                                            if 'two' in lstred and q in lstred or \
                                                                    'two' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                two_x = 460
                                                                two_y = 330
                                                        elif three_y == w and three_x == z:
                                                            if 'three' in lstred and q in lstred or \
                                                                    'three' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                three_x = 460
                                                                three_y = 330
                                                        elif four_y == w and four_x == z:
                                                            if 'four' in lstred and q in lstred or \
                                                                    'four' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                four_x = 460
                                                                four_y = 330
                                                        elif five_y == w and five_x == z:
                                                            if 'five' in lstred and q in lstred or \
                                                                    'five' in lstgreen and q in lstgreen:
                                                                five_x = 460
                                                                five_y = 330
                                                        elif six_y == w and six_x == z:
                                                            if 'six' in lstred and q in lstred or \
                                                                    'six' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                six_x = 460
                                                                six_y = 330
                                                        elif seven_y == w and seven_x == z:
                                                            if 'seven' in lstred and q in lstred or \
                                                                    'seven' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                seven_x = 460
                                                                seven_y = 330
                                                        elif eight_y == w and eight_x == z:
                                                            if 'eight' in lstred and q in lstred or \
                                                                    'eight' in lstgreen and q in lstgreen:
                                                                q2 = 1
                                                                eight_x = 460
                                                                eight_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst2[3] == 1:
                                                                    w = 180
                                                                    lst3[1] = 1
                                                                    lst2[3] = 0
                                                                elif lst2[2] == 1:
                                                                    w = 230
                                                                    lst3[1] = 1
                                                                    lst2[2] = 0
                                                                elif lst2[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 1
                                                                    lst2[1] = 0
                                                                elif lst2[0] == 1:
                                                                    w = 330
                                                                    lst3[1] = 1
                                                                    lst2[0] = 0
                                                            elif y1 == 150:
                                                                if lst1[3] == 1:
                                                                    w = 180
                                                                    lst3[1] = 1
                                                                    lst1[3] = 0
                                                                elif lst1[2] == 1:
                                                                    w = 230
                                                                    lst3[1] = 1
                                                                    lst1[2] = 0
                                                                elif lst1[1] == 1:
                                                                    w = 280
                                                                    lst3[1] = 1
                                                                    lst1[1] = 0
                                                                elif lst1[0] == 1:
                                                                    w = 330
                                                                    lst3[1] = 1
                                                                    lst1[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x == 460:
                                                        q = 'one'
                                                    elif two_x == 460:
                                                        q = 'two'
                                                    elif three_x == 460:
                                                        q = 'three'
                                                    elif four_x == 460:
                                                        q = 'four'
                                                    elif five_x == 460:
                                                        q = 'five'
                                                    elif six_x == 460:
                                                        q = 'six'
                                                    elif seven_x == 460:
                                                        q = 'seven'
                                                    elif eight_x == 460:
                                                        q = 'eight'
                                                    if y2 == 150:
                                                        z = 360
                                                        if lst2[3] == 1:
                                                            w = 180
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                    elif y1 == 150:
                                                        z = 260
                                                        if lst1[3] == 1:
                                                            w = 180
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y == w and one_x == z:
                                                        if 'one' in lstred and q in lstred or \
                                                                'one' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            one_x = 460
                                                            one_y = 280
                                                    elif two_y == w and two_x == z:
                                                        if 'two' in lstred and q in lstred or \
                                                                'two' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            two_x = 460
                                                            two_y = 280
                                                    elif three_y == w and three_x == z:
                                                        if 'three' in lstred and q in lstred or \
                                                                'three' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            three_x = 460
                                                            three_y = 280
                                                    elif four_y == w and four_x == z:
                                                        if 'four' in lstred and q in lstred or \
                                                                'four' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            four_x = 460
                                                            four_y = 280
                                                    elif five_y == w and five_x == z:
                                                        if 'five' in lstred and q in lstred or \
                                                                'five' in lstgreen and q in lstgreen:
                                                            five_x = 460
                                                            five_y = 280
                                                    elif six_y == w and six_x == z:
                                                        if 'six' in lstred and q in lstred or \
                                                                'six' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            six_x = 460
                                                            six_y = 280
                                                    elif seven_y == w and seven_x == z:
                                                        if 'seven' in lstred and q in lstred or \
                                                                'seven' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            seven_x = 260
                                                            seven_y = 280
                                                    elif eight_y == w and eight_x == z:
                                                        if 'eight' in lstred and q in lstred or \
                                                                'eight' in lstgreen and q in lstgreen:
                                                            q2 = 1
                                                            eight_x = 460
                                                            eight_y = 280
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst2[3] == 1:
                                                                w = 180
                                                                lst3[2] = 1
                                                                lst2[3] = 0
                                                            elif lst2[2] == 1:
                                                                w = 230
                                                                lst3[2] = 1
                                                                lst2[2] = 0
                                                            elif lst2[1] == 1:
                                                                w = 280
                                                                lst3[2] = 1
                                                                lst2[1] = 0
                                                            elif lst2[0] == 1:
                                                                w = 330
                                                                lst3[2] = 1
                                                                lst2[0] = 0
                                                        elif y1 == 150:
                                                            if lst1[3] == 1:
                                                                w = 180
                                                                lst3[2] = 1
                                                                lst1[3] = 0
                                                            elif lst1[2] == 1:
                                                                w = 230
                                                                lst3[2] = 1
                                                                lst1[2] = 0
                                                            elif lst1[1] == 1:
                                                                w = 280
                                                                lst3[2] = 1
                                                                lst1[1] = 0
                                                            elif lst1[0] == 1:
                                                                w = 330
                                                                lst3[2] = 1
                                                                lst1[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x == 460:
                                                    q = 'one'
                                                elif two_x == 460:
                                                    q = 'two'
                                                elif three_x == 460:
                                                    q = 'three'
                                                elif four_x == 460:
                                                    q = 'four'
                                                elif five_x == 460:
                                                    q = 'five'
                                                elif six_x == 460:
                                                    q = 'six'
                                                elif seven_x == 460:
                                                    q = 'seven'
                                                elif eight_x == 460:
                                                    q = 'eight'
                                                if y2 == 150:
                                                    z = 360
                                                    if lst2[3] == 1:
                                                        w = 180
                                                    elif lst2[2] == 1:
                                                        w = 230
                                                    elif lst2[1] == 1:
                                                        w = 280
                                                    elif lst2[0] == 1:
                                                        w = 330
                                                elif y1 == 150:
                                                    z = 260
                                                    if lst1[3] == 1:
                                                        w = 180
                                                    elif lst1[2] == 1:
                                                        w = 230
                                                    elif lst1[1] == 1:
                                                        w = 280
                                                    elif lst1[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_y == w and one_x == z:
                                                    if 'one' in lstred and q in lstred or \
                                                            'one' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        one_x = 460
                                                        one_y = 230
                                                elif two_y == w and two_x == z:
                                                    if 'two' in lstred and q in lstred or \
                                                            'two' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        two_x = 460
                                                        two_y = 230
                                                elif three_y == w and three_x == z:
                                                    if 'three' in lstred and q in lstred or \
                                                            'three' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        three_x = 460
                                                        three_y = 230
                                                elif four_y == w and four_x == z:
                                                    if 'four' in lstred and q in lstred or \
                                                            'four' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        four_x = 460
                                                        four_y = 230
                                                elif five_y == w and five_x == z:
                                                    if 'five' in lstred and q in lstred or \
                                                            'five' in lstgreen and q in lstgreen:
                                                        five_x = 460
                                                        five_y = 230
                                                elif six_y == w and six_x == z:
                                                    if 'six' in lstred and q in lstred or \
                                                            'six' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        six_x = 460
                                                        six_y = 230
                                                elif seven_y == w and seven_x == z:
                                                    if 'seven' in lstred and q in lstred or \
                                                            'seven' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        seven_x = 460
                                                        seven_y = 230
                                                elif eight_y == w and eight_x == z:
                                                    if 'eight' in lstred and q in lstred or \
                                                            'eight' in lstgreen and q in lstgreen:
                                                        q2 = 1
                                                        eight_x = 460
                                                        eight_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst2[3] == 1:
                                                            w = 180
                                                            lst3[3] = 1
                                                            lst2[3] = 0
                                                        elif lst2[2] == 1:
                                                            w = 230
                                                            lst3[3] = 1
                                                            lst2[2] = 0
                                                        elif lst2[1] == 1:
                                                            w = 280
                                                            lst3[3] = 1
                                                            lst2[1] = 0
                                                        elif lst2[0] == 1:
                                                            w = 330
                                                            lst3[3] = 1
                                                            lst2[0] = 0
                                                    elif y1 == 150:
                                                        if lst1[3] == 1:
                                                            w = 180
                                                            lst3[3] = 1
                                                            lst1[3] = 0
                                                        elif lst1[2] == 1:
                                                            w = 230
                                                            lst3[3] = 1
                                                            lst1[2] = 0
                                                        elif lst1[1] == 1:
                                                            w = 280
                                                            lst3[3] = 1
                                                            lst1[1] = 0
                                                        elif lst1[0] == 1:
                                                            w = 330
                                                            lst3[3] = 1
                                                            lst1[0] = 0
                            else:
                                lstsup[2] = 1
                                sup = 0
                                for i in lstsup:
                                    if i == 1:
                                        sup += 1
                                if sup == 2:
                                    time2 = int(
                                        str(str(dt.datetime.now().time()).split(':')[-1]).split(
                                            '.')[0]) + int(
                                        str(str(dt.datetime.now().time()).split(':')[
                                                1])) * 60 + int(
                                        str(str(dt.datetime.now().time()).split(':')[0])) * 360
                                    result = time2 - time
                                    q = result % 60
                                    if q < 10:
                                        fanction2(1, f'{result // 60}:0{q}')
                                    else:
                                        fanction2(1, f'{result // 60}:{q}')

                running = True
                fps = 60
                all_sprites = pygame.sprite.Group()
                buttle1(all_sprites, 250, 200)
                buttle2(all_sprites, 350, 200)
                buttle3(all_sprites, 450, 200)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('one')
                else:
                    color = 'green'
                    lstgreen.append('one')
                lst.remove(num)
                one = Player(rect_sprite, one_x + 30, one_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('two')
                else:
                    color = 'green'
                    lstgreen.append('two')
                lst.remove(num)
                two = Player(rect_sprite, two_x + 30, two_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('three')
                else:
                    color = 'green'
                    lstgreen.append('three')
                lst.remove(num)
                three = Player(rect_sprite, three_x + 30, three_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('four')
                else:
                    color = 'green'
                    lstgreen.append('four')
                lst.remove(num)
                four = Player(rect_sprite, four_x + 30, four_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('five')
                else:
                    color = 'green'
                    lstgreen.append('five')
                lst.remove(num)
                five = Player(rect_sprite, five_x + 30, five_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('six')
                else:
                    color = 'green'
                    lstgreen.append('six')
                lst.remove(num)
                six = Player(rect_sprite, six_x + 30, six_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('seven')
                else:
                    color = 'green'
                    lstgreen.append('seven')
                lst.remove(num)
                seven = Player(rect_sprite, seven_x + 30, seven_y + 25, color)
                num = choice(lst)
                if num == 0:
                    color = 'red'
                    lstred.append('eight')
                else:
                    color = 'green'
                    lstgreen.append('eight')
                lst.remove(num)
                eight = Player(rect_sprite, eight_x + 30, eight_y + 25, color)

                def draw():
                    screen.fill("black")
                    all_sprites.update()
                    all_sprites.draw(screen)
                    pygame.display.flip()

                def run():
                    while True:
                        one.q(one_x + 29, one_y + 25)
                        two.q(two_x + 29, two_y + 25)
                        three.q(three_x + 29, three_y + 25)
                        four.q(four_x + 29, four_y + 25)
                        five.q(five_x + 29, five_y + 25)
                        six.q(six_x + 29, six_y + 25)
                        seven.q(seven_x + 29, seven_y + 25)
                        eight.q(eight_x + 29, eight_y + 25)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print(lst1)
                                print(lst2)
                                print(lst3)
                                print()
                                all_sprites.update(event)
                        screen.fill((0, 0, 0))
                        all_sprites.draw(screen)
                        rect_sprite.draw(screen)
                        pygame.display.flip()

                if __name__ == "__main__":
                    run()
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.name == 2 and self.name:
                class Player(pygame.sprite.Sprite):
                    def __init__(self, group, x, y, color):
                        super().__init__(group)
                        self.image = pygame.Surface((54, 50))
                        self.image.fill(color)
                        self.rect = self.image.get_rect()
                        self.rect.center = (x, y)
                        self.flag = True

                    def q(self, x, y):
                        self.rect.center = (x, y)

                def load_image(name, colorkey=None):
                    image = pygame.image.load('buttle.jpg')
                    if colorkey is not None:
                        image = image.convert()
                        if colorkey == -1:
                            colorkey = image.get_at((1, 1))
                    else:
                        image = image.convert_alpha()
                    return image

                time = int(str(str(dt.datetime.now().time()).split(':')[-1]).split('.')[0]) + int(
                    str(str(dt.datetime.now().time()).split(':')[1])) * 60 + int(
                    str(str(dt.datetime.now().time()).split(':')[0])) * 360

                class buttle1(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y1
                        y1 = self.rect.y
                        self.count = 1
                        self.b11 = 0
                        self.b12 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                                five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                                one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2, y1, q
                            self.b11 = 0
                            self.b12 = 0
                            if lst12[3] == 1:
                                if 'one' in lstred2 and one_x2 == 160:
                                    self.b11 += 1
                                if 'one' in lstgreen2 and one_x2 == 160:
                                    self.b12 += 1
                                if 'two' in lstred2 and two_x2 == 160:
                                    self.b11 += 1
                                if 'two' in lstgreen2 and two_x2 == 160:
                                    self.b12 += 1
                                if 'three' in lstred2 and three_x2 == 160:
                                    self.b11 += 1
                                if 'three' in lstgreen2 and three_x2 == 160:
                                    self.b12 += 1
                                if 'four' in lstred2 and four_x2 == 160:
                                    self.b11 += 1
                                if 'four' in lstgreen2 and four_x2 == 160:
                                    self.b12 += 1
                                if 'five' in lstred2 and five_x2 == 160:
                                    self.b11 += 1
                                if 'five' in lstgreen2 and five_x2 == 160:
                                    self.b12 += 1
                                if 'six' in lstred2 and six_x2 == 160:
                                    self.b11 += 1
                                if 'six' in lstgreen2 and six_x2 == 160:
                                    self.b12 += 1
                                if 'seven' in lstred2 and seven_x2 == 160:
                                    self.b11 += 1
                                if 'seven' in lstgreen2 and seven_x2 == 160:
                                    self.b12 += 1
                                if 'eight' in lstred2 and eight_x2 == 160:
                                    self.b11 += 1
                                if 'eight' in lstgreen2 and eight_x2 == 160:
                                    self.b12 += 1
                                if 'nine' in lstred2 and nine_x == 160:
                                    self.b11 += 1
                                if 'nine' in lstgreen2 and nine_x == 160:
                                    self.b12 += 1
                                if 'ten' in lstred2 and ten_x == 160:
                                    self.b11 += 1
                                if 'ten' in lstgreen2 and ten_x == 160:
                                    self.b12 += 1
                                if 'eleven' in lstred2 and eleven_x == 160:
                                    self.b11 += 1
                                if 'eleven' in lstgreen2 and eleven_x == 160:
                                    self.b12 += 1
                                if 'twelve' in lstred2 and twelve_x == 160:
                                    self.b11 += 1
                                if 'twelve' in lstgreen2 and twelve_x == 160:
                                    self.b12 += 1
                            if self.b11 != 4 and self.b12 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y1 -= 50
                                        if one_x2 == 160:
                                            one_y2 -= 50
                                        if two_x2 == 160:
                                            two_y2 -= 50
                                        if three_x2 == 160:
                                            three_y2 -= 50
                                        if four_x2 == 160:
                                            four_y2 -= 50
                                        if five_x2 == 160:
                                            five_y2 -= 50
                                        if six_x2 == 160:
                                            six_y2 -= 50
                                        if seven_x2 == 160:
                                            seven_y2 -= 50
                                        if eight_x2 == 160:
                                            eight_y2 -= 50
                                        if nine_x == 160:
                                            nine_y -= 50
                                        if ten_x == 160:
                                            ten_y -= 50
                                        if eleven_x == 160:
                                            eleven_y -= 50
                                        if twelve_x == 160:
                                            twelve_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y1 += 50
                                        if one_x2 == 160:
                                            one_y2 += 50
                                        if two_x2 == 160:
                                            two_y2 += 50
                                        if three_x2 == 160:
                                            three_y2 += 50
                                        if four_x2 == 160:
                                            four_y2 += 50
                                        if five_x2 == 160:
                                            five_y2 += 50
                                        if six_x2 == 160:
                                            six_y2 += 50
                                        if seven_x2 == 160:
                                            seven_y2 += 50
                                        if eight_x2 == 160:
                                            eight_y2 += 50
                                        if nine_x == 160:
                                            nine_y += 50
                                        if ten_x == 160:
                                            ten_y += 50
                                        if eleven_x == 160:
                                            eleven_y += 50
                                        if twelve_x == 160:
                                            twelve_y += 50
                                        self.count += 1
                                    else:
                                        global y5, y4, y3, y2
                                        if lst12[3] == 0:
                                            if lst12[2] == 0:
                                                if lst12[1] == 0:
                                                    if lst12[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst12[0] = 1
                                                                lst22[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst12[0] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst12[0] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst12[0] = 1
                                                                lst22[0] = 0
                                                        if y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst12[0] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst12[0] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst12[0] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst12[0] = 1
                                                                lst32[0] = 0
                                                        if y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst12[0] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst12[0] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst12[0] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst12[0] = 1
                                                                lst42[0] = 0
                                                        if y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst12[0] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst12[0] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst12[0] = 1
                                                                lst52[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst12[0] = 1
                                                                lst52[0] = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            one_x2 = 160
                                                            one_y2 = 380
                                                        elif two_y2 == w and two_x2 == z:
                                                            two_x2 = 160
                                                            two_y2 = 380
                                                        elif three_y2 == w and three_x2 == z:
                                                            three_x2 = 160
                                                            three_y2 = 380
                                                        elif four_y2 == w and four_x2 == z:
                                                            four_x2 = 160
                                                            four_y2 = 380
                                                        elif five_y2 == w and five_x2 == z:
                                                            five_x2 = 160
                                                            five_y2 = 380
                                                        elif six_y2 == w and six_x2 == z:
                                                            six_x = 160
                                                            six_y = 380
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            seven_x2 = 160
                                                            seven_y2 = 380
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            eight_x2 = 160
                                                            eight_y2 = 380
                                                        elif nine_y == w and nine_x == z:
                                                            nine_x = 160
                                                            nine_y = 380
                                                        elif ten_y == w and ten_x == z:
                                                            ten_x = 160
                                                            ten_y = 380
                                                        elif eleven_y == w and eleven_x == z:
                                                            eleven_x = 160
                                                            eleven_y = 380
                                                        elif twelve_y == w and twelve_x == z:
                                                            twelve_x = 160
                                                            twelve_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x2 == 160:
                                                            q = 'one'
                                                        elif two_x2 == 160:
                                                            q = 'two'
                                                        elif three_x2 == 160:
                                                            q = 'three'
                                                        elif four_x2 == 160:
                                                            q = 'four'
                                                        elif five_x2 == 160:
                                                            q = 'five'
                                                        elif six_x2 == 160:
                                                            q = 'six'
                                                        elif seven_x2 == 160:
                                                            q = 'seven'
                                                        elif eight_x2 == 160:
                                                            q = 'eight'
                                                        elif nine_x == 160:
                                                            q = 'nine'
                                                        elif ten_x == 160:
                                                            q = 'ten'
                                                        elif eleven_x == 160:
                                                            q = 'eleven'
                                                        elif twelve_x == 160:
                                                            q = 'twelve'
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                        elif y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                        elif y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 180
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                            elif lst52[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                    'one' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                one_x2 = 160
                                                                one_y2 = 330
                                                        elif two_y2 == w and two_x2 == z:
                                                            if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                    'two' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                two_x2 = 160
                                                                two_y2 = 330
                                                        elif three_y2 == w and three_x2 == z:
                                                            if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                    'three' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                three_x2 = 160
                                                                three_y2 = 330
                                                        elif four_y2 == w and four_x2 == z:
                                                            if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                    'four' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                four_x2 = 160
                                                                four_y2 = 330
                                                        elif five_y2 == w and five_x2 == z:
                                                            if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                    'five' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                five_x2 = 160
                                                                five_y2 = 330
                                                        elif six_y2 == w and six_x2 == z:
                                                            if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                    'six' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                six_x2 = 160
                                                                six_y2 = 330
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                    'seven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                seven_x2 = 160
                                                                seven_y2 = 330
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                    'eight' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eight_x2 = 160
                                                                eight_y2 = 330
                                                        elif nine_y == w and nine_x == z:
                                                            if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                    'nine' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                nine_x = 160
                                                                nine_y = 330
                                                        elif ten_y == w and ten_x == z:
                                                            if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                    'ten' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                ten_x = 160
                                                                ten_y = 330
                                                        elif eleven_y == w and eleven_x == z:
                                                            if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                    'eleven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eleven_x = 160
                                                                eleven_y = 330
                                                        elif twelve_y == w and twelve_x == z:
                                                            if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                    'twelve' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                twelve_x = 160
                                                                twelve_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst22[3] == 1:
                                                                    w = 180
                                                                    lst12[1] = 1
                                                                    lst22[3] = 0
                                                                elif lst22[2] == 1:
                                                                    w = 230
                                                                    lst12[1] = 1
                                                                    lst22[2] = 0
                                                                elif lst22[1] == 1:
                                                                    w = 280
                                                                    lst12[1] = 1
                                                                    lst22[1] = 0
                                                                elif lst22[0] == 1:
                                                                    w = 330
                                                                    lst12[1] = 1
                                                                    lst22[0] = 0
                                                            elif y3 == 150:
                                                                if lst32[3] == 1:
                                                                    w = 180
                                                                    lst12[1] = 1
                                                                    lst32[3] = 0
                                                                elif lst32[2] == 1:
                                                                    w = 230
                                                                    lst12[1] = 1
                                                                    lst32[2] = 0
                                                                elif lst32[1] == 1:
                                                                    w = 280
                                                                    lst12[1] = 1
                                                                    lst32[1] = 0
                                                                elif lst32[0] == 1:
                                                                    w = 330
                                                                    lst12[1] = 1
                                                                    lst32[0] = 0
                                                            elif y4 == 150:
                                                                if lst42[3] == 1:
                                                                    w = 180
                                                                    lst12[1] = 1
                                                                    lst42[3] = 0
                                                                elif lst42[2] == 1:
                                                                    w = 230
                                                                    lst12[1] = 1
                                                                    lst42[2] = 0
                                                                elif lst42[1] == 1:
                                                                    w = 280
                                                                    lst12[1] = 1
                                                                    lst42[1] = 0
                                                                elif lst42[0] == 1:
                                                                    w = 330
                                                                    lst12[1] = 1
                                                                    lst42[0] = 0
                                                            elif y5 == 150:
                                                                if lst52[3] == 1:
                                                                    w = 180
                                                                    lst12[1] = 1
                                                                    lst52[3] = 0
                                                                elif lst52[2] == 1:
                                                                    w = 230
                                                                    lst12[1] = 1
                                                                    lst52[2] = 0
                                                                elif lst52[1] == 1:
                                                                    w = 280
                                                                    lst12[1] = 1
                                                                    lst52[1] = 0
                                                                elif lst52[0] == 1:
                                                                    w = 330
                                                                    lst12[1] = 1
                                                                    lst52[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x2 == 160:
                                                        q = 'one'
                                                    elif two_x2 == 160:
                                                        q = 'two'
                                                    elif three_x2 == 160:
                                                        q = 'three'
                                                    elif four_x2 == 160:
                                                        q = 'four'
                                                    elif five_x2 == 160:
                                                        q = 'five'
                                                    elif six_x2 == 160:
                                                        q = 'six'
                                                    elif seven_x2 == 160:
                                                        q = 'seven'
                                                    elif eight_x2 == 160:
                                                        q = 'eight'
                                                    elif nine_x == 160:
                                                        q = 'nine'
                                                    elif ten_x == 160:
                                                        q = 'ten'
                                                    elif eleven_x == 160:
                                                        q = 'eleven'
                                                    elif twelve_x == 160:
                                                        q = 'twelve'
                                                    if y2 == 150:
                                                        z = 260
                                                        if lst22[3] == 1:
                                                            w = 180
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 360
                                                        if lst32[3] == 1:
                                                            w = 180
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                    elif y4 == 150:
                                                        z = 460
                                                        if lst42[3] == 1:
                                                            w = 180
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                    elif y5 == 150:
                                                        z = 560
                                                        if lst52[3] == 1:
                                                            w = 180
                                                        elif lst52[2] == 1:
                                                            w = 230
                                                        elif lst52[1] == 1:
                                                            w = 280
                                                        elif lst52[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y2 == w and one_x2 == z:
                                                        if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                'one' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            one_x2 = 160
                                                            one_y2 = 280
                                                    elif two_y2 == w and two_x2 == z:
                                                        if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                'two' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            two_x2 = 160
                                                            two_y2 = 280
                                                    elif three_y2 == w and three_x2 == z:
                                                        if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                'three' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            three_x2 = 160
                                                            three_y2 = 280
                                                    elif four_y2 == w and four_x2 == z:
                                                        if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                'four' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            four_x2 = 160
                                                            four_y2 = 280
                                                    elif five_y2 == w and five_x2 == z:
                                                        if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                'five' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            five_x2 = 160
                                                            five_y2 = 280
                                                    elif six_y2 == w and six_x2 == z:
                                                        if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                'six' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            six_x2 = 160
                                                            six_y2 = 280
                                                    elif seven_y2 == w and seven_x2 == z:
                                                        if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                'seven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            seven_x2 = 160
                                                            seven_y2 = 280
                                                    elif eight_y2 == w and eight_x2 == z:
                                                        if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                'eight' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eight_x2 = 160
                                                            eight_y2 = 280
                                                    elif nine_y == w and nine_x == z:
                                                        if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                'nine' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            nine_x = 160
                                                            nine_y = 280
                                                    elif ten_y == w and ten_x == z:
                                                        if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                'ten' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            ten_x = 160
                                                            ten_y = 280
                                                    elif eleven_y == w and eleven_x == z:
                                                        if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                'eleven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eleven_x = 160
                                                            eleven_y = 280
                                                    elif twelve_y == w and twelve_x == z:
                                                        if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                'twelve' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            twelve_x = 160
                                                            twelve_y = 280
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst12[2] = 1
                                                                lst22[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst12[2] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst12[2] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst12[2] = 1
                                                                lst22[0] = 0
                                                        elif y3 == 150:
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst12[2] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst12[2] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst12[2] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst12[2] = 1
                                                                lst32[0] = 0
                                                        elif y4 == 150:
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst12[2] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst12[2] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst12[2] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst12[2] = 1
                                                                lst42[0] = 0
                                                        elif y5 == 150:
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst12[2] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst12[2] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst12[2] = 1
                                                                lst52[1] = 0
                                                            elif lst52[0] == 1:
                                                                w = 330
                                                                lst12[2] = 1
                                                                lst52[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x2 == 160:
                                                    q = 'one'
                                                elif two_x2 == 160:
                                                    q = 'two'
                                                elif three_x2 == 160:
                                                    q = 'three'
                                                elif four_x2 == 160:
                                                    q = 'four'
                                                elif five_x2 == 160:
                                                    q = 'five'
                                                elif six_x2 == 160:
                                                    q = 'six'
                                                elif seven_x2 == 160:
                                                    q = 'seven'
                                                elif eight_x2 == 160:
                                                    q = 'eight'
                                                elif nine_x == 160:
                                                    q = 'nine'
                                                elif ten_x == 160:
                                                    q = 'ten'
                                                elif eleven_x == 160:
                                                    q = 'eleven'
                                                elif twelve_x == 160:
                                                    q = 'twelve_'
                                                if y2 == 150:
                                                    z = 260
                                                    if lst22[3] == 1:
                                                        w = 180
                                                    elif lst22[2] == 1:
                                                        w = 230
                                                    elif lst22[1] == 1:
                                                        w = 280
                                                    elif lst22[0] == 1:
                                                        w = 330
                                                elif y3 == 150:
                                                    z = 360
                                                    if lst32[3] == 1:
                                                        w = 180
                                                    elif lst32[2] == 1:
                                                        w = 230
                                                    elif lst32[1] == 1:
                                                        w = 280
                                                    elif lst32[0] == 1:
                                                        w = 330
                                                elif y4 == 150:
                                                    z = 460
                                                    if lst42[3] == 1:
                                                        w = 180
                                                    elif lst42[2] == 1:
                                                        w = 230
                                                    elif lst42[1] == 1:
                                                        w = 280
                                                    elif lst42[0] == 1:
                                                        w = 330
                                                elif y5 == 150:
                                                    z = 560
                                                    if lst52[3] == 1:
                                                        w = 180
                                                    elif lst52[2] == 1:
                                                        w = 230
                                                    elif lst52[1] == 1:
                                                        w = 280
                                                    elif lst52[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_y2 == w and one_x2 == z:
                                                    if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                            'one' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        one_x2 = 160
                                                        one_y2 = 230
                                                elif two_y2 == w and two_x2 == z:
                                                    if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                            'two' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        two_x2 = 160
                                                        two_y2 = 230
                                                elif three_y2 == w and three_x2 == z:
                                                    if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                            'three' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        three_x2 = 160
                                                        three_y2 = 230
                                                elif four_y2 == w and four_x2 == z:
                                                    if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                            'four' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        four_x2 = 160
                                                        four_y2 = 230
                                                elif five_y2 == w and five_x2 == z:
                                                    if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                            'five' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        five_x2 = 160
                                                        five_y2 = 230
                                                elif six_y2 == w and six_x2 == z:
                                                    if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                            'six' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        six_x2 = 160
                                                        six_y2 = 230
                                                elif seven_y2 == w and seven_x2 == z:
                                                    if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                            'seven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        seven_x2 = 160
                                                        seven_y2 = 230
                                                elif eight_y2 == w and eight_x2 == z:
                                                    if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                            'eight' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eight_x2 = 160
                                                        eight_y2 = 230
                                                elif nine_y == w and nine_x == z:
                                                    if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                            'nine' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        nine_x = 160
                                                        nine_y = 230
                                                elif ten_y == w and ten_x == z:
                                                    if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                            'ten' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        ten_x = 160
                                                        ten_y = 230
                                                elif eleven_y == w and eleven_x == z:
                                                    if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                            'eleven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eleven_x = 160
                                                        eleven_y = 230
                                                elif twelve_y == w and twelve_x == z:
                                                    if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                            'twelve' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        twelve_x = 160
                                                        twelve_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst22[3] == 1:
                                                            w = 180
                                                            lst12[3] = 1
                                                            lst22[3] = 0
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                            lst12[3] = 1
                                                            lst22[2] = 0
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                            lst12[3] = 1
                                                            lst22[1] = 0
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                            lst12[3] = 1
                                                            lst22[0] = 0
                                                    elif y3 == 150:
                                                        if lst32[3] == 1:
                                                            w = 180
                                                            lst12[3] = 1
                                                            lst32[3] = 0
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                            lst12[3] = 1
                                                            lst32[2] = 0
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                            lst12[3] = 1
                                                            lst32[1] = 0
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                            lst12[3] = 1
                                                            lst32[0] = 0
                                                    elif y4 == 150:
                                                        if lst42[3] == 1:
                                                            w = 180
                                                            lst12[3] = 1
                                                            lst42[3] = 0
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                            lst12[3] = 1
                                                            lst42[2] = 0
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                            lst12[3] = 1
                                                            lst42[1] = 0
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                            lst12[3] = 1
                                                            lst42[0] = 0
                                                    elif y5 == 150:
                                                        if lst52[3] == 1:
                                                            w = 180
                                                            lst12[3] = 1
                                                            lst52[3] = 0
                                                        elif lst52[2] == 1:
                                                            w = 230
                                                            lst12[3] = 1
                                                            lst52[2] = 0
                                                        elif lst52[1] == 1:
                                                            w = 280
                                                            lst12[3] = 1
                                                            lst52[1] = 0
                                                        elif lst52[0] == 1:
                                                            w = 330
                                                            lst12[3] = 1
                                                            lst52[0] = 0
                                        else:
                                            lstsup2[2] = 1
                                            sup = 0
                                            for i in lstsup2:
                                                if i == 1:
                                                    sup += 1
                                            if sup == 2:
                                                time2 = int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            -1]).split(
                                                        '.')[0]) + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            1])) * 60 + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            0])) * 360
                                                result = time2 - time
                                                q = result % 60
                                                if q < 10:
                                                    fanction2(2, f'{result // 60}:0{q}')
                                                else:
                                                    fanction2(2, f'{result // 60}:{q}')

                class buttle2(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y2
                        y2 = self.rect.y
                        self.count = 1
                        self.b21 = 0
                        self.b22 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                                five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                                one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2, y2, q
                            self.b21 = 0
                            self.b22 = 0
                            if lst12[3] == 1:
                                if 'one' in lstred2 and one_x2 == 260:
                                    self.b21 += 1
                                if 'one' in lstgreen2 and one_x2 == 260:
                                    self.b22 += 1
                                if 'two' in lstred2 and two_x2 == 260:
                                    self.b21 += 1
                                if 'two' in lstgreen2 and two_x2 == 260:
                                    self.b22 += 1
                                if 'three' in lstred2 and three_x2 == 260:
                                    self.b21 += 1
                                if 'three' in lstgreen2 and three_x2 == 260:
                                    self.b22 += 1
                                if 'four' in lstred2 and four_x2 == 260:
                                    self.b21 += 1
                                if 'four' in lstgreen2 and four_x2 == 260:
                                    self.b22 += 1
                                if 'five' in lstred2 and five_x2 == 260:
                                    self.b21 += 1
                                if 'five' in lstgreen2 and five_x2 == 260:
                                    self.b22 += 1
                                if 'six' in lstred2 and six_x2 == 260:
                                    self.b21 += 1
                                if 'six' in lstgreen2 and six_x2 == 260:
                                    self.b22 += 1
                                if 'seven' in lstred2 and seven_x2 == 260:
                                    self.b21 += 1
                                if 'seven' in lstgreen2 and seven_x2 == 260:
                                    self.b22 += 1
                                if 'eight' in lstred2 and eight_x2 == 260:
                                    self.b21 += 1
                                if 'eight' in lstgreen2 and eight_x2 == 260:
                                    self.b22 += 1
                                if 'nine' in lstred2 and nine_x == 260:
                                    self.b21 += 1
                                if 'nine' in lstgreen2 and nine_x == 260:
                                    self.b22 += 1
                                if 'ten' in lstred2 and ten_x == 260:
                                    self.b21 += 1
                                if 'ten' in lstgreen2 and ten_x == 260:
                                    self.b22 += 1
                                if 'eleven' in lstred2 and eleven_x == 260:
                                    self.b21 += 1
                                if 'eleven' in lstgreen2 and eleven_x == 260:
                                    self.b22 += 1
                                if 'twelve' in lstred2 and twelve_x == 260:
                                    self.b21 += 1
                                if 'twelve' in lstgreen2 and twelve_x == 260:
                                    self.b22 += 1
                            if self.b21 != 4 and self.b22 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y2 -= 50
                                        if one_x2 == 260:
                                            one_y2 -= 50
                                        if two_x2 == 260:
                                            two_y2 -= 50
                                        if three_x2 == 260:
                                            three_y2 -= 50
                                        if four_x2 == 260:
                                            four_y2 -= 50
                                        if five_x2 == 260:
                                            five_y2 -= 50
                                        if six_x2 == 260:
                                            six_y2 -= 50
                                        if seven_x2 == 260:
                                            seven_y2 -= 50
                                        if eight_x2 == 260:
                                            eight_y2 -= 50
                                        if nine_x == 260:
                                            nine_y -= 50
                                        if ten_x == 260:
                                            ten_y -= 50
                                        if eleven_x == 260:
                                            eleven_y -= 50
                                        if twelve_x == 260:
                                            twelve_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y2 += 50
                                        if one_x2 == 260:
                                            one_y2 += 50
                                        if two_x2 == 260:
                                            two_y2 += 50
                                        if three_x2 == 260:
                                            three_y2 += 50
                                        if four_x2 == 260:
                                            four_y2 += 50
                                        if five_x2 == 260:
                                            five_y2 += 50
                                        if six_x2 == 260:
                                            six_y2 += 50
                                        if seven_x2 == 260:
                                            seven_y2 += 50
                                        if eight_x2 == 260:
                                            eight_y2 += 50
                                        if nine_x == 260:
                                            nine_y += 50
                                        if ten_x == 260:
                                            ten_y += 50
                                        if eleven_x == 260:
                                            eleven_y += 50
                                        if twelve_x == 260:
                                            twelve_y += 50
                                        self.count += 1
                                    else:
                                        global y5, y4, y3, y1
                                        if lst22[3] == 0:
                                            if lst22[2] == 0:
                                                if lst22[1] == 0:
                                                    if lst22[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst22[0] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst22[0] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst22[0] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst22[0] = 1
                                                                lst12[0] = 0
                                                        if y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst22[0] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst22[0] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst22[0] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst22[0] = 1
                                                                lst32[0] = 0
                                                        if y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst22[0] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst22[0] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst22[0] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst22[0] = 1
                                                                lst42[0] = 0
                                                        if y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst22[0] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst22[0] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst22[0] = 1
                                                                lst52[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst22[0] = 1
                                                                lst52[0] = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            one_x2 = 260
                                                            one_y2 = 380
                                                        elif two_y2 == w and two_x2 == z:
                                                            two_x2 = 260
                                                            two_y2 = 380
                                                        elif three_y2 == w and three_x2 == z:
                                                            three_x2 = 260
                                                            three_y2 = 380
                                                        elif four_y2 == w and four_x2 == z:
                                                            four_x2 = 260
                                                            four_y2 = 380
                                                        elif five_y2 == w and five_x2 == z:
                                                            five_x2 = 260
                                                            five_y2 = 380
                                                        elif six_y2 == w and six_x2 == z:
                                                            six_x = 260
                                                            six_y = 380
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            seven_x2 = 260
                                                            seven_y2 = 380
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            eight_x2 = 260
                                                            eight_y2 = 380
                                                        elif nine_y == w and nine_x == z:
                                                            nine_x = 260
                                                            nine_y = 380
                                                        elif ten_y == w and ten_x == z:
                                                            ten_x = 260
                                                            ten_y = 380
                                                        elif eleven_y == w and eleven_x == z:
                                                            eleven_x = 260
                                                            eleven_y = 380
                                                        elif twelve_y == w and twelve_x == z:
                                                            twelve_x = 260
                                                            twelve_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x2 == 260:
                                                            q = 'one'
                                                        elif two_x2 == 260:
                                                            q = 'two'
                                                        elif three_x2 == 260:
                                                            q = 'three'
                                                        elif four_x2 == 260:
                                                            q = 'four'
                                                        elif five_x2 == 260:
                                                            q = 'five'
                                                        elif six_x2 == 260:
                                                            q = 'six'
                                                        elif seven_x2 == 260:
                                                            q = 'seven'
                                                        elif eight_x2 == 260:
                                                            q = 'eight'
                                                        elif nine_x == 260:
                                                            q = 'nine'
                                                        elif ten_x == 260:
                                                            q = 'ten'
                                                        elif eleven_x == 260:
                                                            q = 'eleven'
                                                        elif twelve_x == 260:
                                                            q = 'twelve'
                                                        if y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 230 - 50
                                                            elif lst12[2] == 1:
                                                                w = 280 - 50
                                                            elif lst12[1] == 1:
                                                                w = 330 - 50
                                                            elif lst12[0] == 1:
                                                                w = 330 - 50
                                                        elif y3 == 380:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 230 - 50
                                                            elif lst32[2] == 1:
                                                                w = 280 - 50
                                                            elif lst32[1] == 1:
                                                                w = 330 - 50
                                                            elif lst32[0] == 1:
                                                                w = 330 - 50
                                                        elif y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 230 - 50
                                                            elif lst42[2] == 1:
                                                                w = 280 - 50
                                                            elif lst42[1] == 1:
                                                                w = 330 - 50
                                                            elif lst42[0] == 1:
                                                                w = 380 - 50
                                                        elif y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 230 - 50
                                                            elif lst52[2] == 1:
                                                                w = 280 - 50
                                                            elif lst52[1] == 1:
                                                                w = 330 - 50
                                                            elif lst52[0] == 1:
                                                                w = 380 - 50
                                                        q2 = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                    'one' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                one_x2 = 260
                                                                one_y2 = 330
                                                        elif two_y2 == w and two_x2 == z:
                                                            if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                    'two' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                two_x2 = 260
                                                                two_y2 = 330
                                                        elif three_y2 == w and three_x2 == z:
                                                            if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                    'three' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                three_x2 = 260
                                                                three_y2 = 330
                                                        elif four_y2 == w and four_x2 == z:
                                                            if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                    'four' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                four_x2 = 260
                                                                four_y2 = 330
                                                        elif five_y2 == w and five_x2 == z:
                                                            if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                    'five' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                five_x2 = 260
                                                                five_y2 = 330
                                                        elif six_y2 == w and six_x2 == z:
                                                            if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                    'six' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                six_x2 = 260
                                                                six_y2 = 330
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                    'seven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                seven_x2 = 260
                                                                seven_y2 = 330
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                    'eight' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eight_x2 = 260
                                                                eight_y2 = 330
                                                        elif nine_y == w and nine_x == z:
                                                            if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                    'nine' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                nine_x = 260
                                                                nine_y = 330
                                                        elif ten_y == w and ten_x == z:
                                                            if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                    'ten' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                ten_x = 260
                                                                ten_y = 330
                                                        elif eleven_y == w and eleven_x == z:
                                                            if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                    'eleven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eleven_x = 260
                                                                eleven_y = 330
                                                        elif twelve_y == w and twelve_x == z:
                                                            if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                    'twelve' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                twelve_x = 260
                                                                twelve_y = 330
                                                        if q2 == 1:
                                                            if y1 == 150:
                                                                if lst12[3] == 1:
                                                                    w = 180
                                                                    lst22[1] = 1
                                                                    lst12[3] = 0
                                                                elif lst12[2] == 1:
                                                                    w = 230
                                                                    lst22[1] = 1
                                                                    lst12[2] = 0
                                                                elif lst12[1] == 1:
                                                                    w = 280
                                                                    lst22[1] = 1
                                                                    lst12[1] = 0
                                                                elif lst12[0] == 1:
                                                                    w = 330
                                                                    lst22[1] = 1
                                                                    lst12[0] = 0
                                                            elif y3 == 150:
                                                                if lst32[3] == 1:
                                                                    w = 180
                                                                    lst22[1] = 1
                                                                    lst32[3] = 0
                                                                elif lst32[2] == 1:
                                                                    w = 230
                                                                    lst22[1] = 1
                                                                    lst32[2] = 0
                                                                elif lst32[1] == 1:
                                                                    w = 280
                                                                    lst22[1] = 1
                                                                    lst32[1] = 0
                                                                elif lst32[0] == 1:
                                                                    w = 330
                                                                    lst22[1] = 1
                                                                    lst32[0] = 0
                                                            elif y4 == 150:
                                                                if lst42[3] == 1:
                                                                    w = 180
                                                                    lst22[1] = 1
                                                                    lst42[3] = 0
                                                                elif lst42[2] == 1:
                                                                    w = 230
                                                                    lst22[1] = 1
                                                                    lst42[2] = 0
                                                                elif lst42[1] == 1:
                                                                    w = 280
                                                                    lst22[1] = 1
                                                                    lst42[1] = 0
                                                                elif lst42[0] == 1:
                                                                    w = 330
                                                                    lst22[1] = 1
                                                                    lst42[0] = 0
                                                            elif y5 == 150:
                                                                if lst52[3] == 1:
                                                                    w = 180
                                                                    lst22[1] = 1
                                                                    lst52[3] = 0
                                                                elif lst52[2] == 1:
                                                                    w = 230
                                                                    lst22[1] = 1
                                                                    lst52[2] = 0
                                                                elif lst52[1] == 1:
                                                                    w = 280
                                                                    lst22[1] = 1
                                                                    lst52[1] = 0
                                                                elif lst52[0] == 1:
                                                                    w = 330
                                                                    lst22[1] = 1
                                                                    lst52[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x2 == 260:
                                                        q = 'one'
                                                    elif two_x2 == 260:
                                                        q = 'two'
                                                    elif three_x2 == 260:
                                                        q = 'three'
                                                    elif four_x2 == 260:
                                                        q = 'four'
                                                    elif five_x2 == 260:
                                                        q = 'five'
                                                    elif six_x2 == 260:
                                                        q = 'six'
                                                    elif seven_x2 == 260:
                                                        q = 'seven'
                                                    elif eight_x2 == 260:
                                                        q = 'eight'
                                                    elif nine_x == 260:
                                                        q = 'nine'
                                                    elif ten_x == 260:
                                                        q = 'ten'
                                                    elif eleven_x == 260:
                                                        q = 'eleven'
                                                    elif twelve_x == 260:
                                                        q = 'twelve'
                                                    if y1 == 150:
                                                        z = 160
                                                        if lst12[3] == 1:
                                                            w = 230 - 50
                                                        elif lst12[2] == 1:
                                                            w = 280 - 50
                                                        elif lst12[1] == 1:
                                                            w = 330 - 50
                                                        elif lst12[0] == 1:
                                                            w = 380 - 50
                                                    elif y3 == 150:
                                                        z = 360
                                                        if lst32[3] == 1:
                                                            w = 230 - 50
                                                        elif lst32[2] == 1:
                                                            w = 280 - 50
                                                        elif lst32[1] == 1:
                                                            w = 330 - 50
                                                        elif lst32[0] == 1:
                                                            w = 380 - 50
                                                    elif y4 == 150:
                                                        z = 460
                                                        if lst42[3] == 1:
                                                            w = 230 - 50
                                                        elif lst42[2] == 1:
                                                            w = 280 - 50
                                                        elif lst42[1] == 1:
                                                            w = 330 - 50
                                                        elif lst42[0] == 1:
                                                            w = 380 - 50
                                                    elif y5 == 150:
                                                        z = 560
                                                        if lst52[3] == 1:
                                                            w = 230 - 50
                                                        elif lst52[2] == 1:
                                                            w = 280 - 50
                                                        elif lst52[1] == 1:
                                                            w = 330 - 50
                                                        elif lst52[0] == 1:
                                                            w = 380 - 50
                                                    q2 = 0
                                                    if one_y2 == w and one_x2 == z:
                                                        if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                'one' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            one_x2 = 260
                                                            one_y2 = 280
                                                    elif two_y2 == w and two_x2 == z:
                                                        if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                'two' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            two_x2 = 260
                                                            two_y2 = 280
                                                    elif three_y2 == w and three_x2 == z:
                                                        if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                'three' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            three_x2 = 260
                                                            three_y2 = 280
                                                    elif four_y2 == w and four_x2 == z:
                                                        if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                'four' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            four_x2 = 260
                                                            four_y2 = 280
                                                    elif five_y2 == w and five_x2 == z:
                                                        if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                'five' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            five_x2 = 260
                                                            five_y2 = 280
                                                    elif six_y2 == w and six_x2 == z:
                                                        if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                'six' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            six_x2 = 260
                                                            six_y2 = 330
                                                    elif seven_y2 == w and seven_x2 == z:
                                                        if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                'seven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            seven_x2 = 260
                                                            seven_y2 = 280
                                                    elif eight_y2 == w and eight_x2 == z:
                                                        if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                'eight' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eight_x2 = 260
                                                            eight_y2 = 280
                                                    elif nine_y == w and nine_x == z:
                                                        if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                'nine' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            nine_x = 260
                                                            nine_y = 280
                                                    elif ten_y == w and ten_x == z:
                                                        if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                'ten' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            ten_x = 260
                                                            ten_y = 280
                                                    elif eleven_y == w and eleven_x == z:
                                                        if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                'eleven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eleven_x = 260
                                                            eleven_y = 280
                                                    elif twelve_y == w and twelve_x == z:
                                                        if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                'twelve' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            twelve_x = 260
                                                            twelve_y = 280
                                                    if q2 == 1:
                                                        if y1 == 150:
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst22[2] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst22[2] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst22[2] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst22[2] = 1
                                                                lst12[0] = 0
                                                        elif y3 == 150:
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst22[2] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst22[2] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst22[2] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst22[2] = 1
                                                                lst32[0] = 0
                                                        elif y4 == 150:
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst22[2] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst22[2] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst22[2] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst22[2] = 1
                                                                lst42[0] = 0
                                                        elif y5 == 150:
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst22[2] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst22[2] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst22[2] = 1
                                                                lst52[1] = 0
                                                            elif lst52[0] == 1:
                                                                w = 330
                                                                lst22[2] = 1
                                                                lst52[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x2 == 260:
                                                    q = 'one'
                                                elif two_x2 == 260:
                                                    q = 'two'
                                                elif three_x2 == 260:
                                                    q = 'three'
                                                elif four_x2 == 260:
                                                    q = 'four'
                                                elif five_x2 == 260:
                                                    q = 'five'
                                                elif six_x2 == 260:
                                                    q = 'six'
                                                elif seven_x2 == 260:
                                                    q = 'seven'
                                                elif eight_x2 == 260:
                                                    q = 'eight'
                                                elif nine_x == 260:
                                                    q = 'nine'
                                                elif ten_x == 260:
                                                    q = 'ten'
                                                elif eleven_x == 260:
                                                    q = 'eleven'
                                                elif twelve_x == 260:
                                                    q = 'twelve'
                                                if y1 == 150:
                                                    z = 160
                                                    if lst12[3] == 1:
                                                        w = 230 - 50
                                                    elif lst12[2] == 1:
                                                        w = 280 - 50
                                                    elif lst12[1] == 1:
                                                        w = 330 - 50
                                                    elif lst12[0] == 1:
                                                        w = 380 - 50
                                                elif y3 == 150:
                                                    z = 360
                                                    if lst32[3] == 1:
                                                        w = 230 - 50
                                                    elif lst32[2] == 1:
                                                        w = 280 - 50
                                                    elif lst32[1] == 1:
                                                        w = 330 - 50
                                                    elif lst32[0] == 1:
                                                        w = 380 - 50
                                                elif y4 == 150:
                                                    z = 460
                                                    if lst42[3] == 1:
                                                        w = 230 - 50
                                                    elif lst42[2] == 1:
                                                        w = 280 - 50
                                                    elif lst42[1] == 1:
                                                        w = 330 - 50
                                                    elif lst42[0] == 1:
                                                        w = 380 - 50
                                                elif y5 == 150:
                                                    z = 560
                                                    if lst52[3] == 1:
                                                        w = 230 - 50
                                                    elif lst52[2] == 1:
                                                        w = 280 - 50
                                                    elif lst52[1] == 1:
                                                        w = 330 - 50
                                                    elif lst52[0] == 1:
                                                        w = 380 - 50
                                                q2 = 0
                                                if one_y2 == w and one_x2 == z:
                                                    if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                            'one' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        one_x2 = 260
                                                        one_y2 = 230
                                                elif two_y2 == w and two_x2 == z:
                                                    if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                            'two' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        two_x2 = 260
                                                        two_y2 = 230
                                                elif three_y2 == w and three_x2 == z:
                                                    if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                            'three' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        three_x2 = 260
                                                        three_y2 = 230
                                                elif four_y2 == w and four_x2 == z:
                                                    if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                            'four' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        four_x2 = 260
                                                        four_y2 = 230
                                                elif five_y2 == w and five_x2 == z:
                                                    if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                            'five' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        five_x2 = 260
                                                        five_y2 = 230
                                                elif six_y2 == w and six_x2 == z:
                                                    if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                            'six' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        six_x2 = 260
                                                        six_y2 = 230
                                                elif seven_y2 == w and seven_x2 == z:
                                                    if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                            'seven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        seven_x2 = 260
                                                        seven_y2 = 230
                                                elif eight_y2 == w and eight_x2 == z:
                                                    if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                            'eight' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eight_x2 = 260
                                                        eight_y2 = 230
                                                elif nine_y == w and nine_x == z:
                                                    if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                            'nine' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        nine_x = 260
                                                        nine_y = 230
                                                elif ten_y == w and ten_x == z:
                                                    if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                            'ten' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        ten_x = 260
                                                        ten_y = 230
                                                elif eleven_y == w and eleven_x == z:
                                                    if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                            'eleven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eleven_x = 260
                                                        eleven_y = 230
                                                elif twelve_y == w and twelve_x == z:
                                                    if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                            'twelve' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        twelve_x = 260
                                                        twelve_y = 230
                                                if q2 == 1:
                                                    if y1 == 150:
                                                        if lst12[3] == 1:
                                                            w = 180
                                                            lst22[3] = 1
                                                            lst12[3] = 0
                                                        elif lst12[2] == 1:
                                                            w = 230
                                                            lst22[3] = 1
                                                            lst12[2] = 0
                                                        elif lst12[1] == 1:
                                                            w = 280
                                                            lst22[3] = 1
                                                            lst12[1] = 0
                                                        elif lst12[0] == 1:
                                                            w = 330
                                                            lst22[3] = 1
                                                            lst12[0] = 0
                                                    elif y3 == 150:
                                                        if lst32[3] == 1:
                                                            w = 180
                                                            lst22[3] = 1
                                                            lst32[3] = 0
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                            lst22[3] = 1
                                                            lst32[2] = 0
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                            lst22[3] = 1
                                                            lst32[1] = 0
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                            lst22[3] = 1
                                                            lst32[0] = 0
                                                    elif y4 == 150:
                                                        if lst42[3] == 1:
                                                            w = 180
                                                            lst22[3] = 1
                                                            lst42[3] = 0
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                            lst22[3] = 1
                                                            lst42[2] = 0
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                            lst22[3] = 1
                                                            lst42[1] = 0
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                            lst22[3] = 1
                                                            lst42[0] = 0
                                                    elif y5 == 150:
                                                        if lst52[3] == 1:
                                                            w = 180
                                                            lst22[3] = 1
                                                            lst52[3] = 0
                                                        elif lst52[2] == 1:
                                                            w = 230
                                                            lst22[3] = 1
                                                            lst52[2] = 0
                                                        elif lst52[1] == 1:
                                                            w = 280
                                                            lst22[3] = 1
                                                            lst52[1] = 0
                                                        elif lst52[0] == 1:
                                                            w = 330
                                                            lst22[3] = 1
                                                            lst52[0] = 0
                                        else:
                                            lstsup2[2] = 1
                                            sup = 0
                                            for i in lstsup2:
                                                if i == 1:
                                                    sup += 1
                                            if sup == 2:
                                                time2 = int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            -1]).split(
                                                        '.')[0]) + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            1])) * 60 + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            0])) * 360
                                                result = time2 - time
                                                q = result % 60
                                                if q < 10:
                                                    fanction2(2, f'{result // 60}:0{q}')
                                                else:
                                                    fanction2(2, f'{result // 60}:{q}')

                class buttle3(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y3
                        y3 = self.rect.y
                        self.count = 1
                        self.b31 = 0
                        self.b32 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                                five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                                one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2, y3, q
                            self.b31 = 0
                            self.b32 = 0
                            if lst12[3] == 1:
                                if 'one' in lstred2 and one_x2 == 360:
                                    self.b31 += 1
                                if 'one' in lstgreen2 and one_x2 == 360:
                                    self.b32 += 1
                                if 'two' in lstred2 and two_x2 == 360:
                                    self.b31 += 1
                                if 'two' in lstgreen2 and two_x2 == 360:
                                    self.b32 += 1
                                if 'three' in lstred2 and three_x2 == 360:
                                    self.b31 += 1
                                if 'three' in lstgreen2 and three_x2 == 360:
                                    self.b32 += 1
                                if 'four' in lstred2 and four_x2 == 360:
                                    self.b31 += 1
                                if 'four' in lstgreen2 and four_x2 == 360:
                                    self.b32 += 1
                                if 'five' in lstred2 and five_x2 == 360:
                                    self.b31 += 1
                                if 'five' in lstgreen2 and five_x2 == 360:
                                    self.b32 += 1
                                if 'six' in lstred2 and six_x2 == 360:
                                    self.b31 += 1
                                if 'six' in lstgreen2 and six_x2 == 360:
                                    self.b32 += 1
                                if 'seven' in lstred2 and seven_x2 == 360:
                                    self.b31 += 1
                                if 'seven' in lstgreen2 and seven_x2 == 360:
                                    self.b32 += 1
                                if 'eight' in lstred2 and eight_x2 == 360:
                                    self.b31 += 1
                                if 'eight' in lstgreen2 and eight_x2 == 360:
                                    self.b32 += 1
                                if 'nine' in lstred2 and nine_x == 360:
                                    self.b31 += 1
                                if 'nine' in lstgreen2 and nine_x == 360:
                                    self.b32 += 1
                                if 'ten' in lstred2 and ten_x == 360:
                                    self.b31 += 1
                                if 'ten' in lstgreen2 and ten_x == 360:
                                    self.b32 += 1
                                if 'eleven' in lstred2 and eleven_x == 360:
                                    self.b31 += 1
                                if 'eleven' in lstgreen2 and eleven_x == 360:
                                    self.b32 += 1
                                if 'twelve' in lstred2 and twelve_x == 360:
                                    self.b31 += 1
                                if 'twelve' in lstgreen2 and twelve_x == 360:
                                    self.b32 += 1
                            if self.b31 != 4 and self.b32 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y3 -= 50
                                        if one_x2 == 360:
                                            one_y2 -= 50
                                        if two_x2 == 360:
                                            two_y2 -= 50
                                        if three_x2 == 360:
                                            three_y2 -= 50
                                        if four_x2 == 360:
                                            four_y2 -= 50
                                        if five_x2 == 360:
                                            five_y2 -= 50
                                        if six_x2 == 360:
                                            six_y2 -= 50
                                        if seven_x2 == 360:
                                            seven_y2 -= 50
                                        if eight_x2 == 360:
                                            eight_y2 -= 50
                                        if nine_x == 360:
                                            nine_y -= 50
                                        if ten_x == 360:
                                            ten_y -= 50
                                        if eleven_x == 360:
                                            eleven_y -= 50
                                        if twelve_x == 360:
                                            twelve_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y3 += 50
                                        if one_x2 == 360:
                                            one_y2 += 50
                                        if two_x2 == 360:
                                            two_y2 += 50
                                        if three_x2 == 360:
                                            three_y2 += 50
                                        if four_x2 == 360:
                                            four_y2 += 50
                                        if five_x2 == 360:
                                            five_y2 += 50
                                        if six_x2 == 360:
                                            six_y2 += 50
                                        if seven_x2 == 360:
                                            seven_y2 += 50
                                        if eight_x2 == 160:
                                            eight_y2 += 50
                                        if nine_x == 360:
                                            nine_y += 50
                                        if ten_x == 360:
                                            ten_y += 50
                                        if eleven_x == 360:
                                            eleven_y += 50
                                        if twelve_x == 360:
                                            twelve_y += 50
                                        self.count += 1
                                    else:
                                        global y5, y4, y2, y1
                                        if lst32[3] == 0:
                                            if lst32[2] == 0:
                                                if lst32[1] == 0:
                                                    if lst32[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst32[0] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst32[0] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst32[0] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst32[0] = 1
                                                                lst12[0] = 0
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst22[0] = 1
                                                                lst32[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst32[0] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst32[0] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst32[0] = 1
                                                                lst22[0] = 0
                                                        if y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst32[0] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst32[0] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst32[0] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst32[0] = 1
                                                                lst42[0] = 0
                                                        if y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst32[0] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst32[0] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst32[0] = 1
                                                                lst52[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst32[0] = 1
                                                                lst52[0] = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            one_x2 = 360
                                                            one_y2 = 380
                                                        elif two_y2 == w and two_x2 == z:
                                                            two_x2 = 360
                                                            two_y2 = 380
                                                        elif three_y2 == w and three_x2 == z:
                                                            three_x2 = 360
                                                            three_y2 = 380
                                                        elif four_y2 == w and four_x2 == z:
                                                            four_x2 = 360
                                                            four_y2 = 380
                                                        elif five_y2 == w and five_x2 == z:
                                                            five_x2 = 360
                                                            five_y2 = 380
                                                        elif six_y2 == w and six_x2 == z:
                                                            six_x = 360
                                                            six_y = 380
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            seven_x2 = 360
                                                            seven_y2 = 380
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            eight_x2 = 360
                                                            eight_y2 = 380
                                                        elif nine_y == w and nine_x == z:
                                                            nine_x = 360
                                                            nine_y = 380
                                                        elif ten_y == w and ten_x == z:
                                                            ten_x = 360
                                                            ten_y = 380
                                                        elif eleven_y == w and eleven_x == z:
                                                            eleven_x = 360
                                                            eleven_y = 380
                                                        elif twelve_y == w and twelve_x == z:
                                                            twelve_x = 360
                                                            twelve_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x2 == 360:
                                                            q = 'one'
                                                        elif two_x2 == 360:
                                                            q = 'two'
                                                        elif three_x2 == 360:
                                                            q = 'three'
                                                        elif four_x2 == 360:
                                                            q = 'four'
                                                        elif five_x2 == 360:
                                                            q = 'five'
                                                        elif six_x2 == 360:
                                                            q = 'six'
                                                        elif seven_x2 == 360:
                                                            q = 'seven'
                                                        elif eight_x2 == 360:
                                                            q = 'eight'
                                                        elif nine_x == 360:
                                                            q = 'nine'
                                                        elif ten_x == 360:
                                                            q = 'ten'
                                                        elif eleven_x == 360:
                                                            q = 'eleven'
                                                        elif twelve_x == 360:
                                                            q = 'twelve'
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 230 - 50
                                                            elif lst22[2] == 1:
                                                                w = 280 - 50
                                                            elif lst22[1] == 1:
                                                                w = 330 - 50
                                                            elif lst22[0] == 1:
                                                                w = 380 - 50
                                                        elif y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 230 - 50
                                                            elif lst12[2] == 1:
                                                                w = 280 - 50
                                                            elif lst12[1] == 1:
                                                                w = 330 - 50
                                                            elif lst12[0] == 1:
                                                                w = 380 - 50
                                                        elif y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 230 - 50
                                                            elif lst42[2] == 1:
                                                                w = 280 - 50
                                                            elif lst42[1] == 1:
                                                                w = 330 - 50
                                                            elif lst42[0] == 1:
                                                                w = 380 - 50
                                                        elif y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 230 - 50
                                                            elif lst52[2] == 1:
                                                                w = 280 - 50
                                                            elif lst52[1] == 1:
                                                                w = 330 - 50
                                                            elif lst52[0] == 1:
                                                                w = 380 - 50
                                                        q2 = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                    'one' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                one_x2 = 360
                                                                one_y2 = 330
                                                        elif two_y2 == w and two_x2 == z:
                                                            if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                    'two' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                two_x2 = 360
                                                                two_y2 = 330
                                                        elif three_y2 == w and three_x2 == z:
                                                            if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                    'three' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                three_x2 = 360
                                                                three_y2 = 330
                                                        elif four_y2 == w and four_x2 == z:
                                                            if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                    'four' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                four_x2 = 360
                                                                four_y2 = 330
                                                        elif five_y2 == w and five_x2 == z:
                                                            if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                    'five' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                five_x2 = 360
                                                                five_y2 = 330
                                                        elif six_y2 == w and six_x2 == z:
                                                            if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                    'six' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                six_x2 = 360
                                                                six_y2 = 330
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                    'seven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                seven_x2 = 360
                                                                seven_y2 = 330
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                    'eight' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eight_x2 = 360
                                                                eight_y2 = 330
                                                        elif nine_y == w and nine_x == z:
                                                            if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                    'nine' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                nine_x = 360
                                                                nine_y = 330
                                                        elif ten_y == w and ten_x == z:
                                                            if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                    'ten' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                ten_x = 360
                                                                ten_y = 330
                                                        elif eleven_y == w and eleven_x == z:
                                                            if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                    'eleven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eleven_x = 360
                                                                eleven_y = 330
                                                        elif twelve_y == w and twelve_x == z:
                                                            if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                    'twelve' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                twelve_x = 360
                                                                twelve_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst22[3] == 1:
                                                                    w = 180
                                                                    lst32[1] = 1
                                                                    lst22[3] = 0
                                                                elif lst22[2] == 1:
                                                                    w = 230
                                                                    lst32[1] = 1
                                                                    lst22[2] = 0
                                                                elif lst22[1] == 1:
                                                                    w = 280
                                                                    lst32[1] = 1
                                                                    lst22[1] = 0
                                                                elif lst22[0] == 1:
                                                                    w = 330
                                                                    lst32[1] = 1
                                                                    lst22[0] = 0
                                                            elif y1 == 150:
                                                                if lst12[3] == 1:
                                                                    w = 180
                                                                    lst32[1] = 1
                                                                    lst12[3] = 0
                                                                elif lst12[2] == 1:
                                                                    w = 230
                                                                    lst32[1] = 1
                                                                    lst12[2] = 0
                                                                elif lst12[1] == 1:
                                                                    w = 280
                                                                    lst32[1] = 1
                                                                    lst12[1] = 0
                                                                elif lst12[0] == 1:
                                                                    w = 330
                                                                    lst32[1] = 1
                                                                    lst12[0] = 0
                                                            elif y4 == 150:
                                                                if lst42[3] == 1:
                                                                    w = 180
                                                                    lst32[1] = 1
                                                                    lst42[3] = 0
                                                                elif lst42[2] == 1:
                                                                    w = 230
                                                                    lst32[1] = 1
                                                                    lst42[2] = 0
                                                                elif lst42[1] == 1:
                                                                    w = 280
                                                                    lst32[1] = 1
                                                                    lst42[1] = 0
                                                                elif lst42[0] == 1:
                                                                    w = 330
                                                                    lst32[1] = 1
                                                                    lst42[0] = 0
                                                            elif y5 == 150:
                                                                if lst52[3] == 1:
                                                                    w = 180
                                                                    lst32[1] = 1
                                                                    lst52[3] = 0
                                                                elif lst52[2] == 1:
                                                                    w = 230
                                                                    lst32[1] = 1
                                                                    lst52[2] = 0
                                                                elif lst52[1] == 1:
                                                                    w = 280
                                                                    lst32[1] = 1
                                                                    lst52[1] = 0
                                                                elif lst52[0] == 1:
                                                                    w = 330
                                                                    lst32[1] = 1
                                                                    lst52[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x2 == 360:
                                                        q = 'one'
                                                    elif two_x2 == 360:
                                                        q = 'two'
                                                    elif three_x2 == 360:
                                                        q = 'three'
                                                    elif four_x2 == 360:
                                                        q = 'four'
                                                    elif five_x2 == 360:
                                                        q = 'five'
                                                    elif six_x2 == 360:
                                                        q = 'six'
                                                    elif seven_x2 == 360:
                                                        q = 'seven'
                                                    elif eight_x2 == 360:
                                                        q = 'eight'
                                                    elif nine_x == 360:
                                                        q = 'nine'
                                                    elif ten_x == 360:
                                                        q = 'ten'
                                                    elif eleven_x == 360:
                                                        q = 'eleven'
                                                    elif twelve_x == 360:
                                                        q = 'twelve'
                                                    if y2 == 150:
                                                        z = 260
                                                        if lst22[3] == 1:
                                                            w = 230 - 50
                                                        elif lst22[2] == 1:
                                                            w = 280 - 50
                                                        elif lst22[1] == 1:
                                                            w = 330 - 50
                                                        elif lst22[0] == 1:
                                                            w = 380 - 50
                                                    elif y1 == 150:
                                                        z = 160
                                                        if lst12[3] == 1:
                                                            w = 230 - 50
                                                        elif lst12[2] == 1:
                                                            w = 280 - 50
                                                        elif lst12[1] == 1:
                                                            w = 330 - 50
                                                        elif lst12[0] == 1:
                                                            w = 380 - 50
                                                    elif y4 == 150:
                                                        z = 460
                                                        if lst42[3] == 1:
                                                            w = 230 - 50
                                                        elif lst42[2] == 1:
                                                            w = 280 - 50
                                                        elif lst42[1] == 1:
                                                            w = 330 - 50
                                                        elif lst42[0] == 1:
                                                            w = 380 - 50
                                                    elif y5 == 150:
                                                        z = 560
                                                        if lst52[3] == 1:
                                                            w = 230 - 50
                                                        elif lst52[2] == 1:
                                                            w = 280 - 50
                                                        elif lst52[1] == 1:
                                                            w = 330 - 50
                                                        elif lst52[0] == 1:
                                                            w = 380 - 50
                                                    q2 = 0
                                                    if one_y2 == w and one_x2 == z:
                                                        if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                'one' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            one_x2 = 360
                                                            one_y2 = 280
                                                    elif two_y2 == w and two_x2 == z:
                                                        if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                'two' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            two_x2 = 360
                                                            two_y2 = 280
                                                    elif three_y2 == w and three_x2 == z:
                                                        if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                'three' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            three_x2 = 360
                                                            three_y2 = 280
                                                    elif four_y2 == w and four_x2 == z:
                                                        if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                'four' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            four_x2 = 360
                                                            four_y2 = 280
                                                    elif five_y2 == w and five_x2 == z:
                                                        if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                'five' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            five_x2 = 360
                                                            five_y2 = 280
                                                    elif six_y2 == w and six_x2 == z:
                                                        if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                'six' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            six_x2 = 360
                                                            six_y2 = 280
                                                    elif seven_y2 == w and seven_x2 == z:
                                                        if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                'seven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            seven_x2 = 360
                                                            seven_y2 = 280
                                                    elif eight_y2 == w and eight_x2 == z:
                                                        if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                'eight' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eight_x2 = 360
                                                            eight_y2 = 280
                                                    elif nine_y == w and nine_x == z:
                                                        if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                'nine' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            nine_x = 360
                                                            nine_y = 280
                                                    elif ten_y == w and ten_x == z:
                                                        if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                'ten' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            ten_x = 360
                                                            ten_y = 280
                                                    elif eleven_y == w and eleven_x == z:
                                                        if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                'eleven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eleven_x = 360
                                                            eleven_y = 280
                                                    elif twelve_y == w and twelve_x == z:
                                                        if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                'twelve' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            twelve_x = 360
                                                            twelve_y = 280
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst32[2] = 1
                                                                lst22[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst32[2] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst32[2] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst32[2] = 1
                                                                lst22[0] = 0
                                                        elif y1 == 150:
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst32[2] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst32[2] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst32[2] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst32[2] = 1
                                                                lst12[0] = 0
                                                        elif y4 == 150:
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst32[2] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst32[2] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst32[2] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst32[2] = 1
                                                                lst42[0] = 0
                                                        elif y5 == 150:
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst32[2] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst32[2] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst32[2] = 1
                                                                lst52[1] = 0
                                                            elif lst52[0] == 1:
                                                                w = 330
                                                                lst32[2] = 1
                                                                lst52[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x2 == 360:
                                                    q = 'one'
                                                elif two_x2 == 360:
                                                    q = 'two'
                                                elif three_x2 == 360:
                                                    q = 'three'
                                                elif four_x2 == 360:
                                                    q = 'four'
                                                elif five_x2 == 360:
                                                    q = 'five'
                                                elif six_x2 == 360:
                                                    q = 'six'
                                                elif seven_x2 == 360:
                                                    q = 'seven'
                                                elif eight_x2 == 360:
                                                    q = 'eight'
                                                elif nine_x == 360:
                                                    q = 'nine'
                                                elif ten_x == 360:
                                                    q = 'ten'
                                                elif eleven_x == 360:
                                                    q = 'eleven'
                                                elif twelve_x == 360:
                                                    q = 'twelve'
                                                if y2 == 150:
                                                    z = 260
                                                    if lst22[3] == 1:
                                                        w = 230 - 50
                                                    elif lst22[2] == 1:
                                                        w = 280 - 50
                                                    elif lst22[1] == 1:
                                                        w = 330 - 50
                                                    elif lst22[0] == 1:
                                                        w = 380 - 50
                                                elif y1 == 150:
                                                    z = 160
                                                    if lst12[3] == 1:
                                                        w = 230 - 50
                                                    elif lst12[2] == 1:
                                                        w = 280 - 50
                                                    elif lst12[1] == 1:
                                                        w = 330 - 50
                                                    elif lst12[0] == 1:
                                                        w = 380 - 50
                                                elif y4 == 150:
                                                    z = 460
                                                    if lst42[3] == 1:
                                                        w = 230 - 50
                                                    elif lst42[2] == 1:
                                                        w = 280 - 50
                                                    elif lst42[1] == 1:
                                                        w = 330 - 50
                                                    elif lst42[0] == 1:
                                                        w = 380 - 50
                                                elif y5 == 150:
                                                    z = 560
                                                    if lst52[3] == 1:
                                                        w = 230 - 50
                                                    elif lst52[2] == 1:
                                                        w = 280 - 50
                                                    elif lst52[1] == 1:
                                                        w = 330 - 50
                                                    elif lst52[0] == 1:
                                                        w = 380 - 50
                                                q2 = 0
                                                if one_y2 == w and one_x2 == z:
                                                    if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                            'one' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        one_x2 = 360
                                                        one_y2 = 230
                                                elif two_y2 == w and two_x2 == z:
                                                    if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                            'two' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        two_x2 = 360
                                                        two_y2 = 230
                                                elif three_y2 == w and three_x2 == z:
                                                    if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                            'three' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        three_x2 = 360
                                                        three_y2 = 230
                                                elif four_y2 == w and four_x2 == z:
                                                    if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                            'four' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        four_x2 = 360
                                                        four_y2 = 230
                                                elif five_y2 == w and five_x2 == z:
                                                    if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                            'five' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        five_x2 = 360
                                                        five_y2 = 230
                                                elif six_y2 == w and six_x2 == z:
                                                    if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                            'six' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        six_x2 = 360
                                                        six_y2 = 230
                                                elif seven_y2 == w and seven_x2 == z:
                                                    if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                            'seven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        seven_x2 = 360
                                                        seven_y2 = 230
                                                elif eight_y2 == w and eight_x2 == z:
                                                    if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                            'eight' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eight_x2 = 360
                                                        eight_y2 = 230
                                                elif nine_y == w and nine_x == z:
                                                    if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                            'nine' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        nine_x = 360
                                                        nine_y = 230
                                                elif ten_y == w and ten_x == z:
                                                    if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                            'ten' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        ten_x = 360
                                                        ten_y = 230
                                                elif eleven_y == w and eleven_x == z:
                                                    if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                            'eleven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eleven_x = 360
                                                        eleven_y = 230
                                                elif twelve_y == w and twelve_x == z:
                                                    if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                            'twelve' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        twelve_x = 360
                                                        twelve_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst22[3] == 1:
                                                            w = 180
                                                            lst32[3] = 1
                                                            lst22[3] = 0
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                            lst32[3] = 1
                                                            lst22[2] = 0
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                            lst32[3] = 1
                                                            lst22[1] = 0
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                            lst32[3] = 1
                                                            lst22[0] = 0
                                                    elif y1 == 150:
                                                        if lst12[3] == 1:
                                                            w = 180
                                                            lst32[3] = 1
                                                            lst12[3] = 0
                                                        elif lst12[2] == 1:
                                                            w = 230
                                                            lst32[3] = 1
                                                            lst12[2] = 0
                                                        elif lst12[1] == 1:
                                                            w = 280
                                                            lst32[3] = 1
                                                            lst12[1] = 0
                                                        elif lst12[0] == 1:
                                                            w = 330
                                                            lst32[3] = 1
                                                            lst12[0] = 0
                                                    elif y4 == 150:
                                                        if lst42[3] == 1:
                                                            w = 180
                                                            lst32[3] = 1
                                                            lst42[3] = 0
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                            lst32[3] = 1
                                                            lst42[2] = 0
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                            lst32[3] = 1
                                                            lst42[1] = 0
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                            lst32[3] = 1
                                                            lst42[0] = 0
                                                    elif y5 == 150:
                                                        if lst52[3] == 1:
                                                            w = 180
                                                            lst32[3] = 1
                                                            lst52[3] = 0
                                                        elif lst52[2] == 1:
                                                            w = 230
                                                            lst32[3] = 1
                                                            lst52[2] = 0
                                                        elif lst52[1] == 1:
                                                            w = 280
                                                            lst32[3] = 1
                                                            lst52[1] = 0
                                                        elif lst52[0] == 1:
                                                            w = 330
                                                            lst32[3] = 1
                                                            lst52[0] = 0
                                        else:
                                            lstsup2[2] = 1
                                            sup = 0
                                            for i in lstsup2:
                                                if i == 1:
                                                    sup += 1
                                            if sup == 2:
                                                time2 = int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            -1]).split(
                                                        '.')[0]) + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            1])) * 60 + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            0])) * 360
                                                result = time2 - time
                                                q = result % 60
                                                if q < 10:
                                                    fanction2(2, f'{result // 60}:0{q}')
                                                else:
                                                    fanction2(2, f'{result // 60}:{q}')

                class buttle4(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y4
                        y4 = self.rect.y
                        self.count = 1
                        self.b41 = 0
                        self.b42 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                                five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                                one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2, y4, q
                            self.b41 = 0
                            self.b42 = 0
                            if lst12[3] == 1:
                                if 'one' in lstred2 and one_x2 == 460:
                                    self.b41 += 1
                                if 'one' in lstgreen2 and one_x2 == 460:
                                    self.b42 += 1
                                if 'two' in lstred2 and two_x2 == 460:
                                    self.b41 += 1
                                if 'two' in lstgreen2 and two_x2 == 460:
                                    self.b42 += 1
                                if 'three' in lstred2 and three_x2 == 460:
                                    self.b41 += 1
                                if 'three' in lstgreen2 and three_x2 == 460:
                                    self.b42 += 1
                                if 'four' in lstred2 and four_x2 == 460:
                                    self.b41 += 1
                                if 'four' in lstgreen2 and four_x2 == 460:
                                    self.b42 += 1
                                if 'five' in lstred2 and five_x2 == 460:
                                    self.b41 += 1
                                if 'five' in lstgreen2 and five_x2 == 460:
                                    self.b42 += 1
                                if 'six' in lstred2 and six_x2 == 460:
                                    self.b41 += 1
                                if 'six' in lstgreen2 and six_x2 == 460:
                                    self.b42 += 1
                                if 'seven' in lstred2 and seven_x2 == 460:
                                    self.b41 += 1
                                if 'seven' in lstgreen2 and seven_x2 == 460:
                                    self.b42 += 1
                                if 'eight' in lstred2 and eight_x2 == 460:
                                    self.b41 += 1
                                if 'eight' in lstgreen2 and eight_x2 == 460:
                                    self.b42 += 1
                                if 'nine' in lstred2 and nine_x == 460:
                                    self.b41 += 1
                                if 'nine' in lstgreen2 and nine_x == 460:
                                    self.b42 += 1
                                if 'ten' in lstred2 and ten_x == 460:
                                    self.b41 += 1
                                if 'ten' in lstgreen2 and ten_x == 460:
                                    self.b42 += 1
                                if 'eleven' in lstred2 and eleven_x == 460:
                                    self.b41 += 1
                                if 'eleven' in lstgreen2 and eleven_x == 460:
                                    self.b42 += 1
                                if 'twelve' in lstred2 and twelve_x == 460:
                                    self.b41 += 1
                                if 'twelve' in lstgreen2 and twelve_x == 460:
                                    self.b42 += 1
                            if self.b41 != 4 and self.b42 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y4 -= 50
                                        if one_x2 == 460:
                                            one_y2 -= 50
                                        if two_x2 == 460:
                                            two_y2 -= 50
                                        if three_x2 == 460:
                                            three_y2 -= 50
                                        if four_x2 == 460:
                                            four_y2 -= 50
                                        if five_x2 == 460:
                                            five_y2 -= 50
                                        if six_x2 == 460:
                                            six_y2 -= 50
                                        if seven_x2 == 460:
                                            seven_y2 -= 50
                                        if eight_x2 == 460:
                                            eight_y2 -= 50
                                        if nine_x == 460:
                                            nine_y -= 50
                                        if ten_x == 460:
                                            ten_y -= 50
                                        if eleven_x == 460:
                                            eleven_y -= 50
                                        if twelve_x == 460:
                                            twelve_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y4 += 50
                                        if one_x2 == 460:
                                            one_y2 += 50
                                        if two_x2 == 460:
                                            two_y2 += 50
                                        if three_x2 == 460:
                                            three_y2 += 50
                                        if four_x2 == 460:
                                            four_y2 += 50
                                        if five_x2 == 460:
                                            five_y2 += 50
                                        if six_x2 == 460:
                                            six_y2 += 50
                                        if seven_x2 == 460:
                                            seven_y2 += 50
                                        if eight_x2 == 460:
                                            eight_y2 += 50
                                        if nine_x == 460:
                                            nine_y += 50
                                        if ten_x == 460:
                                            ten_y += 50
                                        if eleven_x == 460:
                                            eleven_y += 50
                                        if twelve_x == 460:
                                            twelve_y += 50
                                        self.count += 1
                                    else:
                                        global y5, y2, y3, y1
                                        if lst42[3] == 0:
                                            if lst42[2] == 0:
                                                if lst42[1] == 0:
                                                    if lst42[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst42[0] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst42[0] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst42[0] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst42[0] = 1
                                                                lst12[0] = 0
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst42[0] = 1
                                                                lst32[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst42[0] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst42[0] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst42[0] = 1
                                                                lst22[0] = 0
                                                        if y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst42[0] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst42[0] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst42[0] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst42[0] = 1
                                                                lst32[0] = 0
                                                        if y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst42[0] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst42[0] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst42[0] = 1
                                                                lst52[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst42[0] = 1
                                                                lst52[0] = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            one_x2 = 460
                                                            one_y2 = 380
                                                        elif two_y2 == w and two_x2 == z:
                                                            two_x2 = 460
                                                            two_y2 = 380
                                                        elif three_y2 == w and three_x2 == z:
                                                            three_x2 = 460
                                                            three_y2 = 380
                                                        elif four_y2 == w and four_x2 == z:
                                                            four_x2 = 460
                                                            four_y2 = 380
                                                        elif five_y2 == w and five_x2 == z:
                                                            five_x2 = 460
                                                            five_y2 = 380
                                                        elif six_y2 == w and six_x2 == z:
                                                            six_x = 460
                                                            six_y = 380
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            seven_x2 = 460
                                                            seven_y2 = 380
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            eight_x2 = 460
                                                            eight_y2 = 380
                                                        elif nine_y == w and nine_x == z:
                                                            nine_x = 460
                                                            nine_y = 380
                                                        elif ten_y == w and ten_x == z:
                                                            ten_x = 460
                                                            ten_y = 380
                                                        elif eleven_y == w and eleven_x == z:
                                                            eleven_x = 460
                                                            eleven_y = 380
                                                        elif twelve_y == w and twelve_x == z:
                                                            twelve_x = 460
                                                            twelve_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x2 == 460:
                                                            q = 'one'
                                                        elif two_x2 == 460:
                                                            q = 'two'
                                                        elif three_x2 == 460:
                                                            q = 'three'
                                                        elif four_x2 == 460:
                                                            q = 'four'
                                                        elif five_x2 == 460:
                                                            q = 'five'
                                                        elif six_x2 == 460:
                                                            q = 'six'
                                                        elif seven_x2 == 460:
                                                            q = 'seven'
                                                        elif eight_x2 == 460:
                                                            q = 'eight'
                                                        elif nine_x == 460:
                                                            q = 'nine'
                                                        elif ten_x == 460:
                                                            q = 'ten'
                                                        elif eleven_x == 460:
                                                            q = 'eleven'
                                                        elif twelve_x == 460:
                                                            q = 'twelve'
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 230 - 50
                                                            elif lst22[2] == 1:
                                                                w = 280 - 50
                                                            elif lst22[1] == 1:
                                                                w = 330 - 50
                                                            elif lst22[0] == 1:
                                                                w = 380 - 50
                                                        elif y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 230 - 50
                                                            elif lst12[2] == 1:
                                                                w = 280 - 50
                                                            elif lst12[1] == 1:
                                                                w = 330 - 50
                                                            elif lst12[0] == 1:
                                                                w = 380 - 50
                                                        elif y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 230 - 50
                                                            elif lst32[2] == 1:
                                                                w = 280 - 50
                                                            elif lst32[1] == 1:
                                                                w = 330 - 50
                                                            elif lst32[0] == 1:
                                                                w = 380 - 50
                                                        elif y5 == 150:
                                                            z = 560
                                                            if lst52[3] == 1:
                                                                w = 230 - 50
                                                            elif lst52[2] == 1:
                                                                w = 280 - 50
                                                            elif lst52[1] == 1:
                                                                w = 330 - 50
                                                            elif lst52[0] == 1:
                                                                w = 380 - 50
                                                        q2 = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                    'one' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                one_x2 = 460
                                                                one_y2 = 330
                                                        elif two_y2 == w and two_x2 == z:
                                                            if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                    'two' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                two_x2 = 460
                                                                two_y2 = 330
                                                        elif three_y2 == w and three_x2 == z:
                                                            if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                    'three' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                three_x2 = 460
                                                                three_y2 = 330
                                                        elif four_y2 == w and four_x2 == z:
                                                            if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                    'four' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                four_x2 = 460
                                                                four_y2 = 330
                                                        elif five_y2 == w and five_x2 == z:
                                                            if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                    'five' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                five_x2 = 460
                                                                five_y2 = 330
                                                        elif six_y2 == w and six_x2 == z:
                                                            if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                    'six' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                six_x2 = 460
                                                                six_y2 = 330
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                    'seven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                seven_x2 = 460
                                                                seven_y2 = 330
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                    'eight' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eight_x2 = 460
                                                                eight_y2 = 330
                                                        elif nine_y == w and nine_x == z:
                                                            if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                    'nine' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                nine_x = 460
                                                                nine_y = 330
                                                        elif ten_y == w and ten_x == z:
                                                            if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                    'ten' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                ten_x = 460
                                                                ten_y = 330
                                                        elif eleven_y == w and eleven_x == z:
                                                            if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                    'eleven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eleven_x = 460
                                                                eleven_y = 330
                                                        elif twelve_y == w and twelve_x == z:
                                                            if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                    'twelve' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                twelve_x = 460
                                                                twelve_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst22[3] == 1:
                                                                    w = 180
                                                                    lst42[1] = 1
                                                                    lst22[3] = 0
                                                                elif lst22[2] == 1:
                                                                    w = 230
                                                                    lst42[1] = 1
                                                                    lst22[2] = 0
                                                                elif lst22[1] == 1:
                                                                    w = 280
                                                                    lst42[1] = 1
                                                                    lst22[1] = 0
                                                                elif lst22[0] == 1:
                                                                    w = 330
                                                                    lst42[1] = 1
                                                                    lst22[0] = 0
                                                            elif y1 == 150:
                                                                if lst12[3] == 1:
                                                                    w = 180
                                                                    lst42[1] = 1
                                                                    lst12[3] = 0
                                                                elif lst12[2] == 1:
                                                                    w = 230
                                                                    lst42[1] = 1
                                                                    lst12[2] = 0
                                                                elif lst12[1] == 1:
                                                                    w = 280
                                                                    lst42[1] = 1
                                                                    lst12[1] = 0
                                                                elif lst12[0] == 1:
                                                                    w = 330
                                                                    lst42[1] = 1
                                                                    lst12[0] = 0
                                                            elif y3 == 150:
                                                                if lst32[3] == 1:
                                                                    w = 180
                                                                    lst42[1] = 1
                                                                    lst32[3] = 0
                                                                elif lst32[2] == 1:
                                                                    w = 230
                                                                    lst42[1] = 1
                                                                    lst32[2] = 0
                                                                elif lst32[1] == 1:
                                                                    w = 280
                                                                    lst42[1] = 1
                                                                    lst32[1] = 0
                                                                elif lst32[0] == 1:
                                                                    w = 330
                                                                    lst42[1] = 1
                                                                    lst32[0] = 0
                                                            elif y5 == 150:
                                                                if lst52[3] == 1:
                                                                    w = 180
                                                                    lst42[1] = 1
                                                                    lst52[3] = 0
                                                                elif lst52[2] == 1:
                                                                    w = 230
                                                                    lst42[1] = 1
                                                                    lst52[2] = 0
                                                                elif lst52[1] == 1:
                                                                    w = 280
                                                                    lst42[1] = 1
                                                                    lst52[1] = 0
                                                                elif lst52[0] == 1:
                                                                    w = 330
                                                                    lst42[1] = 1
                                                                    lst52[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x2 == 460:
                                                        q = 'one'
                                                    elif two_x2 == 460:
                                                        q = 'two'
                                                    elif three_x2 == 460:
                                                        q = 'three'
                                                    elif four_x2 == 460:
                                                        q = 'four'
                                                    elif five_x2 == 460:
                                                        q = 'five'
                                                    elif six_x2 == 460:
                                                        q = 'six'
                                                    elif seven_x2 == 460:
                                                        q = 'seven'
                                                    elif eight_x2 == 460:
                                                        q = 'eight'
                                                    elif nine_x == 460:
                                                        q = 'nine'
                                                    elif ten_x == 460:
                                                        q = 'ten'
                                                    elif eleven_x == 460:
                                                        q = 'eleven'
                                                    elif twelve_x == 460:
                                                        q = 'twelve'
                                                    if y2 == 150:
                                                        z = 260
                                                        if lst22[3] == 1:
                                                            w = 230 - 50
                                                        elif lst22[2] == 1:
                                                            w = 230 - 50
                                                        elif lst22[1] == 1:
                                                            w = 280 - 50
                                                        elif lst22[0] == 1:
                                                            w = 380 - 50
                                                    elif y1 == 150:
                                                        z = 160
                                                        if lst12[3] == 1:
                                                            w = 230 - 50
                                                        elif lst12[2] == 1:
                                                            w = 280 - 50
                                                        elif lst12[1] == 1:
                                                            w = 330 - 50
                                                        elif lst12[0] == 1:
                                                            w = 380 - 50
                                                    elif y3 == 150:
                                                        z = 360
                                                        if lst32[3] == 1:
                                                            w = 230 - 50
                                                        elif lst32[2] == 1:
                                                            w = 280 - 50
                                                        elif lst32[1] == 1:
                                                            w = 330 - 50
                                                        elif lst32[0] == 1:
                                                            w = 380 - 50
                                                    elif y5 == 150:
                                                        z = 560
                                                        if lst52[3] == 1:
                                                            w = 230 - 50
                                                        elif lst52[2] == 1:
                                                            w = 280 - 50
                                                        elif lst52[1] == 1:
                                                            w = 330 - 50
                                                        elif lst52[0] == 1:
                                                            w = 380 - 50
                                                    q2 = 0
                                                    if one_y2 == w and one_x2 == z:
                                                        if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                'one' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            one_x2 = 460
                                                            one_y2 = 280
                                                    elif two_y2 == w and two_x2 == z:
                                                        if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                'two' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            two_x2 = 460
                                                            two_y2 = 280
                                                    elif three_y2 == w and three_x2 == z:
                                                        if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                'three' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            three_x2 = 460
                                                            three_y2 = 280
                                                    elif four_y2 == w and four_x2 == z:
                                                        if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                'four' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            four_x2 = 460
                                                            four_y2 = 280
                                                    elif five_y2 == w and five_x2 == z:
                                                        if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                'five' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            five_x2 = 460
                                                            five_y2 = 280
                                                    elif six_y2 == w and six_x2 == z:
                                                        if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                'six' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            six_x2 = 460
                                                            six_y2 = 280
                                                    elif seven_y2 == w and seven_x2 == z:
                                                        if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                'seven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            seven_x2 = 460
                                                            seven_y2 = 280
                                                    elif eight_y2 == w and eight_x2 == z:
                                                        if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                'eight' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eight_x2 = 460
                                                            eight_y2 = 280
                                                    elif nine_y == w and nine_x == z:
                                                        if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                'nine' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            nine_x = 460
                                                            nine_y = 280
                                                    elif ten_y == w and ten_x == z:
                                                        if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                'ten' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            ten_x = 460
                                                            ten_y = 280
                                                    elif eleven_y == w and eleven_x == z:
                                                        if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                'eleven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eleven_x = 460
                                                            eleven_y = 280
                                                    elif twelve_y == w and twelve_x == z:
                                                        if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                'twelve' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            twelve_x = 460
                                                            twelve_y = 330
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst42[2] = 1
                                                                lst22[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst42[2] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst42[2] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst42[2] = 1
                                                                lst22[0] = 0
                                                        elif y1 == 150:
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst42[2] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst42[2] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst42[2] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst42[2] = 1
                                                                lst12[0] = 0
                                                        elif y3 == 150:
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst42[2] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst42[2] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst42[2] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst42[2] = 1
                                                                lst32[0] = 0
                                                        elif y5 == 150:
                                                            if lst52[3] == 1:
                                                                w = 180
                                                                lst42[2] = 1
                                                                lst52[3] = 0
                                                            elif lst52[2] == 1:
                                                                w = 230
                                                                lst42[2] = 1
                                                                lst52[2] = 0
                                                            elif lst52[1] == 1:
                                                                w = 280
                                                                lst42[2] = 1
                                                                lst52[1] = 0
                                                            elif lst52[0] == 1:
                                                                w = 330
                                                                lst42[2] = 1
                                                                lst52[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x2 == 460:
                                                    q = 'one'
                                                elif two_x2 == 460:
                                                    q = 'two'
                                                elif three_x2 == 460:
                                                    q = 'three'
                                                elif four_x2 == 460:
                                                    q = 'four'
                                                elif five_x2 == 460:
                                                    q = 'five'
                                                elif six_x2 == 460:
                                                    q = 'six'
                                                elif seven_x2 == 460:
                                                    q = 'seven'
                                                elif eight_x2 == 460:
                                                    q = 'eight'
                                                elif nine_x == 460:
                                                    q = 'nine'
                                                elif ten_x == 460:
                                                    q = 'ten'
                                                elif eleven_x == 460:
                                                    q = 'eleven'
                                                elif twelve_x == 460:
                                                    q = 'twelve'
                                                if y2 == 150:
                                                    z = 260
                                                    if lst22[3] == 1:
                                                        w = 180
                                                    elif lst22[2] == 1:
                                                        w = 230
                                                    elif lst22[1] == 1:
                                                        w = 280
                                                    elif lst22[0] == 1:
                                                        w = 330
                                                elif y1 == 150:
                                                    z = 160
                                                    if lst12[3] == 1:
                                                        w = 180
                                                    elif lst12[2] == 1:
                                                        w = 230
                                                    elif lst12[1] == 1:
                                                        w = 280
                                                    elif lst12[0] == 1:
                                                        w = 330
                                                elif y3 == 150:
                                                    z = 360
                                                    if lst32[3] == 1:
                                                        w = 180
                                                    elif lst32[2] == 1:
                                                        w = 230
                                                    elif lst32[1] == 1:
                                                        w = 280
                                                    elif lst32[0] == 1:
                                                        w = 330
                                                elif y5 == 150:
                                                    z = 560
                                                    if lst52[3] == 1:
                                                        w = 180
                                                    elif lst52[2] == 1:
                                                        w = 230
                                                    elif lst52[1] == 1:
                                                        w = 280
                                                    elif lst52[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_y2 == w and one_x2 == z:
                                                    if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                            'one' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        one_x2 = 460
                                                        one_y2 = 230
                                                elif two_y2 == w and two_x2 == z:
                                                    if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                            'two' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        two_x2 = 460
                                                        two_y2 = 230
                                                elif three_y2 == w and three_x2 == z:
                                                    if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                            'three' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        three_x2 = 460
                                                        three_y2 = 230
                                                elif four_y2 == w and four_x2 == z:
                                                    if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                            'four' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        four_x2 = 460
                                                        four_y2 = 230
                                                elif five_y2 == w and five_x2 == z:
                                                    if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                            'five' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        five_x2 = 460
                                                        five_y2 = 230
                                                elif six_y2 == w and six_x2 == z:
                                                    if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                            'six' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        six_x2 = 460
                                                        six_y2 = 230
                                                elif seven_y2 == w and seven_x2 == z:
                                                    if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                            'seven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        seven_x2 = 460
                                                        seven_y2 = 230
                                                elif eight_y2 == w and eight_x2 == z:
                                                    if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                            'eight' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eight_x2 = 460
                                                        eight_y2 = 230
                                                elif nine_y == w and nine_x == z:
                                                    if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                            'nine' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        nine_x = 460
                                                        nine_y = 230
                                                elif ten_y == w and ten_x == z:
                                                    if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                            'ten' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        ten_x = 460
                                                        ten_y = 230
                                                elif eleven_y == w and eleven_x == z:
                                                    if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                            'eleven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eleven_x = 460
                                                        eleven_y = 230
                                                elif twelve_y == w and twelve_x == z:
                                                    if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                            'twelve' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        twelve_x = 460
                                                        twelve_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst22[3] == 1:
                                                            w = 180
                                                            lst42[3] = 1
                                                            lst22[3] = 0
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                            lst42[3] = 1
                                                            lst22[2] = 0
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                            lst42[3] = 1
                                                            lst22[1] = 0
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                            lst42[3] = 1
                                                            lst22[0] = 0
                                                    elif y1 == 150:
                                                        if lst12[3] == 1:
                                                            w = 180
                                                            lst42[3] = 1
                                                            lst12[3] = 0
                                                        elif lst12[2] == 1:
                                                            w = 230
                                                            lst42[3] = 1
                                                            lst12[2] = 0
                                                        elif lst12[1] == 1:
                                                            w = 280
                                                            lst42[3] = 1
                                                            lst12[1] = 0
                                                        elif lst12[0] == 1:
                                                            w = 330
                                                            lst42[3] = 1
                                                            lst12[0] = 0
                                                    elif y3 == 150:
                                                        if lst32[3] == 1:
                                                            w = 180
                                                            lst42[3] = 1
                                                            lst32[3] = 0
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                            lst42[3] = 1
                                                            lst32[2] = 0
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                            lst42[3] = 1
                                                            lst32[1] = 0
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                            lst42[3] = 1
                                                            lst32[0] = 0
                                                    elif y5 == 150:
                                                        if lst52[3] == 1:
                                                            w = 180
                                                            lst42[3] = 1
                                                            lst52[3] = 0
                                                        elif lst52[2] == 1:
                                                            w = 230
                                                            lst42[3] = 1
                                                            lst52[2] = 0
                                                        elif lst52[1] == 1:
                                                            w = 280
                                                            lst42[3] = 1
                                                            lst52[1] = 0
                                                        elif lst52[0] == 1:
                                                            w = 330
                                                            lst42[3] = 1
                                                            lst52[0] = 0
                                        else:
                                            lstsup2[2] = 1
                                            sup = 0
                                            for i in lstsup2:
                                                if i == 1:
                                                    sup += 1
                                            if sup == 2:
                                                time2 = int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            -1]).split(
                                                        '.')[0]) + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            1])) * 60 + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            0])) * 360
                                                result = time2 - time
                                                q = result % 60
                                                if q < 10:
                                                    fanction2(2, f'{result // 60}:0{q}')
                                                else:
                                                    fanction2(2, f'{result // 60}:{q}')

                class buttle5(pygame.sprite.Sprite):
                    if os.name == 'posix':
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.5, 0.5)
                    else:
                        image = pygame.transform.rotozoom(load_image("buttle.jpg"), 0.53, 0.52)

                    def __init__(self, group, x, y):
                        super().__init__(group)
                        self.image = buttle1.image
                        self.rect = self.image.get_rect()
                        self.rect.x = x
                        self.rect.y = y
                        global y5
                        y5 = self.rect.y
                        self.count = 1
                        self.b51 = 0
                        self.b52 = 0

                    def update(self, *args):
                        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                                self.rect.collidepoint(args[0].pos):
                            global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                                five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                                one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2, y5, q
                            self.b51 = 0
                            self.b52 = 0
                            if lst12[3] == 1:
                                if 'one' in lstred2 and one_x2 == 560:
                                    self.b51 += 1
                                if 'one' in lstgreen2 and one_x2 == 560:
                                    self.b52 += 1
                                if 'two' in lstred2 and two_x2 == 560:
                                    self.b51 += 1
                                if 'two' in lstgreen2 and two_x2 == 560:
                                    self.b52 += 1
                                if 'three' in lstred2 and three_x2 == 560:
                                    self.b51 += 1
                                if 'three' in lstgreen2 and three_x2 == 560:
                                    self.b52 += 1
                                if 'four' in lstred2 and four_x2 == 560:
                                    self.b51 += 1
                                if 'four' in lstgreen2 and four_x2 == 560:
                                    self.b52 += 1
                                if 'five' in lstred2 and five_x2 == 560:
                                    self.b51 += 1
                                if 'five' in lstgreen2 and five_x2 == 560:
                                    self.b52 += 1
                                if 'six' in lstred2 and six_x2 == 560:
                                    self.b51 += 1
                                if 'six' in lstgreen2 and six_x2 == 560:
                                    self.b52 += 1
                                if 'seven' in lstred2 and seven_x2 == 560:
                                    self.b51 += 1
                                if 'seven' in lstgreen2 and seven_x2 == 560:
                                    self.b52 += 1
                                if 'eight' in lstred2 and eight_x2 == 560:
                                    self.b51 += 1
                                if 'eight' in lstgreen2 and eight_x2 == 560:
                                    self.b52 += 1
                                if 'nine' in lstred2 and nine_x == 560:
                                    self.b51 += 1
                                if 'nine' in lstgreen2 and nine_x == 560:
                                    self.b52 += 1
                                if 'ten' in lstred2 and ten_x == 560:
                                    self.b51 += 1
                                if 'ten' in lstgreen2 and ten_x == 560:
                                    self.b52 += 1
                                if 'eleven' in lstred2 and eleven_x == 560:
                                    self.b51 += 1
                                if 'eleven' in lstgreen2 and eleven_x == 560:
                                    self.b52 += 1
                                if 'twelve' in lstred2 and twelve_x == 560:
                                    self.b51 += 1
                                if 'twelve' in lstgreen2 and twelve_x == 560:
                                    self.b52 += 1
                            if self.b51 != 4 and self.b52 != 4:
                                if q == 0:
                                    if self.count % 2 != 0:
                                        q = 1
                                        self.rect.y -= 50
                                        self.count += 1
                                        y5 -= 50
                                        if one_x2 == 560:
                                            one_y2 -= 50
                                        if two_x2 == 560:
                                            two_y2 -= 50
                                        if three_x2 == 560:
                                            three_y2 -= 50
                                        if four_x2 == 560:
                                            four_y2 -= 50
                                        if five_x2 == 560:
                                            five_y2 -= 50
                                        if six_x2 == 560:
                                            six_y2 -= 50
                                        if seven_x2 == 560:
                                            seven_y2 -= 50
                                        if eight_x2 == 560:
                                            eight_y2 -= 50
                                        if nine_x == 560:
                                            nine_y -= 50
                                        if ten_x == 560:
                                            ten_y -= 50
                                        if eleven_x == 560:
                                            eleven_y -= 50
                                        if twelve_x == 560:
                                            twelve_y -= 50
                                else:
                                    if self.count % 2 == 0:
                                        q = 0
                                        self.rect.y += 50
                                        y5 += 50
                                        if one_x2 == 560:
                                            one_y2 += 50
                                        if two_x2 == 560:
                                            two_y2 += 50
                                        if three_x2 == 560:
                                            three_y2 += 50
                                        if four_x2 == 560:
                                            four_y2 += 50
                                        if five_x2 == 560:
                                            five_y2 += 50
                                        if six_x2 == 560:
                                            six_y2 += 50
                                        if seven_x2 == 560:
                                            seven_y2 += 50
                                        if eight_x2 == 560:
                                            eight_y2 += 50
                                        if nine_x == 560:
                                            nine_y += 50
                                        if ten_x == 560:
                                            ten_y += 50
                                        if eleven_x == 560:
                                            eleven_y += 50
                                        if twelve_x == 560:
                                            twelve_y += 50
                                        self.count += 1
                                    else:
                                        global y4, y2, y3, y1
                                        if lst52[3] == 0:
                                            if lst52[2] == 0:
                                                if lst52[1] == 0:
                                                    if lst52[0] == 0:
                                                        w = 0
                                                        z = 0
                                                        if y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst52[0] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst52[0] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst52[0] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst52[0] = 1
                                                                lst12[0] = 0
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst52[0] = 1
                                                                lst32[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst52[0] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst52[0] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst52[0] = 1
                                                                lst22[0] = 0
                                                        if y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst52[0] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst52[0] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst52[0] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst52[0] = 1
                                                                lst32[0] = 0
                                                        if y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst52[0] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst52[0] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst52[0] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst52[0] = 1
                                                                lst42[0] = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            one_x2 = 560
                                                            one_y2 = 380
                                                        elif two_y2 == w and two_x2 == z:
                                                            two_x2 = 560
                                                            two_y2 = 380
                                                        elif three_y2 == w and three_x2 == z:
                                                            three_x2 = 560
                                                            three_y2 = 380
                                                        elif four_y2 == w and four_x2 == z:
                                                            four_x2 = 560
                                                            four_y2 = 380
                                                        elif five_y2 == w and five_x2 == z:
                                                            five_x2 = 560
                                                            five_y2 = 380
                                                        elif six_y2 == w and six_x2 == z:
                                                            six_x = 560
                                                            six_y = 380
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            seven_x2 = 560
                                                            seven_y2 = 380
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            eight_x2 = 560
                                                            eight_y2 = 380
                                                        elif nine_y == w and nine_x == z:
                                                            nine_x = 560
                                                            nine_y = 380
                                                        elif ten_y == w and ten_x == z:
                                                            ten_x = 560
                                                            ten_y = 380
                                                        elif eleven_y == w and eleven_x == z:
                                                            eleven_x = 560
                                                            eleven_y = 380
                                                        elif twelve_y == w and twelve_x == z:
                                                            twelve_x = 560
                                                            twelve_y = 380
                                                    else:
                                                        w = 0
                                                        z = 0
                                                        q = ''
                                                        if one_x2 == 560:
                                                            q = 'one'
                                                        elif two_x2 == 560:
                                                            q = 'two'
                                                        elif three_x2 == 560:
                                                            q = 'three'
                                                        elif four_x2 == 560:
                                                            q = 'four'
                                                        elif five_x2 == 560:
                                                            q = 'five'
                                                        elif six_x2 == 560:
                                                            q = 'six'
                                                        elif seven_x2 == 560:
                                                            q = 'seven'
                                                        elif eight_x2 == 560:
                                                            q = 'eight'
                                                        elif nine_x == 560:
                                                            q = 'nine'
                                                        elif ten_x == 560:
                                                            q = 'ten'
                                                        elif eleven_x == 560:
                                                            q = 'eleven'
                                                        elif twelve_x == 560:
                                                            q = 'twelve'
                                                        if y2 == 150:
                                                            z = 260
                                                            if lst22[3] == 1:
                                                                w = 180
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                        elif y1 == 150:
                                                            z = 160
                                                            if lst12[3] == 1:
                                                                w = 180
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                        elif y3 == 150:
                                                            z = 360
                                                            if lst32[3] == 1:
                                                                w = 180
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                        elif y4 == 150:
                                                            z = 460
                                                            if lst42[3] == 1:
                                                                w = 180
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                        q2 = 0
                                                        if one_y2 == w and one_x2 == z:
                                                            if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                    'one' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                one_x2 = 560
                                                                one_y2 = 330
                                                        elif two_y2 == w and two_x2 == z:
                                                            if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                    'two' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                two_x2 = 560
                                                                two_y2 = 330
                                                        elif three_y2 == w and three_x2 == z:
                                                            if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                    'three' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                three_x2 = 560
                                                                three_y2 = 330
                                                        elif four_y2 == w and four_x2 == z:
                                                            if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                    'four' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                four_x2 = 560
                                                                four_y2 = 330
                                                        elif five_y2 == w and five_x2 == z:
                                                            if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                    'five' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                five_x2 = 560
                                                                five_y2 = 330
                                                        elif six_y2 == w and six_x2 == z:
                                                            if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                    'six' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                six_x2 = 560
                                                                six_y2 = 330
                                                        elif seven_y2 == w and seven_x2 == z:
                                                            if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                    'seven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                seven_x2 = 560
                                                                seven_y2 = 330
                                                        elif eight_y2 == w and eight_x2 == z:
                                                            if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                    'eight' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eight_x2 = 560
                                                                eight_y2 = 330
                                                        elif nine_y == w and nine_x == z:
                                                            if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                    'nine' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                nine_x = 560
                                                                nine_y = 330
                                                        elif ten_y == w and ten_x == z:
                                                            if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                    'ten' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                ten_x = 560
                                                                ten_y = 330
                                                        elif eleven_y == w and eleven_x == z:
                                                            if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                    'eleven' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                eleven_x = 560
                                                                eleven_y = 330
                                                        elif twelve_y == w and twelve_x == z:
                                                            if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                    'twelve' in lstblue2 and q in lstblue2:
                                                                q2 = 1
                                                                twelve_x = 560
                                                                twelve_y = 330
                                                        if q2 == 1:
                                                            if y2 == 150:
                                                                if lst22[3] == 1:
                                                                    w = 180
                                                                    lst52[1] = 1
                                                                    lst22[3] = 0
                                                                elif lst22[2] == 1:
                                                                    w = 230
                                                                    lst52[1] = 1
                                                                    lst22[2] = 0
                                                                elif lst22[1] == 1:
                                                                    w = 280
                                                                    lst52[1] = 1
                                                                    lst22[1] = 0
                                                                elif lst22[0] == 1:
                                                                    w = 330
                                                                    lst52[1] = 1
                                                                    lst22[0] = 0
                                                            elif y1 == 150:
                                                                if lst12[3] == 1:
                                                                    w = 180
                                                                    lst52[1] = 1
                                                                    lst12[3] = 0
                                                                elif lst12[2] == 1:
                                                                    w = 230
                                                                    lst52[1] = 1
                                                                    lst12[2] = 0
                                                                elif lst12[1] == 1:
                                                                    w = 280
                                                                    lst52[1] = 1
                                                                    lst12[1] = 0
                                                                elif lst12[0] == 1:
                                                                    w = 330
                                                                    lst52[1] = 1
                                                                    lst12[0] = 0
                                                            elif y3 == 150:
                                                                if lst32[3] == 1:
                                                                    w = 180
                                                                    lst52[1] = 1
                                                                    lst32[3] = 0
                                                                elif lst32[2] == 1:
                                                                    w = 230
                                                                    lst52[1] = 1
                                                                    lst32[2] = 0
                                                                elif lst32[1] == 1:
                                                                    w = 280
                                                                    lst52[1] = 1
                                                                    lst32[1] = 0
                                                                elif lst32[0] == 1:
                                                                    w = 330
                                                                    lst52[1] = 1
                                                                    lst32[0] = 0
                                                            elif y4 == 150:
                                                                if lst42[3] == 1:
                                                                    w = 180
                                                                    lst52[1] = 1
                                                                    lst42[3] = 0
                                                                elif lst42[2] == 1:
                                                                    w = 230
                                                                    lst52[1] = 1
                                                                    lst42[2] = 0
                                                                elif lst42[1] == 1:
                                                                    w = 280
                                                                    lst52[1] = 1
                                                                    lst42[1] = 0
                                                                elif lst42[0] == 1:
                                                                    w = 330
                                                                    lst52[1] = 1
                                                                    lst42[0] = 0
                                                else:
                                                    w = 0
                                                    z = 0
                                                    q = ''
                                                    if one_x2 == 560:
                                                        q = 'one'
                                                    elif two_x2 == 560:
                                                        q = 'two'
                                                    elif three_x2 == 560:
                                                        q = 'three'
                                                    elif four_x2 == 560:
                                                        q = 'four'
                                                    elif five_x2 == 560:
                                                        q = 'five'
                                                    elif six_x2 == 560:
                                                        q = 'six'
                                                    elif seven_x2 == 560:
                                                        q = 'seven'
                                                    elif eight_x2 == 560:
                                                        q = 'eight'
                                                    elif nine_x == 560:
                                                        q = 'nine'
                                                    elif ten_x == 560:
                                                        q = 'ten'
                                                    elif eleven_x == 560:
                                                        q = 'eleven'
                                                    elif twelve_x == 560:
                                                        q = 'twelve'
                                                    if y2 == 150:
                                                        z = 260
                                                        if lst22[3] == 1:
                                                            w = 180
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                    elif y1 == 150:
                                                        z = 160
                                                        if lst12[3] == 1:
                                                            w = 180
                                                        elif lst12[2] == 1:
                                                            w = 230
                                                        elif lst12[1] == 1:
                                                            w = 280
                                                        elif lst12[0] == 1:
                                                            w = 330
                                                    elif y3 == 150:
                                                        z = 360
                                                        if lst32[3] == 1:
                                                            w = 180
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                    elif y4 == 150:
                                                        z = 460
                                                        if lst42[3] == 1:
                                                            w = 180
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                    q2 = 0
                                                    if one_y2 == w and one_x2 == z:
                                                        if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                                'one' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            one_x2 = 560
                                                            one_y2 = 280
                                                    elif two_y2 == w and two_x2 == z:
                                                        if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                                'two' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            two_x2 = 560
                                                            two_y2 = 280
                                                    elif three_y2 == w and three_x2 == z:
                                                        if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                                'three' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            three_x2 = 560
                                                            three_y2 = 280
                                                    elif four_y2 == w and four_x2 == z:
                                                        if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                                'four' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            four_x2 = 560
                                                            four_y2 = 280
                                                    elif five_y2 == w and five_x2 == z:
                                                        if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                                'five' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            five_x2 = 560
                                                            five_y2 = 280
                                                    elif six_y2 == w and six_x2 == z:
                                                        if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                                'six' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            six_x2 = 560
                                                            six_y2 = 280
                                                    elif seven_y2 == w and seven_x2 == z:
                                                        if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                                'seven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            seven_x2 = 560
                                                            seven_y2 = 280
                                                    elif eight_y2 == w and eight_x2 == z:
                                                        if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                                'eight' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eight_x2 = 560
                                                            eight_y2 = 280
                                                    elif nine_y == w and nine_x == z:
                                                        if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                                'nine' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            nine_x = 560
                                                            nine_y = 280
                                                    elif ten_y == w and ten_x == z:
                                                        if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                                'ten' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            ten_x = 560
                                                            ten_y = 280
                                                    elif eleven_y == w and eleven_x == z:
                                                        if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                                'eleven' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            eleven_x = 560
                                                            eleven_y = 280
                                                    elif twelve_y == w and twelve_x == z:
                                                        if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                                'twelve' in lstblue2 and q in lstblue2:
                                                            q2 = 1
                                                            twelve_x = 560
                                                            twelve_y = 280
                                                    if q2 == 1:
                                                        if y2 == 150:
                                                            if lst22[3] == 1:
                                                                w = 180
                                                                lst52[2] = 1
                                                                lst22[3] = 0
                                                            elif lst22[2] == 1:
                                                                w = 230
                                                                lst52[2] = 1
                                                                lst22[2] = 0
                                                            elif lst22[1] == 1:
                                                                w = 280
                                                                lst52[2] = 1
                                                                lst22[1] = 0
                                                            elif lst22[0] == 1:
                                                                w = 330
                                                                lst52[2] = 1
                                                                lst22[0] = 0
                                                        elif y1 == 150:
                                                            if lst12[3] == 1:
                                                                w = 180
                                                                lst52[2] = 1
                                                                lst12[3] = 0
                                                            elif lst12[2] == 1:
                                                                w = 230
                                                                lst52[2] = 1
                                                                lst12[2] = 0
                                                            elif lst12[1] == 1:
                                                                w = 280
                                                                lst52[2] = 1
                                                                lst12[1] = 0
                                                            elif lst12[0] == 1:
                                                                w = 330
                                                                lst52[2] = 1
                                                                lst12[0] = 0
                                                        elif y3 == 150:
                                                            if lst32[3] == 1:
                                                                w = 180
                                                                lst52[2] = 1
                                                                lst32[3] = 0
                                                            elif lst32[2] == 1:
                                                                w = 230
                                                                lst52[2] = 1
                                                                lst32[2] = 0
                                                            elif lst32[1] == 1:
                                                                w = 280
                                                                lst52[2] = 1
                                                                lst32[1] = 0
                                                            elif lst32[0] == 1:
                                                                w = 330
                                                                lst52[2] = 1
                                                                lst32[0] = 0
                                                        elif y4 == 150:
                                                            if lst42[3] == 1:
                                                                w = 180
                                                                lst52[2] = 1
                                                                lst42[3] = 0
                                                            elif lst42[2] == 1:
                                                                w = 230
                                                                lst52[2] = 1
                                                                lst42[2] = 0
                                                            elif lst42[1] == 1:
                                                                w = 280
                                                                lst52[2] = 1
                                                                lst42[1] = 0
                                                            elif lst42[0] == 1:
                                                                w = 330
                                                                lst52[2] = 1
                                                                lst42[0] = 0
                                            else:
                                                w = 0
                                                z = 0
                                                q = ''
                                                if one_x2 == 560:
                                                    q = 'one'
                                                elif two_x2 == 560:
                                                    q = 'two'
                                                elif three_x2 == 560:
                                                    q = 'three'
                                                elif four_x2 == 560:
                                                    q = 'four'
                                                elif five_x2 == 560:
                                                    q = 'five'
                                                elif six_x2 == 560:
                                                    q = 'six'
                                                elif seven_x2 == 560:
                                                    q = 'seven'
                                                elif eight_x2 == 560:
                                                    q = 'eight'
                                                elif nine_x == 560:
                                                    q = 'nine'
                                                elif ten_x == 560:
                                                    q = 'ten'
                                                elif eleven_x == 560:
                                                    q = 'eleven'
                                                elif twelve_x == 560:
                                                    q = 'twelve'
                                                if y2 == 150:
                                                    z = 260
                                                    if lst22[3] == 1:
                                                        w = 180
                                                    elif lst22[2] == 1:
                                                        w = 230
                                                    elif lst22[1] == 1:
                                                        w = 280
                                                    elif lst22[0] == 1:
                                                        w = 330
                                                elif y1 == 150:
                                                    z = 160
                                                    if lst12[3] == 1:
                                                        w = 180
                                                    elif lst12[2] == 1:
                                                        w = 230
                                                    elif lst12[1] == 1:
                                                        w = 280
                                                    elif lst12[0] == 1:
                                                        w = 330
                                                elif y3 == 150:
                                                    z = 360
                                                    if lst32[3] == 1:
                                                        w = 180
                                                    elif lst32[2] == 1:
                                                        w = 230
                                                    elif lst32[1] == 1:
                                                        w = 280
                                                    elif lst32[0] == 1:
                                                        w = 330
                                                elif y4 == 150:
                                                    z = 460
                                                    if lst42[3] == 1:
                                                        w = 180
                                                    elif lst42[2] == 1:
                                                        w = 230
                                                    elif lst42[1] == 1:
                                                        w = 280
                                                    elif lst42[0] == 1:
                                                        w = 330
                                                q2 = 0
                                                if one_y2 == w and one_x2 == z:
                                                    if 'one' in lstred2 and q in lstred2 or 'one' in lstgreen2 and q in lstgreen2 or \
                                                            'one' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        one_x2 = 560
                                                        one_y2 = 230
                                                elif two_y2 == w and two_x2 == z:
                                                    if 'two' in lstred2 and q in lstred2 or 'two' in lstgreen2 and q in lstgreen2 or \
                                                            'two' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        two_x2 = 560
                                                        two_y2 = 230
                                                elif three_y2 == w and three_x2 == z:
                                                    if 'three' in lstred2 and q in lstred2 or 'three' in lstgreen2 and q in lstgreen2 or \
                                                            'three' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        three_x2 = 560
                                                        three_y2 = 230
                                                elif four_y2 == w and four_x2 == z:
                                                    if 'four' in lstred2 and q in lstred2 or 'four' in lstgreen2 and q in lstgreen2 or \
                                                            'four' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        four_x2 = 560
                                                        four_y2 = 230
                                                elif five_y2 == w and five_x2 == z:
                                                    if 'five' in lstred2 and q in lstred2 or 'five' in lstgreen2 and q in lstgreen2 or \
                                                            'five' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        five_x2 = 560
                                                        five_y2 = 230
                                                elif six_y2 == w and six_x2 == z:
                                                    if 'six' in lstred2 and q in lstred2 or 'six' in lstgreen2 and q in lstgreen2 or \
                                                            'six' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        six_x2 = 560
                                                        six_y2 = 230
                                                elif seven_y2 == w and seven_x2 == z:
                                                    if 'seven' in lstred2 and q in lstred2 or 'seven' in lstgreen2 and q in lstgreen2 or \
                                                            'seven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        seven_x2 = 560
                                                        seven_y2 = 230
                                                elif eight_y2 == w and eight_x2 == z:
                                                    if 'eight' in lstred2 and q in lstred2 or 'eight' in lstgreen2 and q in lstgreen2 or \
                                                            'eight' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eight_x2 = 560
                                                        eight_y2 = 230
                                                elif nine_y == w and nine_x == z:
                                                    if 'nine' in lstred2 and q in lstred2 or 'nine' in lstgreen2 and q in lstgreen2 or \
                                                            'nine' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        nine_x = 560
                                                        nine_y = 230
                                                elif ten_y == w and ten_x == z:
                                                    if 'ten' in lstred2 and q in lstred2 or 'ten' in lstgreen2 and q in lstgreen2 or \
                                                            'ten' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        ten_x = 560
                                                        ten_y = 230
                                                elif eleven_y == w and eleven_x == z:
                                                    if 'eleven' in lstred2 and q in lstred2 or 'eleven' in lstgreen2 and q in lstgreen2 or \
                                                            'eleven' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        eleven_x = 560
                                                        eleven_y = 230
                                                elif twelve_y == w and twelve_x == z:
                                                    if 'twelve' in lstred2 and q in lstred2 or 'twelve' in lstgreen2 and q in lstgreen2 or \
                                                            'twelve' in lstblue2 and q in lstblue2:
                                                        q2 = 1
                                                        twelve_x = 560
                                                        twelve_y = 230
                                                if q2 == 1:
                                                    if y2 == 150:
                                                        if lst22[3] == 1:
                                                            w = 180
                                                            lst52[3] = 1
                                                            lst22[3] = 0
                                                        elif lst22[2] == 1:
                                                            w = 230
                                                            lst52[3] = 1
                                                            lst22[2] = 0
                                                        elif lst22[1] == 1:
                                                            w = 280
                                                            lst52[3] = 1
                                                            lst22[1] = 0
                                                        elif lst22[0] == 1:
                                                            w = 330
                                                            lst52[3] = 1
                                                            lst22[0] = 0
                                                    elif y1 == 150:
                                                        if lst12[3] == 1:
                                                            w = 180
                                                            lst52[3] = 1
                                                            lst12[3] = 0
                                                        elif lst12[2] == 1:
                                                            w = 230
                                                            lst52[3] = 1
                                                            lst12[2] = 0
                                                        elif lst12[1] == 1:
                                                            w = 280
                                                            lst52[3] = 1
                                                            lst12[1] = 0
                                                        elif lst12[0] == 1:
                                                            w = 330
                                                            lst52[3] = 1
                                                            lst12[0] = 0
                                                    elif y3 == 150:
                                                        if lst32[3] == 1:
                                                            w = 180
                                                            lst52[3] = 1
                                                            lst32[3] = 0
                                                        elif lst32[2] == 1:
                                                            w = 230
                                                            lst52[3] = 1
                                                            lst32[2] = 0
                                                        elif lst32[1] == 1:
                                                            w = 280
                                                            lst52[3] = 1
                                                            lst32[1] = 0
                                                        elif lst32[0] == 1:
                                                            w = 330
                                                            lst52[3] = 1
                                                            lst32[0] = 0
                                                    elif y4 == 150:
                                                        if lst42[3] == 1:
                                                            w = 180
                                                            lst52[3] = 1
                                                            lst42[3] = 0
                                                        elif lst42[2] == 1:
                                                            w = 230
                                                            lst52[3] = 1
                                                            lst42[2] = 0
                                                        elif lst42[1] == 1:
                                                            w = 280
                                                            lst52[3] = 1
                                                            lst42[1] = 0
                                                        elif lst42[0] == 1:
                                                            w = 330
                                                            lst52[3] = 1
                                                            lst42[0] = 0
                                        else:
                                            lstsup2[2] = 1
                                            sup = 0
                                            for i in lstsup2:
                                                if i == 1:
                                                    sup += 1
                                            if sup == 2:
                                                time2 = int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            -1]).split(
                                                        '.')[0]) + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            1])) * 60 + int(
                                                    str(str(dt.datetime.now().time()).split(':')[
                                                            0])) * 360
                                                result = time2 - time
                                                q = result % 60
                                                if q < 10:
                                                    fanction2(2, f'{result // 60}:0{q}')
                                                else:
                                                    fanction2(2, f'{result // 60}:{q}')

                global nine_y, nine_x, ten_y, ten_x, eleven_y, eleven_x, twelve_x, twelve_y, \
                    five_y2, five_x2, six_y2, six_x2, seven_y2, seven_x2, eight_x2, eight_y2, \
                    one_y2, one_x2, two_y2, two_x2, three_y2, three_x2, four_x2, four_y2
                running = True
                fps = 60
                rect_sprite = pygame.sprite.Group()
                all_sprites = pygame.sprite.Group()
                buttle1(all_sprites, 150, 200)
                buttle2(all_sprites, 250, 200)
                buttle3(all_sprites, 350, 200)
                buttle4(all_sprites, 450, 200)
                buttle5(all_sprites, 550, 200)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('one')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('one')
                else:
                    color = 'green'
                    lstgreen2.append('one')
                lst222.remove(num)
                one = Player(rect_sprite, one_x2 + 30, one_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('two')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('two')
                else:
                    color = 'green'
                    lstgreen2.append('two')
                lst222.remove(num)
                two = Player(rect_sprite, two_x2 + 30, two_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('three')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('three')
                else:
                    color = 'green'
                    lstgreen2.append('three')
                lst222.remove(num)
                three = Player(rect_sprite, three_x2 + 30, three_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('four')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('four')
                else:
                    color = 'green'
                    lstgreen2.append('four')
                lst222.remove(num)
                four = Player(rect_sprite, four_x2 + 30, four_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('five')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('five')
                else:
                    color = 'green'
                    lstgreen2.append('five')
                lst222.remove(num)
                five = Player(rect_sprite, five_x2 + 30, five_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('six')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('six')
                else:
                    color = 'green'
                    lstgreen2.append('six')
                lst222.remove(num)
                six = Player(rect_sprite, six_x2 + 30, six_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('seven')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('seven')
                else:
                    color = 'green'
                    lstgreen2.append('seven')
                lst222.remove(num)
                seven = Player(rect_sprite, seven_x2 + 30, seven_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('eight')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('eight')
                else:
                    color = 'green'
                    lstgreen2.append('eight')
                lst222.remove(num)
                eight = Player(rect_sprite, eight_x2 + 30, eight_y2 + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('nine')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('nine')
                else:
                    color = 'green'
                    lstgreen2.append('nine')
                lst222.remove(num)
                nine = Player(rect_sprite, nine_x + 30, nine_y + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('ten')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('ten')
                else:
                    color = 'green'
                    lstgreen2.append('ten')
                lst222.remove(num)
                ten = Player(rect_sprite, ten_x + 30, ten_y + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('eleven')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('eleven')
                else:
                    color = 'green'
                    lstgreen2.append('eleven')
                lst222.remove(num)
                eleven = Player(rect_sprite, eleven_x + 30, eleven_y + 25, color)
                num = choice(lst222)
                if num == 0:
                    color = 'red'
                    lstred2.append('twelve')
                elif num == 2:
                    color = 'blue'
                    lstred2.append('twelve')
                else:
                    color = 'green'
                    lstgreen2.append('twelve')
                lst222.remove(num)
                twelve = Player(rect_sprite, twelve_x + 30, twelve_y + 25, color)

                def run():
                    while True:
                        one.q(one_x2 + 29, one_y2 + 25)
                        two.q(two_x2 + 29, two_y2 + 25)
                        three.q(three_x2 + 29, three_y2 + 25)
                        four.q(four_x2 + 29, four_y2 + 25)
                        five.q(five_x2 + 29, five_y2 + 25)
                        six.q(six_x2 + 29, six_y2 + 25)
                        seven.q(seven_x2 + 29, seven_y2 + 25)
                        eight.q(eight_x2 + 29, eight_y2 + 25)
                        nine.q(nine_x + 29, nine_y + 25)
                        ten.q(ten_x + 29, ten_y + 25)
                        eleven.q(eleven_x + 29, eleven_y + 25)
                        twelve.q(twelve_x + 29, twelve_y + 25)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print(lst12)
                                print(lst22)
                                print(lst32)
                                print(lst42)
                                print(lst52)
                                print()
                                all_sprites.update(event)
                        screen.fill((0, 0, 0))
                        all_sprites.draw(screen)
                        rect_sprite.draw(screen)
                        pygame.display.flip()

                def draw():
                    screen.fill("black")
                    all_sprites.update()
                    all_sprites.draw(screen)
                    pygame.display.flip()

                if __name__ == "__main__":
                    run()
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image
            else:
                self.image = self.image

    class Button(pygame.sprite.Sprite):
        def __init__(self, group, x, y, image, fl):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.fl = fl
            self.flag = True

        def flag(self):
            return self.flag

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and self.fl:
                a1.flag = False
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos) and not self.fl:
                a1.flag = 2
            if args and args[0].type == pygame.MOUSEMOTION and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image
            else:
                self.image = self.image

    class FON(pygame.sprite.Sprite):

        def __init__(self, group, x, y, image):
            super().__init__(group)
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    FON(sprite_Button_levels, 0, 0,
        pygame.transform.scale(
            load_image(f"3.jpeg"),
            (600, 400)))
    c = 80
    for i in range(1, 6):
        Button_levels(sprite_Button_levels, c, 100,
                      pygame.transform.scale(load_image(
                          f"3.jpeg"),
                          (70, 70)), i)
        c += 100

    FON(sprite_Button, 0, 0,
        pygame.transform.scale(load_image("3.jpeg"),
                               (700, 500)))
    FON(sprite_Button, 0, 250,
        pygame.transform.scale(load_image("4.jpeg", -1), (1832 // 6, 712 // 6)))
    a2 = Button(sprite_Button, 70, 130,
                pygame.transform.scale(load_image("5.jpeg", -1), (240, 70)), False)
    a1 = Button(sprite_Button, 320, 130,
                pygame.transform.scale(load_image("5.jpeg", -1), (200, 70)), True)
    Button_levels(sprite_Button_levels, 420, 230,
                  pygame.transform.scale(load_image(
                      "3.jpeg"),
                      (120, 70)), False)
    FON(sprite_Button_resultats, 0, 0, pygame.transform.scale(load_image(
        "3.jpeg"),
        (700, 500)))
    Button_levels(sprite_Button_resultats, 450, 250,
                  pygame.transform.scale(load_image(
                      "3.jpeg"),
                      (100, 50)), False)
    d = pygame.sprite.Group()
    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, sheet, columns, rows, x, y):
            super().__init__(d)
            self.frames = []
            self.cut_sheet(sheet, columns, rows)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.rect = self.rect.move(x, y)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

        def update(self):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]

    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 10)
    sound1 = pygame.mixer.Sound('Sound_07433 (mp3cut.net).wav')

    AnimatedSprite(
        pygame.transform.rotozoom(load_image('3353.jpg', -1), 0.1, 0.1), 4, 2, 100, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a1.flag and a1.flag != 2:
                    sprite_Button.update(event)
                elif a1.flag != 2:
                    sprite_Button_levels.update(event)
                sprite_Button_resultats.update(event)
            if event.type == pygame.MOUSEMOTION:
                sprite_Button.update(event, True)
            for event in pygame.event.get():
                if event.type == MYEVENTTYPE:
                    d.update()
        if not a1.flag and a1.flag != 2:
            screen.fill((0, 0, 0))
            sprite_Button_levels.draw(screen)
            help_23(screen)
        elif a1.flag == 2:
            screen.fill((0, 0, 0))
            sprite_Button_resultats.draw(screen)
            help_43(screen)
        else:
            sprite_Button.draw(screen)
            help2(screen)
        d.draw(screen)
        pygame.display.flip()
    pygame.quit()


fanction()
