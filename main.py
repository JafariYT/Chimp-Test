import pygame
import random
from rects import num1rectget, num2rectget, num3rectget, num4rectget, num5rectget, num6rectget, num7rectget, num8rectget, num9rectget
from itertools import islice

pygame.init()

# DIFFICULTY TIMES IN SECONDS
# If you wanna play with a different time just change a difficulty's number and select that difficulty in the menu!
SUPERHUMAN = 2
HARD = 3
MEDIUM = 5
EASY = 10

WIDTH = pygame.display.Info().current_w
HEIGHT = WIDTH * 0.5625
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
currTime = 0
state = 0
timedMode = True
numAmtPerm = 3
increase = True
difficulty = 2
timerS = MEDIUM * 10

pygame.display.set_caption('Chimp Test')
numAmt = numAmtPerm
running = True
test_font = pygame.font.Font("graphics/Mogra-Regular.ttf", int(WIDTH/34))
fontnum = 5
currNum = 1
streak = 0
logo = pygame.transform.scale(pygame.image.load('graphics/logo.png').convert_alpha(), (WIDTH/1.15, HEIGHT/3.57))
logo_rotation = 0
logo_rotation_direction = 1
play = pygame.transform.scale(pygame.image.load('graphics/play.png').convert_alpha(), (WIDTH/3.1, HEIGHT/4))
playhover = pygame.transform.scale(pygame.image.load('graphics/playhover.png').convert_alpha(), (WIDTH/3, HEIGHT/3.8))
playwidth = play.get_width()
playheight = play.get_height()
play_zoom = 1
play_zoom_direction = 1
zoom_speed = 0
beginFlag = False
rotation_speed = 0
zoom_speed = 0
updateNumRects = True
loc = [0] * 18

bkgrDef = pygame.transform.scale(pygame.image.load('graphics/bkgrDef.png').convert(), (WIDTH, HEIGHT))
bkgr1 = pygame.transform.scale(pygame.image.load('graphics/bkgr1.png').convert(), (WIDTH, HEIGHT))
bkgr2 = pygame.transform.scale(pygame.image.load('graphics/bkgr2.png').convert(), (WIDTH, HEIGHT))
bkgr3 = pygame.transform.scale(pygame.image.load('graphics/bkgr3.png').convert(), (WIDTH, HEIGHT))
bkgr4 = pygame.transform.scale(pygame.image.load('graphics/bkgr4.png').convert(), (WIDTH, HEIGHT))
bkgr5 = pygame.transform.scale(pygame.image.load('graphics/bkgr5.png').convert(), (WIDTH, HEIGHT))
bkgrWin = pygame.transform.scale(pygame.image.load('graphics/bkgrWin.png').convert(), (WIDTH, HEIGHT))
num1 = pygame.transform.scale(pygame.image.load('graphics/num1.png').convert(), (WIDTH/20, WIDTH/20))
num2 = pygame.transform.scale(pygame.image.load('graphics/num2.png').convert(), (WIDTH/20, WIDTH/20))
num3 = pygame.transform.scale(pygame.image.load('graphics/num3.png').convert(), (WIDTH/20, WIDTH/20))
num4 = pygame.transform.scale(pygame.image.load('graphics/num4.png').convert(), (WIDTH/20, WIDTH/20))
num5 = pygame.transform.scale(pygame.image.load('graphics/num5.png').convert(), (WIDTH/20, WIDTH/20))
num6 = pygame.transform.scale(pygame.image.load('graphics/num6.png').convert(), (WIDTH/20, WIDTH/20))
num7 = pygame.transform.scale(pygame.image.load('graphics/num7.png').convert(), (WIDTH/20, WIDTH/20))
num8 = pygame.transform.scale(pygame.image.load('graphics/num8.png').convert(), (WIDTH/20, WIDTH/20))
num9 = pygame.transform.scale(pygame.image.load('graphics/num9.png').convert(), (WIDTH/20, WIDTH/20))
check = pygame.transform.scale(pygame.image.load('graphics/correct.png').convert_alpha(), (WIDTH/5, WIDTH/5))
xmark = pygame.transform.scale(pygame.image.load('graphics/game over.png').convert_alpha(), (WIDTH/5, WIDTH/5))

white = pygame.Surface((WIDTH/20, WIDTH/20))
white.fill((255, 255, 255))
num1rect = num1rectget(num1, WIDTH, HEIGHT, loc)
num2rect = num2rectget(num2, WIDTH, HEIGHT, loc)
num3rect = num3rectget(num3, WIDTH, HEIGHT, loc)
num4rect = num4rectget(num4, WIDTH, HEIGHT, loc)
num5rect = num5rectget(num5, WIDTH, HEIGHT, loc)
num6rect = num6rectget(num6, WIDTH, HEIGHT, loc)
num7rect = num7rectget(num7, WIDTH, HEIGHT, loc)
num8rect = num8rectget(num8, WIDTH, HEIGHT, loc)
num9rect = num9rectget(num9, WIDTH, HEIGHT, loc)
number_rects = [num1rect, num2rect, num3rect, num4rect, num5rect, num6rect, num7rect, num8rect, num9rect]
collideflags = [True] * len(number_rects)
postClickFlag = False

cont = test_font.render("CONTINUE", True, (0, 255, 0))
cont = pygame.transform.scale(cont, (cont.get_width()*3, cont.get_height()*3))
contrect = cont.get_rect(topleft=(WIDTH/2-cont.get_width()/2, HEIGHT-HEIGHT/2.5))
begin = test_font.render("START", True, (0, 255, 0))
begin = pygame.transform.scale(begin, (begin.get_width()*3, begin.get_height()*3))
beginrect = begin.get_rect(topleft=((WIDTH-begin.get_width())/2, (HEIGHT-begin.get_height())/2))
redo = test_font.render("RESTART", True, (255, 0, 0))
redo = pygame.transform.scale(redo, (redo.get_width()*3, redo.get_height()*3))
redorect = redo.get_rect(topleft=(WIDTH/2-redo.get_width()/2, HEIGHT-HEIGHT/2.5))

space = WIDTH/85.35
option_timed = test_font.render("TIMED", True, (112, 112, 112))
option_timedSel = test_font.render("TIMED", True, (255, 255, 255))
option_timedHov = test_font.render("TIMED", True, (255, 112, 0))
option_untimed = test_font.render("UNTIMED", True, (112, 112, 112))
option_untimedSel = test_font.render("UNTIMED", True, (255, 255, 255))
option_untimedHov = test_font.render("UNTIMED", True, (255, 112, 0))
option_space_time = option_untimed.get_width() + option_timed.get_width() + space

option_super = test_font.render("SUPERHUMAN", True, (112, 112, 112))
option_superSel = test_font.render("SUPERHUMAN", True, (255, 255, 255))
option_superHov = test_font.render("SUPERHUMAN", True, (255, 112, 0))
option_superOff = test_font.render("SUPERHUMAN", True, (70, 70, 70))
option_hard = test_font.render("HARD", True, (112, 112, 112))
option_hardSel = test_font.render("HARD", True, (255, 255, 255))
option_hardHov = test_font.render("HARD", True, (255, 112, 0))
option_hardOff = test_font.render("HARD", True, (70, 70, 70))
option_medium = test_font.render("MEDIUM", True, (112, 112, 112))
option_mediumSel = test_font.render("MEDIUM", True, (255, 255, 255))
option_mediumHov = test_font.render("MEDIUM", True, (255, 112, 0))
option_mediumOff = test_font.render("MEDIUM", True, (70, 70, 70))
option_easy = test_font.render("EASY", True, (112, 112, 112))
option_easySel = test_font.render("EASY", True, (255, 255, 255))
option_easyHov = test_font.render("EASY", True, (255, 112, 0))
option_easyOff = test_font.render("EASY", True, (70, 70, 70))
option_space_difficulty = option_super.get_width() + option_hard.get_width() + option_medium.get_width() + option_easy.get_width() + 3*space

option_3 = test_font.render("3", True, (112, 112, 112))
option_3Sel = test_font.render("3", True, (255, 255, 255))
option_3Hov = test_font.render("3", True, (255, 112, 0))
option_5 = test_font.render("5", True, (112, 112, 112))
option_5Sel = test_font.render("5", True, (255, 255, 255))
option_5Hov = test_font.render("5", True, (255, 112, 0))
option_7 = test_font.render("7", True, (112, 112, 112))
option_7Sel = test_font.render("7", True, (255, 255, 255))
option_7Hov = test_font.render("7", True, (255, 112, 0))
option_8 = test_font.render("8", True, (112, 112, 112))
option_8Sel = test_font.render("8", True, (255, 255, 255))
option_8Hov = test_font.render("8", True, (255, 112, 0))
option_9 = test_font.render("9", True, (112, 112, 112))
option_9Sel = test_font.render("9", True, (255, 255, 255))
option_9Hov = test_font.render("9", True, (255, 112, 0))
option_space_nums = option_3.get_width() + option_5.get_width() + option_7.get_width() + option_8.get_width() + option_9.get_width() + 4*space

option_yes = test_font.render("YES", True, (112, 112, 112))
option_yesSel = test_font.render("YES", True, (255, 255, 255))
option_yesHov = test_font.render("YES", True, (255, 112, 0))
option_yesOff = test_font.render("YES", True, (70, 70, 70))
option_no = test_font.render("NO", True, (112, 112, 112))
option_noSel = test_font.render("NO", True, (255, 255, 255))
option_noHov = test_font.render("NO", True, (255, 112, 0))
option_noOff = test_font.render("NO", True, (70, 70, 70))
option_space_inc = option_yes.get_width() + option_no.get_width() + space
lightsoutFlag = False
lightsoutFlag2 = True

def RNG(numAmt):
    grid = [[0 for _ in range(9)] for _ in range(6)]
    generate9 = 1
    id = 0
    while generate9 < numAmt+1:
        Xloc = random.randint(0, 5) # offset: -3
        Yloc = random.randint(0, 8) # offset: -4
        if grid[Xloc][Yloc] > 0: continue
        grid[Xloc][Yloc] = generate9
        loc[id] = Xloc-3
        loc[id+1] = Yloc-4
        id += 2
        generate9 += 1
    return loc

loc = RNG(numAmt)

while running:
    mousePos = pygame.mouse.get_pos()
    time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and state == 0 and test_font.render("QUIT", True, (0, 255, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)).collidepoint(mousePos)):
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and postClickFlag:
            postClickFlag = False
            pygame.mixer.Sound('sounds/start.mp3').play()
            if state == 3: streak = 0
            state = 1
            currNum = 1
            currTime = time
            loc = RNG(numAmt)
            updateNumRects = True
            beginflag = False
            lightsoutFlag = False
            lightsoutFlag2 = True
        elif event.type == pygame.MOUSEBUTTONDOWN and state == 0:
            if pygame.transform.scale(play, (playwidth*play_zoom, playheight*play_zoom)).get_rect(center=(WIDTH/2, HEIGHT-HEIGHT/5.7)).collidepoint(mousePos):
                pygame.mixer.Sound('sounds/s3.mp3').play()
                numAmt = numAmtPerm
                beginflag = True
                state = 2
            if timedMode and option_untimed.get_rect(topleft=(((WIDTH-option_space_time)//2)+option_timed.get_width()+space, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)).collidepoint(mousePos):
                timedMode = False
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif not timedMode and option_timed.get_rect(topleft=((WIDTH-option_space_time)//2, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)).collidepoint(mousePos):
                timedMode = True
                pygame.mixer.Sound('sounds/start.mp3').play()
            if difficulty != 0 and timedMode and option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)).collidepoint(mousePos):
                difficulty = 0
                timerS = SUPERHUMAN * 10
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif difficulty != 1 and timedMode and option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)).collidepoint(mousePos):
                difficulty = 1
                timerS = HARD * 10
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif difficulty != 2 and timedMode and option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)).collidepoint(mousePos):
                difficulty = 2
                timerS = MEDIUM * 10
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif difficulty != 3 and timedMode and option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_medium.get_width()+option_hard.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)).collidepoint(mousePos):
                difficulty = 3
                timerS = EASY * 10
                pygame.mixer.Sound('sounds/start.mp3').play()
            if numAmtPerm != 3 and screen.blit(option_3, option_3.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                numAmtPerm = 3
                numAmt = numAmtPerm
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif numAmtPerm != 5 and screen.blit(option_5, option_5.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+1*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                numAmtPerm = 5
                numAmt = numAmtPerm
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif numAmtPerm != 7 and screen.blit(option_7, option_7.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+2*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                numAmtPerm = 7
                numAmt = numAmtPerm
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif numAmtPerm != 8 and screen.blit(option_8, option_8.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+3*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                numAmtPerm = 8
                numAmt = numAmtPerm
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif numAmtPerm != 9 and screen.blit(option_9, option_9.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+option_8.get_width()+4*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                numAmtPerm = 9
                numAmt = numAmtPerm
                pygame.mixer.Sound('sounds/start.mp3').play()
            if not increase and numAmtPerm < 9 and screen.blit(option_yes, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                increase = True
                pygame.mixer.Sound('sounds/start.mp3').play()
            elif increase and numAmtPerm < 9 and screen.blit(option_no, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos):
                increase = False
                pygame.mixer.Sound('sounds/start.mp3').play()
        elif event.type == pygame.MOUSEBUTTONDOWN and state > 0:
            if test_font.render("MENU", True, (0, 255, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)).collidepoint(mousePos):
                streak = 0
                state = 0
                pygame.mixer.Sound('sounds/start.mp3').play()
            if (contrect.collidepoint(mousePos) and not beginflag and state == 2) or ((beginrect.collidepoint(mousePos) and beginflag and state == 2)) or (redorect.collidepoint(mousePos) and state == 3):
                postClickFlag = True
            for i, rect in islice(enumerate(number_rects, start=1), numAmt):
                if state == 1 and collideflags[i-1] and rect.collidepoint(mousePos): # if pygame.Rect(0, 0, 100, 50).collidepoint(pygame.mouse.get_pos()): # this is like a hard reset
                    if currNum == i:
                        currNum += 1
                        pygame.mixer.Sound('sounds/s1.mp3').play()
                        if currNum == numAmt+1:
                            streak += 1
                            pygame.mixer.Sound('sounds/correct.mp3').play()
                            if increase and numAmt < 9: numAmt += 1
                            state = 2
                        collideflags[i-1] = False
                    else:
                        pygame.mixer.Sound('sounds/incorrect.mp3').play()
                        numAmt = numAmtPerm
                        state = 3

    if state > 0: # TEST IS RUNNING
        if numAmt == 3 or numAmt == 4: screen.blit(bkgr1, (0, 0))
        elif numAmt == 5 or numAmt == 6: screen.blit(bkgr2, (0, 0))
        elif numAmt == 7 or numAmt == 8: screen.blit(bkgr3, (0, 0))
        elif numAmtPerm == 9 and timedMode and difficulty == 0: screen.blit(bkgr5, (0, 0))
        else: screen.blit(bkgr4, (0, 0))

        if updateNumRects:
            num1rect = num1rectget(num1, WIDTH, HEIGHT, loc)
            num2rect = num2rectget(num2, WIDTH, HEIGHT, loc)
            num3rect = num3rectget(num3, WIDTH, HEIGHT, loc)
            if numAmt >= 4: num4rect = num4rectget(num4, WIDTH, HEIGHT, loc)
            if numAmt >= 5: num5rect = num5rectget(num5, WIDTH, HEIGHT, loc)
            if numAmt >= 6: num6rect = num6rectget(num6, WIDTH, HEIGHT, loc)
            if numAmt >= 7: num7rect = num7rectget(num7, WIDTH, HEIGHT, loc)
            if numAmt >= 8: num8rect = num8rectget(num8, WIDTH, HEIGHT, loc)
            if numAmt >= 9: num9rect = num9rectget(num9, WIDTH, HEIGHT, loc)
            number_rects = [num1rect, num2rect, num3rect, num4rect, num5rect, num6rect, num7rect, num8rect, num9rect]
            collideflags = [True] * len(number_rects)
            updateNumRects = False
        
        if state == 3: screen.blit(test_font.render("SCORE: " + str(streak), True, (255, 255, 255)), ((WIDTH-test_font.render("SCORE: " + str(streak), True, (255, 255, 255)).get_width())/2, HEIGHT-HEIGHT/4))
        else: screen.blit(test_font.render("SCORE: " + str(streak), True, (255, 255, 255)), (WIDTH/85.35, WIDTH/85.35))
        if timedMode: screen.blit(pygame.transform.scale(test_font.render("TIMED", True, "#dddddd"), (test_font.render("TIMED", True, "#dddddd").get_width()/1.75, test_font.render("TIMED", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*4))
        else: screen.blit(pygame.transform.scale(test_font.render("UNTIMED", True, "#dddddd"), (test_font.render("UNTIMED", True, "#dddddd").get_width()/1.75, test_font.render("UNTIMED", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*4))
        screen.blit(pygame.transform.scale(test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd"), (test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd").get_width()/1.75, test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*5.5))
        if increase and numAmt < 9: screen.blit(pygame.transform.scale(pygame.image.load('graphics/arrow.png'), (WIDTH/95, WIDTH/70)), (WIDTH/85.35+pygame.transform.scale(test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd"), (test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd").get_width()/1.75, test_font.render(str(numAmt) + " NUMBERS", True, "#dddddd").get_height()/1.75)).get_width()+WIDTH/200, WIDTH/85.35*5.5))
        if timedMode and difficulty == 3: screen.blit(pygame.transform.scale(test_font.render("EASY", True, "#dddddd"), (test_font.render("EASY", True, "#dddddd").get_width()/1.75, test_font.render("EASY", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*7))
        elif timedMode and difficulty == 2: screen.blit(pygame.transform.scale(test_font.render("MEDIUM", True, "#dddddd"), (test_font.render("NORMAL", True, "#dddddd").get_width()/1.75, test_font.render("NORMAL", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*7))
        elif timedMode and difficulty == 1: screen.blit(pygame.transform.scale(test_font.render("HARD", True, "#dddddd"), (test_font.render("HARD", True, "#dddddd").get_width()/1.75, test_font.render("HARD", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*7))
        elif timedMode and difficulty == 0: screen.blit(pygame.transform.scale(test_font.render("SUPERHUMAN", True, "#dddddd"), (test_font.render("SUPERHUMAN", True, "#dddddd").get_width()/1.75, test_font.render("SUPERHUMAN", True, "#dddddd").get_height()/1.75)), (WIDTH/85.35, WIDTH/85.35*7))
        
        if test_font.render("MENU", True, (0, 255, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)).collidepoint(mousePos): screen.blit(test_font.render("MENU", True, (255, 255, 255)), test_font.render("MENU", True, (255, 255, 255)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)))
        else: screen.blit(test_font.render("MENU", True, (0, 255, 0)), test_font.render("MENU", True, (0, 255, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)))
        
        if state == 2 and not beginflag: screen.blit(check, ((WIDTH-check.get_width())/2, HEIGHT-HEIGHT/1.3))
        if state == 2 and not beginflag and not contrect.collidepoint(mousePos): screen.blit(cont, contrect)
        elif state == 2 and not beginflag and contrect.collidepoint(mousePos): screen.blit(pygame.transform.scale(test_font.render("CONTINUE", True, (255, 255, 255)), (cont.get_width(), cont.get_height())), cont.get_rect(topleft=(WIDTH/2-cont.get_width()/2, HEIGHT-HEIGHT/2.5)))
        if state == 2 and beginflag and not beginrect.collidepoint(mousePos): screen.blit(begin, beginrect)
        elif state == 2 and beginflag and beginrect.collidepoint(mousePos): screen.blit(pygame.transform.scale(test_font.render("START", True, (255, 255, 255)), (begin.get_width(), begin.get_height())), begin.get_rect(topleft=((WIDTH-begin.get_width())/2, (HEIGHT-begin.get_height())/2)))
        if state == 3: screen.blit(xmark, ((WIDTH-xmark.get_width())/2, HEIGHT-HEIGHT/1.3))
        if state == 3 and not contrect.collidepoint(mousePos): screen.blit(redo, redorect)
        elif state == 3 and contrect.collidepoint(mousePos): screen.blit(pygame.transform.scale(test_font.render("RESTART", True, (255, 255, 255)), (redo.get_width(), redo.get_height())), redo.get_rect(topleft=(WIDTH/2-redo.get_width()/2, HEIGHT-HEIGHT/2.5)))
        
        if state == 1 and currNum <= 1 and ((timedMode and ((time-currTime) // 100 == timerS))): lightsoutFlag = True
        if lightsoutFlag and lightsoutFlag2:
            pygame.mixer.Sound('sounds/lightsout.mp3').play()
            lightsoutFlag2 = False
        
        if state == 1 and currNum <= 1 and ((timedMode and ((time-currTime) // 100 < timerS)) or not timedMode):
            if state == 1: screen.blit(num1, num1rectget(num1, WIDTH, HEIGHT, loc))
            if state == 1: screen.blit(num2, num2rectget(num2, WIDTH, HEIGHT, loc))
            if state == 1: screen.blit(num3, num3rectget(num3, WIDTH, HEIGHT, loc))
            if numAmt >= 4 and state == 1: screen.blit(num4, num4rectget(num4, WIDTH, HEIGHT, loc))
            if numAmt >= 5 and state == 1: screen.blit(num5, num5rectget(num5, WIDTH, HEIGHT, loc))
            if numAmt >= 6 and state == 1: screen.blit(num6, num6rectget(num6, WIDTH, HEIGHT, loc))
            if numAmt >= 7 and state == 1: screen.blit(num7, num7rectget(num7, WIDTH, HEIGHT, loc))
            if numAmt >= 8 and state == 1: screen.blit(num8, num8rectget(num8, WIDTH, HEIGHT, loc))
            if numAmt >= 9 and state == 1: screen.blit(num9, num9rectget(num9, WIDTH, HEIGHT, loc))
        else:
            if currNum <= 1 and state == 1: screen.blit(white, num1rectget(num1, WIDTH, HEIGHT, loc))
            if currNum <= 2 and state == 1: screen.blit(white, num2rectget(num2, WIDTH, HEIGHT, loc))
            if currNum <= 3 and state == 1: screen.blit(white, num3rectget(num3, WIDTH, HEIGHT, loc))
            if numAmt >= 4 and currNum <= 4 and state == 1: screen.blit(white, num4rectget(num4, WIDTH, HEIGHT, loc))
            if numAmt >= 5 and currNum <= 5 and state == 1: screen.blit(white, num5rectget(num5, WIDTH, HEIGHT, loc))
            if numAmt >= 6 and currNum <= 6 and state == 1: screen.blit(white, num6rectget(num6, WIDTH, HEIGHT, loc))
            if numAmt >= 7 and currNum <= 7 and state == 1: screen.blit(white, num7rectget(num7, WIDTH, HEIGHT, loc))
            if numAmt >= 8 and currNum <= 8 and state == 1: screen.blit(white, num8rectget(num8, WIDTH, HEIGHT, loc))
            if numAmt >= 9 and currNum <= 9 and state == 1: screen.blit(white, num9rectget(num9, WIDTH, HEIGHT, loc))

    else: # MENU
        screen.blit(bkgrDef, (0, 0))
        if test_font.render("QUIT", True, (0, 255, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)).collidepoint(mousePos): screen.blit(test_font.render("QUIT", True, (255, 255, 255)), test_font.render("QUIT", True, (255, 255, 255)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)))
        else: screen.blit(test_font.render("QUIT", True, (255, 0, 0)), test_font.render("QUIT", True, (255, 0, 0)).get_rect(topright=(WIDTH-WIDTH/85.35, WIDTH/85.35)))
        screen.blit(test_font.render("by JAFARI", True, "#6d46ff"), test_font.render("by JAFARI", True, "#6d46ff").get_rect(bottomleft=(WIDTH/85.35, HEIGHT-HEIGHT/85.35)))
        screen.blit(pygame.transform.rotate(logo, logo_rotation), (pygame.transform.rotate(logo, logo_rotation).get_rect(center=(((WIDTH // 2), HEIGHT/5.5)))))
        rotation_speed = logo_rotation_direction * ((3.15 - abs(logo_rotation)) / 12.5)
        logo_rotation += rotation_speed
        if logo_rotation >= 3:
            logo_rotation_direction = -1
        elif logo_rotation <= -3:
            logo_rotation_direction = 1
        
        if pygame.transform.scale(play, (playwidth*play_zoom, playheight*play_zoom)).get_rect(center=(WIDTH/2, HEIGHT-HEIGHT/5.7)).collidepoint(mousePos): screen.blit(pygame.transform.scale(playhover, (playwidth*play_zoom, playheight*play_zoom)), pygame.transform.scale(play, (playwidth*play_zoom, playheight*play_zoom)).get_rect(center=(WIDTH/2, HEIGHT-HEIGHT/5.7)))
        else: screen.blit(pygame.transform.scale(play, (playwidth*play_zoom, playheight*play_zoom)), pygame.transform.scale(play, (playwidth*play_zoom, playheight*play_zoom)).get_rect(center=(WIDTH/2, HEIGHT-HEIGHT/5.7)))
        
        zoom_speed = play_zoom_direction * ((1.105 - abs(play_zoom-1.05)*20) / 300)
        play_zoom += zoom_speed
        if play_zoom >= 1.1:
            play_zoom_direction = -1
        elif play_zoom <= 1:
            play_zoom_direction = 1

        screen.blit(test_font.render("MODE", True, (0, 255, 0)), test_font.render("MODE", True, (0, 255, 0)).get_rect(topleft=((WIDTH-test_font.render("MODE", True, (0, 255, 0)).get_width())/2, HEIGHT-HEIGHT/1.58)))
        if timedMode: screen.blit(option_timedSel, option_timed.get_rect(topleft=((WIDTH-option_space_time)//2, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))
        elif option_timed.get_rect(topleft=((WIDTH-option_space_time)//2, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)).collidepoint(mousePos): screen.blit(option_timedHov, option_timed.get_rect(topleft=((WIDTH-option_space_time)//2, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))
        else: screen.blit(option_timed, option_timed.get_rect(topleft=((WIDTH-option_space_time)//2, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))
        if not timedMode: screen.blit(option_untimedSel, option_untimed.get_rect(topleft=(((WIDTH-option_space_time)//2)+option_timed.get_width()+space, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))
        elif screen.blit(option_untimed, option_untimed.get_rect(topleft=(((WIDTH-option_space_time)//2)+option_timed.get_width()+space, (HEIGHT-HEIGHT/1.58)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_untimedHov, option_untimed.get_rect(topleft=(((WIDTH-option_space_time)//2)+option_timed.get_width()+space, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))
        else: screen.blit(option_untimed, option_untimed.get_rect(topleft=(((WIDTH-option_space_time)//2)+option_timed.get_width()+space, (HEIGHT-HEIGHT/1.58)+HEIGHT/22)))

        if timedMode: screen.blit(test_font.render("SPEED", True, (0, 255, 0)), test_font.render("SPEED", True, (0, 255, 0)).get_rect(topleft=((WIDTH-test_font.render("SPEED", True, (0, 255, 0)).get_width())/2, HEIGHT-HEIGHT/2.3)))
        else: screen.blit(test_font.render("SPEED", True, (70, 70, 70)), test_font.render("SPEED", True, (70, 70, 70)).get_rect(topleft=((WIDTH-test_font.render("SPEED", True, (70, 70, 70)).get_width())/2, HEIGHT-HEIGHT/2.3)))
        if not timedMode: screen.blit(option_superOff, option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif difficulty == 0: screen.blit(option_superSel, option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif screen.blit(option_super, option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_superHov, option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        else: screen.blit(option_super, option_super.get_rect(topleft=((WIDTH-option_space_difficulty)//2, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        if not timedMode: screen.blit(option_hardOff, option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif difficulty == 1: screen.blit(option_hardSel, option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif screen.blit(option_hard, option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_hardHov, option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        else: screen.blit(option_hard, option_hard.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        if not timedMode: screen.blit(option_mediumOff, option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif difficulty == 2: screen.blit(option_mediumSel, option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif screen.blit(option_medium, option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_mediumHov, option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        else: screen.blit(option_medium, option_medium.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+2*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        if not timedMode: screen.blit(option_easyOff, option_easy.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+option_medium.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif difficulty == 3: screen.blit(option_easySel, option_easy.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+option_medium.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        elif screen.blit(option_easy, option_easy.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+option_medium.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_easyHov, option_easy.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+option_medium.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))
        else: screen.blit(option_easy, option_easy.get_rect(topleft=((WIDTH-option_space_difficulty)//2+option_super.get_width()+option_hard.get_width()+option_medium.get_width()+3*space, (HEIGHT-HEIGHT/2.3)+HEIGHT/22)))

        screen.blit(test_font.render("NUMBERS", True, (0, 255, 0)), test_font.render("NUMBERS", True, (0, 255, 0)).get_rect(topright=((WIDTH-WIDTH/1.5, HEIGHT-HEIGHT/1.85))))
        if numAmtPerm == 3: screen.blit(option_3Sel, option_3.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_3, option_3.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_3Hov, option_3.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_3, option_3.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        if numAmtPerm == 5: screen.blit(option_5Sel, option_5.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+1*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_5, option_5.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+1*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_5Hov, option_5.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+1*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_5, option_5.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+1*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        if numAmtPerm == 7: screen.blit(option_7Sel, option_7.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+2*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_7, option_7.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+2*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_7Hov, option_7.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+2*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_7, option_7.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+2*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        if numAmtPerm == 8: screen.blit(option_8Sel, option_8.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+3*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_8, option_8.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+3*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_8Hov, option_8.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+3*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_8, option_8.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+3*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        if numAmtPerm == 9: screen.blit(option_9Sel, option_9.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+option_8.get_width()+4*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_9, option_9.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+option_8.get_width()+4*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_9Hov, option_9.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+option_8.get_width()+4*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_9, option_9.get_rect(topleft=(WIDTH-WIDTH/1.5-option_space_nums+option_3.get_width()+option_5.get_width()+option_7.get_width()+option_8.get_width()+4*space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))

        if numAmtPerm < 9: screen.blit(test_font.render("INCREASE", True, (0, 255, 0)), test_font.render("INCREASE", True, (0, 255, 0)).get_rect(topleft=(WIDTH/1.5, HEIGHT-HEIGHT/1.85)))
        else: screen.blit(test_font.render("INCREASE", True, (70, 70, 70)), test_font.render("INCREASE", True, (0, 255, 0)).get_rect(topleft=(WIDTH/1.5, HEIGHT-HEIGHT/1.85)))
        if numAmtPerm == 9: screen.blit(option_yesOff, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif increase and numAmtPerm < 9: screen.blit(option_yesSel, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_yes, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_yesHov, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_yes, option_yes.get_rect(topleft=(WIDTH/1.5, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        if numAmtPerm == 9: screen.blit(option_noOff, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif not increase and numAmtPerm < 9: screen.blit(option_noSel, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        elif screen.blit(option_no, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22))).collidepoint(mousePos): screen.blit(option_noHov, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
        else: screen.blit(option_no, option_no.get_rect(topleft=(WIDTH/1.5+option_yes.get_width()+space, (HEIGHT-HEIGHT/1.85)+HEIGHT/22)))
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
