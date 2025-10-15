DELIMITER $
$

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR
(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT DEFAULT 0;
DECLARE
CONTINUE
HANDLER FOR NOT FOUND
SET v_project_id
= NULL;

-- Try to get the project_id
SELECT id
INTO v_project_id
FROM projects
WHERE name = p_project_name
LIMIT 1;

-- If project does not exist, insert it
IF v_project_id IS NULL THEN
INSERT INTO projects
    (name)
VALUES
    (p_project_name);
SET v_project_id
= LAST_INSERT_ID
();
END
IF;

    -- Insert the new correction
    INSERT INTO corrections
    (user_id, project_id, score)
VALUES
    (p_user_id, v_project_id, p_score);
END$$

DELIMITER ;
