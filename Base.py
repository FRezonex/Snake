from Classes import *

pygame.init()

#Variables:
perdu = False
listeMorceaux = []

#Fenetre
largeur = 640
hauteur = 480
fenetre = pygame.display.set_mode((largeur, hauteur))

#Creation objets
fond = ElementGraphique(pygame.image.load("Fond.png").convert_alpha(), fenetre)
joueur = Joueur(pygame.image.load("Joueur.png").convert_alpha(), fenetre, 50, 50)
morceau = MorceauJoueur(pygame.image.load("Joueur.png").convert_alpha(), fenetre, 50, 50)
listeMorceaux.append(morceau)
point = Point(pygame.image.load("Point.png").convert_alpha(), fenetre)

#Timer
horloge = pygame.time.Clock()
continuer = True

#Boucle du jeu
while continuer:
    horloge.tick(60)

    #Script
    joueur.deplacer(largeur, hauteur)
    if joueur.collision(point):
        joueur.prendre(point)
        joueur.score += 1
        joueur.ajouterMorceau(listeMorceaux, fenetre, joueur)

    for morceau in listeMorceaux:
        morceau.deplacer(joueur)

    #Point
    if point.mort:
        point = Point(pygame.image.load("Point.png").convert_alpha(), fenetre)
        point.mort = False


    #Affichage
    fond.afficher()
    joueur.afficher()
    point.afficher()

    for morceau in listeMorceaux:
        morceau.afficher()


    #Game over
    if joueur.mort:
        print("Perdu")
        continuer = False









    #Truc
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    touche = pygame.key.get_pressed()
    if touche[pygame.K_ESCAPE]:
        continuer = False

pygame.quit()