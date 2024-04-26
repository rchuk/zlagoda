-- Security tables setup
-- depends: 0001.basic-tables-setup

CREATE TABLE roles
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO roles (name)
VALUES ('ADMIN'),
 ('MANAGER'),
 ('CASHIER');

CREATE TABLE users
(
    login VARCHAR(50) PRIMARY KEY,
    password_hash VARCHAR(255) NOT NULL,
    role_id INTEGER NOT NULL,
    employee_id VARCHAR(10),
    CONSTRAINT fk_role
        FOREIGN KEY (role_id)
            REFERENCES roles(id)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
            REFERENCES employee(id)
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

