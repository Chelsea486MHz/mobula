CREATE DATABASE mobula;

USE mobula;

CREATE TABLE IF NOT EXISTS tokens (
    id SERIAL PRIMARY KEY,
    token VARCHAR(48) UNIQUE NOT NULL
);

INSERT INTO tokens (token) VALUES ('replace-this-token');