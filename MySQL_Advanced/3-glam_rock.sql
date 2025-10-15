-- Script that runs teh origins of bands base on total numbers
-- Select the band name and origin country

SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
