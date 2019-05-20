import pygame
from random import *


#Classes
class ElementGraphique():

    def __init__(self, image, fenetre, x=0, y=0):

        self.fenetre = fenetre
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def collision(self, objet):
        if self.rect.colliderect(objet.rect):
            return True
        return False

class Objet(ElementGraphique):

    def __init__(self, image, fenetre, x=0, y=0):
        super().__init__(image, fenetre, x, y)

        self.mort = False


class MorceauJoueur(ElementGraphique):
    def __init__(self, image, fenetre, x=0, y=0):
        super().__init__(image, fenetre, x, y)

    def placer(self, joueur, listeMorceaux):
        if joueur.direction == "droite":
            self.rect.x = listeMorceaux[-1].rect.x - joueur.dimension
            self.rect.y = listeMorceaux[-1].rect.y
        elif joueur.direction == "gauche":
            self.rect.x = listeMorceaux[-1].rect.x + joueur.dimension
            self.rect.y = listeMorceaux[-1].rect.y
        elif joueur.direction == "bas":
            self.rect.x = listeMorceaux[-1].rect.x
            self.rect.y = listeMorceaux[-1].rect.y - joueur.dimension
        else:
            self.rect.x = listeMorceaux[-1].rect.x
            self.rect.y = listeMorceaux[-1].rect.y + joueur.dimension

    def deplacer(self, joueur):
        if joueur.direction == "droite":
            self.rect.x += joueur.vitesse
        elif joueur.direction == "gauche":
            self.rect.x -= joueur.vitesse
        elif joueur.direction == "bas":
            self.rect.y += joueur.vitesse
        else:
            self.rect.y -= joueur.vitesse

    


class Joueur(Objet):

    def __init__(self, image, fenetre, x=0, y=0):
        super().__init__(image, fenetre, x, y)

        self.dimension = 15
        self.direction = "droite"
        self.vitesse = 6
        self.score = 0
        self.nbMorceaux = 0

    def deplacer(self, largeur, hauteur):

        touche = pygame.key.get_pressed()

        #Changement de direction
        if  touche[pygame.K_d] and self.direction != "gauche":
            self.direction = "droite"
        if  touche[pygame.K_a] and self.direction != "droite":
            self.direction = "gauche"
        if  touche[pygame.K_s] and self.direction != "haut":
            self.direction = "bas"
        if  touche[pygame.K_w] and self.direction != "bas":
            self.direction = "haut"

        #Avancement
        if self.direction == "droite":
            self.rect.x += self.vitesse
        if self.direction == "gauche":
            self.rect.x -= self.vitesse
        if self.direction == "bas":
            self.rect.y += self.vitesse
        if self.direction == "haut":
            self.rect.y -= self.vitesse

        #Test collisions murs
        if self.rect.x > largeur - self.dimension*3 or self.rect.x < self.dimension*2 or self.rect.y > hauteur - self.dimension*3 or self.rect.y < self.dimension*2:
            self.mort = True

    def prendre(self, objet):
        objet.mort = True

    def ajouterMorceau(self, listeMorceaux, fenetre, joueur):
        morceau = MorceauJoueur(pygame.image.load("Joueur.png").convert_alpha(), fenetre)
        morceau.placer(joueur, listeMorceaux)
        listeMorceaux.append(morceau)




class Point(Objet):

    def __init__(self, image, fenetre, x=0, y=0):
        super().__init__(image, fenetre, x, y)

        self.rect.x = randrange(30, 595)
        self.rect.y = randrange(30, 435)











