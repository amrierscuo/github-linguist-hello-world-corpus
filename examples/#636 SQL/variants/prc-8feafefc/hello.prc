DELIMITER //
CREATE PROCEDURE corpus_greeting()
BEGIN
  SELECT 'Hello, World!' AS message;
END//
DELIMITER ;
CALL corpus_greeting();
