SELECT DISTINCT account, loan_type FROM Loans AS L1 WHERE account = ANY (SELECT account FROM Loans AS L2 WHERE L1.id <> L2.id and L1.loan_type = L2.loan_type);