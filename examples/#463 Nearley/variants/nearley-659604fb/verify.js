const nearley = require('nearley');
const grammar = require('./hello.js');
const parser = new nearley.Parser(nearley.Grammar.fromCompiled(grammar));
parser.feed('Hello, World!');
if (parser.results.length !== 1 || parser.results[0] !== 'Hello, World!') throw new Error('Unexpected parse');
console.log(parser.results[0]);
