-- Write a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.
DELIMITER $$
CREATE TRIGGER reset_validEmail
BEFORE UPDATE on users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        IF OLD.valid_email = 1 THEN
            SET NEW.valid_email = 0;
        ELSEIF OLD.valid_email = 0 THEN
            SET NEW.valid_email = 1;
        END IF;
    END IF;
END$$