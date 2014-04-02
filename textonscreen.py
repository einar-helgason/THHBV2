from main import*

def drawScore(screen, score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score), 1,(255,255,255))
   screen.blit(scoretext, (200, 45))

def drawText(screen,text,x,y):
    #initialize font
    myfont = pygame.font.SysFont("Arial", 30)

    # render text
    label = myfont.render("ESC to exit!", 1, (255,0,0))
    screen.blit(label, (x, y))


def drawTime(screen, time):
   font=pygame.font.Font(None,30)
   timetext=font.render("Time:"+str(time), 1,(255,255,255))
   screen.blit(timetext, (200, 45))
