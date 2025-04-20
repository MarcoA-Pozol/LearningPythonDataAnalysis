CREATE TABLE IF NOT EXISTS Occupations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150),
    avg_salary NUMERIC(10, 2) NOT NULL DEFAULT 800,
    avg_gender VARCHAR(15) NOT NULL DEFAULT 'Male' CHECK(avg_gender IN ('Male', 'Female', 'Other', 'I prefer not to say'))
);