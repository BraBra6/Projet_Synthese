# Sources de données – Projet de synthèse en informatique

## Système d’analyse décisionnelle sur l’immigration au Québec

---

# 1. Présentation générale des données

Dans le cadre de ce projet, des données ouvertes officielles du Gouvernement du Québec ont été utilisées afin d’analyser les tendances de l’immigration permanente et temporaire.  
Les jeux de données proviennent du portail officiel **Données Québec**, qui diffuse les données produites par les ministères québécois.

L’ensemble des données sélectionnées est cohérent avec la problématique du projet portant sur :

- l’immigration permanente (CSQ, admissions)
- l’immigration temporaire (étudiants internationaux)
- les programmes d’immigration du Québec (PEQ, travailleurs qualifiés, etc.)

---

# 2. Dataset 1 – Admissions des personnes immigrantes (permanentes)

## Nom du fichier

`admission-trimestre-4-2021-caracteristique.csv`

## Description

Ce jeu de données présente diverses caractéristiques des personnes immigrantes admises au Québec selon :

- l’âge
- le sexe
- la catégorie d’immigration
- la langue
- la région de destination
- le pays de naissance

Il permet d’analyser les profils des immigrants permanents admis au Québec.

## Source officielle

Ministère de l’Immigration, de la Francisation et de l’Intégration (MIFI)  
Gouvernement du Québec

## Plateforme de diffusion

Données Québec : https://www.donneesquebec.ca

## Utilité pour le projet

- Analyse des tendances d’immigration permanente
- Analyse par catégorie (économique, réfugiés, regroupement familial)
- Analyse démographique (âge, sexe, langue)

---

# 3. Dataset 2 – Étudiants internationaux (immigration temporaire)

## Nom du fichier

`temporaire-etudiants-permis-annee-2018-2022.csv`

## Description

Ce jeu de données décrit les caractéristiques des personnes immigrantes temporaires titulaires d’un permis d’études au Québec, incluant :

- nombre de permis d’études
- niveau d’études
- groupe d’âge
- région de destination
- langue connue
- pays de naissance

Il permet d’étudier l’évolution des étudiants internationaux au Québec.

## Source officielle

Ministère de l’Immigration, de la Francisation et de l’Intégration (MIFI)  
Gouvernement du Québec

## Plateforme de diffusion

Données Québec : https://www.donneesquebec.ca

## Utilité pour le projet

- Analyse des étudiants internationaux
- Comparaison immigration temporaire vs permanente
- Analyse des tendances 2018–2022

---

# 4. Dataset 3 – Certificats de sélection du Québec (CSQ) et programmes d’immigration

## Nom du fichier

`csq_delivres_2016_2023.csv`

## Description

Ce jeu de données présente le nombre de Certificats de sélection du Québec (CSQ) délivrés par programme d’immigration, notamment :

- Travailleurs qualifiés (PRTQ)
- PEQ Étudiants
- PEQ Travailleurs
- Regroupement familial
- Réfugiés

Le CSQ est une étape clé du processus d’immigration permanente au Québec.

## Source officielle

Ministère de l’Immigration, de la Francisation et de l’Intégration (MIFI)  
Gouvernement du Québec

## Lien officiel

https://www.donneesquebec.ca/recherche/dataset/nombre-de-certificats-de-selection-du-quebec-csq-delivres-par-programme-d-immigration

## Utilité pour le projet

- Analyse spécifique du programme PEQ
- Analyse des politiques d’immigration économique
- Compréhension de l’évolution des programmes d’immigration

---

# 5. Justification du choix des données (cohérence avec le projet)

Les trois datasets sont complémentaires et permettent une analyse complète :

| Type d’immigration       | Dataset utilisé           | Objectif                                 |
| ------------------------ | ------------------------- | ---------------------------------------- |
| Immigration permanente   | Admissions trimestrielles | Profil des immigrants                    |
| Immigration temporaire   | Étudiants internationaux  | Analyse des permis d’études              |
| Programmes d’immigration | CSQ par programme         | Analyse du PEQ et travailleurs qualifiés |

Cette combinaison permet de construire un système d’aide à la décision basé sur des données réelles et officielles.

---

# 6. Format des données

- Format : CSV
- Type : Données ouvertes gouvernementales
- Période couverte : 2016 à 2023 (selon le dataset)
- Niveau de fiabilité : Élevé (source gouvernementale officielle)

# 7. Remarque méthodologique (important pour le rapport)

Les données utilisées sont :

- publiques
- anonymisées
- non sensibles
- conformes aux principes éthiques de recherche

Aucune donnée personnelle identifiable n’est utilisée dans ce projet.

---

# 8. Conclusion

Les jeux de données sélectionnés sont pertinents, suffisants et cohérents avec l’objectif du projet de synthèse en informatique.  
Ils permettent la conception d’un outil d’analyse décisionnelle concret basé sur des données officielles du MIFI, couvrant à la fois l’immigration permanente, temporaire et les programmes d’immigration du Québec.
