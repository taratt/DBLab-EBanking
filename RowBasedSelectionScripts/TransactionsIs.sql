SELECT transaction_id, account_id, amount, transaction_type, transaction_date, admin_id FROM Transactions WHERE NOT admin_id IS NULL AND amount > 180000000;