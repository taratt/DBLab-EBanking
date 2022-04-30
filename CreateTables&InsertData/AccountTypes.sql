CREATE TABLE AccountTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL UNIQUE,
    interest INT NOT NULL,
    can_withdraw BOOLEAN NOT NULL,
    can_borrow_loan BOOLEAN NOT NULL,
    can_get_card BOOLEAN NOT NULL,
    CONSTRAINT interest_check CHECK (interest>=0 AND interest<100)
);