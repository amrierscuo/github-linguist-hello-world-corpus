--#SET TERMINATOR @
CREATE PROCEDURE corpus_greeting(OUT greeting VARCHAR(13))
LANGUAGE SQL
BEGIN ATOMIC
    SET greeting = 'Hello, ' || 'World!';
END@
