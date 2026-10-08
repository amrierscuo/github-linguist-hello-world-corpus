import fs from 'node:fs';
const {createServicesForGrammar} = await import(process.env.LANGIUM_MODULE || 'langium/grammar');
const services = await createServicesForGrammar({grammar: fs.readFileSync('hello.langium', 'utf8')});
const parsed = services.parser.LangiumParser.parse(fs.readFileSync('hello.txt', 'utf8'));
if (parsed.lexerErrors.length || parsed.parserErrors.length || parsed.value.audience !== 'World') throw new Error(JSON.stringify(parsed));
console.log(JSON.stringify({type: parsed.value.$type, audience: parsed.value.audience}));
