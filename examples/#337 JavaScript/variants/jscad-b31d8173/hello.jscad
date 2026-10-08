const { text, geometries } = require("@jscad/modeling");
const main = () => text.vectorText({ input: "Hello, World!" }).map(points => geometries.path2.fromPoints({}, points));
module.exports = { main };
