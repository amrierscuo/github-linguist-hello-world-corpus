const nunjucks = require('nunjucks');
const environment = new nunjucks.Environment(new nunjucks.FileSystemLoader('.'), {autoescape: true, throwOnUndefined: true});
const actual = environment.render('hello.njk', {audience: 'World'});
if (actual !== '<p>Hello, World!</p>\n') throw new Error('Unexpected rendering');
process.stdout.write(actual);
