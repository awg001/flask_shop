CREATE TABLE users(	
    id integer PRIMARY KEY,
    email string NOT NULL UNIQUE,
    password string NOT NULL UNIQUE,
    isAdmin boolean DEFAULT FALSE
    );