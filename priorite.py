from timeit import default_timer as timer

from chemins import rechercheChemins
from LP import analyseAttentes, analyseRobustesse, repartitionDurees

def cheminPrioritaire(carrefour):
    print("Demandes:", carrefour.demandesPriorite, '\n')
    
    begin = timer()
    
    # Calcule tous les chemins possibles
    cheminsPossibles = rechercheChemins(carrefour)
    
    # Analyse chacun des chemins avec la LP
    cheminsFaisables = []
    
    for chemin in cheminsPossibles:
#        print(chemin, '\n')
#        analyseAttentes(chemin, True)
#        print(chemin.resultat, '\n')
        analyseAttentes(chemin)
        if chemin.resultat:
            cheminsFaisables.append(chemin)
    
    # Trouve le meilleur chemin
    cheminsFaisables.sort(key=lambda chemin: chemin.resultat.score)
#    meilleurChemin = cheminsFaisables[0]
    
#    print("Analyse Robustesse: ", '\n')
    for chemin in cheminsFaisables:
        analyseRobustesse(chemin)
#        print(chemin, '\n')
#        print(chemin.resultat, '\n')
        if all(retard >= 0.2*demande.delaiApproche for retard,demande \
               in zip(chemin.resultat.retards, carrefour.demandesPriorite) ):
            meilleurChemin = chemin
            break
    else:
        cheminsFaisables.sort(key=lambda chemin: min(chemin.resultat.retards) )
        meilleurChemin = cheminsFaisables[0]
#    
#    # Derniere repartition des durees pour garder les proportions le plus possible
    repartitionDurees(meilleurChemin)
    
    end = timer()
    
    
#    for chemin in cheminsFaisables:
#        print(chemin, '\n')
#        print(chemin.resultat, '\n')
    print("Meilleur chemin:", '\n')
    print(meilleurChemin, '\n')
    print(meilleurChemin.resultat, '\n')
    print("Chemins analyses:", len(cheminsPossibles) )
    print("Temps:", 1000*(end-begin), "ms", '\n\n\n\n')
#    
    # Returns
    return meilleurChemin

#    return 60, carrefour.phaseActuelle
