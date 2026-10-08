CREATE OR REPLACE TRIGGER corpus_greeting
BEFORE INSERT ON corpus_events
FOR EACH ROW
BEGIN
  :NEW.message := 'Hello, World!';
END;
/
