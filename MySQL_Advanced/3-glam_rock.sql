-- Script that runs teh origins of bands base on total numbers

-- Select the band name and origin country
SELECT
    band_name,
    COALESCE(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
