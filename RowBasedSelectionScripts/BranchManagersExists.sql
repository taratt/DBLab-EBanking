SELECT * FROM BranchManagers WHERE EXISTS (SELECT id FROM Branches WHERE BranchManagers.branch = Branches.id AND capital>390000000000 );