import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { initializeTestEnvironment, assertSucceeds, assertFails } from '@firebase/rules-unit-testing';
import { doc, getDoc, setDoc, updateDoc, deleteDoc } from 'firebase/firestore';

const test = await initializeTestEnvironment({
  projectId: 'demo-corpus',
  firestore: { host: '127.0.0.1', port: 8788, rules: await readFile('firestore.rules', 'utf8') },
});
try {
  await test.clearFirestore();
  const publicDb = test.unauthenticatedContext().firestore();
  const signedInDb = test.authenticatedContext('reader').firestore();
  await assertFails(setDoc(doc(publicDb, 'greetings/hello'), { message: 'Hello, World!' }));
  await assertFails(setDoc(doc(signedInDb, 'greetings/hello'), { message: 'Other' }));
  await assertFails(setDoc(doc(signedInDb, 'greetings/hello'), { message: 'Hello, World!', extra: true }));
  await assertSucceeds(setDoc(doc(signedInDb, 'greetings/hello'), { message: 'Hello, World!' }));
  const greeting = await assertSucceeds(getDoc(doc(publicDb, 'greetings/hello')));
  assert.equal(greeting.data().message, 'Hello, World!');
  await assertFails(getDoc(doc(publicDb, 'greetings/other')));
  await assertFails(updateDoc(doc(signedInDb, 'greetings/hello'), { message: 'Other' }));
  await assertFails(deleteDoc(doc(signedInDb, 'greetings/hello')));
  console.log('Hello, World!');
  console.log('PASS: genuine emulator read/create/update/delete permission assertions');
} finally {
  await test.cleanup();
}
