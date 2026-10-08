const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict');
const Lexer = require(path.resolve(process.argv[2], 'node_modules/jison-lex'));
const lexer = new Lexer(fs.readFileSync('hello.jisonlex', 'utf8'));
lexer.setInput('Hello, World!');
const tokens=[], values=[];
for (;;) { const token=lexer.lex(); if(token==='EOF') break; tokens.push(token); values.push(lexer.yytext); }
assert.deepEqual(tokens, ['HELLO','COMMA','WORLD','BANG']);
assert.deepEqual(values, ['Hello',',','World','!']);
const text=values[0]+values[1]+' '+values[2]+values[3];
assert.equal(text, 'Hello, World!');
lexer.setInput('?'); assert.equal(lexer.lex(), 'INVALID');
console.log(text);
console.log('PASS: genuine Jison Lex scanner generation and lexemes');
