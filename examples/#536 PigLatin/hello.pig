names = LOAD 'names.tsv' USING PigStorage('\t') AS (name:chararray);
greetings = FOREACH names GENERATE CONCAT(CONCAT('Hello, ', name), '!') AS message;
DUMP greetings;
