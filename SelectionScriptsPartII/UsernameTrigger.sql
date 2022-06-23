CREATE TRIGGER UsernameTrigger
BEFORE UPDATE ON InternetBanks FOR EACH ROW
BEGIN
DECLARE t integer;
SELECT MAX(number_of_changes) INTO t FROM UsernameChanges WHERE db_user = OLD.id;
IF t IS NULL THEN
SET t = 0;
END IF;
IF ((SELECT COUNT(id) FROM UsernameChanges WHERE OLD.id = UsernameChanges.db_user AND TIMESTAMPDIFF(day, UsernameChanges.update_time, NOW())<1) = 2 ) THEN
 SIGNAL SQLSTATE '45000' 
 SET MESSAGE_TEXT = "Cant change username more than twice a day";
ELSE
 INSERT INTO UsernameChanges(db_user, prev_username, new_user, update_time, number_of_changes) VALUES (OLD.id, OLD.username, NEW.username, NOW(),t+1);
END IF; 
END$$
