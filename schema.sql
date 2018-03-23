DROP table judoka;

CREATE TABLE judoka (
    ID INT PRIMARY KEY,
    family_name TEXT,
    given_name TEXT,
    gender TEXT,
    ftechnique TEXT,
    side CHAR(1),
    height INT,
    age INT,
    country TEXT,
    categories TEXT
);
