-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.

DELIMITER $$

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
