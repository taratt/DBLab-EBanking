SELECT DISTINCT account_id FROM AccountOwnerships AS A1 WHERE account_id = ANY (SELECT account_id FROM AccountOwnerships AS A2 WHERE A1.ownership_id <> A2.ownership_id);
