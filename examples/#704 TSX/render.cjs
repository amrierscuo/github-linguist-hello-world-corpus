const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const { Greeting } = require("./build/hello.js");
const actual = renderToStaticMarkup(React.createElement(Greeting, { audience: "World" }));
if (actual !== "<p>Hello, World!</p>") throw new Error(actual);
console.log(actual);
