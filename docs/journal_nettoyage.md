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


## Table activite_hebdo (130967 lignes avant, 129837 après)

1. **nb_connexions_lms** : 1298 valeurs manquantes conservées vides. 57 valeurs impossibles mises à vide (45 négatives et 12 comprises entre 3604 et 8636, alors que les valeurs normales vont de 0 à 26), car on ne devine pas le vrai nombre.
2. **devoirs_rendus** : 30 valeurs hors de 0 à 2 (3, 4 et 7), mises à vide.
3. **semaine** : 70 lignes avec une semaine hors de 1 à 30 (-1, 0, 31, 32, 99), supprimées. Sans semaine valide, une ligne ne peut pas être placée dans le temps.
4. **note_moyenne** : virgules décimales remplacées par des points et conversion en nombres. 135 notes hors de 0 à 20 mises à vide. Les cases vides d'origine (semaines sans évaluation) sont normales et conservées.
5. **Doublons exacts** : 890 lignes supprimées.
6. **Semaines répétées** : 170 couples (étudiant, semaine) en double. Dans 167 couples, seul le nombre de connexions diffère, et 3 couples diffèrent aussi par les devoirs ou la note. Première ligne gardée, car rien ne permet de choisir.
7. **Cohérence avec etudiants** : aucun identifiant inconnu, et les 5000 étudiants ont de l'activité (y compris les 10 sans inscription).

## Table tutorat (1291 lignes avant, 1255 après)

1. **Nom de colonne** : `ID Etudiant` renommé `id_etudiant`.
2. **type_tuteur** : 9 écritures pour 2 valeurs (pair, enseignant). Hypothèses : « étudiant » désigne un tuteur pair et « Prof » un enseignant.
3. **Doublons exacts** : 30 lignes supprimées.
4. **Identifiants inconnus** : 6 lignes supprimées car absentes de etudiants (HZ81487, HZ82856, HZ84311, HZ84721, HZ88180, HZ88484).
5. **semaine_debut** : 10 valeurs hors de 1 à 30 (0, 45 et 52) mises à vide. Lignes conservées : l'étudiant a bien été tutoré, seule la date est fausse. À traiter dans base_survie.
6. **nb_seances** : 8 valeurs négatives mises à vide, et 8 valeurs manquantes d'origine conservées.

## Table messages (3200 lignes avant, 3200 après)

1. **Encodage** : UTF-8 correct, aucune correction. Aucun doublon, aucune semaine hors plage, aucun identifiant inconnu.
2. **texte** : 7 valeurs manquantes conservées vides.
3. **Données personnelles** : 33 e-mails remplacés par [EMAIL], 45 numéros de téléphone par [TELEPHONE], et 96 noms complets par [NOM] (45 après « Je suis », 51 après « c'est »). Aucune donnée personnelle ne doit atteindre un assistant IA externe.
4. **Limite connue** : un prénom seul, ou un nom écrit en minuscules, ne serait pas détecté par ces règles.

## Hypothèses et points ouverts

- boursier : 0 et 1 recodés en Non et Oui, sans confirmation du dictionnaire des données.
- inscriptions : 41 statuts vides et 22 abandons sans date de fin, à trancher avec la règle des 4 semaines.
- 10 étudiants sans inscription, conservés.
- Distances jusqu'à 546,1 km conservées : plausibles, sans maximum imposé.

## Tableau avant / après

| Table | Lignes avant | Lignes après | Vides avant | Vides après | Doublons avant | Doublons après |
|---|---|---|---|---|---|---|
| etudiants | 5085 | 5000 | 522 | 567 | 60 | 0 |
| inscriptions | 5024 | 4990 | 3931 | 3909 | 20 | 0 |
| activite_hebdo | 130967 | 129837 | 74872 | 74454 | 870 | 0 |
| tutorat | 1291 | 1255 | 8 | 26 | 30 | 0 |
| messages | 3200 | 3200 | 7 | 7 | 0 | 0 |

Les valeurs manquantes augmentent pour etudiants et tutorat car les valeurs impossibles ont été mises à vide. Elles baissent pour inscriptions et activite_hebdo car les lignes supprimées contenaient elles-mêmes des cases vides. Pour inscriptions, les lignes comptées « avant » sont les 5024 lignes brutes (dont 20 doublons exacts).