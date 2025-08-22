CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
INSERT INTO users (name, email, age) VALUES
('Usman', 'Usman@example.com', 19),
('Hamza', 'Hamza123@example.com', 20),
('Ahsan', 'Ahsan@example.com', 22);

DELETE FROM users
WHERE name = 'Hamza';

SELECT * FROM users;

UPDATE users
SET age = 23
WHERE name = 'Ahsan';

CREATE TABLE bill (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    amount NUMERIC(10,2),
    date DATE,
    description TEXT
);

INSERT INTO bill (user_id, amount, date, description) VALUES
( 1, 300.00, '2025-08-05', 'Water Bill'),
( 2, 500.00, '2025-08-01', 'Electricity Bill');



SELECT *
FROM users
JOIN bill
ON users.id = bill.user_id;




