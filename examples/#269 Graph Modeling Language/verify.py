from pathlib import Path
import sys
import networkx as nx
graph = nx.read_gml(Path(sys.argv[1]), label=None)
assert graph.is_directed()
assert list(graph.nodes) == [0]
assert graph.nodes[0]['label'] == 'Hello, World!'
assert graph.number_of_edges() == 0
print(graph.nodes[0]['label'])
print('PASS: existing GML parser, directed graph and node label')
