CREATE TABLE AccountOwnerships (
    ownership_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
	customer_id INT NOT NULL,
	FOREIGN KEY (account_id) REFERENCES Accounts(id),
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);
