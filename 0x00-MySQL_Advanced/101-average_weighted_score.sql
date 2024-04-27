-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.

DELIMITER $$

-- create a procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE WeightedAvg FLOAT;
    DECLARE user_id_param INT;
    DECLARE total_users INT;
    DECLARE i INT;
    SET i = 0;

    -- get the total count of the users
    SELECT COUNT(id) INTO total_users
    FROM users;

    loop_label: LOOP
        -- get the user_id
        SET user_id_param = (
            SELECT id FROM users LIMIT 1 offset i
        );

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

        -- increment i
        SET i = i + 1;
        -- check if the loop has iterated all the users
        IF i = total_users THEN
            LEAVE loop_label;
        END IF;
    END LOOP;
END$$