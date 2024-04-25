-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- check if project name exists otherwise insert project_name as a new project
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0 THEN
        INSERT into projects (name) VALUES(project_name);
    END IF;

    -- insert a new row to the corrections table
    INSERT into corrections (user_id, project_id, score)
        VALUES(
            user_id,
            (SELECT id FROM projects WHERE name = project_name),
            score
            );
END$$