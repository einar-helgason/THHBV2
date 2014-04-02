from main import*

def drawScore(screen, SCREENRECT, score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score), 1,(255,255,255))
   screen.blit(scoretext, (SCREENRECT.width*0.3, SCREENRECT.height*0.05))

def drawText(screen,SCREENRECT,text,x,y):
    #initialize font
    myfont = pygame.font.SysFont("Arial", 20)

    # render text
    label = myfont.render("ESC to exit!", 1, (255,0,0))
    screen.blit(label,(x, y))


def drawTime(screen, time):
   font=pygame.font.Font(None,30)
   timetext=font.render("Time:"+str(time), 1,(255,255,255))
   screen.blit(timetext, (SCREENRECT.width*0.1, SCREENRECT.height*0.9))
