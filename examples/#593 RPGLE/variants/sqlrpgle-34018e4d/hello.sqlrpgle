**free
dcl-s greeting char(13);
exec sql values('Hello, World!') into :greeting;
dsply greeting;
*inlr = *on;
return;
