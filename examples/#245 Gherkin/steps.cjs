const assert = require('node:assert/strict');
const { Given, When, Then } = require('@cucumber/cucumber');
Given('the recipient is {string}', function(recipient) { this.recipient = recipient; });
When('I compose the greeting', function() { this.greeting = `Hello, ${this.recipient}!`; });
Then('the greeting is {string}', function(expected) { assert.equal(this.greeting, expected); });
