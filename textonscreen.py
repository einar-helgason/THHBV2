from main import*
from globals import *

def drawScore(screen, SCREENRECT, score):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score: "+str(score), 1,(255,255,255))
    screen.blit(scoretext, (SCREENRECT.width*0.27, SCREENRECT.height*0.05))

def drawText(screen,SCREENRECT,text,x,y):
    myfont = pygame.font.SysFont("Arial", 20)
    label = myfont.render("ESC to exit!", 1, (255,0,0))
    screen.blit(label,(x, y))


def drawTime(screen, time):
    font=pygame.font.Font(None,30)
    timetext=font.render("Time: "+str(time), 1,(255,255,255))
    screen.blit(timetext, (SCREENRECT.width*0.1, SCREENRECT.height*0.9))
   

def drawHighScore(screen, score_lst):
    score_lst = score_lst[::-1] #reverse the list
    offset = 30
    font=pygame.font.Font(None,30)
    count = 0
    for i in range(len(score_lst)):
        if i >= 3 : break
        scoretext=font.render("HighScore: "+str(score_lst[i][2]), 1,(255,255,255))
        screen.blit(scoretext, (SCREENRECT.width*0.1, SCREENRECT.height*0.6+i*offset))

