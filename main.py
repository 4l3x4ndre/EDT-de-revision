from datetime import datetime, timedelta

jours_a_remonter = [0, 3, 5, 8, 13, 21]
jours_noms = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
jours_noms_FR = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

emploi_du_temps = [
    {'Lundi': ['histoire', 'français']},
    {'Mardi': ['maths']},
    {'Mercredi': ['histoire']},
    {'Jeudi': ['maths', 'français']},
    {'Vendredi': ['histoire', 'maths', 'français']},
    {'Samedi': []},
    {'Dimanche': []}
]


def main():

    print("-----------")
    # Affiche le jour et le mois. Les "str" servent à convertir les nombres en chaines de caractères pour pouvoir
    # les ajouter avec le "/"
    print("Aujourd'hui", str(datetime.now().day) + '/' + str(datetime.now().month), "vous devez réviser:")

    # Parcourt la liste des jours: 3eme, 5eme, ...
    for nombre_de_jours_a_remonter in jours_a_remonter:

        # Recupere le jour sous forme de chiffre
        jour_a_reviser = datetime.now() - timedelta(days=nombre_de_jours_a_remonter)

        # Va chercher l'index du jour dans le tableau anglais pour selectionner le jour equivalent en français.
        # maliste.index(element) permet de trouver l'index de "element" dans la liste "maliste"
        index_du_jour_a_reviser = jours_noms.index(jour_a_reviser.strftime('%A'))
        nom_du_jour = jours_noms_FR[index_du_jour_a_reviser]
        
        # Accès au matiere de ce jour. Première paire de crochers pour le dictionnaire, puis pour la liste des matieres.
        matieres = emploi_du_temps[index_du_jour_a_reviser][nom_du_jour]
        if (len(matieres) == 0): # S'il n'y a pas de matière, on affiche pas le jour et on continue le tour suivant de la boucle
            continue

        # Commence a écrire du texte. Si plusieurs matières, ajout d'un -s
        # end="" permet de ne pas revenir à la ligne au prochain print()
        print("Le", end="")
        if (len(matieres) > 1):
            print("s", end="")

        # Affiche le jour de la semaine en lettre, puis le jour du mois, puis le mois.
        print(" cours du", nom_du_jour, str(jour_a_reviser.day) + '/' + str(jour_a_reviser.month), ": ", end="")

        # Affiche les matères les unes après les autres sur une même ligne
        for matiere in matieres:
            print(matiere, end=" ")
        
        # Revient a la ligne, puis saute une ligne
        print()
        print()


main()