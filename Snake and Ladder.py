import pygame
from random import randint
import time

clock = pygame.time.Clock()

pygame.init()
w = 1366
h = 768
G_DIS = pygame.display.set_mode([w, h])
pygame.display.update()

board = pygame.image.load("Snake_and_ladders_board.jpg")
dice1 = pygame.image.load("Dice1.png")
dice2 = pygame.image.load("Dice2.png")
dice3 = pygame.image.load("Dice3.png")
dice4 = pygame.image.load("Dice4.png")
dice5 = pygame.image.load("Dice5.png")
dice6 = pygame.image.load("Dice6.png")
redcoin = pygame.image.load("redcoin.png")
yellowcoin = pygame.image.load("yellowcoin.png")
greencoin = pygame.image.load("greencoin.png")
bluecoin = pygame.image.load("bluecoin.png")
home_backgroundbg = pygame.image.load("home_background.jpg")
p = pygame.image.load("play_background.png")
Team_name  = pygame.image.load("Team_name.png")
opening_image= pygame.image.load("opening_image.png")
credits1 = pygame.image.load("credits.jpg")
pygame.mixer.music.load("music.mp3")
snakesound = pygame.mixer.Sound("snake.wav")
win = pygame.mixer.Sound("win.wav")
lose = pygame.mixer.Sound("lose.wav")
ladder = pygame.mixer.Sound("ladder.wav")

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

black = (10, 10, 10)
white = (250, 250, 250)

def buttontext_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = buttontext_object(text, largeText)
    TextRect.center = (x, y)
    G_DIS.blit(TextSurf, TextRect)

def buttontext_object(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def comments_display(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = comment_objects(text, largeText)
    TextRect.center = (x, y)
    G_DIS.blit(TextSurf, TextRect)

def comment_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def coin(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y

def ladders(x):
    if x == 5:
        return 35
    elif x == 9:
        return 51
    elif x == 23:
        return 42
    elif x == 48:
        return 86
    elif x == 62:
        return 83
    elif x == 69:
        return 91
    else:
        return x

def snakes(x):
    if x == 36:
        return 5
    elif x == 49:
        return 7
    elif x == 56:
        return 8
    elif x == 82:
        return 20
    elif x == 87:
        return 66
    elif x == 95:
        return 38
    else:
        return x

def dice(a):
    if a == 1:
        a = dice1
    elif a == 2:
        a = dice2
    elif a == 3:
        a = dice3
    elif a == 4:
        a = dice4
    elif a == 5:
        a = dice5
    elif a == 6:
        a = dice6
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        G_DIS.blit(a, (1000, 500))
        pygame.display.update()

def menu_button(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(G_DIS, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(G_DIS, i, [x, y, w, h])
    buttontext_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)

def playscreen_button(text, xmouse, ymouse, x, y, w, h, i, a, fs):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(G_DIS, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
    else:
        pygame.draw.rect(G_DIS, i, [x, y, w, h])
    buttontext_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)

def turn(score, l, s):
    a = randint(1, 6)
    if a == 6:
        six = True
    else:
        six = False
    p = dice(a)
    score += a
    if score <= 100:
        lad = ladders(score)
        if lad != score:
            l = True
            pygame.mixer.Sound.play(ladder)
            time = pygame.time.get_ticks()
            score = lad
        snk = snakes(score)
        if snk != score:
            s = True
            pygame.mixer.Sound.play(snakesound)
            score = snk
    else:
        score -= a
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 1500:
            comments_display("Can't move!", 650, 50, 35, black)
            pygame.display.update()
    return score, l, s, six

def Quit():
    pygame.quit()
    quit()

def option_button(text, xmouse, ymouse, x, y, w, h, i, a, fs, b):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(G_DIS, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 5:
                return 5
            elif b == 0:
                Quit()
            elif b == "s" or b == 2 or b == 3 or b == 4:
                return b
            elif b == 7:
                options()
            else:
                return True
    else:
        pygame.draw.rect(G_DIS, i, [x, y, w, h])
    buttontext_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)

def intro():
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        G_DIS.blit(Team_name, (0, 0))
        pygame.display.update()
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        G_DIS.blit(opening_image, (0, 0))
        pygame.display.update()

def credit():
    while True:
        G_DIS.blit(credits1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if option_button("Back", mouse[0], mouse[1], w / 2 - 100, 700, 200, 50, red, b_red, 25, 20):
            main()

        pygame.display.update()

red = (200, 0, 0)
b_red = (240, 0, 0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (150, 150, 0)
purple = (43, 3, 132)
b_purple = (60, 0, 190)
orange= (247, 106, 5)
b_orange=(247, 199, 5)

def main():
    pygame.mixer.music.play(-1)
    home_background = True
    while home_background:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        G_DIS.blit(home_backgroundbg, (0, 0))
        option_button("Play", mouse[0], mouse[1], (w / 2 - 150), 250, 300, 50, green, b_green, 30, 1)
        option_button("Quit", mouse[0], mouse[1], (w / 2 - 150), 350, 300, 50, red, b_red, 30, 0)

        mouse = pygame.mouse.get_pos()
        if menu_button("Mute Music", mouse[0], mouse[1], (w / 2 - 150), 450, 300, 50, orange, b_orange, 25):
            pygame.mixer.music.pause()
        if menu_button("Play Music", mouse[0], mouse[1], (w / 2 - 150), 550, 300, 50,orange, b_orange, 25):
            pygame.mixer.music.unpause()
        if menu_button("Credits", mouse[0], mouse[1], (w / 2 - 150), 650, 300, 50, purple, b_purple, 25):
            credit()
        pygame.display.update()

def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        b1 = b2 = b3 = b4 = b5 = -1
        G_DIS.blit(home_backgroundbg, (0, 0))
        b1 = option_button("Solo", mouse[0], mouse[1], (w / 2 - 150), 250, 300, 50, green, b_green, 30, "s")
        b2 = option_button("Duo", mouse[0], mouse[1], (w / 2) - 150, 350, 300, 50, green, b_green, 30, 2)
        b3 = option_button("Trio", mouse[0], mouse[1], (w / 2) - 150, 450, 300, 50, green, b_green, 30, 3)
        b4 = option_button("Quad", mouse[0], mouse[1], (w / 2) - 150, 550, 300, 50, green, b_green, 30, 4)
        b5 = option_button("Back", mouse[0], mouse[1], 1166, 718, 200, 50, red, b_red, 30, 5)
        if b5 == 5:
            main()
        if b1 == "s":
            play(21)
        if b2 == 2:
            play(2)
        if b3 == 3:
            play(3)
        if b4 == 4:
            play(4)
        pygame.display.update()

def play(b):
    b6 = -1
    time = 3000
    if b6 == 7:
        options()
    G_DIS.blit(p, (0, 0))
    G_DIS.blit(board, (w / 2 - 250, h / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    G_DIS.blit(redcoin, (xcy, ycy))
    if 5 > b > 1 or b == 21:
        G_DIS.blit(yellowcoin, (xcy, ycy))

    if 5 > b > 2 or b == 21:
        G_DIS.blit(greencoin, (xcg, ycg))
    if 5 > b > 2:
        G_DIS.blit(bluecoin, (xcb, ycb))
    p1 = "Player 1"
    p1score = 0
    if b == 21:
        p2 = "Computer"
        p2score = 0
    if 5 > b > 1:
        p2 = "Player 2"
        p2score = 0
    if 5 > b > 2:
        p3 = "Player 3"
        p3score = 0
    if 5 > b > 3:
        p4 = "Player 4"
        p4score = 0
    t = 1
    play = True
    while True:
        l = False
        s = False
        time = 3000
        G_DIS.blit(p, (0, 0))
        G_DIS.blit(board, (w / 2 - 250, h / 2 - 250))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        if b == 21:
            if playscreen_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red, grey, 30):
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    if not six:
                        t += 1
                    xcr, ycr = coin(p1score)
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Player 1 Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
            playscreen_button("Computer", mouse[0], mouse[1], 400, 700, 200, 50, yellow, grey, 30)
            if True:
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xcy, ycy = coin(p2score)
                    if not six:
                        t += 1
                        if b < 3 or b == 21:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Computer Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5 > b > 1:
            if playscreen_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red, grey, 30):
                if t == 1:
                    p1score, l, s, six = turn(p1score, l, s)
                    xcr, ycr = coin(p1score)
                    if not six:
                        t += 1
                    if p1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Player 1 Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
            if playscreen_button("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow, grey, 30):
                if t == 2:
                    p2score, l, s, six = turn(p2score, l, s)
                    xcy, ycy = coin(p2score)
                    if not six:
                        t += 1
                        if b < 3:
                            t = 1
                    if p2score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Player 2 Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
        if 5 > b > 2:
            if playscreen_button("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green, grey, 30):
                if t == 3:
                    p3score, l, s, six = turn(p3score, l, s)
                    xcg, ycg = coin(p3score)
                    if not six:
                        t += 1
                        if b < 4:
                            t = 1
                    if p3score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Player 3 Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
        if 5 > b > 3:
            if playscreen_button("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue, grey, 30):
                if t == 4:
                    p4score, l, s, six = turn(p4score, l, s)
                    xcb, ycb = coin(p4score)
                    if not six:
                        t += 1
                        if b < 5:
                            t = 1
                    if p4score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            comments_display("Player 4 Wins", 650, 50, 50, black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
        b6 = option_button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red, b_red, 30, 7)
        G_DIS.blit(redcoin, (xcr, ycr))
        if 5 > b > 1 or b == 21:
            G_DIS.blit(yellowcoin, (xcy + 2, ycy))
        if 5 > b > 2:
            G_DIS.blit(greencoin, (xcg + 4, ycg))
        if 5 > b > 3:
            G_DIS.blit(bluecoin, (xcb + 6, ycb))
        if l:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                comments_display("There's a Ladder!", 650, 50, 35, black)
                pygame.display.update()
        if s:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                comments_display("There's a Snake!", 650, 50, 35, black)
                pygame.display.update()
        clock.tick(7)
        pygame.display.update()
intro()
main()