from main import*
from globals import *

def drawScore(screen, score):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score: "+str(score), 1,(255,255,255))
    screen.blit(scoretext, (SCREENRECT.width*0.80, SCREENRECT.height*0.05))

def drawText(screen):
    myfont = pygame.font.SysFont("Arial", 20)
    restart = myfont.render("R to Restart!", 1, (255,0,0))
    screen.blit(restart, (SCREENRECT.width*0.05, SCREENRECT.height*0.88))
    esc = myfont.render("ESC to Exit!", 1, (255,0,0))
    screen.blit(esc, (SCREENRECT.width*0.05, SCREENRECT.height*0.93))


def drawTime(screen, time):
    font=pygame.font.Font(None,30)
    timetext=font.render("Time: "+str(time), 1,(255,255,255))
    screen.blit(timetext, (SCREENRECT.width*0.80, SCREENRECT.height*0.9))
   

def drawHighScore(screen, score_lst):
    score_lst = score_lst[::-1] #reverse the list
    offset = 30
    font=pygame.font.Font(None,30)
    count = 0
    
    scoretext=font.render("High Scores:", 1,(255,255,255))
    screen.blit(scoretext, (SCREENRECT.width*0.80, SCREENRECT.height*0.29))
    
    for i in range(len(score_lst)):
        if i >= 3 : break
        scorevalue = font.render(str(score_lst[i][2]), 1,(255,255,255))
        screen.blit(scorevalue, (SCREENRECT.width*0.80, SCREENRECT.height*0.36+i*offset))

def drawWin(screen, score):
    font=pygame.font.Font(None,40)
    wintext = font.render("Thank you for playing our game! :D", 1,pink)
    screen.blit(wintext, (SCREENRECT.width*0.2, SCREENRECT.height*0.4))
    scoretext=font.render("Your score was: "+str(score), 1,pink)
    screen.blit(scoretext, (SCREENRECT.width*0.2, SCREENRECT.height*0.5))
    continuetext=font.render("Press any key to return to the game. ", 1,pink)
    screen.blit(continuetext, (SCREENRECT.width*0.2, SCREENRECT.height*0.6))
    
def main():
    """
    This module contains game specific functions that draw text to the screen at 
    some hard-coded position on the screen based on window-size percentages.
    """
    print main.__doc__
    
if __name__ == "__main__":
    main()