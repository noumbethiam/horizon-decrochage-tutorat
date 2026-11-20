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