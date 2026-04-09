# Produit scalaire de deux vecteurs avec une boucle for

print("Calcul du produit scalaire de deux vecteurs")
print("-" * 45)

# Vecteurs d'exemple
vecteur1 = [1, 2, 3]
vecteur2 = [4, 5, 6]

print(f"Vecteur 1 : {vecteur1}")
print(f"Vecteur 2 : {vecteur2}")

produit_scalaire = 0

for i in range(len(vecteur1)):
    produit_scalaire += vecteur1[i] * vecteur2[i]
    print(f"Étape {i+1} : {vecteur1[i]} × {vecteur2[i]} = {vecteur1[i] * vecteur2[i]}, somme partielle : {produit_scalaire}")

print("-" * 45)
print(f"Produit scalaire (vecteur1 · vecteur2) = {produit_scalaire}")