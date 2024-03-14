-- A script that converts hbtn_0c_0 database to UTF8:
--		(utf8mb4, collate utf8mb4_unicode_ci)
-- You need to convert all of the following to UTF8:
-- 		Database hbtn_0c_0
--		Table first_table
-- 		Field name in first_table


-- Altering the database character set and collation
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Altering the table character set and collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modifying the column 'name' to use UTF8 character set and collation
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
