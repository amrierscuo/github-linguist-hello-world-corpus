import qbs
import qbs.TextFile
Project {
    Product {
        name: "corpus-greeting"
        type: ["greeting"]
        Rule {
            multiplex: true
            Artifact { filePath: "greeting.txt"; fileTags: ["greeting"] }
            prepare: {
                var cmd = new JavaScriptCommand();
                cmd.description = "Create greeting";
                cmd.outputPath = output.filePath;
                cmd.sourceCode = function() {
                    var f = new TextFile(outputPath, TextFile.WriteOnly);
                    f.writeLine("Hello, World!"); f.close();
                };
                return [cmd];
            }
        }
    }
}
