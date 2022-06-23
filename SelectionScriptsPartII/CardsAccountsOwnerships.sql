SELECT Cards.id, cvv2,owner, account FROM Cards WHERE account = ANY(SELECT account FROM Cards JOIN Accounts ON account = Accounts.id JOIN AccountOwnerships ON account_id = Accounts.id GROUP BY account_id Having COUNT(customer_id)>1) ORDER BY account;