-- redo task 101

DELIMITER $$

-- create a procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE WeightedAvg FLOAT;
    DECLARE user_id_param INT
    DECLARE total_users INT;
    DECLARE i INT
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
            LEAVE loop_label
        END IF;
    END LOOP;
END
        

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;

    -- Declare cursor for iterating over users
    DECLARE user_cursor CURSOR FOR 
        SELECT id
        FROM users;

    -- Declare continue handler to exit loop when no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor
    OPEN user_cursor;

    -- Start loop
    read_loop: LOOP
        -- Fetch next user_id from cursor
        FETCH user_cursor INTO user_id;

        -- Exit loop if no more rows
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weight for this user
        SELECT SUM(weight) INTO total_weight
        FROM projects;

        -- Calculate the weighted score for this user
        SELECT SUM(score * weight) INTO weighted_score
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Update the average_score for this user
        UPDATE users
        SET average_score = IFNULL(weighted_score / total_weight, 0)
        WHERE id = user_id;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END$$

DELIMITER ;
