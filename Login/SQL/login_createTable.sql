CREATE TABLE IF NOT EXISTS accounts(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
);