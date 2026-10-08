const path = require('node:path');
const tools = path.resolve(process.argv[2] || '.tools');
const source = path.resolve(process.argv[3] || 'hello.zmodel');
const output = path.resolve(process.argv[4] || 'generated.prisma');
const { loadDocument } = require(path.join(tools, 'node_modules/zenstack/cli/cli-util.js'));
const { PrismaSchemaGenerator } = require(path.join(tools,
  'node_modules/zenstack/plugins/prisma/schema-generator.js'));
(async () => {
  const model = await loadDocument(source);
  await new PrismaSchemaGenerator(model).generate({ output, schemaPath: source, format: false });
  console.log('PASS: original ZenStack parser and Prisma generator consumed hello.zmodel');
})().catch(error => { console.error(error); process.exitCode = 1; });
