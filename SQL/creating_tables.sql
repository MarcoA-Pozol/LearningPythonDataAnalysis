/* TABLES: CREATING CUSTOMERS, EMPLOYEES, DEPARTMENTS, AREAS, PRODUCTS, SERVICES AND INVOICES TABLES */
-- Enum types for customers table
CREATE TYPE source_channel_enum AS ENUM ('Announcement', 'Instagram', 'Website', 'Referral', 'Campaign', 'Contact', 'Other');
CREATE TYPE membership_level_enum AS ENUM ('Basic', 'Medium', 'Thunder')

CREATE TABLE IF NOT EXISTS 
customers (
    id SERIAL PRIMARY KEY, 
    firstname VARCHAR(70) NOT NULL DEFAULT 'NA', 
    lastname VARCHAR(70) NOT NULL DEFAULT 'NA', 
    email VARCHAR(150) UNIQUE NOT NULL, 
    phone_number VARCHAR(20) UNIQUE NULL, 
    age INT NOT NULL DEFAULT 18, 
    country VARCHAR(100) NOT NULL DEFAULT 'USA',
    gender VARCHAR(20) CHECK (gender IN ('Male', 'Female', 'Non-binary', 'Prefer not to say')) DEFAULT 'Prefer not to say' NOT NULL, 
    birthdate DATE NULL,
    source_channel source_channel_enum VARCHAR(100) NULL DEFAULT 'Announcement',
    membership_level membership_level_enum VARCHAR(20) NULL DEFAULT 'Basic',
    thunderpoints INT NULL DEFAULT 0, -- Points the customer will be generating every new buy or during actions are performing using the services
    prefered_language VARCHAR(10) NULL DEFAULT 'en',
    is_married BOOLEAN NULL DEFAULT FALSE, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS 