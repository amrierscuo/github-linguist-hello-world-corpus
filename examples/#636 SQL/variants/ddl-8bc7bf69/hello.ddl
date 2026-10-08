CREATE TABLE greeting(message TEXT NOT NULL CHECK(message = 'Hello, World!'));
INSERT INTO greeting VALUES ('Hello, World!');
SELECT message FROM greeting;
