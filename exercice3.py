
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes/31536000)
    secondeRestanteAnnee = secondes % 31536000

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines =  int(secondeRestanteAnnee / 604800)
    secondeRestanteSemaine = secondeRestanteAnnee % 604800

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int(secondeRestanteSemaine/86400)
    secondeRestanteJour= secondeRestanteSemaine%86400

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int (secondeRestanteJour/3600)
    secondeRestanteHeur =  secondeRestanteJour%3600

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int(secondeRestanteHeur/60)
    secondeRestanteMinute = secondeRestanteHeur % 60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondeRestanteMinute

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
