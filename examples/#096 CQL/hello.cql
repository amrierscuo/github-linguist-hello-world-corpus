-- Cassandra Query Language, CQL 3, for a disposable development instance.
CREATE KEYSPACE IF NOT EXISTS hello_world_corpus
  WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS hello_world_corpus.greetings (
  id int PRIMARY KEY,
  message text
);

INSERT INTO hello_world_corpus.greetings (id, message)
VALUES (1, 'Hello, World!');

SELECT message FROM hello_world_corpus.greetings WHERE id = 1;
