CREATE TRIGGER CustomerDeleted 
BEFORE DELETE ON Customers FOR EACH ROW
DELETE FROM AccountOwnerships WHERE AccountOwnerships.customer_id = OLD.id;

CREATE TRIGGER AccountDeleted 
BEFORE DELETE ON Accounts FOR EACH ROW
DELETE FROM AccountOwnerships WHERE AccountOwnerships.account_id = OLD.id;