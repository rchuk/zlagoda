-- Basic tables setup
-- depends:

CREATE TABLE customer_card
(
    id               SERIAL PRIMARY KEY,
    last_name        VARCHAR(50) NOT NULL,
    first_name       VARCHAR(50) NOT NULL,
    patronymic       VARCHAR(50),
    phone_number     VARCHAR(13) NOT NULL,
    city             VARCHAR(50),
    street           VARCHAR(50),
    zip_code         VARCHAR(9),
    discount_percent INTEGER     NOT NULL
);

CREATE TABLE employee
(
    id              SERIAL PRIMARY KEY,
    last_name       VARCHAR(50) NOT NULL,
    first_name      VARCHAR(50) NOT NULL,
    patronymic      VARCHAR(50),
    role            VARCHAR(10) NOT NULL,
    salary          INTEGER     NOT NULL,
    birth_date      DATE        NOT NULL,
    work_start_date DATE        NOT NULL,
    phone_number    VARCHAR(13) NOT NULL,
    city            VARCHAR(50) NOT NULL,
    street          VARCHAR(50) NOT NULL,
    zip_code        VARCHAR(9)  NOT NULL
);

CREATE TABLE product_category
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE product_archetype
(
    id           SERIAL PRIMARY KEY,
    category     INTEGER     NOT NULL,
    name         VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    description  VARCHAR(50) NOT NULL,
    CONSTRAINT fk_category
        FOREIGN KEY (category)
            REFERENCES product_category (id)
            ON UPDATE CASCADE
            ON DELETE NO ACTION
);

CREATE TABLE product
(
    upc           VARCHAR(12) PRIMARY KEY,
    discount_id  VARCHAR(12),
    archetype    INTEGER     NOT NULL,
    price        INTEGER     NOT NULL,
    quantity     INTEGER     NOT NULL,
    has_discount BOOLEAN     NOT NULL,
    CONSTRAINT fk_discount
        FOREIGN KEY (discount_id)
            REFERENCES product (upc)
            ON UPDATE CASCADE
            ON DELETE SET NULL,
    CONSTRAINT fk_archetype
        FOREIGN KEY (archetype)
            REFERENCES product_archetype (id)
            ON UPDATE CASCADE
            ON DELETE NO ACTION
);

CREATE TABLE receipt
(
    id               SERIAL PRIMARY KEY,
    cashier_id       INTEGER   NOT NULL,
    customer_card_id INTEGER,
    date_time        TIMESTAMP NOT NULL,
    total_price      INTEGER   NOT NULL,
    vat              INTEGER   NOT NULL,
    CONSTRAINT fk_cashier
        FOREIGN KEY (cashier_id)
            REFERENCES employee (id)
            ON UPDATE CASCADE
            ON DELETE NO ACTION,
    CONSTRAINT fk_customer_card
        FOREIGN KEY (customer_card_id)
            REFERENCES customer_card (id)
            ON UPDATE CASCADE
            ON DELETE NO ACTION
);

CREATE TABLE receipt_item
(
    upc        VARCHAR(12),
    receipt_id INTEGER,
    quantity   INTEGER NOT NULL,
    price      INTEGER NOT NULL,
    PRIMARY KEY (upc, receipt_id),
    CONSTRAINT fk_upc
        FOREIGN KEY (upc)
            REFERENCES product (upc)
            ON UPDATE CASCADE
            ON DELETE NO ACTION,
    CONSTRAINT fk_receipt
        FOREIGN KEY (receipt_id)
            REFERENCES receipt (id)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);