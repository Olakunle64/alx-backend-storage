-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;
    
    -- Calculate the total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects;
    
    -- Calculate the weighted score for the user
    SELECT SUM(score * weight) INTO weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    
    -- Update the average_score for the user
    UPDATE users
    SET average_score = IFNULL(weighted_score / total_weight, 0)
    WHERE id = user_id;
END$$
