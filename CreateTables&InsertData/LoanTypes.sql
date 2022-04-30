CREATE TABLE LoanTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL UNIQUE,
    interest INT NOT NULL,
    amount BIGINT NOT NULL,
    period INT NOT NULL,
    number_of_payments INT NOT NULL,
    CONSTRAINT interest_check CHECK (interest>=0 AND interest<100)
);