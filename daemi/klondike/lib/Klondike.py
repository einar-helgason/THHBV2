from random import shuffle


class Options(object):

    Donnes = 3
    NouvelleDonne = True

    @staticmethod
    def update(**options):
        for option,value in options.items():
            if option == "Donnes":
                setattr(Options,"Donnes",value)
                Options.NouvelleDonne = True
            elif option == "NouvelleDonne":
                setattr(Options,"NouvelleDonne",value)
                if Options.NouvelleDonne == False:
                    Options.Donnes = 1
            break


class Klondike(object):

    class Carte(object):

        def __init__(self,famille,valeur):
            self.valeur  = valeur
            self.famille = famille
            self.couleur = famille&1
            self.status  = True

    class Pioche(list):

        def Piocher(self):
            if self.index == 0:
                if Options.NouvelleDonne: self.index = len(self)
                return False
            self.index -= Options.Donnes
            if self.index < 0: self.index = 0
            return True

        def PrendreCarte(self):
            if self.index < len(self):
                return self.pop(self.index)
            return False

        def ReposerCarte(self,carte):
            self.insert(self.index,carte)

    class Stack(list):

        def PoserCarte(self,carte):
            if isinstance(carte,Klondike.Carte): carte = [carte]
            if (not self and carte[0].valeur == 12) or (self and self[-1].couleur != carte[0].couleur and self[-1].valeur == carte[0].valeur + 1):
                self.extend(carte)
                return True
            return False

        def PrendreCarte(self,index):
            if self[index].status:
                cartes = self[index:]
                del(self[index:])
                return cartes
            return False

        def ReposerCarte(self,carte):
            self.extend(carte)


    class Home(list):

        def PoserCarte(self,carte):
            if not isinstance(carte,Klondike.Carte):
                if len(carte) == 1: carte = carte[0]
                else: return False
            if (not self and carte.valeur == 0) or\
               (self and carte.valeur == self[-1].valeur + 1 and carte.famille == self[-1].famille):
                   self.append(carte)
                   return True
            return False

        def PrendreCarte(self):
            if self: return self.pop()
            return False

        def ReposerCarte(self,carte):
            self.append(carte)

    def __init__(self):
        self.stack = [Klondike.Stack(),Klondike.Stack(),Klondike.Stack(),Klondike.Stack(),Klondike.Stack(),Klondike.Stack(),Klondike.Stack()]
        self.home = [Klondike.Home(),Klondike.Home(),Klondike.Home(),Klondike.Home()]
        self.pioche = Klondike.Pioche()
        self.NouvellePartie()

    def NouvellePartie(self):
        cartes = [Klondike.Carte(famille, valeur) for famille in range(4) for valeur in range(13)]
        shuffle(cartes)

        for s in self.stack:
            s[:] = []

        for rang in range(7):
            for tirage in range(rang):
                self.stack[rang].append(cartes.pop())
                self.stack[rang][-1].status = False
            self.stack[rang].append(cartes.pop())

        for h in self.home:
            h[:] = []

        self.pioche[:] = cartes
        self.pioche.index = len(self.pioche)
        self.carte = None
        self.hist = None


    def Piocher(self):
        self.hist = None,None,None,None,self.pioche.index
        return self.pioche.Piocher()

    def PrendreCarteDans(self,stack,index=-1):
        if not isinstance(stack,Klondike.Stack):
            self.carte = stack.PrendreCarte()
        else:
            self.carte = stack.PrendreCarte(index)
        if self.carte:
            self.source = stack
            return True
        return False

    def PoserCarteSur(self,stack):
        stackcopy = stack[:]
        if stack.PoserCarte(self.carte):
            self.hist = self.carte,self.source,stack,stackcopy,None
            self.carte = None
            if self.source: self.source[-1].status = True
            return True
        return False

    def ReposerCarte(self):
        self.source.ReposerCarte(self.carte)
        self.carte = None

    def Undo(self):
        if self.hist:
            carte,source,stack,stackcopy,index = self.hist
            self.hist = None
            if index:
                self.pioche.index = index
                return (self.pioche,)
            else:
                if isinstance(source,Klondike.Stack) and source: source[-1].status = False
                source.ReposerCarte(carte)
                stack[:] = stackcopy
                return source,stack
        return False

    @property
    def CartesPiochees(self):
        return self.pioche[self.pioche.index:self.pioche.index+Options.Donnes]

    @property
    def RestePioche(self):
        return self.pioche.index > 0

