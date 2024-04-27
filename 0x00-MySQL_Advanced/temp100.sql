-- redo task 100

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id_param INT)
BEGIN
    DECLARE WeightedAvg;
    -- divided the product of score and weight by the sum of the weight of each project
    SELECT user_id, sum(score * weight) / sum(weight) INTO WeightedAvg
    FROM corrections
    JOIN projects
    ON project_id = id
    WHERE user_id = user_id_param
    GROUP BY user_id_param;

    -- update the average score of the user
    UPDATE users
    SET average_score = IFNULL(WeightedAvg, 0)
    WHERE id = user_id_param;
END