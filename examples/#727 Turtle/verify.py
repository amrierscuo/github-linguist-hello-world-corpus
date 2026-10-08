from rdflib import Graph,URIRef,Literal
g=Graph().parse("hello.ttl",format="turtle")
value=g.value(URIRef("https://example.invalid/corpus/greeting"),URIRef("http://www.w3.org/2000/01/rdf-schema#label"))
assert value==Literal("Hello, World!",lang="en")
assert len(g)==1
print(str(value))
