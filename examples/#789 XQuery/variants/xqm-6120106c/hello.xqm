xquery version "3.1";
module namespace greeting = "urn:corpus:greeting";
declare function greeting:message() as xs:string { "Hello, World!" };
