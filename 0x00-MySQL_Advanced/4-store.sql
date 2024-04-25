-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$
CREATE TRIGGER dec_quantity
AFTER INSERT ON orders
FOR EACH ROW
    BEGIN
        UPDATE items SET quantity = quantity - NEW.number
        WHERE NEW.item_name = items.name;
    END$$