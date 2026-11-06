print("Programme de calcul d'aires et volumes")
import math

def aire_cercle(rayon):
    return math.pi * rayon**2

def aire_rectangle(longueur, largeur):
    return longueur * largeur

def volume_cylindre(rayon, hauteur):
    return aire_cercle(rayon) * hauteur

print("Aire du cercle (r=5) :", aire_cercle(5))
print("Aire du rectangle (L=4, l=3) :", aire_rectangle(4, 3))
print("Volume du cylindre (r=5, h=10) :", volume_cylindre(5, 10))
