# Nettoyage et préparation des données – Semaine 2

## Projet de synthèse – Analyse de l’immigration au Québec

**Étudiant :** Brahim Thiam  
**Programme :** Informatique – UQO  
**Outils utilisés :** Excel, VS Code  
**Période :** Semaine 2 – Exploration et nettoyage initial des données

---

# 1. Contexte du projet

Ce projet de synthèse porte sur l’analyse des données d’immigration au Québec, en particulier :

- les étudiants temporaires,
- les admissions permanentes,
- les CSQ délivrés par programme (incluant le PEQ étudiants).

L’objectif est de construire un système d’analyse de données fiable permettant :

- l’analyse statistique,
- la modélisation des tendances,
- la création d’un tableau de bord interactif (Power BI).

La Semaine 2 est dédiée à l’exploration et au nettoyage initial des datasets afin d’obtenir des données propres pour les étapes futures (Python, SQL Server et Power BI).

---

# 2. Description des datasets utilisés

Trois datasets principaux ont été utilisés :

1. **etudiants_temporaires_2018_2022**  
   Données sur les permis d’études au Québec.

2. **admissions_permanentes_2021**  
   Données trimestrielles sur les admissions permanentes.

3. **csq_delivres_par_programme_2016_2023**  
   Données sur les Certificats de sélection du Québec (CSQ), incluant les programmes économiques et le PEQ.

Les fichiers bruts étaient initialement stockés dans le dossier :

Data/raw

---

# 3. Problèmes identifiés dans les données brutes

Lors de l’exploration des fichiers Excel, plusieurs problèmes de qualité des données ont été observés.

## 3.1 Problèmes de format numérique

- Présence de nombres avec espaces (ex : "30 527")
- Nombres enregistrés en format texte
- Valeurs contenant le symbole "\*"

Ces formats empêchent une analyse correcte dans Excel, Python et SQL.

## 3.2 Valeurs manquantes

- Présence de cellules vides
- Symboles "\*" utilisés à la place de données numériques
- Valeurs NULL implicites non standardisées

## 3.3 Structure non adaptée à l’analyse

- Tableaux en format large (plusieurs colonnes par année)
- Colonnes non standardisées
- Données difficiles à exploiter en SQL et en Python

## 3.4 Erreurs et incohérences

- Années incorrectes détectées (ex : 2027 au lieu de 2017)
- Espaces inutiles dans certaines colonnes
- Colonne ID répétitive et non analytique
- Données très longues et hétérogènes (plusieurs sections dans un seul fichier)

---

# 4. Objectifs du nettoyage (Semaine 2)

Les objectifs principaux du nettoyage étaient :

- Convertir les nombres en format numérique
- Gérer les valeurs manquantes
- Corriger les erreurs d’années
- Structurer les datasets pour l’analyse
- Obtenir des fichiers propres pour Python, SQL Server et Power BI

---

# 5. Étapes de nettoyage réalisées dans Excel

## 5.1 Conversion des nombres en format numérique

Actions réalisées :

- Suppression des espaces dans les nombres (ex : 30 527 → 30527)
- Conversion du format texte en format nombre
- Vérification du type de données dans Excel

Importance :  
Permet d’effectuer des calculs corrects et d’éviter des erreurs lors de l’analyse.

---

## 5.2 Gestion des valeurs manquantes (\* et cellules vides)

Actions réalisées :

- Remplacement des "\*" par des valeurs NULL ou cellules vides standardisées
- Nettoyage des sections vides du dataset

Justification :  
Les outils analytiques (Python, SQL, Power BI) interprètent mieux les valeurs NULL que les symboles non standards.

---

## 5.3 Correction des erreurs dans la colonne "année"

Actions réalisées :

- Détection des valeurs incorrectes (ex : 2027)
- Correction manuelle pour correspondre à la période réelle (2016–2023)
- Vérification de la cohérence temporelle

Importance :  
Les erreurs d’années faussent totalement l’analyse des tendances.

---

## 5.4 Gestion de la colonne ID

Observation :

- La colonne ID se répétait pour plusieurs années
- Elle ne représentait pas une clé unique analytique

Décision :

- Conservation possible pour référence
- Mais non utilisée comme clé principale pour l’analyse

Dans ce dataset, l’unicité logique repose plutôt sur :

- categorie
- detail
- annee

---

## 5.5 Renommage et standardisation des colonnes

Les colonnes ont été nettoyées et standardisées :

- categorie
- description
- details
- annee
- nombre

Importance :
Des noms de colonnes clairs facilitent l’utilisation dans :

- pandas (Python)
- SQL Server
- Power BI

---

## 5.6 Transformation en format long (tidy data)

Le dataset CSQ a été transformé du format large vers un format long :

Format final :

categorie | description | details | annee | nombre

Avantages :

- Compatible avec SQL
- Compatible avec Power BI
- Meilleure analyse temporelle
- Structure professionnelle en data analytics

---

# 6. Organisation des fichiers après nettoyage

Structure du projet utilisée :

Data/
├── raw/ (données brutes)
├── clean/ (données nettoyées)
docs/
excel/
├──(données nettoyées en excel)
figures/

Les fichiers nettoyés ont été sauvegardés en :

- .xlsx (travail Excel)
- .csv (préparation pour Python et SQL)

---

# 7. Validation de la qualité des données

Après le nettoyage, plusieurs vérifications ont été effectuées :

- Correction des années erronées
- Suppression des incohérences
- Absence de doublons critiques
- Format numérique correct pour la colonne "nombre"
- Dataset exploitable pour l’analyse future

---

# 8. Limites du nettoyage initial

Certaines limites existent encore :

- Nettoyage manuel (Excel)
- Risque d’erreurs humaines
- Valeurs manquantes structurelles dans certaines catégories
- Dataset très volumineux et hétérogène

Un nettoyage avancé sera réalisé en Python durant les Semaines 3–4.

---

# 9. Conclusion

Le nettoyage initial des données en Semaine 2 a permis de transformer des datasets bruts, longs et comportant plusieurs erreurs en datasets propres, structurés et exploitables.

Grâce à la correction des formats numériques, la gestion des valeurs manquantes, la correction des années et la transformation en format long, les données sont désormais prêtes pour :

- l’automatisation avec Python,
- l’intégration dans une base de données SQL,
- la visualisation avancée avec Power BI.

Cette étape est essentielle pour garantir la fiabilité et la rigueur analytique du projet de synthèse en data
