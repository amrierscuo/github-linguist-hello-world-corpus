BEGIN;
CREATE FUNCTION pg_temp.greeting(name text) RETURNS text LANGUAGE plpgsql AS $$
BEGIN
  RETURN 'Hello, ' || name || '!';
END;
$$;
SELECT pg_temp.greeting('World');
DO $$ BEGIN IF pg_temp.greeting('Reader') <> 'Hello, Reader!' THEN RAISE EXCEPTION 'Parameter control failed'; END IF; END $$;
ROLLBACK;
