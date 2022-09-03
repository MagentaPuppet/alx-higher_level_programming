-- converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts table first_table to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts the field name in first_table to UTF8
USE hbtn_0c_0;
ALTER TABLE first_table MODIFY `name` VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
