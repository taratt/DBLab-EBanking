CREATE TABLE UsernameChanges(
    id INT AUTO_INCREMENT PRIMARY KEY,
    db_user INT,
    prev_username VARCHAR(24),
    new_user VARCHAR(24),
    update_time DATETIME,
    number_of_changes INT
);