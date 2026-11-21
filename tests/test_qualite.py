from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).resolve().parent.parent / "data" / "processed"


def charger(nom):
    return pd.read_csv(PROCESSED / f"{nom}.csv")


def test_etudiants_identifiants_uniques_et_bien_formes():
    df = charger("etudiants")
    assert len(df) == 5000
    assert df["id_etudiant"].is_unique
    assert df["id_etudiant"].str.match(r"^HZ[0-9]{5}$").all()


def test_etudiants_modalites_harmonisees():
    df = charger("etudiants")
    assert set(df["genre"]) <= {"F", "M"}
    assert set(df["boursier"]) <= {"Oui", "Non"}
    assert set(df["filiere"]) <= {"Informatique", "Gestion", "Droit", "Communication", "Génie civil"}
    assert set(df["mention_bac"].dropna()) <= {"Passable", "Assez bien", "Bien", "Très bien"}


def test_etudiants_valeurs_dans_les_plages():
    df = charger("etudiants")
    assert df["age"].dropna().between(17, 35).all()
    assert df["note_bac"].dropna().between(10, 20).all()
    assert (df["distance_campus_km"].dropna() > 0).all()


def test_inscriptions_coherentes_avec_etudiants():
    insc = charger("inscriptions")
    etu = charger("etudiants")
    assert insc["id_etudiant"].is_unique
    assert set(insc["id_etudiant"]) <= set(etu["id_etudiant"])
    assert set(insc["statut_final"].dropna()) <= {"inscrit", "abandon", "transfert"}


def test_inscriptions_dates_coherentes():
    insc = charger("inscriptions")
    debut = pd.to_datetime(insc["date_debut"])
    fin = pd.to_datetime(insc["date_fin"])
    a_une_fin = fin.notna()
    assert (fin[a_une_fin] >= debut[a_une_fin]).all()
    semaines = (fin[a_une_fin] - debut[a_une_fin]).dt.days / 7
    assert (semaines <= 30).all()


def test_activite_semaines_dans_1_30():
    act = charger("activite_hebdo")
    assert act["semaine"].between(1, 30).all()


def test_activite_bornes_des_variables():
    act = charger("activite_hebdo")
    assert act["devoirs_rendus"].dropna().between(0, 2).all()
    assert act["absences"].between(0, 20).all()
    assert act["note_moyenne"].dropna().between(0, 20).all()
    assert (act["nb_connexions_lms"].dropna() >= 0).all()


def test_activite_une_ligne_par_etudiant_et_semaine():
    act = charger("activite_hebdo")
    assert not act.duplicated(subset=["id_etudiant", "semaine"]).any()


def test_tutorat_regles_de_qualite():
    tut = charger("tutorat")
    etu = charger("etudiants")
    assert tut["id_etudiant"].is_unique
    assert set(tut["id_etudiant"]) <= set(etu["id_etudiant"])
    assert set(tut["type_tuteur"]) <= {"pair", "enseignant"}
    assert tut["semaine_debut"].dropna().between(1, 30).all()
    assert (tut["nb_seances"].dropna() >= 0).all()


def test_messages_pseudonymises():
    msg = charger("messages")
    assert msg["id_message"].is_unique
    assert msg["semaine"].between(1, 30).all()
    assert not msg["texte"].str.contains("@", na=False).any()