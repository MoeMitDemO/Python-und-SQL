BEGIN;
INSERT INTO person (name, vorname, geburtstag)
Values ('Wildenhain', 'Moritz', '2002-11-06');

INSERT INTO adresse (plz, ort, strasse, nr, typ)
Values('56370', 'Kördorf', 'Lahnstrasse', '28', 'Wohnort');

INSERT INTO anschluss
COMMIT;