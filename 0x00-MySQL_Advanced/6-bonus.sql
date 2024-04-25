-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    IF (SELECT id FROM projects WHERE name = project_name) IS NULL THEN
        INSERT into projects (name) VALUES(project_name);
    END IF;
    UPDATE corrections
    SET score = score
    WHERE user_id = user_id AND project_id = (
        SELECT id FROM projects WHERE name = project_name
    );
END$$