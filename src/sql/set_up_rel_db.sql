CREATE DATABASE bigstoremanager;

USE bigstoremanager;

CREATE TABLE product_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL,
    parent_type_id INT,
    FOREIGN KEY (parent_type_id) REFERENCES product_type(id) ON DELETE SET NULL
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    serial_number VARCHAR(255),
    type_id INT,
    FOREIGN KEY (type_id) REFERENCES product_type(id)
);

INSERT INTO product_type (type_name, parent_type_id) VALUES
('Electronics', NULL),
('Clothing', NULL),
('Books', NULL);

INSERT INTO product_type (type_name, parent_type_id) VALUES
('Smartphones', 1),
('Laptops', 1),
('T-shirts', 2),
('Novels', 3);
