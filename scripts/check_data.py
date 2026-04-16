import pandas as pd


def check_dataset(path, name):
    print(f"\n {name} ")

    df = pd.read_csv(path)

    print("\n✔ Dimensions :")
    print(df.shape)

    print("\n✔ Colonnes :")
    print(df.columns.tolist())

    print("\n✔ Types :")
    print(df.dtypes)

    print("\n✔ Valeurs manquantes :")
    print(df.isna().sum())

    print("\n✔ Exemple de données :")
    print(df.sample(5))

    print("\n✔ Valeurs uniques categorie :")
    print(df["categorie"].unique())

    print("\n✔ Doublons logiques :")
    print(df.duplicated(subset=df.columns.tolist()).sum())


# Vérifier les 3 fichiers
check_dataset("Data/processed/etudiants_final.csv", "ETUDIANTS")
check_dataset("Data/processed/permanents_final.csv", "PERMANENTS")
check_dataset("Data/processed/csq_final.csv", "CSQ")
