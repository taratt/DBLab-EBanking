SELECT id, payslip_code FROM Guarantors WHERE EXISTS (SELECT id FROM Loans WHERE Loans.guarantor = Guarantors.id AND remainder > 80000000);