import tsplib95
p = tsplib95.load("hello.tsp")
assert p.dimension == 3
assert list(p.get_nodes()) == [1, 2, 3]
assert p.get_weight(1, 2) == 1
assert p.comment == "Hello, World!"
print(p.comment)
