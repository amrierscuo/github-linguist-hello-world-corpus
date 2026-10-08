from rdflib import Graph,URIRef,Literal,RDF,RDFS,OWL
g=Graph().parse('hello.owl',format='xml');subject=URIRef('urn:corpus:Greeting')
assert (subject,RDF.type,OWL.Class) in g
value=g.value(subject,RDFS.label);assert value==Literal('Hello, World!',lang='en')
print(str(value));print('PASS: genuine RDF/OWL serialization graph, class and language-tagged label')
