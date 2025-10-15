-- AddBonus where it takes 3 imputs

DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- init to NULL
    SET project_id = NULL;

    -- Get project id from user_id and project_name
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;
    LIMIT 1;

    -- if not found, insert the project
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert new correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$

DELIMITER ;
