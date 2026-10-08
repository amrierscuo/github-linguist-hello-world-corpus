--#SET TERMINATOR @
CREATE PROCEDURE corpus_greeting(OUT greeting VARCHAR(13))
LANGUAGE SQL
BEGIN
    SET greeting = 'Hello, ' || 'World!';
END@
