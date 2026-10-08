CREATE OR REPLACE PACKAGE BODY corpus_greeting AS
  FUNCTION greeting RETURN VARCHAR2 IS
  BEGIN RETURN 'Hello, World!'; END;
END corpus_greeting;
/
