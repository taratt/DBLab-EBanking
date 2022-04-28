CREATE TABLE Guarantors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    national_code CHAR(10) NOT NULL,
    payslip_code VARCHAR(255) NOT NULL,
);