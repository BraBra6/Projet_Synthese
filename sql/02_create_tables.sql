USE immigration_qc;

CREATE TABLE etudiants (
    id INT IDENTITY(1,1) PRIMARY KEY,
    categorie VARCHAR(100),
    detail VARCHAR(150),
    annee INT,
    nombre_etudiants INT
);

CREATE TABLE permanents (
    id INT IDENTITY(1,1) PRIMARY KEY,
    categorie VARCHAR(150),
    detail VARCHAR(200),
    annee INT,
    nombre_immigrants INT
);

CREATE TABLE csq (
    id INT IDENTITY(1,1) PRIMARY KEY,
    categorie VARCHAR(100),
    description VARCHAR(150),
    detail VARCHAR(200),
    annee INT,
    nombre_csq INT
);
