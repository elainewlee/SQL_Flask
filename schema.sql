CREATE TABLE Users (id INTEGER, email VARCHAR(64), password VARCHAR(64), name VARCHAR(64));

CREATE TABLE Tasks (id INTEGER, title VARCHAR(64), created_at DATETIME, completed_at DATETIME, user_id INTEGER);