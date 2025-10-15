-- Drops view if it exists already
DROP VIEW IF EXISTS need_meeting;

-- Creates a view to show
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
    AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
