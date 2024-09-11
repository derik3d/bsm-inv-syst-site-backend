create DATABASE bigstoremanager;
use bigstoremanager;

CREATE TABLE product_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(255) UNIQUE NOT NULL,
    parent_type_id INT,
    nemo VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (parent_type_id) REFERENCES product_type(id) ON DELETE SET NULL
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name TEXT NOT NULL,
    product_description TEXT NOT NULL,
    fk_product_type_id INT NOT NULL,
    FOREIGN KEY (fk_product_type_id) REFERENCES product_type(id)
);

INSERT INTO product_type (type_name, nemo, parent_type_id) VALUES
('public item', 'PUT', NULL),
('personal item', 'PEI', NULL),
('public document', 'PUD', NULL);

INSERT INTO product_type (type_name, nemo, parent_type_id) VALUES
('dataphone', 'DTP', 1),
('card', 'CRD', 2),
('checkbook', 'CKB', 2),
('web signed contract', 'WSC', 3),
('personal signed contract', 'PSC', 3);

INSERT INTO product (product_name, product_description, fk_product_type_id) VALUES
('Smartphone', 'A high-end smartphone with advanced features for client fidelization.', 1),
('Big dataphone', 'Old type dataphone.', 4),
('ID Card', 'A personalized ID card with unique identification.', 5),
('Credit Card', 'A personalized ID card to handle credit.', 5),
('Business Checkbook', 'A checkbook for business transactions.', 6),
('Contract Web Document', 'A legally binding document signed online.', 7),
('Personal on place Agreement', 'A contract signed personally for agreement.', 8);

