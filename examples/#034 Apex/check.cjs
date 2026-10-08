const fs = require('node:fs');
const assert = require('node:assert/strict');
const { ApexParserFactory, ApexErrorListener } = require('@apexdevtools/apex-parser');
const errors = [];
class Listener extends ApexErrorListener {
  apexSyntaxError(line, column, message) { errors.push({ line, column, message }); }
}
const source = fs.readFileSync('hello.apex', 'utf8');
const { parser } = ApexParserFactory.createLexerAndParser(source, new Listener());
parser.anonymousUnit();
assert.deepEqual(errors, []);
console.log('Apex anonymousUnit parsed: 0 lexer/parser syntax errors.');
