CREATE TABLE IF NOT EXISTS Employees (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(60) NOT NULL DEFAULT 'NA',
    lastname VARCHAR(60) NOT NULL DEFAULT 'NA',
    email VARCHAR(150) NULL CHECK(email LIKE '%@%' AND email LIKE '%.%'),
    phone_number VARCHAR(12) NULL,
    age INT NOT NULL DEFAULT 18 CHECK(age >= 18 AND age <= 120),
    gender VARCHAR(20) NOT NULL DEFAULT 'Other' CHECK(gender IN('Male', 'Female', 'Other', 'I prefer not to say')),
    country_id INT REFERENCES Countries(id),
    occupation_id INT REFERENCES Occupations(id),
    salary NUMERIC(10, 2) NOT NULL DEFAULT 800
);