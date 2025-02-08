-- Drop the table if it exists
IF OBJECT_ID('TableA', 'U') IS NOT NULL
    DROP TABLE TableA;

-- Create the table
CREATE TABLE TableA (
    Id VARCHAR(255) PRIMARY KEY,
    Name NVARCHAR(100),
    Type NVARCHAR(100),
    Parent_Id VARCHAR(255),
    TimeStamp DATETIME
);

-- Insert data from the Excel file
INSERT INTO TableA (Id, Name, Type, Parent_Id, TimeStamp)
SELECT Id, Name, Type, Parent_Id, TimeStamp
FROM OPENROWSET(
    'Microsoft.ACE.OLEDB.16.0',
    'Excel 12.0;HDR=YES;Database=C:\\Users\\M\\Downloads\\interview_tasks.xlsx',
    'SELECT * FROM [Sheet1$]'
);