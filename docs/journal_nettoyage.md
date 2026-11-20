# Journal de nettoyage

## Table etudiants (5085 lignes avant, 5000 après)

1. **Noms de colonnes** : `id_etudiant ` avait un espace final, `Distance campus (km)` était mal formaté. Espaces retirés, colonne renommée `distance_campus_km`, pour des noms utilisables sans erreur.
2. **genre** : 10 écritures pour 2 valeurs, 407 lignes. Recodage en M / F, pour des groupes cohérents.
3. **boursier** : 12 écritures pour 2 valeurs, 513 lignes. Recodage en Oui / Non. Hypothèse : 0 = Non et 1 = Oui (97 lignes), non confirmée par LISEZMOI.md, retenue car c'est la convention courante.
4. **emploi_parallele** : 205 valeurs manquantes. Conservées vides, car inventer une réponse fausserait les analyses.
5. **filiere** : 22 écritures pour 5 filières, 458 lignes. Recodage. Hypothèse : Com, GC et INFO désignent chacune une seule filière.
6. **mention_bac** : 15 écritures pour 4 mentions, 349 lignes recodées. 154 valeurs manquantes conservées vides.
7. **region_origine** : 28 écritures pour 14 régions, 256 lignes recodées. Hypothèse : Zig = Ziguinchor. 91 valeurs manquantes conservées vides.
8. **age** : 46 valeurs avec le texte « ans », converties en nombres. 14 valeurs impossibles (0, 3, 99, 150, 210) mises à vide, car LISEZMOI.md attend 17 à 35 et on ne devine pas l'âge réel. 86 valeurs vides au total.
9. **note_bac** : 250 virgules décimales converties en points. 18 valeurs aberrantes (-2, 0, 25.5, 112, 135) mises à vide, car la plage attendue est 10 à 20.
10. **distance_campus_km** : 238 valeurs avec virgule ou « km » converties. 25 valeurs impossibles mises à vide (15 négatives ou nulles, 10 valeurs codées 9999). Distances élevées (jusqu'à 546,1 km) conservées : plausibles et sans maximum imposé, à surveiller en modélisation.
11. **id_etudiant** : 25 identifiants mal formatés (minuscules, espaces), corrigés au format HZ + 5 chiffres.
12. **Doublons** : 61 doublons exacts supprimés. 24 étudiants en double qui ne différaient que par la distance : première ligne gardée, car aucune date de saisie ne permet de choisir.

## Table inscriptions (5024 lignes avant, 4990 après)

1. **Structure** : séparateur point-virgule, précisé à la lecture.
2. **statut_final** : 12 écritures pour 3 valeurs, 400 lignes recodées. 41 valeurs manquantes conservées vides : elles ressemblent à des « inscrit » (sans date de fin), à trancher avec activite_hebdo.
3. **Dates** : 4 formats mélangés dans date_debut et date_fin, convertis en vraies dates (jj/mm/aaaa confirmé par des dates comme 27/10/2024).
4. **Dates inversées** : 12 lignes avec une fin avant le début, tous des abandons. Dates échangées, car chaque ligne redevient cohérente.
5. **Fins trop tardives** : 6 dates de fin en 2027, au-delà des 30 semaines. Mises à vide, statut abandon conservé.
6. **Abandons sans date de fin** : 22 lignes, conservées, à traiter avec la règle des 4 semaines.
7. **Doublons** : 20 doublons exacts supprimés.
8. **Inscriptions orphelines** : 14 identifiants absents de etudiants, supprimés : HZ96836, HZ99803, HZ97757, HZ98126, HZ96440, HZ92314, HZ95264, HZ92645, HZ98611, HZ92894, HZ95618, HZ97985, HZ94863, HZ96554.
9. **Étudiants sans inscription** : 10 étudiants conservés dans etudiants (HZ26334, HZ59964, HZ98561, HZ48786, HZ57625, HZ92422, HZ55371, HZ20355, HZ10213, HZ64225), à recroiser avec activite_hebdo.