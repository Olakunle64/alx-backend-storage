-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id_param INT)
BEGIN
    DECLARE WeightedAvg FLOAT;
    -- divided the product of score and weight by the sum of the weight of each project
    SELECT SUM(score * weight) / SUM(weight) INTO WeightedAvg
    FROM corrections
    JOIN projects
    ON corrections.project_id = projects.id
    WHERE user_id = user_id_param
    GROUP BY user_id_param;

    -- update the average score of the user
    UPDATE users
    SET average_score = IFNULL(WeightedAvg, 0)
    WHERE id = user_id_param;
END$$