-- Prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user if not found
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants privileges                                                                                                                                         
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
-- Givse privileges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev"@"localhost';
-- Gives select privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev"@"localhost';
