CREATE TABLE Cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cvv2 CHAR(3) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    close_date DATE,
    first_password CHAR(64) NOT NULL,
    second_password CHAR(64) NOT NULL,
    status BOOLEAN NOT NULL,
    owner INT NOT NULL,
    branch INT NOT NULL,
    account INT NOT NULL,
    issuer INT NOT NULL,
    closer INT,
    FOREIGN KEY (branch) REFERENCES Branches(id),
    FOREIGN KEY (owner) REFERENCES Customers(id),
    FOREIGN KEY (account) REFERENCES Accounts(id),
    FOREIGN KEY (issuer) REFERENCES BankTellers(id),
    FOREIGN KEY (closer) REFERENCES BankTellers(id)
);