CREATE DATABASE bigstoremanager;

USE bigstoremanager;

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

INSERT INTO product (name, description) VALUES 
('Smartphone', 'a nice phone'),
('Headphones', 'a good looking headphones'),
('Monitor', 'something to see the work very well');
