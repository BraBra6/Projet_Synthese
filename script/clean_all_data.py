import pandas as pd
import os

# creer le dossier de sortie
os.makedirs("Data/processed", exist_ok=True)


# 1. ETUDIANTS
def clean_etudiants():
    df = pd.read_csv("Data/clean/etudiants_temporaires_clean.csv")

    # renommer la colonne nombre
    df = df.rename(columns={"nombre": "nombre_etudiants"})

    # nettoyer le texte
    df["categorie"] = df["categorie"].astype(str).str.strip().str.lower()
    df["detail"] = df["detail"].astype(str).str.strip().str.lower()

    # rendre certaines categories plus claires
    df["categorie"] = df["categorie"].replace(
        {
            "groupe d'âge": "age",
            "langue connue": "langue",
            "niveau d'études": "niveau_etude",
            "région de destination": "region",
            "principaux pays de naissance (ordre de 2022)": "pays",
            "permis initial": "type_permis",
            "permis multiples": "type_permis",
            "permis subséquent": "type_permis",
            "permis unique": "type_permis",
        }
    )

    # corriger detail pour les permis
    df["detail"] = df["detail"].replace(
        {
            "permis initial": "permis_initial",
            "permis multiples": "permis_multiples",
            "permis subséquent": "permis_subsequent",
            "permis unique": "permis_unique",
        }
    )

    # remplacer les espaces par _
    df["detail"] = df["detail"].str.replace(" ", "_", regex=False)

    # convertir les colonnes numeriques
    df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
    df["nombre_etudiants"] = pd.to_numeric(df["nombre_etudiants"], errors="coerce")

    # supprimer les lignes invalides
    df = df.dropna(subset=["categorie", "detail", "annee", "nombre_etudiants"])

    # convertir en int
    df["annee"] = df["annee"].astype(int)
    df["nombre_etudiants"] = df["nombre_etudiants"].astype(int)

    # supprimer les doublons
    df = df.drop_duplicates(subset=["categorie", "detail", "annee"])

    # trier
    df = df.sort_values(["annee", "categorie", "detail"])

    # exporter
    df.to_csv("Data/processed/etudiants_final.csv", index=False)
    print("etudiants final cree")


# 2. PERMANENTS


def clean_permanents():
    df = pd.read_csv("Data/clean/permanent_immigration_qc_clean_2020_2021.csv")

    # renommer la colonne nombre
    df = df.rename(columns={"nombre": "nombre_immigrants"})

    # nettoyer le texte
    df["categorie"] = df["categorie"].astype(str).str.strip().str.lower()
    df["detail"] = df["detail"].astype(str).str.strip().str.lower()

    # simplifier certaines categories
    df["categorie"] = df["categorie"].replace(
        {
            "catégorie d'immigration": "type_immigration",
            "groupe d'âge": "age",
            "région de destination projetée": "region_destination",
            "immigration totale": "immigration_totale",
            "connaissance du français et de l'anglais": "langue_connue",
            "connaissance du français et de l'anglais (travailleurs qualifiés âgés de 18 ans et plus)": "langue_travailleurs_qualifies",
            "sexe": "sexe",
        }
    )

    # raccourcir les categories de region de naissance
    df["categorie"] = df["categorie"].str.replace(
        "continent et région de naissance ", "region_naissance_", regex=False
    )

    # petites corrections pour rendre tout plus uniforme
    df["categorie"] = df["categorie"].replace(
        {
            "region_naissance_amérique": "region_naissance_amerique",
            "region_naissance_océanie et autres lieux": "region_naissance_oceanie_autres_lieux",
        }
    )

    # detail plus propre
    df["detail"] = df["detail"].str.replace(" ", "_", regex=False)

    # convertir les colonnes numeriques
    df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
    df["nombre_immigrants"] = pd.to_numeric(df["nombre_immigrants"], errors="coerce")

    # supprimer les lignes invalides
    df = df.dropna(subset=["categorie", "detail", "annee", "nombre_immigrants"])

    # convertir en int
    df["annee"] = df["annee"].astype(int)
    df["nombre_immigrants"] = df["nombre_immigrants"].astype(int)

    # supprimer les doublons
    df = df.drop_duplicates(subset=["categorie", "detail", "annee"])

    # trier
    df = df.sort_values(["annee", "categorie", "detail"])

    # exporter
    df.to_csv("Data/processed/permanents_final.csv", index=False)
    print("permanents final cree")


# 3. CSQ


def clean_csq():
    df = pd.read_csv("Data/clean/csq_clean_2016_2023.csv")

    # renommer certaines colonnes
    df = df.rename(
        columns={
            "Details": "detail",
            "Description": "description",
            "nombre": "nombre_csq",
        }
    )

    # nettoyer le texte
    df["categorie"] = df["categorie"].astype(str).str.strip().str.lower()
    df["description"] = df["description"].astype(str).str.strip().str.lower()
    df["detail"] = df["detail"].astype(str).str.strip().str.lower()

    # simplifier quelques categories
    df["categorie"] = df["categorie"].replace(
        {
            "caractère sexuel": "sexe",
            "réfugiés et personnes en situation semblable": "refugies",
            "regroupement familial": "regroupement_familial",
            "autres immigrants": "autres_immigrants",
            "immigration économique": "immigration_economique",
            "mouvement spécial": "mouvement_special",
            "âge": "age",
        }
    )

    # remplacer les espaces par _
    df["description"] = df["description"].str.replace(" ", "_", regex=False)
    df["detail"] = df["detail"].str.replace(" ", "_", regex=False)

    # petite correction de coherence
    df["description"] = df["description"].replace({"groupe_d'âge": "groupe_age"})

    # convertir les colonnes numeriques
    df["annee"] = pd.to_numeric(df["annee"], errors="coerce")
    df["nombre_csq"] = pd.to_numeric(df["nombre_csq"], errors="coerce")

    # garder seulement les lignes valides
    df = df.dropna(subset=["categorie", "description", "detail", "annee"])

    # remplacer les valeurs manquantes de nombre par 0
    df["nombre_csq"] = df["nombre_csq"].fillna(0)

    # convertir en int
    df["annee"] = df["annee"].astype(int)
    df["nombre_csq"] = df["nombre_csq"].astype(int)

    # supprimer les doublons
    df = df.drop_duplicates(subset=["categorie", "description", "detail", "annee"])

    # trier
    df = df.sort_values(["annee", "categorie", "description", "detail"])

    # exporter
    df.to_csv("Data/processed/csq_final.csv", index=False)
    print("csq final cree")


# EXECUTION

clean_etudiants()
clean_permanents()
clean_csq()

print("les 3 fichiers ont ete nettoyes")
