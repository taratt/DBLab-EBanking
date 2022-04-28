CREATE TABLE Branches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(255) NOT NULL UNIQUE,
    date_of_establishment DATE NOT NULL,
    capital BIGINT NOT NULL,
    phone_number CHAR(11) NOT NULL,
    address VARCHAR(255) NOT NULL,
);