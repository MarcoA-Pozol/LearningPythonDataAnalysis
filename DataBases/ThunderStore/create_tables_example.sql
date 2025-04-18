-- You can create tables once you are connected with an user with permissions using psql


/* PRODUCTS */
-- Creating providers table
CREATE TABLE IF NOT EXISTS providers (id SERIAL PRIMARY KEY, name VARCHAR(150) NOT NULL);

-- Creating countries table
CREATE TABLE IF NOT EXISTS countries (id SERIAL PRIMARY KEY, name VARCHAR(200) NOT NULL);

-- Creating sections table
CREATE TABLE IF NOT EXISTS sections (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, description TEXT, manager_id REFERENCES employees(id) NOT NULL)

-- Creating products table
CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, price NUMERIC(10, 2) NOT NULL, quantity NUMERIC(10, 2) NOT NULL, section_id REFERENCES sections(id) NOT NULL/* Using a FK to make reference to the section in sections table*/, provider_id REFERENCES providers(id) NOT NULL, country_id REFERENCES countries(id) NOT NULL);

-- Creating products_log table
CREATE TABLE IF NOT EXISTS products_log(id SERIAL PRIMARY KEY, product_id REFERENCES products(id) NOT NULL, created_by TEXT DEFAULT CURRENT_USER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

/* USERS */
-- Creating customers table
CREATE TABLE IF NOT EXISTS customers (id SERIAL PRIMARY KEY, firstname VARCHAR(100) NOT NULL, lastname VARCHAR(100) NOT NULL, age INTEGER NOT NULL, gender VARCHAR(50) NOT NULL, country_id REFERENCES countries(id) NOT NULL, ocupation VARCHAR(200) DEFAULT 'Worker' NULL, email TEXT NOT NULL UNIQUE CHECK (email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$') NULL, phone VARCHAR(15) CHECK (phone ~ '^[0-9+\-()\s]+$') NULL, profile_picture TEXT DEFAULT 'profile_pictures/default.jpg');

-- Creating employees table
-- Pending