<cfsetting showdebugoutput="false">
<cfcontent type="text/plain; charset=utf-8" reset="true"><cfscript>
greeting = new Greeting();
result = greeting.hello();
if (result != "Hello, World!" || greeting.hello("Reader") != "Hello, Reader!") {
    throw(type="Corpus.Assertion", message="Greeting component returned an unexpected value");
}
writeOutput(result);
</cfscript>
