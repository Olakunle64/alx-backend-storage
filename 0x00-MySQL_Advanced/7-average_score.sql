-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.

-- change the delimiter temporarily to $$
DELIMITER $$

-- create a procedure
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id_param INT)
BEGIN
    -- update the average_score of the user with the user_id
    UPDATE users
    SET average_score = (
        -- calculate the average score of the user with the user_id
        SELECT AVG(score) FROM corrections
        WHERE user_id = user_id_param
        )
    WHERE id = user_id_param;
END$$
