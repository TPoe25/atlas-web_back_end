-- Script that runs teh origins of bands base on total numbers

-- Select the band name and origin country
SELECT
    origin,
    SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
-- Order by the total number of fans in descending order
ORDER BY nb_fans DESC;
