const fs = require("node:fs");
const Handlebars = require("handlebars");
const template = Handlebars.compile(fs.readFileSync("hello.handlebars", "utf8"), { strict: true });
const rendered = template({ audience: "World" });
if (rendered !== "<p>Hello, World!</p>\n") throw new Error("Unexpected rendering");
process.stdout.write(rendered);
