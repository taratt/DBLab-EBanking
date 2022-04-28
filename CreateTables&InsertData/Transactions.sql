CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT NOT NULL,
    account_id INT NOT NULL,
	amount BIGINT NOT NULL,
	transaction_type VARCHAR(255) NOT NULL,
	transaction_date DATE NOT NULL,
	admin_id INT,
	teller_id INT,
	internet_bank_id INT,
	FOREIGN KEY (account_id) REFERENCES Accounts(id),
	CONSTRAINT primary_key PRIMARY KEY (transaction_id,account_id)
	FOREIGN KEY (admin_id) REFERENCES Admins(id),
	FOREIGN KEY (teller_id) REFERENCES BankTellers(id),
	FOREIGN KEY (internet_bank_id) REFERENCES InternetBanks(id),
	CONSTRAINT transactioner_check CHECK (
    admin_id IS NOT NULL AND teller_id IS NULL AND internet_bank_id IS NULL OR
    admin_id IS NULL AND teller_id IS NOT NULL AND internet_bank_id IS NULL OR
    admin_id IS NULL AND teller_id IS NULL AND internet_bank_id IS NOT NULL)
)
);