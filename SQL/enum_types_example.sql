-- Define the type
CREATE TYPE gender_enum AS ENUM ('Male', 'Female', 'Non-binary', 'Prefer not to say');

-- Use it in the table field definition to validate / 
gender gender_enum DEFAULT 'Prefer not to say'
