-- First vertion of Customers table
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(100) NOT NULL DEFAULT 'NA',
    latname VARCHAR(100) NOT NULL DEFAULT 'NA'
);

INSERT INTO customers (firstname, lastname) VALUES
('Pedro','Garcia'),
('Liliana', 'Montemayor'),
('Hugo', 'Sanchez'),
('Erika', 'Guzman'),
;

-- Alter customers table
ALTER TABLE customers RENAME TO Customers; -- Renaming table
ALTER TABLE Customers ADD COLUMN gender VARCHAR(15) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other', 'I prefer not to say')) DEFAULT 'Other'; -- Adding a new column
ALTER TABLE Customers ADD COLUMN age INT NOT NULL CHECK (age >= 18 AND <= 120) DEFAULT 18;


-- To add a new field of FOREIGN KEY type in Sqlite3, we need to enable it first, and then, recreate the last table in a new one, droping the last existing table, and copy the data to the new, with the applied changes
PRAGMA foreign_keys = ON; -- Enabling the use of foreign keys

CREATE TABLE Customers2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(50) NOT NULL DEFAULT 'NA',
    lastname VARCHAR(50) NOT NULL DEFAULT 'NA',
    email VARCHAR(150) NULL, 
    phone_number VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL DEFAULT 18 CHECK (age >= 18 AND <= 120),
    gender VARCHAR(15) NOT NULL DEFAULT 'Other' CHECK (gender IN ('Male', 'Female', 'Other', 'I prefer not to say')),
    weight NUMERIC(10, 2) NULL,
    height NUMERIC(10, 2) NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(id) ON DELETE CASCADE ON UPDATE RESTRICT,
    FOREIGN KEY (occupation_id) REFERENCES Occupations(id) ON DELETE CASCADE ON UPDATE RESTRICT,
    salary NUMERIC(10, 2) NOT NULL DEFAULT 800,
    is_married BOOLEAN NOT NULL DEFAULT FALSE,
    thunder_points INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Copying data from old table to the new one
INSERT INTO Customers2 SELECT * Customers;

-- Drop old table
DROP TABLE Customers;

-- Rename new table
ALTER TABLE Customers2 RENAME TO Customers;

-- Adding an index for better performance
CREATE INDEX idx_customers_country_id ON Customers(country_id);
CREATE INDEX idx_customers_occupation_id ON Customers(occupation_id);