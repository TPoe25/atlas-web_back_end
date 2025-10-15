-- 10-div.sql
-- Function that divides 2 numbers safely

DELIMITER $$

CREATE FUNCTION SavDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN a / b;
END $$

DELIMITER ;
