# Projet de synthèse – Analyse des données d'immigration au Québec

## Description du projet

Ce projet vise à développer un **système d’analyse décisionnelle** permettant d’explorer et d’analyser des données ouvertes liées à l’immigration au Québec.

Les données utilisées proviennent principalement du portail **Données Québec** et incluent plusieurs ensembles de données concernant :

- les étudiants internationaux
- les admissions permanentes
- les certificats de sélection du Québec (CSQ)

L’objectif du projet est de transformer ces données brutes en **informations exploitables** à l’aide d’outils d’analyse de données et de visualisation.

---

# Objectifs du projet

Les objectifs principaux sont :

- Identifier des jeux de données ouverts liés à l’immigration au Québec
- Nettoyer et préparer les données
- Structurer les données dans une base de données relationnelle
- Réaliser des analyses à l’aide de SQL et Python
- Concevoir un tableau de bord interactif pour visualiser les résultats

---

# Jeux de données utilisés

## Étudiants internationaux – permis d’études (2018–2022)

Contient des informations sur les permis d’études délivrés aux étudiants internationaux au Québec.

Variables principales :

- groupe d’âge
- niveau d’études
- région de destination
- pays de naissance
- langues connues

---

## Admissions permanentes au Québec

Dataset contenant des informations sur les admissions permanentes selon différentes caractéristiques démographiques.

Variables principales :

- groupe d’âge
- région de naissance
- catégorie d’immigration

---

## Certificats de sélection du Québec (CSQ)

Dataset présentant les certificats de sélection délivrés selon différents programmes d’immigration entre **2016 et 2023**.

---

# Technologies utilisées

Le projet utilise plusieurs outils d’analyse de données :

- **Excel** – nettoyage initial des données
- **Python (Pandas)** – nettoyage avancé et automatisation
- **SQL Server** – stockage et requêtes analytiques
- **Power BI** – visualisation des données

---

# Structure du projet

```
Projet_Synthese/

data/
   raw/        → datasets bruts
   clean/      → datasets nettoyés

excel/
   nettoyage_donnees.xlsx

python/
   eda.ipynb
   cleaning.ipynb

sql/
   database_schema.sql
   queries.sql

dashboard/
   powerbi_dashboard.pbix


```

---

# Étapes du projet

Le projet est organisé selon le plan de travail suivant :

1. Définition de la problématique
2. Recherche bibliographique
3. Exploration des données
4. Nettoyage initial des données (Excel)
5. Nettoyage avancé et automatisation (Python)
6. Conception de la base de données (SQL Server)
7. Analyse des données
8. Création du tableau de bord (Power BI)
9. Rédaction du rapport final

---

# Résultats attendus

À la fin du projet, le système permettra :

- d’explorer les tendances liées aux étudiants internationaux
- d’analyser les admissions permanentes
- d’étudier l’évolution des programmes d’immigration au Québec
- de visualiser ces informations dans un tableau de bord interactif

---

# Auteur

**Brahim Landing Thiam**  
Baccalauréat en informatique  
Université du Québec en Outaouais
