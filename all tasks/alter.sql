CREATE SEQUENCE university_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE university (
                            id INTEGER DEFAULT nextval('university_id_seq') PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            created DATE NOT NULL
);

CREATE TABLE Talaba (
                        id SERIAL PRIMARY KEY,
                        serial VARCHAR(10) UNIQUE NOT NULL,
                        name VARCHAR(50) NOT NULL,
                        age INT CHECK (age > 0 AND age < 120),
                        salary FLOAT,
                        birthday DATE,
                        university_id INTEGER REFERENCES university(id),
                        kurs INTEGER,
                        fakultet VARCHAR(100)
);

ALTER TABLE Talaba
    ALTER COLUMN salary TYPE FLOAT;
