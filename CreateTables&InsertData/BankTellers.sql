CREATE TABLE BankTellers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    father_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    place_of_birth VARCHAR(255) NOT NULL,
    phone_number CHAR(11) NOT NULL,
    national_code CHAR(10) NOT NULL UNIQUE,
    identification_number VARCHAR(10) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    postal_code CHAR(10) NOT NULL,
    salary INT NOT NULL CHECK (salary>=0),
    branch INT NOT NULL,
    FOREIGN KEY (branch) REFERENCES Branches(id)
);