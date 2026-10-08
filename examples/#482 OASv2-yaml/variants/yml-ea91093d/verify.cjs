const assert=require('node:assert/strict'),http=require('node:http');
const Parser=require('@apidevtools/swagger-parser'),Ajv=require('ajv');
(async()=>{const doc=await Parser.validate(process.argv[2]);const response=doc.paths['/hello'].get.responses['200'];
const content=doc.openapi?response.content['text/plain']:null;const schema=content?content.schema:response.schema;const example=content?content.example:response.examples['text/plain'];
const validate=new Ajv().compile(schema);assert(validate(example));assert(!validate('Hello, Moon!'));
const server=http.createServer((request,res)=>{if(request.url!='/hello'){res.writeHead(404);return res.end();}res.setHeader('Content-Type','text/plain');res.end(example);});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));try{const r=await fetch(`http://127.0.0.1:${server.address().port}/hello`);assert.equal(r.status,200);const body=await r.text();assert(validate(body));assert.equal(body,'Hello, World!');console.log(body);}finally{await new Promise(resolve=>server.close(resolve));}
})().catch(e=>{console.error(e);process.exitCode=1;});
