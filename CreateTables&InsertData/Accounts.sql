CREATE TABLE Accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sheba CHAR(24) NOT NULL UNIQUE,
    open_date DATE NOT NULL,
    close_date DATE,
    status BOOLEAN NOT NULL,
    balance BIGINT NOT NULL CHECK (balance>=0),
    account_type INT NOT NULL,
    branch INT NOT NULL,
    opener INT NOT NULL,
    closer INT,
    FOREIGN KEY (branch) REFERENCES Branches(id),
    FOREIGN KEY (account_type) REFERENCES AccountTypes(id),
    FOREIGN KEY (opener) REFERENCES BankTellers(id),
    FOREIGN KEY (closer) REFERENCES BankTellers(id)
);