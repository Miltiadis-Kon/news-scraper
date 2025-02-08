-- Recursive CTE to traverse the hierarchy
WITH Hierarchy AS (
    SELECT
        Id,
        Name,
        Type,
        Parent_Id,
        CAST(Name AS NVARCHAR(MAX)) AS FullPath,
        CAST(Id AS NVARCHAR(MAX)) AS FullPathIds
    FROM TableA
    WHERE Type = 'Book'
    
    UNION ALL
    
    SELECT
        a.Id,
        a.Name,
        a.Type,
        a.Parent_Id,
        CAST(h.FullPath + ' > ' + a.Name AS NVARCHAR(MAX)),
        CAST(h.FullPathIds + ' > ' + a.Id AS NVARCHAR(MAX))
    FROM TableA a
    INNER JOIN Hierarchy h ON a.Id = h.Parent_Id
)
-- Select the desired columns
SELECT
    MAX(CASE WHEN h.Type = 'Book' THEN h.Name END) AS Book,
    MAX(CASE WHEN h.Type = 'Book' THEN h.Id END) AS Book_Id,
    MAX(CASE WHEN h.Type = 'Portfolio' THEN h.Name END) AS Portfolio,
    MAX(CASE WHEN h.Type = 'Portfolio' THEN h.Id END) AS Portfolio_Id,
    MAX(CASE WHEN h.Type = 'BusinessUnit' THEN h.Name END) AS BusinessUnit,
    MAX(CASE WHEN h.Type = 'BusinessUnit' THEN h.Id END) AS BusinessUnit_Id,
    MAX(CASE WHEN h.Type = 'LegalEntity' THEN h.Name END) AS LegalEntity,
    MAX(CASE WHEN h.Type = 'LegalEntity' THEN h.Id END) AS LegalEntity_Id,
    MAX(CASE WHEN h.Type = 'Hub' THEN h.Name END) AS Hub
FROM Hierarchy h
GROUP BY h.FullPath, h.FullPathIds
ORDER BY h.FullPath;