-- Store procedures are blocks of "code" in sql which help us to save proceses of SQL which are going to be called many times
-- But in the case of a store procedure it should not return something, but do something for you

-- Store procedure to increase all product prices by 10%
CREATE OR REPLACE PROCEDURE increase_all_product_prices_by_10()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE products
    SET price = price + price * .10;
    RAISE NOTICE 'All prices has been increased by 10%%';
END;
$$;

-- Store procedure to decrease all product prices by 10%
CREATE OR REPLACE PROCEDURE decrease_all_product_prices_by_10()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE products
    SET price = price - price * .10;
    RAISE NOTICE 'All prices has been decreased by 10%%';
END;
$$;

-- Store procedure to give a discount of every product in a given section
CREATE OR REPLACE PROCEDURE add_discount_to_products_of_a_given_section(section TEXT, discount_percent NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE products
    SET products.price = products.price * (1 - discount_percent / 100)
    WHERE products.section = section;
    RETURNING * INTO updated_count; -- Save the number of updated products in this variable "updated_count" to be mentioned in the RAISE NOTICE
    RAISE NOTICE 'All prices of % products from % section had been decreased by %%%', updated_count, section, discount_percent;
END;
$$;

-- Calling the stored procedures
CALL increase_all_product_prices_by_10();
CALL decrease_all_product_prices_by_10();
CALL add_discount_to_products_of_a_given_section('sports', .12);
CALL add_discount_to_products_of_a_given_section('electronics', .15)