-- Script that runs teh origins of bands base on total numbers

-- Select the band name and origin country
SELECT
    band_name,
    COALESCE(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style = '%Glam Rock%'
ORDER BY lifespan DESC;
