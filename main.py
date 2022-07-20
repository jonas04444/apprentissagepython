
controleur_list = ["philipe","jonathan"]

with open("controleurs.txt", "w+") as file:
    for controleur in controleur_list:
        file.write(controleur + "\n")

file.close()