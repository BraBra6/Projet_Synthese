USE immigration_qc;


-- 1. Évolution des étudiants par année

SELECT annee, SUM(nombre_etudiants) AS total_etudiants
FROM etudiants
GROUP BY annee
ORDER BY annee;
GO



-- 2. Top pays des étudiants (filtré)

SELECT TOP 10 detail AS pays, SUM(nombre_etudiants) AS total
FROM etudiants
WHERE categorie = 'pays'
AND detail NOT IN ('total_(personnes_uniques)', 'autres_pays')
GROUP BY detail
ORDER BY total DESC;
GO



-- 3. Répartition des étudiants par niveau d’étude

SELECT detail AS niveau_etude, SUM(nombre_etudiants) AS total
FROM etudiants
WHERE categorie = 'niveau_etude'
GROUP BY detail
ORDER BY total DESC;
GO



-- 4. Répartition des étudiants par région

SELECT detail AS region, SUM(nombre_etudiants) AS total
FROM etudiants
WHERE categorie = 'region'
AND detail <> 'non_précisé'
GROUP BY detail
ORDER BY total DESC;
GO



-- 5. Évolution de l’immigration permanente

SELECT annee, SUM(nombre_immigrants) AS total_immigrants
FROM permanents
GROUP BY annee
ORDER BY annee;
GO



-- 6. Répartition par type d’immigration

SELECT detail AS type_immigration, SUM(nombre_immigrants) AS total
FROM permanents
WHERE categorie = 'type_immigration'
GROUP BY detail
ORDER BY total DESC;
GO



-- 7. Répartition des permanents par région

SELECT detail AS region_destination, SUM(nombre_immigrants) AS total
FROM permanents
WHERE categorie = 'region_destination'
GROUP BY detail
ORDER BY total DESC;
GO



-- 8. Évolution des CSQ par année

SELECT annee, SUM(nombre_csq) AS total_csq
FROM csq
GROUP BY annee
ORDER BY annee;
GO



-- 9. Top pays pour les CSQ (filtré)

SELECT TOP 10 detail AS pays, SUM(nombre_csq) AS total
FROM csq
WHERE categorie = 'pays'
AND detail NOT IN ('autres_pays')
GROUP BY detail
ORDER BY total DESC;
GO



-- 10. CSQ par grandes catégories utiles

SELECT categorie, SUM(nombre_csq) AS total
FROM csq
WHERE categorie IN (
    'immigration_economique',
    'regroupement_familial',
    'refugies'
)
GROUP BY categorie
ORDER BY total DESC;
GO



-- 11. Comparaison globale (TRÈS IMPORTANT)

SELECT annee, 'etudiants' AS source, SUM(nombre_etudiants) AS total
FROM etudiants
GROUP BY annee

UNION ALL

SELECT annee, 'permanents' AS source, SUM(nombre_immigrants) AS total
FROM permanents
GROUP BY annee

UNION ALL

SELECT annee, 'csq' AS source, SUM(nombre_csq) AS total
FROM csq
GROUP BY annee
ORDER BY annee, source;
GO