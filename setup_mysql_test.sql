-- creates Database hbnb_test_db
-- creates user hbnb_test
-- grants all privileges to hbnb_test on hbnb_test_db
-- grants select privileges to hbnb_test on hbnb_test_db


CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
