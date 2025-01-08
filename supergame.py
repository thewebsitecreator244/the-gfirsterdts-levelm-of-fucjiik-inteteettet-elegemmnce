# Importer pygame et initialiser le module
import pygame
pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Définir la taille de la fenêtre et le titre
LARGEUR = 800
HAUTEUR = 600
TITRE = "supergame"
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

mario = pygame.image.load("")
pomme = pygame.image.load("")
boule = pygame.image.load("")

# Définir les variables du jeu
vitesse_mario = 5 # La vitesse de déplacement de Mario
x_mario = LARGEUR // 2 # La position initiale de Mario en x
y_mario = HAUTEUR - mario.get_height() # La position initiale de Mario en y
score = 0 # Le score du joueur
score_max = 0 # Le score maximum du joueur
vitesse_pomme = 3 # La vitesse de chute des pommes
x_pomme = 0 # La position initiale de la pomme en x
y_pomme = 0 # La position initiale de la pomme en y
vitesse_boule = 5 # La vitesse de chute des boules
x_boule = 0 # La position initiale de la boule en x
y_boule = 0 # La position initiale de la boule en y
jeu_en_cours = True # Un indicateur pour savoir si le jeu est en cours ou pas

# Créer une police pour afficher le texte
police = pygame.font.SysFont("Arial", 32)

# Créer une fonction pour afficher le score et le score maximum
def afficher_score():
    global score, score_max
    # Créer un texte avec le score
    texte_score = police.render(f"Score: {score}", True, NOIR)
    # Afficher le texte sur la fenêtre
    fenetre.blit(texte_score, (10, 10))
    # Si le score est supérieur au score maximum, le mettre à jour
    if score > score_max:
        score_max = score
    # Créer un texte avec le score maximum
    texte_score_max = police.render(f"Score max: {score_max}", True, NOIR)
    # Afficher le texte sur la fenêtre
    fenetre.blit(texte_score_max, (10, 50))

# Créer une fonction pour réinitialiser le jeu
def reinitialiser():
    global x_mario, y_mario, x_pomme, y_pomme, x_boule, y_boule, score, jeu_en_cours
    # Remettre Mario au centre
    x_mario = LARGEUR // 2
    y_mario = HAUTEUR - mario.get_height()
    # Remettre la pomme en haut à gauche
    x_pomme = 0
    y_pomme = 0
    # Remettre la boule en haut à droite
    x_boule = LARGEUR - boule.get_width()
    y_boule = 0
    # Remettre le score à zéro
    score = 0
    # Remettre le jeu en cours
    jeu_en_cours = True

# Créer une boucle principale
while True:
    # Gérer les événements
    for event in pygame.event.get():
        # Si l'événement est de fermer la fenêtre, quitter le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Si l'événement est d'appuyer sur une touche
        if event.type == pygame.KEYDOWN:
            # Si la touche est la flèche gauche, déplacer Mario vers la gauche
            if event.key == pygame.K_LEFT:
                x_mario -= vitesse_mario
            # Si la touche est la flèche droite, déplacer Mario vers la droite
            if event.key == pygame.K_RIGHT:
                x_mario += vitesse_mario
            # Si la touche est la barre d'espace et que le jeu n'est pas en cours, réinitialiser le jeu
            if event.key == pygame.K_SPACE and not jeu_en_cours:
                reinitialiser()

    # Remplir la fenêtre avec la couleur blanche
    fenetre.fill(BLANC)

    # Afficher Mario sur la fenêtre
    fenetre.blit(mario, (x_mario, y_mario))

    # Afficher la pomme sur la fenêtre
    fenetre.blit(pomme, (x_pomme, y_pomme))

    # Afficher la boule sur la fenêtre
    fenetre.blit(boule, (x_boule, y_boule))

    # Faire tomber la pomme vers le bas
    y_pomme += vitesse_pomme

    # Faire tomber la boule vers le bas
    y_boule += vitesse_boule

    # Si la pomme sort de la fenêtre, la remettre en haut à une position aléatoire en x
    if y_pomme > HAUTEUR:
        x_pomme = pygame.math.randint(0, LARGEUR - pomme.get_width())
        y_pomme = 0

    # Si la boule sort de la fenêtre, la remettre en haut à une position aléatoire en x
    if y_boule > HAUTEUR:
        x_boule = pygame.math.randint(0, LARGEUR - boule.get_width())
        y_boule = 0

    # Si Mario touche la pomme, augmenter le score et remettre la pomme en haut
    if pygame.Rect(x_mario, y_mario, mario.get_width(), mario.get_height()).colliderect(x_pomme, y_pomme, pomme.get_width(), pomme.get_height()):
        score += 1
        x_pomme = pygame.math.randint(0, LARGEUR - pomme.get_width())
        y_pomme = 0

    # Si Mario touche la boule, arrêter le jeu et afficher un message
    if pygame.Rect(x_mario, y_mario, mario.get_width(), mario.get_height()).colliderect(x_boule, y_boule, boule.get_width(), boule.get_height()):
        jeu_en_cours = False
        texte_perdu = police.render("Game Over ! Press SPACE to replay.", True, ROUGE)
        fenetre.blit(texte_perdu, (LARGEUR // 2 - texte_perdu.get_width() // 2, HAUTEUR // 2 - texte_perdu.get_height() // 2))

    # Afficher le score et le score maximum
    afficher_score()

    # Mettre à jour l'affichage
    pygame.display.update()