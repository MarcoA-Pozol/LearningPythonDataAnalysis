-- Obtain every duplicated occupation row's name (Example: Electric Engineer | 2 & Desntist | 2)
SELECT name, COUNT(*)
FROM Occupations
GROUP BY name
HAVING COUNT(*) > 1;

-- Removing duplicated occupations
WITH duplicates AS (
    SELECT MIN(id) as min_id, name
    FROM Occupations
    GROUP BY name
    HAVING COUNT(*) > 1
)
DELETE FROM Occupations
WHERE id NOT IN (SELECT min_id FROM duplicates)
AND name IN (SELECT name FROM duplicates)DROP 