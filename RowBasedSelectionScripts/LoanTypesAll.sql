SELECT * FROM LoanTypes WHERE number_of_payments >= ALL (SELECT number_of_payments FROM LoanTypes);