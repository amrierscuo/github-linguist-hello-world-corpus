CREATE OR REPLACE TYPE BODY corpus_greeting AS
  MEMBER FUNCTION greeting RETURN VARCHAR2 IS
  BEGIN RETURN 'Hello, ' || SELF.audience || '!'; END;
END;
/
