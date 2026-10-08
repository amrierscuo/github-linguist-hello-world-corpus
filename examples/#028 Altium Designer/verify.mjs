import assert from 'node:assert/strict';
import {readFileSync, existsSync} from 'node:fs';
import {resolve} from 'node:path';
const a = await import(process.env.ALTIUMTS_MODULE_URL || 'altiumts');
const read = name => readFileSync(new URL(name, import.meta.url), 'utf8');
const pcb = a.parseAltiumPcbDoc(read('Hello.PcbDoc'), {mode:'strict'});
const sch = a.parseAltiumSchDoc(read('Hello.SchDoc'));
const project = a.parseAltiumPrjPcb(read('Hello.PrjPCB'));
const job = a.parseAltiumOutJob(read('Hello.OutJob'));
for (const [name, model] of [['Hello.PcbDoc',pcb], ['Hello.SchDoc',sch], ['Hello.PrjPCB',project], ['Hello.OutJob',job]]) {
  const result = a.validateAltiumDocument(model, {profile:'strict'});
  assert.equal(result.valid, true, JSON.stringify(result));
  assert.equal(model.getString(), read(name));
}
assert.ok(pcb.records.some(record=>record.get('TEXT') === 'Hello, World!' && record.get('LAYER') === 'TOPOVERLAY'));
assert.ok(sch.records.some(record=>record.get('TEXT') === 'Hello, World!'));
assert.equal(project.documents.length,3);
for (const doc of project.documents) assert.ok(existsSync(new URL(doc.path,import.meta.url)));
assert.equal(project.variants[0].name,'Hello');
assert.equal(job.outputs[0].dataSource,'Hello.PcbDoc');
assert.equal(job.outputs[0].outputType,'Gerber');
assert.equal(job.containers.length,1);
const svg = a.serializeAltiumPcbLayerToSvg(pcb,'TOPOVERLAY');
assert.ok(svg.includes('Hello, World!'));
console.log('PASS: four Altium ASCII models parsed/validated/round-tripped; greeting text, project references and OutJob preserved.');
console.log('Native Altium Designer reopen and Gerber generation remain pending.');
