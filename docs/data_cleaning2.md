# Nettoyage et Préparation des Données (Python)

## Vue d’ensemble

Dans ce projet, Python a été utilisé pour nettoyer, standardiser et préparer des données d’immigration au Québec afin de permettre leur analyse avec SQL Server et Power BI.

L’objectif principal est de transformer des données brutes en données propres, cohérentes et exploitables.

---

## Jeux de données utilisés

Trois jeux de données ont été traités :

1. **Étudiants temporaires (2018–2022)**
2. **Immigration permanente (2020–2021)**
3. **CSQ – Certificat de sélection du Québec (2016–2023)**

---

## Outils utilisés

- Python
- pandas

---

## Pipeline de traitement des données

Le flux de traitement est organisé comme suit :

Data/raw → Data/clean → Data/processed

- **raw** : données originales
- **clean** : données partiellement nettoyées
- **processed** : données finales prêtes pour SQL et Power BI

---

## Étapes de nettoyage

Les opérations suivantes ont été appliquées :

### 1. Renommage des colonnes

Certaines colonnes ont été renommées pour plus de clarté :

- `nombre` → `nombre_etudiants`
- `nombre` → `nombre_immigrants`
- `nombre` → `nombre_csq`
- `Details` → `detail`
- `Description` → `description`

---

### 2. Nettoyage du texte

Les colonnes texte (`categorie`, `detail`, `description`) ont été nettoyées :

- mise en minuscules
- suppression des espaces inutiles
- uniformisation des valeurs

Exemple :

" Région de destination " → "region"

---

### 3. Standardisation des catégories

Les catégories ont été simplifiées pour faciliter l’analyse :

- `groupe d'âge` → `age`
- `langue connue` → `langue`
- `niveau d'études` → `niveau_etude`
- `permis initial / multiple / unique` → `type_permis`
- `catégorie d'immigration` → `type_immigration`

---

### 4. Normalisation des valeurs (detail)

Les valeurs de la colonne `detail` ont été standardisées :

- remplacement des espaces par `_`
- uniformisation des noms

Exemple :

"permis initial" → "permis_initial"
"bas saint laurent" → "bas_saint_laurent"

---

### 5. Conversion des données numériques

Les colonnes numériques ont été converties avec :

```python
pd.to_numeric(..., errors="coerce")
```

Puis transformées en entiers (`int`).

---

### 6. Gestion des valeurs manquantes

- Suppression des lignes avec des valeurs critiques manquantes
- Pour le dataset CSQ :
  - les valeurs manquantes de `nombre_csq` ont été remplacées par `0`

---

### 7. Suppression des doublons

Les doublons ont été supprimés selon des clés logiques :

- Étudiants : `categorie + detail + annee`
- Permanents : `categorie + detail + annee`
- CSQ : `categorie + description + detail + annee`

---

### 8. Tri des données

Les données ont été triées selon :

```
annee → categorie → detail
```

---

### Résultat final

Les fichiers finaux ont été enregistrés dans :

```
Data/processed/
```

Fichiers :

- `etudiants_final.csv`
- `permanents_final.csv`
- `csq_final.csv`

---

### Validation des données

Un script Python (`check_data.py`) a été utilisé pour vérifier :

- les types de données
- les valeurs manquantes
- les doublons
- la structure globale

Résultat :

- aucune valeur manquante
- aucun doublon
- types corrects

---

### Conclusion

La phase de nettoyage a permis de transformer les données en un format propre et structuré.

Les données sont maintenant prêtes pour :

- l'intégration dans SQL Server
- l'analyse avec SQL
- la visualisation avec Power BI

Cette étape garantit la qualité et la fiabilité des analyses futures.
