CREATE TABLE InternetBanks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(24) NOT NULL UNIQUE,
    password CHAR(64) NOT NULL,
    issue_date DATE NOT NULL,
    customer INT NOT NULL UNIQUE,
    branch INT NOT NULL,
    issuer INT NOT NULL,
    FOREIGN KEY (branch) REFERENCES Branches(id),
    FOREIGN KEY (issuer) REFERENCES BankTellers(id),
    FOREIGN KEY (customer) REFERENCES Customers(id)
);