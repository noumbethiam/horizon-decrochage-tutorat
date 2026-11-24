# Journal de bord

## 18/11/2026

**Fait**
- Dépôt GitHub créé et premier commit (GP-01)
- Trello créé avec les 30 tâches (GP-02)
- Journal de bord et registre des risques créés (GP-03)
- Audit de etudiants.csv : doublons, modalités non harmonisées, valeurs manquantes, colonnes numériques lues comme du texte

**Prévu**
- Lancer value_counts sur les colonnes de catégories
- Nettoyer etudiants.csv (DA-02)

**Blocages**
- Aucun

**Heures** : 6 h

## 20/11/2026

**Fait**
- Nettoyage complet de etudiants.csv (5085 à 5000 lignes), sauvegardé dans data/processed/ (DA-02)
- Nettoyage de inscriptions.csv (5024 à 4990 lignes), sauvegardé dans data/processed/ (DA-03)
- Audit de etudiants.csv et inscriptions.csv (partie de DA-01)

**Prévu**
- Auditer et nettoyer activite_hebdo.csv et tutorat.csv (DA-04)
- Auditer et nettoyer messages.csv (DA-05)
- Terminer DA-01 (audit des 5 fichiers)

**Blocages et erreurs**
- NameError sur df_etudiants : Python oublie les variables quand VS Code est fermé, relancer les cellules de chargement
- KeyError sur id_etudiant : le nom de la colonne contenait un espace à la fin
- Valeurs de boursier codées 0 et 1 non confirmées par LISEZMOI.md : hypothèse notée

**Heures** : environ 1 h 55 (13 h 50 à 14 h 40, 19 h 17 à 20 h 13, 21 h 10 à 21 h 18, pauses déduites)

## 21/11/2026

**Fait**
- Nettoyage de activite_hebdo, tutorat et messages (DA-04, DA-05)
- 10 tests automatiques (pytest) et journal de nettoyage complet (DA-06)
- Construction de base_survie.csv : T, E, tutorat (DA-07, presque fini)

**Prévu**
- Format période-personne pour finir DA-07
- Analyse exploratoire (DA-08), Kaplan-Meier et log-rank (SV-01)

**Blocages et erreurs**
- Mon contrôle des noms ne trouvait que « Je suis », pas « c'est » : règle ajoutée
- 9 étudiants dont le tutorat commence après leur départ : lignes gardées, à traiter dans le DAG (CA-01)

**Heures** : environ 1 h 10 (17 h 08 à 18 h 18)
## 23/11/2026

**Fait**
- Format période-personne (periode_personne.csv, 121934 lignes) : DA-07 terminée

**Prévu**
- Analyse exploratoire (DA-08), Kaplan-Meier et log-rank (SV-01)

**Blocages et erreurs**
- Aucun

**Heures** : [heures du 23/11]

## 24/11/2026

**Fait**
- Analyse exploratoire : profils, taux de censure (71,2 %), deux périodes critiques (DA-08)
- Kaplan-Meier global et par groupe, tests du log-rank, semaines critiques (SV-01)

**Prévu**
- Modèle de Cox et vérification de la proportionnalité (SV-02)
- DAG et choix de la méthode contre le biais du temps immortel (CA-01)

**Blocages et erreurs**
- Aucun

**Heures** : Environ 3h