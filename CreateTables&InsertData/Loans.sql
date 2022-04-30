CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    start_date DATE NOT NULL,
    remainder BIGINT NOT NULL,
    loan_type INT NOT NULL,
    branch INT NOT NULL,
    account INT NOT NULL,
    guarantor INT NOT NULL,
    FOREIGN KEY (branch) REFERENCES Branches(id),
    FOREIGN KEY (loan_type) REFERENCES LoanTypes(id),
    FOREIGN KEY (account) REFERENCES Accounts(id),
    FOREIGN KEY (guarantor) REFERENCES Guarantors(id)
);