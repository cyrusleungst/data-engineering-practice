DROP TABLE IF EXISTS accounts CASCADE;
CREATE TABLE accounts (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address_1 TEXT,
    address_2 TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code INTEGER,
    join_date DATE
);
DROP TABLE IF EXISTS products CASCADE;
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_code INTEGER,
    product_description TEXT
);
DROP TABLE IF EXISTS transactions CASCADE;
CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    transaction_date DATE,
    product_id INTEGER REFERENCES products (product_id),
    product_code INTEGER,
    product_description TEXT,
    quantity INTEGER,
    account_id INTEGER REFERENCES accounts (customer_id)
);