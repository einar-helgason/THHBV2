from pygame import *
from lib.Klondike import *
from lib import MenuSystem
from lib import GetEvent


bg = image.load('images/background.png')
cards = image.load('images/cards.png')
img_carte = [[cards.subsurface(x,y,79,123)for x in range(0,1027,79)] for y in range(0,492,123)]
hidden = image.load('images/hidden.png')

#~ #############################################################
#~ Liaison GUI/Logique
#~ #############################################################

jeu = Klondike()

jeu.pioche.rect0 = Rect(70,70,79,123)
jeu.pioche.rect = Rect(175,70,59+20*Options.Donnes,123)
jeu.pioche.cible = Rect(0,0,79,123)
jeu.pioche.cible.topright = jeu.pioche.rect.topright
[setattr(h,'rect',Rect(x,70,79,123)) for x,h in zip(range(385,701,105),jeu.home)]
[setattr(s,'rect',Rect(x,270,79,300)) for x,s in zip(range(70,701,105),jeu.stack)]


def screenpioche(self):
    if jeu.RestePioche:
        scr.blit(hidden,jeu.pioche.rect0)
    else:
        scr.blit(bg,jeu.pioche.rect0,jeu.pioche.rect0)
    scr.blit(bg,jeu.pioche.rect,jeu.pioche.rect)
    piochees = jeu.CartesPiochees[::-1]
    for x,c in enumerate(piochees,-len(piochees)+1):
        scr.blit(img_carte[c.famille][c.valeur],jeu.pioche.cible.move(x*20,0))

def showpioche(self):
    self.screen()
    display.update((jeu.pioche.rect0,jeu.pioche.rect))

jeu.Pioche.screen = screenpioche
jeu.Pioche.show = showpioche

def screenstack(self):
    scr.blit(bg,self.rect,self.rect)
    l = len(self)
    if not l:
        self.rects = [Rect(self.rect.topleft,(79,123))]
    else:
        if l > 1: self.spacing = min((20,177//(l-1)))
        else: self.spacing = 20
        self.rects = []
        x,y = self.rect.topleft
        for c in self:
            self.rects.append(scr.blit(img_carte[c.famille][c.valeur] if c.status else hidden,(x,y)))
            y += self.spacing

def showstack(self):
    self.screen()
    display.update(self.rect)

jeu.Stack.screen = screenstack
jeu.Stack.show = showstack

def screenhome(self):
    if self: scr.blit(img_carte[self[-1].famille][self[-1].valeur],self.rect)
    else: scr.blit(bg,self.rect,self.rect)

def showhome(self):
    self.screen()
    display.update(self.rect)

jeu.Home.screen = screenhome
jeu.Home.show = showhome
#~ #############################################################
#~ #############################################################

scr = display.set_mode(bg.get_size())

def redraw():
    scr.blit(bg,(0,0))
    jeu.pioche.screen()
    for s in jeu.stack:
        s.screen()
    for h in jeu.home:
        h.screen()
    m_bar.draw()
    display.flip()



#~ #############################################################
#~ MenuBar
#~ #############################################################
MenuSystem.init()
MenuSystem.FGCOLOR      = Color(0xffffff00)
MenuSystem.BGCOLOR      = Color(0x150505ff)
MenuSystem.BGHIGHTLIGHT = Color(0xffffff50)
MenuSystem.FGLOWLIGHT   = Color(0x50505000)
MenuSystem.BORDER_LEFT  = Color(0xffffffff)
MenuSystem.BORDER_RIGHT = Color(0xffffffff)
MenuSystem.FONT         = font.Font('lib/Roboto-Regular.ttf',18)
m_game                  = MenuSystem.Menu('Game', ("New Game","Undo","Replay","Quit"),(1,2))
m_klondike              = MenuSystem.Menu('Klondike',  ('Donne 1 carte','Donne 3 cartes','Pas de nouvelle donne'))
m_bar                   = MenuSystem.MenuBar()
scr.blit(bg,(0,0))
m_bar.set([m_game,m_klondike])
#~ #############################################################
#~ #############################################################


redraw()
source = None
foo = 0

while 1:
    ev = GetEvent.wait()

    display.update(m_bar.update(ev))
    if m_bar: continue
    if m_bar.choice_label == ('Game','New Game'):
        jeu.NouvellePartie()
        redraw()
        m_klondike.exc = ()
    elif m_bar.choice_label == ('Game','Quit'): break
    elif m_bar.choice_label == ('Klondike','Donne 1 carte'):
        Options.update(Donnes=1)
    elif m_bar.choice_label == ('Klondike','Donne 3 cartes'):
        Options.update(Donnes=3)
    elif m_bar.choice_label == ('Klondike','Pas de nouvelle donne'):
        Options.update(NouvelleDonne=False)
    elif m_bar.choice_label == ('Game','Undo'):
        u = jeu.Undo()
        if u:
            for i in u: i.show()
            m_game.exc = (1,2)

    if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
        if jeu.pioche.rect0.collidepoint(ev.pos):
            jeu.Piocher()
            jeu.pioche.show()
            m_klondike.exc = (0,1,2)
            m_game.exc = (2,)
        elif jeu.pioche.cible.collidepoint(ev.pos):
            source = jeu.pioche
        else:
            for s in jeu.stack:
                index = Rect(ev.pos,(0,0)).collidelistall(s.rects)
                if index:
                    stackindex = index[-1]
                    source = s
                    break
            else:
                index = Rect(ev.pos,(0,0)).collidelist([i.rect for i in jeu.home])
                if index > -1:
                    source = jeu.home[index]
        if source: foo = True

    elif ev.type == MOUSEBUTTONUP:
        if jeu.carte:
            display.update(scr.blit(ppp,spriterect,spriterect))

            aire = 0
            S = None
            for s in jeu.stack:
                x,y = spriterect.clip(s.rects[-1]).size
                if x*y > aire:
                    aire = x*y
                    S = s
            for h in jeu.home:
                x,y = spriterect.clip(h.rect).size
                if x*y > aire:
                    aire = x*y
                    S = h
            if S != None and jeu.PoserCarteSur(S):
                S.show()
                jeu.source.show()
                m_game.exc = (2,)
            else:
                jeu.ReposerCarte()
                jeu.source.show()

        elif source and ev.click[1] == 2:
            if jeu.PrendreCarteDans(source):
                for h in jeu.home:
                    if jeu.PoserCarteSur(h):
                        jeu.source.show()
                        h.show()
                        m_game.exc = (2,)
                        break
                else:
                    jeu.ReposerCarte()
        source = None
        foo = False

    elif ev.type == MOUSEMOTION and ev.buttons[0]:
        if foo:
            foo = False
            if isinstance(source,jeu.Pioche) and jeu.PrendreCarteDans(source):
                spriteimg = img_carte[jeu.carte.famille][jeu.carte.valeur]
                spriterect = spritecible = jeu.pioche.cible.copy()
                jeu.pioche.screen()
                ppp = scr.copy()
                display.update((jeu.pioche.rect,scr.blit(spriteimg,spriterect)))
            elif isinstance(source,jeu.Home) and jeu.PrendreCarteDans(source):
                spriteimg = img_carte[jeu.carte.famille][jeu.carte.valeur]
                spriterect = spritecible = source.rect.copy()
                source.screen()
                ppp = scr.copy()
                display.update(scr.blit(spriteimg,spriterect))
            elif jeu.PrendreCarteDans(source,stackindex):
                spritecible = source.rects[stackindex].copy()
                spriterect = source.rects[stackindex].unionall(source.rects[stackindex:])
                spriteimg = Surface(spriterect.size,SRCALPHA)
                y = 0
                for c in jeu.carte:
                    spriteimg.blit(img_carte[c.famille][c.valeur],(0,y))
                    y += s.spacing
                s.screen()
                ppp = scr.copy()
                display.update(scr.blit(spriteimg,spriterect))
        if jeu.carte:
            r = scr.blit(ppp,spriterect,spriterect)
            spriterect.move_ip(ev.rel)
            display.update((r,scr.blit(spriteimg,spriterect)))

    elif ev.type == QUIT: break

quit()