-- 7-average_score to compute and store averages

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    p_user_id INT
)
BEGIN
    DECLARE v_avg FLOAT;

    SELECT AVG(score) INTO v_avg
    FROM corrections
    WHERE user_id = p_user_id;

    UPDATE users
    SET average_score = v_avg
    WHERE id = p_user_id;
END$$

DELIMITER ;
