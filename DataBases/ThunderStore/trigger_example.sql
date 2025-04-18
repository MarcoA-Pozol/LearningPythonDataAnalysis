-- Simple PostgreSQL trigger that executes data inserting on another table after inserting data in the linked table (After Insert)

-- Create products a products_log tables
CREATE TABLE IF NOT EXISTS products (product_code TEXT NOT NULL, name TEXT NOT NULL, price NUMERIC(10, 2) NOT NULL, quantity INTEGER NOT NULL, section TEXT NOT NULL, provider TEXT NOT NULL, country TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS products_log(product_code TEXT NOT NULL, name TEXT NOT NULL, creator_name TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Create a function to store the algorithm the trigger is gonna execute
CREATE OR REPLACE FUNCTION log_new_product() -- Giving name to the function
RETURNS TRIGGER AS $$ -- This function is going to work as a part of a trigger
BEGIN 
    INSERT INTO products_log (product_code, name, creator_name)
    VALUES (NEW.product_code, NEW.name, SESSION_USER);
END;
$$ LANGUAGE plpgsql;

-- Creating the trigger 
CREATE TRIGGER Product_After_Insert
AFTER INSERT ON products
FOR EACH ROW
EXECUTE FUNCTION log_new_product(); -- Calling the previous created function on this trigger. 

-- Test the trigger inserting a new row into products
INSERT INTO products (product_code, name, price, quantity, provider, country)
VALUES ('Laptop', 1200.00, 10, 'TechSoft', 'USA');

-- Check the trigger worked and it inserted data into products_log
SELECT * FROM products_log;