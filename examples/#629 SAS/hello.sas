data _null_;
    length greeting $13;
    greeting = "Hello, " || "World!";
    put greeting;
run;
